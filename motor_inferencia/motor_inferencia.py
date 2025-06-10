from base_conocimiento.base_conocimiento import FERTILIZANTES, DIAGNOSTICOS, ACUAPONIA

def recomendar_fertilizante(cultivo, suelo, clima):
    for regla in FERTILIZANTES:
        if regla['cultivo'] == cultivo and regla['suelo'] == suelo and regla['clima'] == clima:
            return regla['recomendacion']
    return "No hay recomendación registrada para esta combinación."

def diagnosticar_plaga(cultivo, sintomas_usuario):
    sintomas_usuario = set([s.lower() for s in sintomas_usuario])
    for regla in DIAGNOSTICOS:
        if regla['cultivo'] == cultivo:
            sintomas_regla = set([s.lower() for s in regla['sintomas']])
            if sintomas_regla.issubset(sintomas_usuario):
                return f"{regla['diagnostico']}: {regla['recomendacion']}"
    return "No se identificó la plaga o enfermedad."

def recomendar_acuaponia(pez, cultivo):
    for regla in ACUAPONIA:
        if regla['pez'] == pez and regla['cultivo'] == cultivo:
            return regla['recomendacion']
    return "No hay recomendación registrada para esta combinación."