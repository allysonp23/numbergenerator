import json
import uuid
import logging
from kafka import KafkaProducer, KafkaConsumer
from django.conf import settings
import redis

logger = logging.getLogger(__name__)

# Redis client for storing task results
redis_client = redis.Redis.from_url(settings.TASK_RESULT_BACKEND)

class KafkaTaskProducer:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
    
    def send_task(self, task_type, task_data):
        """Send a task to Kafka and return task_id"""
        task_id = str(uuid.uuid4())
        message = {
            'task_id': task_id,
            'task_type': task_type,
            'task_data': task_data
        }
        
        try:
            self.producer.send(settings.KAFKA_TOPIC_REQUESTS, value=message)
            self.producer.flush()
            
            # Set initial status in Redis
            redis_client.setex(f"task:{task_id}", 300, json.dumps({
                'status': 'PENDING',
                'result': None
            }))
            
            return task_id
        except Exception as e:
            logger.error(f"Failed to send task to Kafka: {e}")
            raise

class KafkaTaskConsumer:
    def __init__(self):
        self.consumer = KafkaConsumer(
            settings.KAFKA_TOPIC_REQUESTS,
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
            group_id=settings.KAFKA_CONSUMER_GROUP,
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        
    def consume_tasks(self):
        """Consume tasks from Kafka and process them"""
        for message in self.consumer:
            try:
                task_data = message.value
                self.process_task(task_data)
            except Exception as e:
                logger.error(f"Error processing task: {e}")
    
    def process_task(self, task_data):
        """Process individual task and store result in Redis"""
        task_id = task_data['task_id']
        task_type = task_data['task_type']
        task_params = task_data['task_data']
        
        try:
            # Set status to PROCESSING
            redis_client.setex(f"task:{task_id}", 300, json.dumps({
                'status': 'PROCESSING',
                'result': None
            }))
            
            # Process the task based on type
            result = self._execute_task(task_type, task_params)
            
            # Store success result
            redis_client.setex(f"task:{task_id}", 300, json.dumps({
                'status': 'SUCCESS',
                'result': result
            }))
            
        except Exception as e:
            # Store error result
            redis_client.setex(f"task:{task_id}", 300, json.dumps({
                'status': 'FAILURE',
                'result': None,
                'error': str(e)
            }))
    
    def _execute_task(self, task_type, task_params):
        """Execute the actual task based on type"""
        if task_type == 'generate_cpf':
            from cpf_cnpj.utils import get_cpf
            return {'cpf': get_cpf(task_params.get('mask'))}
        elif task_type == 'generate_cnpj':
            from cpf_cnpj.utils import get_cnpj
            return {'cnpj': get_cnpj(task_params.get('mask'))}
        else:
            raise ValueError(f"Unknown task type: {task_type}")

def get_task_result(task_id):
    """Get task result from Redis"""
    result_data = redis_client.get(f"task:{task_id}")
    if result_data:
        return json.loads(result_data)
    return None
