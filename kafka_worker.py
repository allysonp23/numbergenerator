#!/usr/bin/env python
"""
Kafka Consumer Worker for processing tasks
"""
import os
import sys
import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'numbergenerator.settings')
django.setup()

from numbergenerator.kafka_utils import KafkaTaskConsumer

if __name__ == '__main__':
    print("Starting Kafka task consumer...")
    consumer = KafkaTaskConsumer()
    consumer.consume_tasks()
