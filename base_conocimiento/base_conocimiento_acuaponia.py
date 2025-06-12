PECES_ACUAPONIA = [
    {
        'tipo': 'tilapia',
        'parametros': {
            'temperatura': '22-30°C',
            'pH': '6.5-8.5',
            'oxigeno': '>5 mg/L',
            'amonio': '<0.5 mg/L'
        },
        'recomendaciones': [
            'Mantener temperatura entre 22 y 30°C para un buen crecimiento.',
            'Evitar corrientes bruscas de agua.',
            'Realizar cambios parciales de agua semanalmente (10-20%).',
            'Alimentar 2-3 veces al día, evitando sobrealimentación.',
            'Monitorizar niveles de amonio y nitritos para evitar toxicidad.'
        ]
    },
    {
        'tipo': 'carpa',
        'parametros': {
            'temperatura': '18-26°C',
            'pH': '6.5-8.0',
            'oxigeno': '>4 mg/L',
            'amonio': '<1 mg/L'
        },
        'recomendaciones': [
            'Preferir agua ligeramente alcalina.',
            'Mantener temperatura moderada.',
            'Evitar acumulación de lodo en el fondo.',
            'Alimentar con pienso vegetal y suplementos proteicos.'
        ]
    },
    {
        'tipo': 'bagre',
        'parametros': {
            'temperatura': '24-30°C',
            'pH': '6.0-8.0',
            'oxigeno': '>5 mg/L',
            'amonio': '<0.5 mg/L'
        },
        'recomendaciones': [
            'El bagre tolera aguas turbias, pero requiere buen oxígeno.',
            'Evitar el estrés por manipulación frecuente.',
            'Asegurar buena filtración biológica.'
        ]
    }
]

HORTALIZAS_ACUAPONIA = [
    {
        'tipo': 'lechuga',
        'parametros': {
            'temperatura': '15-25°C',
            'pH': '6.0-7.0',
            'nutrientes': 'Nitrógeno medio-alto, Calcio, Magnesio'
        },
        'recomendaciones': [
            'Evitar exposición directa a sol fuerte.',
            'Cosechar hojas externas para favorecer crecimiento.',
            'Vigilar deficiencia de calcio para prevenir punta quemada.'
        ]
    },
    {
        'tipo': 'espinaca',
        'parametros': {
            'temperatura': '10-24°C',
            'pH': '6.0-7.0',
            'nutrientes': 'Alto nitrógeno, Hierro'
        },
        'recomendaciones': [
            'Requiere agua bien oxigenada.',
            'Evitar calor extremo.',
            'Cosechar hojas maduras periódicamente.'
        ]
    },
    {
        'tipo': 'albahaca',
        'parametros': {
            'temperatura': '18-30°C',
            'pH': '5.5-6.5',
            'nutrientes': 'Nitrógeno, Fósforo, Potasio'
        },
        'recomendaciones': [
            'Prefiere luz intensa.',
            'Recortar regularmente para estimular ramificación.',
            'Evitar suelos encharcados.'
        ]
    },
    {
        'tipo': 'tomate',
        'parametros': {
            'temperatura': '18-26°C',
            'pH': '5.8-6.8',
            'nutrientes': 'Nitrógeno, Calcio, Potasio'
        },
        'recomendaciones': [
            'Asegurar soporte físico para la planta.',
            'Mantener humedad constante.',
            'Vigilar signos de deficiencia de calcio (pudrición apical).'
        ]
    },
    {
        'tipo': 'brocoli',
        'parametros': {
            'temperatura': '14-22°C',
            'pH': '6.0-7.0',
            'nutrientes': 'Alto nitrógeno, Calcio, Magnesio, Azufre'
        },
        'recomendaciones': [
            'Prefiere temperaturas frescas y estables.',
            'Requiere buena disponibilidad de calcio para evitar problemas en la cabeza.',
            'Evitar cambios bruscos de temperatura y humedad.'
        ]
    },
    {
        'tipo': 'coliflor',
        'parametros': {
            'temperatura': '15-20°C',
            'pH': '6.0-7.0',
            'nutrientes': 'Nitrógeno, Calcio, Boro'
        },
        'recomendaciones': [
            'Evitar calor excesivo, prefiere climas templados.',
            'Necesita suficiente boro y calcio para evitar deformidades.',
            'Proteger la cabeza del sol directo para mantenerla blanca.'
        ]
    }
]

COMBINACIONES_ACUAPONIA = [
    # TILAPIA
    {
        'pez': 'tilapia',
        'hortaliza': 'lechuga',
        'recomendaciones': [
            'La tilapia genera abundante nitrógeno para el crecimiento rápido de la lechuga.',
            'Mantén el pH entre 6.5 y 7.0 para ambos.',
            'Evita temperaturas bajo 20°C para no afectar a la tilapia ni a la lechuga.'
        ]
    },
    {
        'pez': 'tilapia',
        'hortaliza': 'espinaca',
        'recomendaciones': [
            'La tilapia proporciona suficiente nitrógeno para la espinaca.',
            'Requiere buena oxigenación para ambos organismos.',
            'No expongas la espinaca a temperaturas superiores a 25°C para evitar espigado.'
        ]
    },
    {
        'pez': 'tilapia',
        'hortaliza': 'albahaca',
        'recomendaciones': [
            'La tilapia produce suficiente nutriente para la albahaca.',
            'Mantén la temperatura en el rango superior para que ambas prosperen.',
            'Ajusta el pH hacia el 6.5 para mejor absorción de nutrientes en albahaca.'
        ]
    },
    {
        'pez': 'tilapia',
        'hortaliza': 'tomate',
        'recomendaciones': [
            'La tilapia y el tomate prosperan en temperaturas cálidas.',
            'Suministra calcio adicional para prevenir pudrición apical en tomate.',
            'Brinda soporte para las plantas de tomate y mantén el agua bien filtrada.'
        ]
    },
    {
        'pez': 'tilapia',
        'hortaliza': 'brocoli',
        'recomendaciones': [
            'La tilapia provee buen nitrógeno para el brócoli.',
            'Mantén el pH entre 6.0 y 7.0 para un desarrollo adecuado del brócoli.',
            'Evita temperaturas superiores a 24°C, ya que el brócoli prefiere climas templados.'
        ]
    },
    {
        'pez': 'tilapia',
        'hortaliza': 'coliflor',
        'recomendaciones': [
            'El amonio producido por tilapia ayuda al crecimiento de la coliflor.',
            'Controla el pH cerca de 6.5.',
            'Coliflor y tilapia toleran agua templada, pero evita temperaturas excesivas para el cultivo.'
        ]
    },

    # CARPA
    {
        'pez': 'carpa',
        'hortaliza': 'lechuga',
        'recomendaciones': [
            'La carpa y la lechuga toleran temperaturas frescas.',
            'Controla el pH entre 6.5 y 7.0.',
            'Evita la sobrealimentación de carpas para mantener agua limpia.'
        ]
    },
    {
        'pez': 'carpa',
        'hortaliza': 'espinaca',
        'recomendaciones': [
            'Ambos soportan temperaturas moderadas a bajas.',
            'Aumenta la aireación porque la espinaca necesita alto oxígeno.',
            'Evita acumulación de lodo para prevenir enfermedades en carpa.'
        ]
    },
    {
        'pez': 'carpa',
        'hortaliza': 'albahaca',
        'recomendaciones': [
            'Mantén el agua bien oxigenada para carpa y albahaca.',
            'Controla el pH cerca de 6.5.',
            'Ubica la albahaca en zonas de buena luz.'
        ]
    },
    {
        'pez': 'carpa',
        'hortaliza': 'tomate',
        'recomendaciones': [
            'Asegura soporte para el tomate y buena aireación para la carpa.',
            'Suministra potasio y calcio extra para el tomate.',
            'Evita el agua demasiado fría para no frenar el crecimiento del tomate.'
        ]
    },
    {
        'pez': 'carpa',
        'hortaliza': 'brocoli',
        'recomendaciones': [
            'La carpa tolera aguas frescas igual que el brócoli.',
            'Mantén el pH entre 6.0 y 7.0.',
            'Evita acumulación de residuos que puedan afectar el desarrollo de la inflorescencia.'
        ]
    },
    {
        'pez': 'carpa',
        'hortaliza': 'coliflor',
        'recomendaciones': [
            'La carpa ayuda a aportar nutrientes para la coliflor.',
            'Prefiere agua fresca y bien oxigenada.',
            'Revisa la dureza del agua para evitar problemas en el crecimiento.'
        ]
    },

    # BAGRE
    {
        'pez': 'bagre',
        'hortaliza': 'lechuga',
        'recomendaciones': [
            'El bagre y la lechuga se adaptan bien a aguas ligeramente cálidas.',
            'Monitorea niveles de amonio, ya que el bagre es sensible.',
            'Evita cambios bruscos de temperatura.'
        ]
    },
    {
        'pez': 'bagre',
        'hortaliza': 'espinaca',
        'recomendaciones': [
            'Ambos requieren aguas oxigenadas.',
            'Mantén la temperatura estable para evitar estrés en el bagre.',
            'Realiza cosechas periódicas de espinaca.'
        ]
    },
    {
        'pez': 'bagre',
        'hortaliza': 'albahaca',
        'recomendaciones': [
            'El bagre tolera aguas turbias, pero la albahaca requiere agua limpia.',
            'Evita acumulación de residuos orgánicos.',
            'Ubica la albahaca bajo luz intensa.'
        ]
    },
    {
        'pez': 'bagre',
        'hortaliza': 'tomate',
        'recomendaciones': [
            'El bagre y el tomate prosperan en aguas cálidas.',
            'Asegura niveles bajos de amonio y alto oxígeno.',
            'Revisa deficiencias de calcio en el tomate regularmente.'
        ]
    },
    {
        'pez': 'bagre',
        'hortaliza': 'brocoli',
        'recomendaciones': [
            'El bagre soporta aguas templadas, pero monitorea la temperatura para el brócoli.',
            'Mantén agua limpia para evitar enfermedades radiculares en el brócoli.',
            'Asegura buena aireación.'
        ]
    },
    {
        'pez': 'bagre',
        'hortaliza': 'coliflor',
        'recomendaciones': [
            'El bagre provee nutrientes para la coliflor, pero vigila niveles de amonio.',
            'Controla el pH entre 6.0 y 7.0.',
            'Evita temperaturas extremas para lograr buenas cabezas de coliflor.'
        ]
    }
]

def get_all_peces():
    return [p['tipo'] for p in PECES_ACUAPONIA]

def get_all_hortalizas():
    return [h['tipo'] for h in HORTALIZAS_ACUAPONIA]

def get_parametros_pez(pez):
    for p in PECES_ACUAPONIA:
        if p['tipo'] == pez:
            return p['parametros']
    return {}

def get_parametros_hortaliza(hortaliza):
    for h in HORTALIZAS_ACUAPONIA:
        if h['tipo'] == hortaliza:
            return h['parametros']
    return {}

def get_recomendaciones_pez(pez):
    for p in PECES_ACUAPONIA:
        if p['tipo'] == pez:
            return p['recomendaciones']
    return []

def get_recomendaciones_hortaliza(hortaliza):
    for h in HORTALIZAS_ACUAPONIA:
        if h['tipo'] == hortaliza:
            return h['recomendaciones']
    return []

def get_combinacion(pez, hortaliza):
    for c in COMBINACIONES_ACUAPONIA:
        if c['pez'] == pez and c['hortaliza'] == hortaliza:
            return c['recomendaciones']
    return []