import random

# List of common Portuguese given names
MALE_NAMES = [
    "João", "Pedro", "Lucas", "Gabriel", "Matheus",
    "Leonardo", "Gustavo", "Felipe", "Daniel", "Thiago",
    "Bruno", "André", "Ricardo", "Eduardo", "Alexandre",
    "Henrique", "Rafael", "Diego", "Victor", "Samuel",
    "Fernando", "Marcelo", "Antônio", "Rodrigo", "Carlos",
    "Adriano", "Vinícius", "Caio", "Fábio", "Igor",
    "Júlio", "Cristian", "Emanuel", "Renan", "Roberto",
    "Márcio", "Nelson", "Wagner", "Sebastião", "Otávio",
    "Raul", "Osvaldo", "Sérgio", "Luciano", "Mauro",
    "Elias", "Marcos", "José", "Heitor"
]

FEMALE_NAMES = [
    "Maria", "Ana", "Júlia", "Mariana", "Beatriz",
    "Camila", "Rafaela", "Sofia", "Isabela", "Carolina",
    "Fernanda", "Larissa", "Vanessa", "Luana", "Gabriela",
    "Tatiane", "Renata", "Patrícia", "Sandra", "Cláudia",
    "Bruna", "Alessandra", "Simone", "Thaís", "Bianca",
    "Cecília", "Natália", "Vitória", "Helena", "Cristiane",
    "Débora", "Letícia", "Roberta", "Daniela", "Elisângela",
    "Flávia", "Juliane", "Ivana", "Elaine", "Michelle",
    "Sílvia", "Jéssica", "Marisa", "Estela", "Ludmila",
    "Mônica", "Regina", "Tatiana", "Adriana", "Paula"
]

# Common Portuguese surnames
SURNAMES = [
    "Silva", "Santos", "Oliveira", "Sousa", "Lima",
    "Costa", "Pereira", "Carvalho", "Rodrigues", "Almeida",
    "Nunes", "Castro", "Freitas", "Gomes", "Fernandes",
    "Martins", "Moreira", "Azevedo", "Monteiro", "Teixeira",
    "Medeiros", "Cardoso", "Bezerra", "Vieira", "Machado",
    "Campos", "Tavares", "Moraes", "Guimarães", "Cunha",
    "Figueiredo", "Barreto", "Ávila", "Andrade", "Aragão",
    "Brito", "Reis", "Fonseca", "Melo", "Bastos",
    "Corrêa", "Passos", "Sales", "Siqueira", "Navarro",
    "Dantas", "Coutinho", "Neves", "Rangel", "Queiroz",
    "Albuquerque", "Bastiani", "Benício", "Bianchi", "Brandão",
    "Camargo", "Capelo", "Caruso", "Damiani", "Domenici",
    "Espinosa", "Fraga", "Lacerda", "Lancastre", "Mendonça",
    "Montanha", "Pasqualini", "Quintana", "Sarmiento", "Toscano"
]

def generate_name(gender=None):
    """
    Generate a fictitious Portuguese full name: first name (male or female) + two distinct surnames.

    :param gender: 'male' or 'female' (optional, random if not specified)
    :return: string with full name
    """
    gender = (gender or '').lower()
    if gender not in ('male', 'female'):
        gender = random.choice(['male', 'female'])
    first = random.choice(MALE_NAMES if gender == 'male' else FEMALE_NAMES)
    surnames = random.sample(SURNAMES, 2)
    return f"{first} {surnames[0]} {surnames[1]}"
