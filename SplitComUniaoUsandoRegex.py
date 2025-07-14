import re

texto = "maçã cama banana anjo laranja anjoteste teste uva"

partes = re.split(r'\s*(?:cama|anjo|teste)\s*', texto)

print(partes)