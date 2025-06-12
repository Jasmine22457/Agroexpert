# motor_inferencia/motor_inferencia.py

from typing import List, Dict, Optional
from base_conocimiento.base_conocimiento import FERTILIZANTES, PARAMETROS
from base_conocimiento.base_conomiento_plagas import PLAGAS



class AsesorAgricola:
    """Sistema experto para recomendaciones agrícolas en El Salvador"""

    def __init__(self):
        self.parametros = PARAMETROS

    def obtener_opciones(self, tipo):
        """
        Devuelve opciones para los selectores en la interfaz
        """
        if tipo == 'cultivos':
            return self.parametros['cultivos']
        elif tipo == 'suelos':
            return self.parametros['suelos']
        elif tipo == 'climas':
            return self.parametros['climas']
        elif tipo == 'etapas':
            return self.parametros['etapas']
        elif tipo == 'variedades_cultivo':
            return self.parametros['variedades']
     
        return []

    def recomendar_fertilizacion(self, cultivo, suelo, clima, variedad=None, etapa=None):
       
        for regla in FERTILIZANTES:
            if (
                regla['cultivo'] == cultivo and
                regla['suelo'] == suelo and
                regla['clima'] == clima and
                (not variedad or regla['variedad'] == variedad) and
                (not etapa or regla['etapa'] == etapa)
            ):
                # Copia la recomendación y añade las condiciones
                recomendacion = regla['recomendacion'].copy()
                recomendacion['condiciones'] = {
                    'suelo': regla['suelo'],
                    'clima': regla['clima'],
                    'variedad': regla['variedad'],
                    'etapa': regla['etapa']
                }
                return {'recomendaciones': recomendacion}
        # Si no se encuentra, retorna sugerencias
        return {
            'sugerencias': [
                "No hay una recomendación técnica registrada para esos parámetros. "
                "Prueba otra combinación de variedad, clima o etapa."
            ]
        }

    # === MANEJO DE PLAGAS ===
    def diagnosticar_plaga(self, cultivo: str, sintomas: List[str]) -> Dict:
        sintomas = set(s.lower().strip() for s in sintomas)
        diagnosticos = []
        for plaga in PLAGAS:
            if plaga['cultivo'] == cultivo:
                sintomas_plaga = set(s.lower() for s in plaga['sintomas'])
                coincidencia = sintomas_plaga.intersection(sintomas)
                if len(coincidencia) >= 2:
                    score = len(coincidencia) / len(sintomas_plaga)
                    diagnostico = {
                        'plaga': plaga['plaga'],
                        'coincidencia': f"{score:.0%}",
                        'sintomas_coincidentes': list(coincidencia),
                        'tratamientos': plaga['tratamientos'],
                        'estrategia': plaga['estrategia']
                    }
                    diagnosticos.append(diagnostico)
        if not diagnosticos:
            return {
                'error': 'No se identificó la plaga',
                'sugerencias': self._sugerir_plagas_comunes(cultivo)
            }
        diagnosticos.sort(key=lambda x: x['coincidencia'], reverse=True)
        return {
            'diagnosticos': diagnosticos,
            'quimicos_recomendados': self._extraer_quimicos(diagnosticos)
        }

    def _sugerir_plagas_comunes(self, cultivo: str) -> List:
        return [p['plaga'] for p in PLAGAS if p['cultivo'] == cultivo][:3]

    def _extraer_quimicos(self, diagnosticos: List) -> List:
        quimicos = []
        seen = set()
        for d in diagnosticos:
            for t in d['tratamientos']:
                if t['producto'] not in seen:
                    quimicos.append({
                        'producto': t['producto'],
                        'clase': t['clase'],
                        'dosis': t['dosis']
                    })
                    seen.add(t['producto'])
        return quimicos

    # === INTERFAZ ===
    def obtener_opciones(self, tipo: str) -> List:
        if tipo in self.parametros:
            return self.parametros[tipo]
        elif tipo == 'variedades':
            return list(self.parametros['variedades'].keys())
        elif tipo == 'variedades_cultivo':
            return self.parametros['variedades']
        elif tipo == 'sintomas':
            # Por defecto, mostrar todos los síntomas conocidos
            sintomas_set = set()
            for plaga in PLAGAS:
                sintomas_set.update(plaga['sintomas'])
            return sorted(list(sintomas_set))
        return []
