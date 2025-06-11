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
    {
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
    # ============================================  HORTALIZAS  =================================================

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

# === PLAGAS Y ENFERMEDADES PRINCIPALES ===
PLAGAS = [
    # === MAÍZ ===
    {
        'cultivo': 'maiz',
        'plaga': 'Gusano cogollero (Spodoptera frugiperda)',
        'sintomas': [
            'hojas raspadas',
            'orificios en hojas nuevas',
            'excremento de larva visible',
            'cogollo dañado'
        ],
        'umbral': '5% plantas afectadas',
        'tratamientos': [
            {
                'producto': 'Coragen 20SC',
                'ingrediente': 'Clorantraniliprol 20%',
                'dosis': '10 ml/100 L agua',
                'intervalo': '15 días',
                'clase': 'Diamida',
                'restricciones': 'Máximo 2 aplicaciones por ciclo'
            }
        ],
        'estrategia': 'Aplicar en horas de la tarde cuando larvas están activas'
    },
    {
        'cultivo': 'maiz',
        'plaga': 'Mancha foliar de Maíz (Bipolaris maydis)',
        'sintomas': [
            'manchas alargadas color marrón',
            'necrosis marginal en hojas',
            'manchas con halo clorótico'
        ],
        'umbral': '10% plantas con síntomas',
        'tratamientos': [
            {
                'producto': 'Opera',
                'ingrediente': 'Pyraclostrobin + Epoxiconazole',
                'dosis': '1 l/ha',
                'intervalo': 'Aplicar a la aparición',
                'clase': 'Estrobilurina + triazol',
                'restricciones': 'No aplicar con viento fuerte'
            }
        ],
        'estrategia': 'Rotar con otros fungicidas'
    },
    # === FRIJOL ===
    {
        'cultivo': 'frijol',
        'plaga': 'Mosca blanca (Bemisia tabaci)',
        'sintomas': [
            'melaza en hojas',
            'fumagina',
            'amarillamiento',
            'enrollamiento hojas'
        ],
        'umbral': '10 adultos/hoja',
        'tratamientos': [
            {
                'producto': 'Actara 25WG',
                'ingrediente': 'Tiametoxam 25%',
                'dosis': '50 g/100 L agua',
                'intervalo': '21 días',
                'clase': 'Neonicotinoide',
                'restricciones': 'No aplicar en floración'
            }
        ],
        'estrategia': 'Rotar con productos de diferente grupo químico'
    },
    {
        'cultivo': 'frijol',
        'plaga': 'Antracnosis',
        'sintomas': [
            'manchas hundidas en vainas',
            'hojas con bordes secos',
            'tallo con lesiones negras'
        ],
        'umbral': 'Primeras lesiones visibles',
        'tratamientos': [
            {
                'producto': 'Cercobin 50WP',
                'ingrediente': 'Carbendazim 50%',
                'dosis': '1 g/L agua',
                'intervalo': '10-14 días',
                'clase': 'Benzimidazol',
                'restricciones': 'Máximo 2 aplicaciones por ciclo'
            }
        ],
        'estrategia': 'Eliminar restos de cosecha'
    },
    # === SORGO ===
    {
        'cultivo': 'sorgo',
        'plaga': 'Pulgón amarillo del sorgo (Melanaphis sacchari)',
        'sintomas': [
            'manchas amarillas en hojas',
            'melaza pegajosa',
            'hormigas en la planta'
        ],
        'umbral': '20 pulgones por hoja',
        'tratamientos': [
            {
                'producto': 'Transform WG',
                'ingrediente': 'Sulfoxaflor',
                'dosis': '0.1 g/L agua',
                'intervalo': '10 días',
                'clase': 'Sulfoximina',
                'restricciones': 'No aplicar durante floración'
            }
        ],
        'estrategia': 'Monitoreo semanal en campo'
    },
    # === ARROZ ===
    {
        'cultivo': 'arroz',
        'plaga': 'Barrenador del tallo (Scirpophaga incertulas)',
        'sintomas': [
            'tallos vacíos',
            'espigas blancas',
            'pupas dentro del tallo'
        ],
        'umbral': '5% plantas afectadas',
        'tratamientos': [
            {
                'producto': 'Virtako 60WG',
                'ingrediente': 'Clorantraniliprol + Lambda cihalotrina',
                'dosis': '60 g/ha',
                'intervalo': '15 días',
                'clase': 'Diamida + piretroide',
                'restricciones': 'Intervalo de seguridad 20 días'
            }
        ],
        'estrategia': 'Eliminar socas después de cosecha'
    },
    # === TOMATE ===
    {
        'cultivo': 'tomate',
        'plaga': 'Tuta absoluta',
        'sintomas': [
            'minas en hojas',
            'galerías en frutos',
            'necrosis de tejidos'
        ],
        'umbral': '3 adultos/trampa/semana',
        'tratamientos': [
            {
                'producto': 'Proclaim 5SG',
                'ingrediente': 'Emamectina benzoato 5%',
                'dosis': '500 g/ha',
                'intervalo': '7 días',
                'clase': 'Avermectina',
                'restricciones': 'Intervalo de seguridad 3 días'
            }
        ],
        'estrategia': 'Combina aplicaciones foliares con trampeo masivo'
    },
    {
        'cultivo': 'tomate',
        'plaga': 'Tizón tardío (Phytophthora infestans)',
        'sintomas': [
            'manchas marrón oscuro en hojas',
            'frutos con áreas acuosas',
            'hojas con bordes marchitos'
        ],
        'umbral': 'Aparición de los primeros síntomas',
        'tratamientos': [
            {
                'producto': 'Ridomil Gold',
                'ingrediente': 'Metalaxil-M + Mancozeb',
                'dosis': '2.5 g/L agua',
                'intervalo': '10 días',
                'clase': 'Fungicida sistémico',
                'restricciones': 'No aplicar después de cuaje'
            }
        ],
        'estrategia': 'Eliminar hojas enfermas, aplicar preventivo en época de lluvias'
    },
    # === CHILE ===
    {
        'cultivo': 'chile',
        'plaga': 'Trips (Frankliniella occidentalis)',
        'sintomas': [
            'manchas plateadas en hojas',
            'hojas deformadas',
            'frutos con cicatrices'
        ],
        'umbral': '5 trips por hoja',
        'tratamientos': [
            {
                'producto': 'Success 48SC',
                'ingrediente': 'Spinosad 48%',
                'dosis': '1 ml/L agua',
                'intervalo': '7 días',
                'clase': 'Espinosina',
                'restricciones': 'No aplicar durante floración'
            }
        ],
        'estrategia': 'Monitorear con trampas azules'
    },
    # === CEBOLLA ===
    {
        'cultivo': 'cebolla',
        'plaga': 'Mosca de la cebolla (Delia antiqua)',
        'sintomas': [
            'plántulas caídas',
            'bulbo podrido',
            'presencia de larvas'
        ],
        'umbral': '2 larvas/planta',
        'tratamientos': [
            {
                'producto': 'Lorsban 480EC',
                'ingrediente': 'Clorpirifos 48%',
                'dosis': '2 ml/L agua',
                'intervalo': '15 días',
                'clase': 'Organofosforado',
                'restricciones': 'Respetar periodo de carencia'
            }
        ],
        'estrategia': 'Rotar con otros ingredientes activos'
    },
    # === LECHUGA ===
    {
        'cultivo': 'lechuga',
        'plaga': 'Pulgón verde (Nasonovia ribisnigri)',
        'sintomas': [
            'hojas enrolladas',
            'colonia de insectos verdes',
            'mielada en hojas'
        ],
        'umbral': '5 pulgones/planta',
        'tratamientos': [
            {
                'producto': 'Movento 100SC',
                'ingrediente': 'Spirotetramat 10%',
                'dosis': '0.75 ml/L agua',
                'intervalo': '14 días',
                'clase': 'Tetramic acid',
                'restricciones': 'No aplicar antes de cosecha'
            }
        ],
        'estrategia': 'Usar jabón potásico previo a tratamiento'
    },
    # === ZANAHORIA ===
    {
        'cultivo': 'zanahoria',
        'plaga': 'Mosca de la zanahoria (Psila rosae)',
        'sintomas': [
            'galerías en raíz',
            'raíz deformada',
            'presencia de larvas'
        ],
        'umbral': '1 larva/raíz',
        'tratamientos': [
            {
                'producto': 'Decis 25EC',
                'ingrediente': 'Deltametrina 25%',
                'dosis': '1 ml/L agua',
                'intervalo': '10 días',
                'clase': 'Piretroide',
                'restricciones': 'No aplicar con alta temperatura'
            }
        ],
        'estrategia': 'Evitar siembra en zonas infestadas'
    },
    # === ESPINACA ===
    {
        'cultivo': 'espinaca',
        'plaga': 'Minador de hoja (Liriomyza spp.)',
        'sintomas': [
            'manchas blancas irregulares',
            'hojas con galerías',
            'reducción de crecimiento'
        ],
        'umbral': '3 minadores/hoja',
        'tratamientos': [
            {
                'producto': 'Agri-Mek 1.8 EC',
                'ingrediente': 'Abamectina 1.8%',
                'dosis': '1 ml/L agua',
                'intervalo': '7 días',
                'clase': 'Avermectina',
                'restricciones': 'Intervalo de seguridad 7 días'
            }
        ],
        'estrategia': 'Eliminar hojas afectadas'
    },
    # === REPOLLO ===
    {
        'cultivo': 'repollo',
        'plaga': 'Palomilla de la col (Plutella xylostella)',
        'sintomas': [
            'orificios en hojas',
            'larvas en envés de hojas',
            'excremento granular'
        ],
        'umbral': '1 larva/planta',
        'tratamientos': [
            {
                'producto': 'Bacillus thuringiensis',
                'ingrediente': 'Bt kurstaki',
                'dosis': '0.5 g/L agua',
                'intervalo': '7 días',
                'clase': 'Microbiológico',
                'restricciones': 'Repetir después de lluvia'
            }
        ],
        'estrategia': 'Rotar cultivos, monitoreo constante'
    },
    # === AYOTE ===
    {
        'cultivo': 'ayote',
        'plaga': 'Antracnosis (Colletotrichum orbiculare)',
        'sintomas': [
            'manchas negruzcas en fruto',
            'hojas con lesiones circulares',
            'caída prematura de hojas'
        ],
        'umbral': 'Primeros síntomas',
        'tratamientos': [
            {
                'producto': 'Score 250EC',
                'ingrediente': 'Difenoconazol 25%',
                'dosis': '0.5 ml/L agua',
                'intervalo': '10 días',
                'clase': 'Triazol',
                'restricciones': 'No aplicar durante floración'
            }
        ],
        'estrategia': 'Aplicar a la aparición de síntomas'
    },
    # === GUISQUIL ===
    {
        'cultivo': 'guisquil',
        'plaga': 'Oídio (Erysiphe cichoracearum)',
        'sintomas': [
            'manchas blancas en hojas',
            'polvo blanco en tallos',
            'enrollamiento de hojas'
        ],
        'umbral': 'Primeras manchas',
        'tratamientos': [
            {
                'producto': 'Azufre mojable',
                'ingrediente': 'Azufre',
                'dosis': '2 g/L agua',
                'intervalo': '7 días',
                'clase': 'Inorgánico',
                'restricciones': 'No aplicar con alta humedad'
            }
        ],
        'estrategia': 'Retirar hojas afectadas'
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
    'etapas': ['siembra', 'trasplante', 'desarrollo', 'floración', 'producción'],
    'sintomas': list(sorted(set(s for p in PLAGAS for s in p['sintomas'])))
}
