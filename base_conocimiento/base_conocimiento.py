# -*- coding: utf-8 -*-
"""
BASE DE CONOCIMIENTO PARA AGRICULTURA EN EL SALVADOR
Datos técnicos validados por INSAFO y literatura técnica Mesoamericana.
Última actualización: Julio 2023
"""

# === FERTILIZANTES QUÍMICOS PARA GRANOS BÁSICOS Y HORTALIZAS ===
FERTILIZANTES = [
    # === MAÍZ ===
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
        'suelo': 'arenoso',
        'clima': 'seco',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '12-30-10 + micronutrientes',
            'dosis': '2.5 qq/manzana',
            'aplicacion': 'Incorporar 5 cm debajo de la semilla',
            'fabricantes': ['Fertica'],
            'precauciones': 'Requiere riego inmediato post-aplicación'
        }
    },
    {
        'cultivo': 'maiz',
        'variedad': 'híbrido',
        'suelo': 'arcilloso',
        'clima': 'tropical',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': '46-0-0 (Urea)',
            'dosis': '2 qq/manzana',
            'aplicacion': 'Aplicar a los 25-30 días después de siembra, en banda',
            'fabricantes': ['Fertica', 'Yara'],
            'precauciones': 'Evitar aplicación en horas calurosas'
        }
    },
    # === FRIJOL ===
    {
        'cultivo': 'frijol',
        'variedad': 'rojo de seda',
        'suelo': 'volcánico',
        'clima': 'húmedo',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '10-30-10',
            'dosis': '2 qq/manzana',
            'aplicacion': 'Aplicar en banda a 5 cm de profundidad',
            'fabricantes': ['Profertil'],
            'precauciones': 'No aplicar en contacto directo con semilla'
        }
    },
    {
        'cultivo': 'frijol',
        'variedad': 'negro',
        'suelo': 'arenoso',
        'clima': 'seco',
        'etapa': 'floración',
        'recomendacion': {
            'formula': '15-5-30 + 2MgO',
            'dosis': '1.5 qq/manzana',
            'aplicacion': 'Aplicación foliar en horas tempranas',
            'fabricantes': ['Yara'],
            'precauciones': 'Suspender si lluvia pronosticada en 24h'
        }
    },
    # === SORGO ===
    {
        'cultivo': 'sorgo',
        'variedad': 'granífero',
        'suelo': 'arcilloso',
        'clima': 'seco',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '80-60-00 + Zn (mezcla física)',
            'dosis': '3 qq/manzana',
            'aplicacion': 'Incorporar pre-siembra con rastra',
            'fabricantes': ['Fertica'],
            'precauciones': 'Requiere análisis de suelo previo'
        }
    },
    # === ARROZ ===
    {
        'cultivo': 'arroz',
        'variedad': 'IR-8',
        'suelo': 'franco',
        'clima': 'húmedo',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '15-15-15',
            'dosis': '2.5 qq/manzana',
            'aplicacion': 'Aplicar al voleo antes de la inundación',
            'fabricantes': ['Profertil'],
            'precauciones': 'No aplicar si suelo saturado'
        }
    },
    # === CAÑA DE AZÚCAR ===
    {
        'cultivo': 'caña',
        'variedad': 'CP 72-2086',
        'suelo': 'franco',
        'clima': 'tropical',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': '25-5-15 + 4S + 1Zn',
            'dosis': '4 qq/manzana',
            'aplicacion': 'Aplicación en banda a 30 cm de planta',
            'fabricantes': ['Profertil'],
            'precauciones': 'No aplicar con vientos >15 km/h'
        }
    },
    # === TOMATE ===
    {
        'cultivo': 'tomate',
        'variedad': 'híbrido',
        'suelo': 'franco',
        'clima': 'tropical',
        'etapa': 'trasplante',
        'recomendacion': {
            'formula': '15-15-15 + Ca + Mg',
            'dosis': '250 lb/manzana',
            'aplicacion': 'Incorporar en hoyo de trasplante',
            'fabricantes': ['Yara'],
            'precauciones': 'Evitar contacto directo con raíces'
        }
    },
    {
        'cultivo': 'tomate',
        'variedad': 'híbrido',
        'suelo': 'franco',
        'clima': 'tropical',
        'etapa': 'floración',
        'recomendacion': {
            'formula': '12-6-24 + 2MgO + micronutrientes',
            'dosis': '3 aplicaciones foliares de 10 lb/manzana',
            'aplicacion': 'Pulverización foliar cada 15 días',
            'fabricantes': ['Haifa'],
            'precauciones': 'Aplicar solo con humedad relativa >60%'
        }
    },
    # === CHILE ===
    {
        'cultivo': 'chile',
        'variedad': 'jalapeño',
        'suelo': 'arenoso',
        'clima': 'seco',
        'etapa': 'producción',
        'recomendacion': {
            'formula': '13-5-30 + Ca + B',
            'dosis': '20 lb/manzana por riego fertirrigado',
            'aplicacion': 'Aplicar cada 15 días vía riego por goteo',
            'fabricantes': ['ICL'],
            'precauciones': 'Regular pH del agua a 5.8-6.2'
        }
    },
    # === CEBOLLA ===
    {
        'cultivo': 'cebolla',
        'variedad': 'amarilla',
        'suelo': 'franco',
        'clima': 'tropical',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '12-24-12 + Mg',
            'dosis': '2 qq/manzana',
            'aplicacion': 'Aplicar al voleo y mezclar en la cama',
            'fabricantes': ['Fertica'],
            'precauciones': 'Evitar excesos para no inhibir germinación'
        }
    },
    # === LECHUGA ===
    {
        'cultivo': 'lechuga',
        'variedad': 'crispada',
        'suelo': 'franco',
        'clima': 'tropical',
        'etapa': 'trasplante',
        'recomendacion': {
            'formula': '15-15-15 + Ca',
            'dosis': '150 lb/manzana',
            'aplicacion': 'En hoyo al trasplantar, mezclado con tierra',
            'fabricantes': ['ICL'],
            'precauciones': 'No sobredosificar, puede quemar raíces'
        }
    },
    # === ZANAHORIA ===
    {
        'cultivo': 'zanahoria',
        'variedad': 'nantesa',
        'suelo': 'limo',
        'clima': 'templado',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '12-30-10',
            'dosis': '2 qq/manzana',
            'aplicacion': 'Aplicar e incorporar antes de la siembra',
            'fabricantes': ['Profertil'],
            'precauciones': 'Realizar análisis de suelo previo'
        }
    },
    # === ESPINACA ===
    {
        'cultivo': 'espinaca',
        'variedad': 'viroflay',
        'suelo': 'franco',
        'clima': 'templado',
        'etapa': 'trasplante',
        'recomendacion': {
            'formula': '10-20-20 + B',
            'dosis': '1.5 qq/manzana',
            'aplicacion': 'Aplicar al trasplante, cubrir con tierra',
            'fabricantes': ['Profertil'],
            'precauciones': 'Mantener humedad sin encharcamiento'
        }
    },
    # === REPOLLO ===
    {
        'cultivo': 'repollo',
        'variedad': 'corazón de buey',
        'suelo': 'franco',
        'clima': 'tropical',
        'etapa': 'trasplante',
        'recomendacion': {
            'formula': '15-15-15 + Mg',
            'dosis': '2 qq/manzana',
            'aplicacion': 'Mezclar en la cama de trasplante',
            'fabricantes': ['ICL'],
            'precauciones': 'Mantener riego moderado'
        }
    },
    # === AYOTE ===
    {
        'cultivo': 'ayote',
        'variedad': 'criollo',
        'suelo': 'arenoso',
        'clima': 'tropical',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '12-24-12 + B',
            'dosis': '1 qq/manzana',
            'aplicacion': 'Al voleo previo a la siembra',
            'fabricantes': ['Fertica'],
            'precauciones': 'No aplicar en exceso'
        }
    },
    # === GUISQUIL ===
    {
        'cultivo': 'guisquil',
        'variedad': 'verde',
        'suelo': 'volcánico',
        'clima': 'húmedo',
        'etapa': 'desarrollo',
        'recomendacion': {
            'formula': '10-30-10',
            'dosis': '1 qq/manzana',
            'aplicacion': 'Aplicar a pie de planta cada 60 días',
            'fabricantes': ['Profertil'],
            'precauciones': 'Evitar contacto directo con tallo'
        }
    },
    # === PIPIAN ===
    {
        'cultivo': 'pipian',
        'variedad': 'criollo',
        'suelo': 'arcilloso',
        'clima': 'húmedo',
        'etapa': 'siembra',
        'recomendacion': {
            'formula': '10-30-10 + B',
            'dosis': '1.5 qq/manzana',
            'aplicacion': 'Incorporar antes de siembra',
            'fabricantes': ['Fertica'],
            'precauciones': 'Regar inmediatamente tras aplicación'
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
            'formula': '10-20-20',
            'dosis': '1 qq/manzana',
            'aplicacion': 'Incorporar superficialmente antes de siembra',
            'fabricantes': ['Profertil'],
            'precauciones': 'Evitar exceso de agua en primeras semanas'
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
