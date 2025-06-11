# -*- coding: utf-8 -*-
"""
BASE DE CONOCIMIENTO PARA AGRICULTURA EN EL SALVADOR
Datos técnicos validados por INSAFO y literatura técnica Mesoamericana.
Última actualización: Julio 2023
"""

# === FERTILIZANTES QUÍMICOS PARA GRANOS BÁSICOS Y HORTALIZAS ===
FERTILIZANTES = [
    # ======= SIEMBRA =======
    {
        'cultivo': 'maiz',
        'variedad': 'híbrido',
        'suelo': 'arcilloso',
        'clima': 'tropical',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '18-46-0 + Zn (DAP con Zinc)',
            'dosis': '3 qq/manzana',
            'aplicacion': 'Aplicar al momento de la siembra, incorporar al suelo',
            'fabricantes': ['Yara', 'Profertil'],
            'precauciones': 'No mezclar con semilla directamente'
        }
    },
    {
        'cultivo': 'maiz',
        'variedad': 'criollo',
        'suelo': 'arcilloso',
        'clima': 'tropical',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '15-15-15',
            'dosis': '2.5 qq/manzana',
            'aplicacion': 'Aplicar en banda junto a la semilla',
            'fabricantes': ['Fertica'],
            'precauciones': 'Evitar contacto directo con la semilla'
        }
    },
    {
        'cultivo': 'maiz',
        'variedad': 'híbrido',
        'suelo': 'volcánico',
        'clima': 'húmedo',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '18-46-0',
            'dosis': '3 qq/manzana',
            'aplicacion': 'Incorporar al suelo antes de la siembra',
            'fabricantes': ['Yara', 'Profertil'],
            'precauciones': 'Regar después de la aplicación si es posible'
        }
    },
    {
        'cultivo': 'maiz',
        'variedad': 'criollo',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '10-30-10',
            'dosis': '2 qq/manzana',
            'aplicacion': 'Al fondo del surco antes de sembrar',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar en exceso para evitar toxicidad'
        }
    },

    # ======= DESARROLLO =======
    {
        'cultivo': 'maiz',
        'variedad': 'híbrido',
        'suelo': 'arcilloso',
        'clima': 'húmedo',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '2 qq/manzana',
            'aplicacion': 'Aplicar a los 25 días después de emergencia, alrededor de la planta',
            'fabricantes': ['Yara', 'Fertica'],
            'precauciones': 'No aplicar sobre hojas mojadas'
        }
    },
    {
        'cultivo': 'maiz',
        'variedad': 'criollo',
        'suelo': 'volcánico',
        'clima': 'tropical',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '1.5 qq/manzana',
            'aplicacion': 'Aplicar entre las hileras a los 20-25 días',
            'fabricantes': ['Fertica'],
            'precauciones': 'Cubrir ligeramente con tierra'
        }
    },
    {
        'cultivo': 'maiz',
        'variedad': 'híbrido',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0) + KCl',
            'dosis': '1.5 qq Urea + 1 qq KCl/manzana',
            'aplicacion': 'Al inicio de macollamiento',
            'fabricantes': ['Yara'],
            'precauciones': 'No exceder dosis de potasio'
        }
    },

    # ======= FLORACIÓN =======
    {
        'cultivo': 'maiz',
        'variedad': 'híbrido',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'KCl (Cloruro de Potasio) 0-0-60',
            'dosis': '1 qq/manzana',
            'aplicacion': 'Aplicar en corona al inicio de floración',
            'fabricantes': ['Yara'],
            'precauciones': 'No exceder dosis para evitar toxicidad'
        }
    },
    {
        'cultivo': 'maiz',
        'variedad': 'criollo',
        'suelo': 'arcilloso',
        'clima': 'húmedo',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'Fosfato monoamónico (12-52-0)',
            'dosis': '0.5 qq/manzana',
            'aplicacion': 'Aplicar al pie de la planta durante floración',
            'fabricantes': ['Fertica'],
            'precauciones': 'Evitar encharcamientos'
        }
    },

    # ======= PRODUCCIÓN =======
    {
        'cultivo': 'maiz',
        'variedad': 'híbrido',
        'suelo': 'volcánico',
        'clima': 'tropical',
        'etapa': 'producción',
        'recomendacion': {
            'formula': 'Fertilizante foliar balanceado',
            'dosis': '0.5 qq/manzana',
            'aplicacion': 'Rociar sobre follaje en etapa de llenado de grano',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar a pleno sol'
        }
    },
    {
        'cultivo': 'maiz',
        'variedad': 'criollo',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'producción',
        'recomendacion': {
            'formula': 'Sulfato de magnesio',
            'dosis': '0.5 qq/manzana',
            'aplicacion': 'Aplicar al follaje 30 días después de floración',
            'fabricantes': ['Fertica'],
            'precauciones': 'Evitar aplicaciones bajo lluvias intensas'
        }
    },

    # ======= TRASPLANTE (menos frecuente, pero posible en almácigos) =======
    {
        'cultivo': 'maiz',
        'variedad': 'híbrido',
        'suelo': 'arcilloso',
        'clima': 'templado',
        'etapa': 'trasplante',
        'recomendacion': {
            'formula': '18-46-0',
            'dosis': '1 qq/manzana',
            'aplicacion': 'Aplicar en hoyo de trasplante',
            'fabricantes': ['Profertil'],
            'precauciones': 'Cubrir bien la raíz para evitar quemaduras'
        }
    },
    {
        'cultivo': 'maiz',
        'variedad': 'criollo',
        'suelo': 'volcánico',
        'clima': 'húmedo',
        'etapa': 'trasplante',
        'recomendacion': {
            'formula': '15-15-15',
            'dosis': '1 qq/manzana',
            'aplicacion': 'En base del hoyo al trasplantar',
            'fabricantes': ['Fertica'],
            'precauciones': 'Regar suavemente después'
        }
    },
    # ======= SIEMBRA =======
    {
        'cultivo': 'frijol',
        'variedad': 'rojo de seda',
        'suelo': 'franco',
        'clima': 'tropical',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '10-30-10',
            'dosis': '2 qq/manzana',
            'aplicacion': 'Al fondo del surco antes de sembrar',
            'fabricantes': ['Fertica', 'Yara'],
            'precauciones': 'Evitar contacto directo con la semilla'
        }
    },
    {
        'cultivo': 'frijol',
        'variedad': 'negro',
        'suelo': 'arcilloso',
        'clima': 'húmedo',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '12-24-12',
            'dosis': '2.5 qq/manzana',
            'aplicacion': 'Aplicar e incorporar antes de la siembra',
            'fabricantes': ['Fertica'],
            'precauciones': 'No aplicar si hay exceso de humedad'
        }
    },
    {
        'cultivo': 'frijol',
        'variedad': 'rojo de seda',
        'suelo': 'volcánico',
        'clima': 'templado',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '15-15-15',
            'dosis': '2 qq/manzana',
            'aplicacion': 'Aplicar al fondo del surco antes de sembrar',
            'fabricantes': ['Yara'],
            'precauciones': 'Regar después de aplicar'
        }
    },

    # ======= DESARROLLO =======
    {
        'cultivo': 'frijol',
        'variedad': 'rojo de seda',
        'suelo': 'franco',
        'clima': 'húmedo',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '1 qq/manzana',
            'aplicacion': 'Aplicar 20 días después de emergencia, entre hileras',
            'fabricantes': ['Yara', 'Fertica'],
            'precauciones': 'No aplicar sobre hojas mojadas'
        }
    },
    {
        'cultivo': 'frijol',
        'variedad': 'negro',
        'suelo': 'volcánico',
        'clima': 'tropical',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '0.5 qq/manzana',
            'aplicacion': 'Aplicar entre hileras, cubrir con tierra',
            'fabricantes': ['Fertica'],
            'precauciones': 'Evitar aplicación si hay lluvia'
        }
    },

    # ======= FLORACIÓN =======
    {
        'cultivo': 'frijol',
        'variedad': 'rojo de seda',
        'suelo': 'franco',
        'clima': 'tropical',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'Fosfato monoamónico (12-52-0)',
            'dosis': '0.5 qq/manzana',
            'aplicacion': 'Aplicar al pie de la planta',
            'fabricantes': ['Yara'],
            'precauciones': 'No exceder la dosis recomendada'
        }
    },
    {
        'cultivo': 'frijol',
        'variedad': 'negro',
        'suelo': 'franco',
        'clima': 'húmedo',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'Sulfato de magnesio',
            'dosis': '0.5 qq/manzana',
            'aplicacion': 'Aplicar al follaje durante floración',
            'fabricantes': ['Fertica'],
            'precauciones': 'Evitar aplicaciones bajo lluvias intensas'
        }
    },

    # ======= PRODUCCIÓN =======
    {
        'cultivo': 'frijol',
        'variedad': 'rojo de seda',
        'suelo': 'volcánico',
        'clima': 'tropical',
        'etapa': 'producción',
        'recomendacion': {
            'formula': 'Fertilizante foliar balanceado',
            'dosis': '0.5 qq/manzana',
            'aplicacion': 'Rociar sobre follaje durante llenado de vaina',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar en horas de sol fuerte'
        }
    },
    {
        'cultivo': 'frijol',
        'variedad': 'negro',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'producción',
        'recomendacion': {
            'formula': 'Sulfato de potasio',
            'dosis': '0.25 qq/manzana',
            'aplicacion': 'Aplicar al pie de la planta',
            'fabricantes': ['Fertica'],
            'precauciones': 'Evitar sobredosis'
        }
    },

    # ======= TRASPLANTE (raro pero posible en almácigo o trasplante de plántulas) =======
    {
        'cultivo': 'frijol',
        'variedad': 'rojo de seda',
        'suelo': 'arcilloso',
        'clima': 'tropical',
        'etapa': 'trasplante',
        'recomendacion': {
            'formula': '10-30-10',
            'dosis': '1 qq/manzana',
            'aplicacion': 'Aplicar al fondo del hoyo al trasplantar',
            'fabricantes': ['Yara', 'Fertica'],
            'precauciones': 'Cubrir bien la raíz'
        }
    },
    {
        'cultivo': 'frijol',
        'variedad': 'negro',
        'suelo': 'volcánico',
        'clima': 'húmedo',
        'etapa': 'trasplante',
        'recomendacion': {
            'formula': '15-15-15',
            'dosis': '1 qq/manzana',
            'aplicacion': 'En base del hoyo al trasplantar',
            'fabricantes': ['Fertica'],
            'precauciones': 'Regar suavemente después'
        }
    },
    # ======= SIEMBRA =======
    {
        'cultivo': 'sorgo',
        'variedad': 'tradicional',
        'suelo': 'arcilloso',
        'clima': 'tropical',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '15-15-15',
            'dosis': '2 qq/manzana',
            'aplicacion': 'Aplicar en banda a 5 cm de profundidad antes de la siembra',
            'fabricantes': ['Fertica', 'Profertil'],
            'precauciones': 'No mezclar con semilla'
        }
    },
    {
        'cultivo': 'sorgo',
        'variedad': 'tradicional',
        'suelo': 'arenoso',
        'clima': 'seco',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '18-46-0',
            'dosis': '2.5 qq/manzana',
            'aplicacion': 'Incorporar al suelo antes de sembrar',
            'fabricantes': ['Yara', 'Profertil'],
            'precauciones': 'Regar si es posible para mejorar absorción'
        }
    },
    {
        'cultivo': 'sorgo',
        'variedad': 'tradicional',
        'suelo': 'volcánico',
        'clima': 'tropical',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '12-24-12',
            'dosis': '2 qq/manzana',
            'aplicacion': 'Al fondo del surco',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar directamente sobre la semilla'
        }
    },

    # ======= DESARROLLO =======
    {
        'cultivo': 'sorgo',
        'variedad': 'tradicional',
        'suelo': 'arcilloso',
        'clima': 'seco',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '1 qq/manzana',
            'aplicacion': 'A los 20 días después de emergencia, entre hileras',
            'fabricantes': ['Fertica'],
            'precauciones': 'Evitar aplicación si hay sequía severa'
        }
    },
    {
        'cultivo': 'sorgo',
        'variedad': 'tradicional',
        'suelo': 'arenoso',
        'clima': 'tropical',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '0.8 qq/manzana',
            'aplicacion': 'Aplicar entre hileras, cubrir ligeramente',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar sobre hojas mojadas'
        }
    },

    # ======= FLORACIÓN =======
    {
        'cultivo': 'sorgo',
        'variedad': 'tradicional',
        'suelo': 'volcánico',
        'clima': 'tropical',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'KCl (0-0-60)',
            'dosis': '0.5 qq/manzana',
            'aplicacion': 'Aplicar al pie de la planta al inicio de floración',
            'fabricantes': ['Yara'],
            'precauciones': 'No exceder dosis recomendada'
        }
    },
    {
        'cultivo': 'sorgo',
        'variedad': 'tradicional',
        'suelo': 'arenoso',
        'clima': 'seco',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'Fertilizante foliar balanceado',
            'dosis': '0.3 qq/manzana',
            'aplicacion': 'Aplicar en spray sobre follaje',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar en horas de mayor radiación solar'
        }
    },

    # ======= PRODUCCIÓN =======
    {
        'cultivo': 'sorgo',
        'variedad': 'tradicional',
        'suelo': 'arcilloso',
        'clima': 'tropical',
        'etapa': 'producción',
        'recomendacion': {
            'formula': 'Sulfato de magnesio',
            'dosis': '0.25 qq/manzana',
            'aplicacion': 'Aplicar en etapa de llenado de grano',
            'fabricantes': ['Fertica'],
            'precauciones': 'Evitar aplicación bajo lluvia intensa'
        }
    },

    # ======= TRASPLANTE (no es lo más común en sorgo, pero posible en investigación o almácigos) =======
    {
        'cultivo': 'sorgo',
        'variedad': 'tradicional',
        'suelo': 'volcánico',
        'clima': 'tropical',
        'etapa': 'trasplante',
        'recomendacion': {
            'formula': '15-15-15',
            'dosis': '1 qq/manzana',
            'aplicacion': 'En hoyo de trasplante',
            'fabricantes': ['Profertil'],
            'precauciones': 'Cubrir raíces y regar inmediatamente'
        }
    },
    # ======= SIEMBRA =======
    {
        'cultivo': 'arroz',
        'variedad': 'IR-8',
        'suelo': 'arcilloso',
        'clima': 'húmedo',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '12-24-12',
            'dosis': '3 qq/manzana',
            'aplicacion': 'Aplicar al momento de la siembra e incorporar al suelo',
            'fabricantes': ['Fertica'],
            'precauciones': 'Mantener suelo húmedo pero no saturado'
        }
    },
    {
        'cultivo': 'arroz',
        'variedad': 'IR-8',
        'suelo': 'franco',
        'clima': 'tropical',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '10-30-10',
            'dosis': '2.5 qq/manzana',
            'aplicacion': 'Al fondo del surco, antes de sembrar',
            'fabricantes': ['Yara'],
            'precauciones': 'Evitar acumulación excesiva de agua'
        }
    },

    # ======= DESARROLLO =======
    {
        'cultivo': 'arroz',
        'variedad': 'IR-8',
        'suelo': 'arcilloso',
        'clima': 'tropical',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '1.5 qq/manzana',
            'aplicacion': 'A los 25 días después de emergencia, entre hileras',
            'fabricantes': ['Yara', 'Fertica'],
            'precauciones': 'Evitar aplicación si hay inundación'
        }
    },
    {
        'cultivo': 'arroz',
        'variedad': 'IR-8',
        'suelo': 'franco',
        'clima': 'húmedo',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '1 qq/manzana',
            'aplicacion': 'Aplicar 20 días después de emergencia',
            'fabricantes': ['Fertica'],
            'precauciones': 'No aplicar sobre hojas mojadas'
        }
    },

    # ======= FLORACIÓN =======
    {
        'cultivo': 'arroz',
        'variedad': 'IR-8',
        'suelo': 'arcilloso',
        'clima': 'húmedo',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'Fertilizante foliar balanceado',
            'dosis': '0.5 qq/manzana',
            'aplicacion': 'Rociar sobre follaje al inicio de floración',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar en horas de sol fuerte'
        }
    },
    {
        'cultivo': 'arroz',
        'variedad': 'IR-8',
        'suelo': 'franco',
        'clima': 'tropical',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'Sulfato de potasio',
            'dosis': '0.5 qq/manzana',
            'aplicacion': 'Aplicar al pie de la planta',
            'fabricantes': ['Fertica'],
            'precauciones': 'Evitar sobredosis'
        }
    },

    # ======= PRODUCCIÓN =======
    {
        'cultivo': 'arroz',
        'variedad': 'IR-8',
        'suelo': 'arcilloso',
        'clima': 'húmedo',
        'etapa': 'producción',
        'recomendacion': {
            'formula': 'Sulfato de magnesio',
            'dosis': '0.5 qq/manzana',
            'aplicacion': 'Aplicar durante el llenado de grano',
            'fabricantes': ['Fertica'],
            'precauciones': 'Evitar aplicación bajo lluvia intensa'
        }
    },
    {
        'cultivo': 'arroz',
        'variedad': 'IR-8',
        'suelo': 'franco',
        'clima': 'tropical',
        'etapa': 'producción',
        'recomendacion': {
            'formula': 'Fertilizante foliar balanceado',
            'dosis': '0.3 qq/manzana',
            'aplicacion': 'Rociar sobre el follaje',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar a pleno sol'
        }
    },

    # ======= TRASPLANTE (usado en arroz bajo riego o trasplante manual) =======
    {
        'cultivo': 'arroz',
        'variedad': 'IR-8',
        'suelo': 'arcilloso',
        'clima': 'tropical',
        'etapa': 'trasplante',
        'recomendacion': {
            'formula': '12-24-12',
            'dosis': '1 qq/manzana',
            'aplicacion': 'En el agua antes de trasplantar las plántulas',
            'fabricantes': ['Fertica'],
            'precauciones': 'Evitar sobredosis en agua'
        }
    },
    {
        'cultivo': 'arroz',
        'variedad': 'IR-8',
        'suelo': 'franco',
        'clima': 'húmedo',
        'etapa': 'trasplante',
        'recomendacion': {
            'formula': '10-30-10',
            'dosis': '1 qq/manzana',
            'aplicacion': 'Aplicar al fondo del surco antes de trasplantar',
            'fabricantes': ['Yara'],
            'precauciones': 'Cubrir bien raíces y regar suavemente'
        }
    },
    
    # === CAÑA DE AZÚCAR ===
    {
        'cultivo': 'caña',
        'variedad': 'CP 72-2086',
        'suelo': 'franco',
        'clima': 'tropical',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '18-46-0',
            'dosis': '4 qq/manzana',
            'aplicacion': 'Aplicar en banda al momento de la siembra',
            'fabricantes': ['Fertica', 'Yara'],
            'precauciones': 'No aplicar en contacto directo con la semilla'
        }
    },
    {
        'cultivo': 'caña',
        'variedad': 'CP 72-2086',
        'suelo': 'volcánico',
        'clima': 'húmedo',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '3 qq/manzana',
            'aplicacion': 'A los 45 días después de brotación',
            'fabricantes': ['Fertica', 'Profertil'],
            'precauciones': 'Evitar aplicación con suelos saturados de agua'
        }
    },
    {# ============================================  HORTALIZAS  =================================================

        'cultivo': 'caña',
        'variedad': 'CP 72-2086',
        'suelo': 'franco',
        'clima': 'tropical',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'Cloruro de potasio (0-0-60)',
            'dosis': '2 qq/manzana',
            'aplicacion': 'Aplicar en corona al inicio de floración',
            'fabricantes': ['Yara'],
            'precauciones': 'No exceder la dosis para evitar quemaduras'
        }
    },
    {
        'cultivo': 'caña',
        'variedad': 'CP 72-2086',
        'suelo': 'franco',
        'clima': 'tropical',
        'etapa': 'producción',
        'recomendacion': {
            'formula': 'Fertilizante foliar balanceado',
            'dosis': '1 qq/manzana',
            'aplicacion': 'Aplicar en etapa de llenado de tallo',
            'fabricantes': ['Fertica'],
            'precauciones': 'No aplicar en horas de pleno sol'
        }
    },
    
    # === TOMATE ===
    {
        'cultivo': 'tomate',
        'variedad': 'híbrido',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '18-18-21',
            'dosis': '2 qq/manzana',
            'aplicacion': 'Incorporar antes del trasplante',
            'fabricantes': ['Yara'],
            'precauciones': 'Evitar exceso de humedad'
        }
    },
    {
        'cultivo': 'tomate',
        'variedad': 'híbrido',
        'suelo': 'volcánico',
        'clima': 'tropical',
        'etapa': 'trasplante',
        'recomendacion': {
            'formula': '15-15-15',
            'dosis': '1.5 qq/manzana',
            'aplicacion': 'En el fondo del hoyo de trasplante',
            'fabricantes': ['Fertica'],
            'precauciones': 'Cubrir raíz con suficiente suelo'
        }
    },
    {
        'cultivo': 'tomate',
        'variedad': 'híbrido',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '0.7 qq/manzana',
            'aplicacion': '20 días después del trasplante, en corona',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar sobre hojas mojadas'
        }
    },
    {
        'cultivo': 'tomate',
        'variedad': 'híbrido',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'Fertilizante foliar balanceado',
            'dosis': '0.5 qq/manzana',
            'aplicacion': 'Rociar sobre follaje al inicio de floración',
            'fabricantes': ['Fertica'],
            'precauciones': 'No aplicar a pleno sol'
        }
    },
    {
        'cultivo': 'tomate',
        'variedad': 'híbrido',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'producción',
        'recomendacion': {
            'formula': 'Sulfato de potasio',
            'dosis': '0.5 qq/manzana',
            'aplicacion': 'Aplicar durante la fructificación',
            'fabricantes': ['Yara'],
            'precauciones': 'Evitar excesos'
        }
    },

    # === CHILE ===
    {
        'cultivo': 'chile',
        'variedad': 'jalapeño',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '15-15-15',
            'dosis': '1.5 qq/manzana',
            'aplicacion': 'Incorporar al suelo antes de trasplante',
            'fabricantes': ['Fertica'],
            'precauciones': 'Evitar exceso de sales'
        }
    },
    {
        'cultivo': 'chile',
        'variedad': 'jalapeño',
        'suelo': 'volcánico',
        'clima': 'tropical',
        'etapa': 'trasplante',
        'recomendacion': {
            'formula': '18-18-21',
            'dosis': '1 qq/manzana',
            'aplicacion': 'Aplicar en base del hoyo',
            'fabricantes': ['Yara'],
            'precauciones': 'Cubrir raíz completamente'
        }
    },
    {
        'cultivo': 'chile',
        'variedad': 'jalapeño',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '0.5 qq/manzana',
            'aplicacion': '15 días después de trasplante',
            'fabricantes': ['Yara'],
            'precauciones': 'Evitar contacto directo con tallo'
        }
    },
    {
        'cultivo': 'chile',
        'variedad': 'jalapeño',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'Fertilizante foliar balanceado',
            'dosis': '0.3 qq/manzana',
            'aplicacion': 'Rociar sobre follaje',
            'fabricantes': ['Fertica'],
            'precauciones': 'No aplicar a pleno sol'
        }
    },
    {
        'cultivo': 'chile',
        'variedad': 'jalapeño',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'producción',
        'recomendacion': {
            'formula': 'Sulfato de potasio',
            'dosis': '0.3 qq/manzana',
            'aplicacion': 'Aplicar en inicio de cosecha',
            'fabricantes': ['Yara'],
            'precauciones': 'Evitar excesos'
        }
    },

    # === CEBOLLA ===
    {
        'cultivo': 'cebolla',
        'variedad': 'amarilla',
        'suelo': 'arenoso',
        'clima': 'templado',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '12-24-12',
            'dosis': '1.5 qq/manzana',
            'aplicacion': 'Incorporar al fondo del surco',
            'fabricantes': ['Fertica'],
            'precauciones': 'Evitar exceso de agua'
        }
    },
    {
        'cultivo': 'cebolla',
        'variedad': 'amarilla',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'trasplante',
        'recomendacion': {
            'formula': '15-15-15',
            'dosis': '1 qq/manzana',
            'aplicacion': 'Aplicar en base del hoyo',
            'fabricantes': ['Yara'],
            'precauciones': 'Cubrir raíz con tierra'
        }
    },
    {
        'cultivo': 'cebolla',
        'variedad': 'amarilla',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '0.5 qq/manzana',
            'aplicacion': '20 días después de trasplante',
            'fabricantes': ['Fertica'],
            'precauciones': 'No aplicar sobre hojas mojadas'
        }
    },
    {
        'cultivo': 'cebolla',
        'variedad': 'amarilla',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'Fertilizante foliar balanceado',
            'dosis': '0.3 qq/manzana',
            'aplicacion': 'Rociar sobre follaje en inicio de floración',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar en sol intenso'
        }
    },
    {
        'cultivo': 'cebolla',
        'variedad': 'amarilla',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'producción',
        'recomendacion': {
            'formula': 'Sulfato de potasio',
            'dosis': '0.2 qq/manzana',
            'aplicacion': 'Aplicar en desarrollo de bulbo',
            'fabricantes': ['Fertica'],
            'precauciones': 'No exceder dosis'
        }
    },

    # === LECHUGA ===
    {
        'cultivo': 'lechuga',
        'variedad': 'crispada',
        'suelo': 'franco',
        'clima': 'húmedo',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '10-30-10',
            'dosis': '1 qq/manzana',
            'aplicacion': 'En fondo del surco',
            'fabricantes': ['Fertica'],
            'precauciones': 'No aplicar en exceso'
        }
    },
    {
        'cultivo': 'lechuga',
        'variedad': 'crispada',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'trasplante',
        'recomendacion': {
            'formula': '12-24-12',
            'dosis': '1 qq/manzana',
            'aplicacion': 'En hoyo de trasplante',
            'fabricantes': ['Yara'],
            'precauciones': 'Cubrir bien raíces'
        }
    },
    {
        'cultivo': 'lechuga',
        'variedad': 'crispada',
        'suelo': 'franco',
        'clima': 'húmedo',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '0.5 qq/manzana',
            'aplicacion': '15 días después del trasplante',
            'fabricantes': ['Fertica'],
            'precauciones': 'No aplicar sobre hojas mojadas'
        }
    },
    {
        'cultivo': 'lechuga',
        'variedad': 'crispada',
        'suelo': 'franco',
        'clima': 'húmedo',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'Fertilizante foliar balanceado',
            'dosis': '0.2 qq/manzana',
            'aplicacion': 'Rociar sobre follaje en inicio de floración',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar bajo sol fuerte'
        }
    },
    {
        'cultivo': 'lechuga',
        'variedad': 'crispada',
        'suelo': 'franco',
        'clima': 'húmedo',
        'etapa': 'producción',
        'recomendacion': {
            'formula': 'Sulfato de magnesio',
            'dosis': '0.2 qq/manzana',
            'aplicacion': 'Durante el desarrollo de hojas',
            'fabricantes': ['Fertica'],
            'precauciones': 'Evitar acumulación en hojas'
        }
    },

    # === ZANAHORIA ===
    {
        'cultivo': 'zanahoria',
        'variedad': 'nantesa',
        'suelo': 'arenoso',
        'clima': 'templado',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '15-15-15',
            'dosis': '1.5 qq/manzana',
            'aplicacion': 'Aplicar al fondo del surco',
            'fabricantes': ['Yara'],
            'precauciones': 'Evitar acumulación cerca de semillas'
        }
    },
    {
        'cultivo': 'zanahoria',
        'variedad': 'nantesa',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'trasplante',
        'recomendacion': {
            'formula': '12-24-12',
            'dosis': '1 qq/manzana',
            'aplicacion': 'En hoyo de trasplante',
            'fabricantes': ['Fertica'],
            'precauciones': 'Cubrir raíz con tierra'
        }
    },
    {
        'cultivo': 'zanahoria',
        'variedad': 'nantesa',
        'suelo': 'arenoso',
        'clima': 'templado',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '0.5 qq/manzana',
            'aplicacion': '15 días después de la siembra',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar en hojas'
        }
    },
    {
        'cultivo': 'zanahoria',
        'variedad': 'nantesa',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'Fertilizante foliar balanceado',
            'dosis': '0.2 qq/manzana',
            'aplicacion': 'Rociar sobre follaje en inicio de floración',
            'fabricantes': ['Fertica'],
            'precauciones': 'No aplicar bajo sol fuerte'
        }
    },
    {
        'cultivo': 'zanahoria',
        'variedad': 'nantesa',
        'suelo': 'arenoso',
        'clima': 'templado',
        'etapa': 'producción',
        'recomendacion': {
            'formula': 'Sulfato de potasio',
            'dosis': '0.2 qq/manzana',
            'aplicacion': 'Durante el crecimiento de raíces',
            'fabricantes': ['Yara'],
            'precauciones': 'No exceder la dosis'
        }
    },

    # === ESPINACA ===
    {
        'cultivo': 'espinaca',
        'variedad': 'viroflay',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '10-30-10',
            'dosis': '1 qq/manzana',
            'aplicacion': 'Incorporar al suelo antes de siembra',
            'fabricantes': ['Fertica'],
            'precauciones': 'Evitar contacto directo con semilla'
        }
    },
    {
        'cultivo': 'espinaca',
        'variedad': 'viroflay',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'trasplante',
        'recomendacion': {
            'formula': '12-24-12',
            'dosis': '1 qq/manzana',
            'aplicacion': 'En hoyo de trasplante',
            'fabricantes': ['Yara'],
            'precauciones': 'Cubrir raíz'
        }
    },
    {
        'cultivo': 'espinaca',
        'variedad': 'viroflay',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '0.5 qq/manzana',
            'aplicacion': '15 días después del trasplante',
            'fabricantes': ['Fertica'],
            'precauciones': 'No aplicar sobre hojas mojadas'
        }
    },
    {
        'cultivo': 'espinaca',
        'variedad': 'viroflay',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'Fertilizante foliar balanceado',
            'dosis': '0.2 qq/manzana',
            'aplicacion': 'Rociar sobre follaje',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar bajo sol fuerte'
        }
    },
    {
        'cultivo': 'espinaca',
        'variedad': 'viroflay',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'producción',
        'recomendacion': {
            'formula': 'Sulfato de magnesio',
            'dosis': '0.2 qq/manzana',
            'aplicacion': 'Durante la cosecha',
            'fabricantes': ['Fertica'],
            'precauciones': 'Evitar acumulación en hojas'
        }
    },

    # === REPOLLO ===
    {
        'cultivo': 'repollo',
        'variedad': 'corazón de buey',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '15-15-15',
            'dosis': '1.5 qq/manzana',
            'aplicacion': 'Al fondo del surco antes de trasplante',
            'fabricantes': ['Fertica'],
            'precauciones': 'No exceder dosis'
        }
    },
    {
        'cultivo': 'repollo',
        'variedad': 'corazón de buey',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'trasplante',
        'recomendacion': {
            'formula': '12-24-12',
            'dosis': '1 qq/manzana',
            'aplicacion': 'En hoyo de trasplante',
            'fabricantes': ['Yara'],
            'precauciones': 'Cubrir bien raíz'
        }
    },
    {
        'cultivo': 'repollo',
        'variedad': 'corazón de buey',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '0.7 qq/manzana',
            'aplicacion': '20 días después del trasplante',
            'fabricantes': ['Fertica'],
            'precauciones': 'No aplicar sobre hojas mojadas'
        }
    },
    {
        'cultivo': 'repollo',
        'variedad': 'corazón de buey',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'Fertilizante foliar balanceado',
            'dosis': '0.3 qq/manzana',
            'aplicacion': 'Rociar sobre follaje en inicio de floración',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar bajo sol intenso'
        }
    },
    {
        'cultivo': 'repollo',
        'variedad': 'corazón de buey',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'producción',
        'recomendacion': {
            'formula': 'Sulfato de magnesio',
            'dosis': '0.2 qq/manzana',
            'aplicacion': 'Durante el desarrollo de cabeza',
            'fabricantes': ['Fertica'],
            'precauciones': 'No exceder dosis'
        }
    },
    
    # === AYOTE ===
    {
        'cultivo': 'ayote',
        'variedad': 'criollo',
        'suelo': 'volcánico',
        'clima': 'tropical',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '15-15-15',
            'dosis': '1 qq/manzana',
            'aplicacion': 'Incorporar al hoyo de siembra',
            'fabricantes': ['Fertica'],
            'precauciones': 'No aplicar en exceso'
        }
    },
    {
        'cultivo': 'ayote',
        'variedad': 'criollo',
        'suelo': 'franco',
        'clima': 'húmedo',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '0.5 qq/manzana',
            'aplicacion': 'Aplicar 20 días después de la emergencia',
            'fabricantes': ['Yara'],
            'precauciones': 'Evitar contacto directo con hojas'
        }
    },
    {
        'cultivo': 'ayote',
        'variedad': 'criollo',
        'suelo': 'volcánico',
        'clima': 'tropical',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'Fertilizante foliar balanceado',
            'dosis': '0.2 qq/manzana',
            'aplicacion': 'Aplicar en el inicio de la floración',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar a pleno sol'
        }
    },
    {
        'cultivo': 'ayote',
        'variedad': 'criollo',
        'suelo': 'volcánico',
        'clima': 'tropical',
        'etapa': 'producción',
        'recomendacion': {
            'formula': 'Sulfato de potasio',
            'dosis': '0.2 qq/manzana',
            'aplicacion': 'Aplicar durante el llenado de fruto',
            'fabricantes': ['Fertica'],
            'precauciones': 'No exceder la dosis'
        }
    },

    # === GUISQUIL ===
    {
        'cultivo': 'guisquil',
        'variedad': 'verde',
        'suelo': 'volcánico',
        'clima': 'húmedo',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '15-15-15',
            'dosis': '1 qq/manzana',
            'aplicacion': 'Incorporar en el hoyo de siembra',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar en contacto con la semilla'
        }
    },
    {
        'cultivo': 'guisquil',
        'variedad': 'verde',
        'suelo': 'franco',
        'clima': 'húmedo',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '0.5 qq/manzana',
            'aplicacion': '20 días después de siembra',
            'fabricantes': ['Fertica'],
            'precauciones': 'No aplicar en hojas mojadas'
        }
    },
    {
        'cultivo': 'guisquil',
        'variedad': 'verde',
        'suelo': 'volcánico',
        'clima': 'húmedo',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'Fertilizante foliar balanceado',
            'dosis': '0.2 qq/manzana',
            'aplicacion': 'Rociar sobre follaje al inicio de floración',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar a pleno sol'
        }
    },
    {
        'cultivo': 'guisquil',
        'variedad': 'verde',
        'suelo': 'franco',
        'clima': 'húmedo',
        'etapa': 'producción',
        'recomendacion': {
            'formula': 'Sulfato de potasio',
            'dosis': '0.2 qq/manzana',
            'aplicacion': 'Aplicar durante el llenado de fruto',
            'fabricantes': ['Fertica'],
            'precauciones': 'No exceder la dosis'
        }
    },

    # === PIPIAN ===
    {
        'cultivo': 'pipian',
        'variedad': 'criollo',
        'suelo': 'volcánico',
        'clima': 'tropical',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '15-15-15',
            'dosis': '1 qq/manzana',
            'aplicacion': 'Incorporar al hoyo de siembra',
            'fabricantes': ['Fertica'],
            'precauciones': 'No aplicar en exceso'
        }
    },
    {
        'cultivo': 'pipian',
        'variedad': 'criollo',
        'suelo': 'franco',
        'clima': 'tropical',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '0.5 qq/manzana',
            'aplicacion': 'Aplicar 20 días después de emergencia',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar sobre hojas mojadas'
        }
    },
    {
        'cultivo': 'pipian',
        'variedad': 'criollo',
        'suelo': 'volcánico',
        'clima': 'tropical',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'Fertilizante foliar balanceado',
            'dosis': '0.2 qq/manzana',
            'aplicacion': 'Aplicar en el inicio de floración',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar en sol fuerte'
        }
    },
    {
        'cultivo': 'pipian',
        'variedad': 'criollo',
        'suelo': 'franco',
        'clima': 'tropical',
        'etapa': 'producción',
        'recomendacion': {
            'formula': 'Sulfato de potasio',
            'dosis': '0.2 qq/manzana',
            'aplicacion': 'Durante llenado de fruto',
            'fabricantes': ['Fertica'],
            'precauciones': 'No exceder dosis'
        }
    },
    
    # === RABANO ===
    {
        'cultivo': 'rabano',
        'variedad': 'criollo',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '12-24-12',
            'dosis': '0.7 qq/manzana',
            'aplicacion': 'Aplicar al fondo del surco antes de la siembra',
            'fabricantes': ['Fertica'],
            'precauciones': 'Evitar el exceso de fertilizante en la línea de semilla'
        }
    },
    {
        'cultivo': 'rabano',
        'variedad': 'criollo',
        'suelo': 'franco',
        'clima': 'húmedo',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': 'Urea (46-0-0)',
            'dosis': '0.2 qq/manzana',
            'aplicacion': 'Aplicar 10 días después de la emergencia',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar sobre hojas mojadas'
        }
    },
    {
        'cultivo': 'rabano',
        'variedad': 'criollo',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'floración',
        'recomendacion': {
            'formula': 'Fertilizante foliar balanceado',
            'dosis': '0.1 qq/manzana',
            'aplicacion': 'Rociar sobre el follaje cuando empiecen a formarse las flores',
            'fabricantes': ['Yara'],
            'precauciones': 'No aplicar bajo sol fuerte'
        }
    },
    {
        'cultivo': 'rabano',
        'variedad': 'criollo',
        'suelo': 'franco',
        'clima': 'húmedo',
        'etapa': 'producción',
        'recomendacion': {
            'formula': 'Sulfato de potasio',
            'dosis': '0.1 qq/manzana',
            'aplicacion': 'Aplicar en etapa de engrosamiento de raíz',
            'fabricantes': ['Fertica'],
            'precauciones': 'Evitar acumulación en hojas'
        }
    },
    {
        'cultivo': 'rabano',
        'variedad': 'criollo',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'trasplante',
        'recomendacion': {
            'formula': '10-30-10',
            'dosis': '0.5 qq/manzana',
            'aplicacion': 'En el hoyo de trasplante si se usa almácigo',
            'fabricantes': ['Fertica'],
            'precauciones': 'Cubrir raíces, regar suavemente'
        }
    }
]

# === PARAMETROS PARA INTERFAZ ===
PARAMETROS = {
    'cultivos': [
        'maiz', 'frijol', 'sorgo', 'arroz', 'caña',
        'tomate', 'chile', 'cebolla', 'lechuga', 'zanahoria',
        'espinaca', 'repollo', 'ayote', 'guisquil', 'pipian', 'rabano'
    ],
    'variedades': {
        'maiz': ['híbrido', 'criollo'],
        'frijol': ['rojo de seda', 'negro'],
        'arroz': ['IR-8'],
        'caña': ['CP 72-2086'],
        'tomate': ['híbrido'],
        'chile': ['jalapeño'],
        'cebolla': ['amarilla'],
        'lechuga': ['crispada'],
        'zanahoria': ['nantesa'],
        'espinaca': ['viroflay'],
        'repollo': ['corazón de buey'],
        'ayote': ['criollo'],
        'guisquil': ['verde'],
        'pipian': ['criollo'],
        'rabano': ['criollo']
    },
    'suelos': ['arcilloso', 'arenoso', 'volcánico', 'franco', 'limo'],
    'climas': ['tropical', 'seco', 'húmedo', 'templado'],
    'etapas': ['siembra', 'trasplante', 'desarrollo', 'floración', 'producción']
}
