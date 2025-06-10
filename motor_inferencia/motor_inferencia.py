from typing import List, Dict, Optional
from base_conocimiento import FERTILIZANTES, PLAGAS, PARAMETROS

class AsesorAgricola:
    """Sistema experto para recomendaciones agrícolas en El Salvador"""
    
    def __init__(self):
        self.parametros = PARAMETROS
    
    # === FERTILIZACIÓN ===
    def recomendar_fertilizacion(self, cultivo: str, suelo: str, clima: str, 
                               variedad: Optional[str] = None, etapa: Optional[str] = None) -> Dict:
        recomendaciones = []
        for regla in FERTILIZANTES:
            match = (
                regla['cultivo'] == cultivo and
                regla['suelo'] == suelo and
                regla['clima'] == clima and
                (variedad is None or regla.get('variedad') == variedad) and
                (etapa is None or regla.get('etapa') == etapa)
            )
            if match:
                rec = regla['recomendacion'].copy()
                rec['condiciones'] = {
                    'suelo': suelo,
                    'clima': clima,
                    'variedad': variedad,
                    'etapa': etapa
                }
                recomendaciones.append(rec)
        if not recomendaciones:
            return {
                'error': 'No se encontraron recomendaciones',
                'sugerencias': self._sugerir_alternativas(cultivo, suelo, clima)
            }
        return {
            'recomendaciones': recomendaciones,
            'advertencias': self._generar_advertencias(cultivo, suelo)
        }
    
    def _sugerir_alternativas(self, cultivo: str, suelo: str, clima: str) -> List:
        alternativas = []
        for regla in FERTILIZANTES:
            if regla['cultivo'] == cultivo and regla['clima'] == clima:
                alternativas.append({
                    'suelo_alternativo': regla['suelo'],
                    'recomendacion': regla['recomendacion']['formula']
                })
        for regla in FERTILIZANTES:
            if regla['cultivo'] == cultivo and regla['suelo'] == suelo:
                alternativas.append({
                    'clima_alternativo': regla['clima'],
                    'recomendacion': regla['recomendacion']['formula']
                })
        return alternativas[:3]
    
    def _generar_advertencias(self, cultivo: str, suelo: str) -> List:
        advertencias = []
        if cultivo == 'maiz' and suelo == 'arenoso':
            advertencias.append('Requiere fertilización fraccionada por lixiviación potencial')
        if cultivo == 'tomate' and suelo == 'arcilloso':
            advertencias.append('Aumentar dosis de potasio en un 20% para este tipo de suelo')
        return advertencias
    
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
        return []