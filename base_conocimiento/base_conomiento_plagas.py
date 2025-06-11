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
        'plaga': 'Gusano elotero (Helicoverpa zea)',
        'sintomas': [
            'orificios en el elote',
            'presencia de larvas en la mazorca',
            'granos dañados en la punta'
        ],
        'umbral': 'Presencia en más del 10% de mazorcas',
        'tratamientos': [
            {
                'producto': 'Intrepid 2F',
                'ingrediente': 'Metoxifenozida 22.6%',
                'dosis': '100 ml/bomba de 20 L',
                'intervalo': 'Cada 10-14 días',
                'clase': 'Regulador de crecimiento',
                'restricciones': 'No aplicar en floración'
            }
        ],
        'estrategia': 'Revisar puntas de mazorca a partir de inicio de llenado'
    },
    {
        'cultivo': 'maiz',
        'plaga': 'Pulgón amarillo (Rhopalosiphum maidis)',
        'sintomas': [
            'hojas enrolladas y pegajosas',
            'presencia de insectos pequeños amarillos',
            'melaza en hojas'
        ],
        'umbral': '20% plantas infestadas',
        'tratamientos': [
            {
                'producto': 'Confidor',
                'ingrediente': 'Imidacloprid',
                'dosis': '0.5 ml/L agua',
                'intervalo': 'Una aplicación al detectar plaga',
                'clase': 'Neonicotinoide',
                'restricciones': 'Evitar contacto con abejas'
            }
        ],
        'estrategia': 'Monitorear desde etapa de plántula'
    },
    {
        'cultivo': 'maiz',
        'plaga': 'Gallina ciega (Phyllophaga spp.)',
        'sintomas': [
            'plántulas arrancadas o marchitas',
            'raíces comidas',
            'presencia de larvas blancas en el suelo'
        ],
        'umbral': 'Detectar 2-3 larvas/m2 de suelo',
        'tratamientos': [
            {
                'producto': 'Lorsban',
                'ingrediente': 'Clorpirifos',
                'dosis': '2 l/ha',
                'intervalo': 'Al momento de la siembra',
                'clase': 'Organofosforado',
                'restricciones': 'No aplicar en presencia de abejas'
            }
        ],
        'estrategia': 'Preparar suelo y aplicar tratamiento antes de la siembra'
    },

    # === ENFERMEDADES ===
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
    {
        'cultivo': 'maiz',
        'plaga': 'Tizón de la hoja (Exserohilum turcicum)',
        'sintomas': [
            'manchas elípticas marrón grisáceo',
            'bordes definidos en manchas',
            'manchas en hojas medias y superiores'
        ],
        'umbral': '10% plantas afectadas',
        'tratamientos': [
            {
                'producto': 'Amistar Xtra',
                'ingrediente': 'Azoxystrobin + Ciproconazol',
                'dosis': '1 l/ha',
                'intervalo': 'Aplicar a la aparición',
                'clase': 'Estrobilurina + triazol',
                'restricciones': 'No aplicar en lluvia'
            }
        ],
        'estrategia': 'Realizar aplicaciones preventivas si hay historial'
    },
    {
        'cultivo': 'maiz',
        'plaga': 'Roya común (Puccinia sorghi)',
        'sintomas': [
            'pústulas anaranjadas en hojas',
            'manchas cloróticas alrededor de pústulas',
            'hojas secas prematuramente'
        ],
        'umbral': '5% plantas con pústulas',
        'tratamientos': [
            {
                'producto': 'Tilt 250 EC',
                'ingrediente': 'Propiconazole',
                'dosis': '0.5 l/ha',
                'intervalo': 'Cada 15 días según presencia',
                'clase': 'Triazol',
                'restricciones': 'No aplicar cerca de cosecha'
            }
        ],
        'estrategia': 'Favorecer buena ventilación y evitar monocultivo'
    },
    {
        'cultivo': 'maiz',
        'plaga': 'Carbón de la espiga (Ustilago maydis)',
        'sintomas': [
            'tumores grises o negros en espigas',
            'espigas deformadas',
            'granulosidad y malformación de granos'
        ],
        'umbral': 'Presencia en cualquier parte del lote',
        'tratamientos': [
            {
                'producto': 'Eliminar plantas afectadas',
                'ingrediente': '---',
                'dosis': '---',
                'intervalo': 'Inmediato',
                'clase': 'Cultural',
                'restricciones': 'No hay tratamiento químico efectivo'
            }
        ],
        'estrategia': 'Rotación de cultivos y selección de semillas sanas'
    },

    # === FRIJOL ===
    {
        'cultivo': 'frijol',
        'plaga': 'Mosca blanca (Bemisia tabaci)',
        'sintomas': [
            'hojas amarillas',
            'presencia de insectos blancos en el envés',
            'melaza y fumagina en hojas'
        ],
        'umbral': '20% plantas infestadas',
        'tratamientos': [
            {
                'producto': 'Confidor 350 SC',
                'ingrediente': 'Imidacloprid',
                'dosis': '0.5 ml/L agua',
                'intervalo': 'A la detección de plaga',
                'clase': 'Neonicotinoide',
                'restricciones': 'No aplicar en floración para proteger abejas'
            }
        ],
        'estrategia': 'Monitorear constantemente y evitar monocultivo'
    },
    {
        'cultivo': 'frijol',
        'plaga': 'Trips (Thrips palmi)',
        'sintomas': [
            'hojas plateadas o bronceadas',
            'deformación de hojas jóvenes',
            'manchas necróticas en bordes'
        ],
        'umbral': '10% plantas afectadas',
        'tratamientos': [
            {
                'producto': 'Spintor 120 SC',
                'ingrediente': 'Spinosad',
                'dosis': '1 ml/L agua',
                'intervalo': 'Aplicar a la detección',
                'clase': 'Espinosinas',
                'restricciones': 'Evitar aplicaciones repetidas'
            }
        ],
        'estrategia': 'Rotar con otros insecticidas'
    },
    {
        'cultivo': 'frijol',
        'plaga': 'Pulgón negro (Aphis craccivora)',
        'sintomas': [
            'hojas rizadas',
            'presencia de insectos negros',
            'melaza pegajosa en las hojas'
        ],
        'umbral': '15% plantas infestadas',
        'tratamientos': [
            {
                'producto': 'Actara 25WG',
                'ingrediente': 'Thiamethoxam',
                'dosis': '0.2 g/L agua',
                'intervalo': 'Una aplicación por ciclo',
                'clase': 'Neonicotinoide',
                'restricciones': 'Evitar aplicaciones en floración'
            }
        ],
        'estrategia': 'Control biológico con mariquitas'
    },
    # === ENFERMEDADES ===
    {
        'cultivo': 'frijol',
        'plaga': 'Antracnosis (Colletotrichum lindemuthianum)',
        'sintomas': [
            'manchas hundidas oscuras en tallos y vainas',
            'hojas con bordes necróticos',
            'caída prematura de hojas'
        ],
        'umbral': '5% plantas con síntomas',
        'tratamientos': [
            {
                'producto': 'Dithane M-45',
                'ingrediente': 'Mancozeb',
                'dosis': '2 g/L agua',
                'intervalo': 'Cada 7 días mientras haya síntomas',
                'clase': 'Ditiocarbamato',
                'restricciones': 'No aplicar cerca de cosecha'
            }
        ],
        'estrategia': 'Usar semilla certificada y eliminar restos de cosecha'
    },
    {
        'cultivo': 'frijol',
        'plaga': 'Mildiu polvoso (Erysiphe polygoni)',
        'sintomas': [
            'polvo blanco sobre hojas',
            'amarillamiento de hojas',
            'defoliación prematura'
        ],
        'umbral': '10% plantas afectadas',
        'tratamientos': [
            {
                'producto': 'Topas 100 EC',
                'ingrediente': 'Penconazole',
                'dosis': '0.5 ml/L agua',
                'intervalo': 'Cada 10 días',
                'clase': 'Triazol',
                'restricciones': 'No aplicar en lluvia'
            }
        ],
        'estrategia': 'Favorecer ventilación y evitar riegos nocturnos'
    },
    {
        'cultivo': 'frijol',
        'plaga': 'Bacteriosis común (Xanthomonas axonopodis pv. phaseoli)',
        'sintomas': [
            'manchas angulares acuosas en hojas',
            'bordes amarillos en lesiones',
            'caída de hojas con lesiones severas'
        ],
        'umbral': '5% plantas con síntomas',
        'tratamientos': [
            {
                'producto': 'Nordox Super 75 WG',
                'ingrediente': 'Óxido cuproso',
                'dosis': '2 g/L agua',
                'intervalo': 'Cada 7 días en brotes',
                'clase': 'Cúprico',
                'restricciones': 'No aplicar con altas temperaturas'
            }
        ],
        'estrategia': 'Rotar cultivos y evitar exceso de humedad'
    },

    # === SORGO ===
    {
        'cultivo': 'sorgo',
        'plaga': 'Pulgón amarillo del sorgo (Melanaphis sacchari)',
        'sintomas': [
            'colonias de pulgones en el envés',
            'hojas amarillas y pegajosas',
            'melaza y presencia de fumagina'
        ],
        'umbral': '10% plantas infestadas',
        'tratamientos': [
            {
                'producto': 'Transform WG',
                'ingrediente': 'Sulfoxaflor',
                'dosis': '0.1 g/L agua',
                'intervalo': 'Aplicar a la detección',
                'clase': 'Sulfoximina',
                'restricciones': 'No aplicar cerca de colmenas'
            }
        ],
        'estrategia': 'Monitorear desde plántula y eliminar malezas cercanas'
    },
    {
        'cultivo': 'sorgo',
        'plaga': 'Mosca de la hoja (Atherigona soccata)',
        'sintomas': [
            'hojas centrales marchitas',
            'plántulas quebradas',
            'tallos secos desde la base'
        ],
        'umbral': 'Presencia en 5% de plántulas',
        'tratamientos': [
            {
                'producto': 'Lorsban 4E',
                'ingrediente': 'Clorpirifos',
                'dosis': '1.5 ml/L agua',
                'intervalo': 'Al detectar plaga',
                'clase': 'Organofosforado',
                'restricciones': 'Evitar aplicación en viento fuerte'
            }
        ],
        'estrategia': 'Aplicar temprano en la mañana'
    },
    # === ENFERMEDADES ===
    {
        'cultivo': 'sorgo',
        'plaga': 'Mancha de ascochyta (Ascochyta sorghi)',
        'sintomas': [
            'manchas ovales marrón con centro claro',
            'lesiones en hojas viejas',
            'hojas secas en la base de la planta'
        ],
        'umbral': '10% plantas afectadas',
        'tratamientos': [
            {
                'producto': 'Dithane M-45',
                'ingrediente': 'Mancozeb',
                'dosis': '2 g/L agua',
                'intervalo': 'Cada 7 días mientras haya síntomas',
                'clase': 'Ditiocarbamato',
                'restricciones': 'No aplicar en pre-cosecha'
            }
        ],
        'estrategia': 'Eliminar residuos y alternar cultivos'
    },
    {
        'cultivo': 'sorgo',
        'plaga': 'Carbón del sorgo (Sporisorium sorghi)',
        'sintomas': [
            'espigas deformadas con masas negras',
            'granos cubiertos de polvo negro',
            'tallos débiles'
        ],
        'umbral': 'Presencia en cualquier parte del lote',
        'tratamientos': [
            {
                'producto': 'Tratamiento de semilla con fungicida',
                'ingrediente': 'Tebuconazole',
                'dosis': 'Según etiqueta',
                'intervalo': 'Antes de la siembra',
                'clase': 'Triazol',
                'restricciones': 'No aplicar en siembra directa'
            }
        ],
        'estrategia': 'Usar semilla certificada y rotar cultivos'
    },
    {
        'cultivo': 'sorgo',
        'plaga': 'Roya del sorgo (Puccinia purpurea)',
        'sintomas': [
            'pústulas marrón-rojizas en hojas',
            'amarillamiento y secado prematuro de hojas',
            'baja producción de grano'
        ],
        'umbral': '10% plantas con pústulas',
        'tratamientos': [
            {
                'producto': 'Tilt 250 EC',
                'ingrediente': 'Propiconazole',
                'dosis': '0.5 l/ha',
                'intervalo': 'Cada 15 días según presencia',
                'clase': 'Triazol',
                'restricciones': 'No aplicar cerca de cosecha'
            }
        ],
        'estrategia': 'Evitar monocultivo y favorecer ventilación'
    },

    # === ARROZ ===
    {
        'cultivo': 'arroz',
        'plaga': 'Barrenador del tallo (Scirpophaga incertulas)',
        'sintomas': [
            'tallos huecos o partidos',
            'hojas centrales secas ("corazón muerto")',
            'presencia de larvas dentro del tallo'
        ],
        'umbral': '5% tallos afectados',
        'tratamientos': [
            {
                'producto': 'Regent 3GR',
                'ingrediente': 'Fipronil',
                'dosis': '25 kg/ha',
                'intervalo': 'Al momento de la siembra',
                'clase': 'Fenilpirazol',
                'restricciones': 'No aplicar cerca de cosecha'
            }
        ],
        'estrategia': 'Rotar productos y monitorear desde plántula'
    },
    {
        'cultivo': 'arroz',
        'plaga': 'Chinche del arroz (Oebalus poecilus)',
        'sintomas': [
            'granos con manchas negras',
            'granos vanos o vacíos',
            'insectos sobre espigas'
        ],
        'umbral': '10% espigas infestadas',
        'tratamientos': [
            {
                'producto': 'Decis 25EC',
                'ingrediente': 'Deltametrina',
                'dosis': '0.5 ml/L agua',
                'intervalo': 'Aplicar a la aparición de chinches',
                'clase': 'Piretroide',
                'restricciones': 'No aplicar en presencia de polinizadores'
            }
        ],
        'estrategia': 'Revisar espigas en pre-cosecha'
    },
    # === ENFERMEDADES ===
    {
        'cultivo': 'arroz',
        'plaga': 'Pyricularia o quemado del arroz (Pyricularia oryzae)',
        'sintomas': [
            'manchas elípticas grises con borde marrón en hojas',
            'necrosis en cuello de espiga',
            'secado rápido de plantas'
        ],
        'umbral': '10% plantas afectadas',
        'tratamientos': [
            {
                'producto': 'Score 250 EC',
                'ingrediente': 'Difenoconazole',
                'dosis': '0.5 l/ha',
                'intervalo': 'Aplicar a la aparición',
                'clase': 'Triazol',
                'restricciones': 'No aplicar en lluvia'
            }
        ],
        'estrategia': 'Evitar riegos nocturnos y rotar cultivos'
    },
    {
        'cultivo': 'arroz',
        'plaga': 'Mancha marrón (Bipolaris oryzae)',
        'sintomas': [
            'manchas marrón oscuro en hojas y glumas',
            'secamiento de puntas de hoja',
            'granulación reducida en grano'
        ],
        'umbral': '15% plantas con síntomas',
        'tratamientos': [
            {
                'producto': 'Dithane M-45',
                'ingrediente': 'Mancozeb',
                'dosis': '2 g/L agua',
                'intervalo': 'Cada 10 días',
                'clase': 'Ditiocarbamato',
                'restricciones': 'No aplicar cerca de cosecha'
            }
        ],
        'estrategia': 'Eliminar residuos de cosecha y favorecer rotación'
    },
    {
        'cultivo': 'arroz',
        'plaga': 'Helminthosporiosis (Helminthosporium oryzae)',
        'sintomas': [
            'manchas pequeñas y alargadas en hojas',
            'bordes oscuros y centro gris',
            'hojas secas en la base'
        ],
        'umbral': '10% hojas afectadas',
        'tratamientos': [
            {
                'producto': 'Amistar Xtra',
                'ingrediente': 'Azoxystrobin + Difenoconazole',
                'dosis': '1 l/ha',
                'intervalo': 'Aplicar al detectar síntomas',
                'clase': 'Estrobilurina + triazol',
                'restricciones': 'No aplicar en viento fuerte'
            }
        ],
        'estrategia': 'Evitar siembras densas y exceso de nitrógeno'
    },

    # CAÑA DE AZUCAR

    {
        'cultivo': 'caña',
        'plaga': 'Barrenador del tallo (Diatraea saccharalis)',
        'sintomas': [
            'tallos perforados y quebradizos',
            'hojas secas y amarillas',
            'presencia de aserrín en orificios'
        ],
        'umbral': '5% tallos perforados',
        'tratamientos': [
            {
                'producto': 'Lorsban 4E',
                'ingrediente': 'Clorpirifos',
                'dosis': '1.5 ml/L agua',
                'intervalo': 'Al detectar plaga',
                'clase': 'Organofosforado',
                'restricciones': 'No aplicar cerca de la cosecha'
            }
        ],
        'estrategia': 'Eliminación de residuos y rotación de cultivos'
    },
    {
        'cultivo': 'caña',
        'plaga': 'Pulgón amarillo (Melanaphis sacchari)',
        'sintomas': [
            'colonias en el envés de la hoja',
            'hojas amarillas y pegajosas',
            'melaza y fumagina'
        ],
        'umbral': '10% plantas infestadas',
        'tratamientos': [
            {
                'producto': 'Confidor 350 SC',
                'ingrediente': 'Imidacloprid',
                'dosis': '0.5 ml/L agua',
                'intervalo': 'A la detección',
                'clase': 'Neonicotinoide',
                'restricciones': 'No aplicar en floración para proteger abejas'
            }
        ],
        'estrategia': 'Monitoreo y control biológico'
    },
    # ENFERMEDADES
    {
        'cultivo': 'caña',
        'plaga': 'Roya de la caña (Puccinia melanocephala)',
        'sintomas': [
            'pústulas anaranjadas en hojas',
            'hojas secas prematuramente',
            'baja producción de caña'
        ],
        'umbral': '10% hojas con pústulas',
        'tratamientos': [
            {
                'producto': 'Tilt 250 EC',
                'ingrediente': 'Propiconazole',
                'dosis': '0.5 l/ha',
                'intervalo': 'Cada 15 días según presencia',
                'clase': 'Triazol',
                'restricciones': 'No aplicar cerca de cosecha'
            }
        ],
        'estrategia': 'Usar variedades resistentes y eliminar residuos'
    },
    {
        'cultivo': 'caña',
        'plaga': 'Carbón de la caña (Sporisorium scitamineum)',
        'sintomas': [
            'espigas negras en el extremo del tallo',
            'crecimiento raquítico',
            'tallos deformados'
        ],
        'umbral': 'Presencia en cualquier parte del lote',
        'tratamientos': [
            {
                'producto': 'Eliminación de plantas afectadas',
                'ingrediente': '---',
                'dosis': '---',
                'intervalo': 'Inmediato',
                'clase': 'Cultural',
                'restricciones': 'No hay tratamiento químico efectivo'
            }
        ],
        'estrategia': 'Usar semilla sana y rotar cultivos'
    },

    # ============================================  HORTALIZAS  =================================================


    # === TOMATE ===
    {
        'cultivo': 'tomate',
        'plaga': 'Mosca blanca (Bemisia tabaci)',
        'sintomas': [
            'hojas amarillas y enrolladas',
            'presencia de insectos blancos en el envés',
            'melaza y fumagina sobre las hojas'
        ],
        'umbral': '10% plantas infestadas',
        'tratamientos': [
            {
                'producto': 'Actara 25WG',
                'ingrediente': 'Thiamethoxam',
                'dosis': '0.4 g/L agua',
                'intervalo': 'Cada 10 días',
                'clase': 'Neonicotinoide',
                'restricciones': 'No aplicar en floración para proteger abejas'
            }
        ],
        'estrategia': 'Monitorear población y evitar resistencia'
    },
    {
        'cultivo': 'tomate',
        'plaga': 'Minador de hoja (Liriomyza spp.)',
        'sintomas': [
            'galerías serpenteantes en hojas',
            'puntos blancos en la superficie foliar',
            'hojas secas y caídas prematuramente'
        ],
        'umbral': '5 minas por hoja',
        'tratamientos': [
            {
                'producto': 'Tracer 480SC',
                'ingrediente': 'Spinosad',
                'dosis': '0.3 ml/L agua',
                'intervalo': 'A la aparición',
                'clase': 'Espinosinas',
                'restricciones': 'No aplicar con sol fuerte'
            }
        ],
        'estrategia': 'Eliminar hojas muy dañadas y alternar productos'
    },
    # ENFERMEDADES
    {
        'cultivo': 'tomate',
        'plaga': 'Tizón tardío (Phytophthora infestans)',
        'sintomas': [
            'manchas marrón oscuro en hojas y tallos',
            'áreas húmedas y de rápida expansión',
            'pudrición de frutos'
        ],
        'umbral': 'Presencia en 5% de plantas',
        'tratamientos': [
            {
                'producto': 'Ridomil Gold',
                'ingrediente': 'Metalaxil + Mancozeb',
                'dosis': '2.5 g/L agua',
                'intervalo': 'Cada 8 días',
                'clase': 'Fenilamida + Ditiocarbamato',
                'restricciones': 'No aplicar en lluvia'
            }
        ],
        'estrategia': 'Eliminar residuos y favorecer ventilación'
    },
    {
        'cultivo': 'tomate',
        'plaga': 'Mildiu polvoso (Oidium lycopersici)',
        'sintomas': [
            'polvo blanco sobre hojas',
            'amarillamiento y enrollamiento foliar',
            'caída de hojas inferiores'
        ],
        'umbral': '10% hojas afectadas',
        'tratamientos': [
            {
                'producto': 'Topas 100EC',
                'ingrediente': 'Penconazole',
                'dosis': '0.4 ml/L agua',
                'intervalo': 'Cada 10 días',
                'clase': 'Triazol',
                'restricciones': 'No aplicar en presencia de lluvia'
            }
        ],
        'estrategia': 'Favorecer ventilación y no mojar follaje al regar'
    },
    {
        'cultivo': 'tomate',
        'plaga': 'Mancha bacteriana (Xanthomonas campestris pv. vesicatoria)',
        'sintomas': [
            'manchas pequeñas y acuosas en hojas',
            'bordes amarillos y lesiones en frutos',
            'caída prematura de hojas'
        ],
        'umbral': 'Presencia en 10% plantas',
        'tratamientos': [
            {
                'producto': 'Nordox Super 75WG',
                'ingrediente': 'Óxido cuproso',
                'dosis': '2 g/L agua',
                'intervalo': 'Cada 7 días en brotes',
                'clase': 'Cúprico',
                'restricciones': 'No aplicar con altas temperaturas'
            }
        ],
        'estrategia': 'Usar semilla certificada y eliminar plantas enfermas'
    },

    # === CHILE ===
    {
        'cultivo': 'chile',
        'plaga': 'Pulgón verde (Myzus persicae)',
        'sintomas': [
            'hojas rizadas y amarillentas',
            'presencia de insectos verdes pequeños',
            'melaza pegajosa sobre las hojas'
        ],
        'umbral': '10% plantas afectadas',
        'tratamientos': [
            {
                'producto': 'Confidor 350 SC',
                'ingrediente': 'Imidacloprid',
                'dosis': '0.5 ml/L agua',
                'intervalo': 'Al detectar plaga',
                'clase': 'Neonicotinoide',
                'restricciones': 'No aplicar en floración para proteger abejas'
            }
        ],
        'estrategia': 'Favorecer control biológico con insectos benéficos'
    },
    {
        'cultivo': 'chile',
        'plaga': 'Trips (Frankliniella occidentalis)',
        'sintomas': [
            'hojas plateadas o bronceadas',
            'deformación en brotes tiernos',
            'manchas necróticas en flores y frutos'
        ],
        'umbral': '10% plantas con síntomas',
        'tratamientos': [
            {
                'producto': 'Spintor 120 SC',
                'ingrediente': 'Spinosad',
                'dosis': '1 ml/L agua',
                'intervalo': 'A la aparición',
                'clase': 'Espinosinas',
                'restricciones': 'No aplicar repetidamente'
            }
        ],
        'estrategia': 'Monitorear y alternar productos'
    },
    # ENFERMEDADES
    {
        'cultivo': 'chile',
        'plaga': 'Mancha bacteriana (Xanthomonas campestris pv. vesicatoria)',
        'sintomas': [
            'manchas acuosas y oscuras en hojas y tallos',
            'lesiones en frutos',
            'caída prematura de hojas'
        ],
        'umbral': 'Presencia en 10% plantas',
        'tratamientos': [
            {
                'producto': 'Nordox Super 75WG',
                'ingrediente': 'Óxido cuproso',
                'dosis': '2 g/L agua',
                'intervalo': 'Cada 7 días',
                'clase': 'Cúprico',
                'restricciones': 'No aplicar bajo sol fuerte'
            }
        ],
        'estrategia': 'Eliminar restos y usar semilla certificada'
    },
    {
        'cultivo': 'chile',
        'plaga': 'Antracnosis (Colletotrichum spp.)',
        'sintomas': [
            'manchas circulares hundidas en frutos',
            'zonas negras en los frutos maduros',
            'frutos blandos y podridos'
        ],
        'umbral': '5% frutos afectados',
        'tratamientos': [
            {
                'producto': 'Dithane M-45',
                'ingrediente': 'Mancozeb',
                'dosis': '2 g/L agua',
                'intervalo': 'Cada 7 días en presencia',
                'clase': 'Ditiocarbamato',
                'restricciones': 'No aplicar cerca de cosecha'
            }
        ],
        'estrategia': 'Eliminar frutos enfermos y alternar productos'
    },

    # === CEBOLLA ===
    {
        'cultivo': 'cebolla',
        'plaga': 'Trips de la cebolla (Thrips tabaci)',
        'sintomas': [
            'hojas con manchas plateadas',
            'puntas secas y decoloradas',
            'hojas enrolladas y torcidas'
        ],
        'umbral': '5-10 trips por hoja',
        'tratamientos': [
            {
                'producto': 'Spintor 120 SC',
                'ingrediente': 'Spinosad',
                'dosis': '1 ml/L agua',
                'intervalo': 'A la aparición',
                'clase': 'Espinosinas',
                'restricciones': 'No aplicar en exceso'
            }
        ],
        'estrategia': 'Evitar monocultivo y alternar insecticidas'
    },
    {
        'cultivo': 'cebolla',
        'plaga': 'Mosca de la cebolla (Delia antiqua)',
        'sintomas': [
            'plántulas cortadas al ras del suelo',
            'presencia de larvas blancas en bulbos',
            'marchitez de plantas jóvenes'
        ],
        'umbral': '5% plantas afectadas',
        'tratamientos': [
            {
                'producto': 'Lorsban 4E',
                'ingrediente': 'Clorpirifos',
                'dosis': '1.5 ml/L agua',
                'intervalo': 'Aplicar al detectar plaga',
                'clase': 'Organofosforado',
                'restricciones': 'No aplicar cerca de la cosecha'
            }
        ],
        'estrategia': 'Eliminar restos y rotar cultivos'
    },
    # ENFERMEDADES
    {
        'cultivo': 'cebolla',
        'plaga': 'Mildiu de la cebolla (Peronospora destructor)',
        'sintomas': [
            'manchas amarillas en hojas',
            'polvo gris o violeta sobre las lesiones',
            'marchitez y secado rápido'
        ],
        'umbral': '10% hojas afectadas',
        'tratamientos': [
            {
                'producto': 'Ridomil Gold',
                'ingrediente': 'Metalaxil + Mancozeb',
                'dosis': '2 g/L agua',
                'intervalo': 'Cada 7 días',
                'clase': 'Fenilamida + Ditiocarbamato',
                'restricciones': 'No aplicar bajo lluvia'
            }
        ],
        'estrategia': 'Favorecer ventilación y espaciamiento'
    },
    {
        'cultivo': 'cebolla',
        'plaga': 'Mancha púrpura (Alternaria porri)',
        'sintomas': [
            'manchas alargadas púrpuras en hojas',
            'tejido seco y necrosado',
            'muerte de puntas de hojas'
        ],
        'umbral': '10% hojas afectadas',
        'tratamientos': [
            {
                'producto': 'Dithane M-45',
                'ingrediente': 'Mancozeb',
                'dosis': '2 g/L agua',
                'intervalo': 'Cada 7-10 días',
                'clase': 'Ditiocarbamato',
                'restricciones': 'No aplicar cerca de cosecha'
            }
        ],
        'estrategia': 'Eliminar restos de cultivo y evitar exceso de riego'
    },

    # === LECHUGA ===
    {
        'cultivo': 'lechuga',
        'plaga': 'Pulgón verde (Myzus persicae)',
        'sintomas': [
            'hojas rizadas y pegajosas',
            'presencia de insectos verdes pequeños',
            'melaza sobre hojas'
        ],
        'umbral': '10% plantas infestadas',
        'tratamientos': [
            {
                'producto': 'Actara 25WG',
                'ingrediente': 'Thiamethoxam',
                'dosis': '0.3 g/L agua',
                'intervalo': 'A la aparición',
                'clase': 'Neonicotinoide',
                'restricciones': 'No aplicar en presencia de abejas'
            }
        ],
        'estrategia': 'Favorecer control biológico con mariquitas'
    },
    {
        'cultivo': 'lechuga',
        'plaga': 'Minador de hoja (Liriomyza spp.)',
        'sintomas': [
            'galerías serpenteantes en hojas',
            'manchas claras irregulares',
            'hojas secas prematuramente'
        ],
        'umbral': '5 minas por hoja',
        'tratamientos': [
            {
                'producto': 'Tracer 480SC',
                'ingrediente': 'Spinosad',
                'dosis': '0.3 ml/L agua',
                'intervalo': 'A la aparición',
                'clase': 'Espinosinas',
                'restricciones': 'No aplicar con sol fuerte'
            }
        ],
        'estrategia': 'Eliminar hojas muy dañadas y alternar productos'
    },
    # ENFERMEDADES
    {
        'cultivo': 'lechuga',
        'plaga': 'Mildiu velloso (Bremia lactucae)',
        'sintomas': [
            'manchas amarillas en el haz',
            'polvo blanco o gris en el envés',
            'marchitez rápida de hojas'
        ],
        'umbral': '10% plantas afectadas',
        'tratamientos': [
            {
                'producto': 'Ridomil Gold',
                'ingrediente': 'Metalaxil + Mancozeb',
                'dosis': '2 g/L agua',
                'intervalo': 'Cada 7 días',
                'clase': 'Fenilamida + Ditiocarbamato',
                'restricciones': 'No aplicar bajo lluvia'
            }
        ],
        'estrategia': 'Favorecer ventilación y espaciamiento'
    },
    {
        'cultivo': 'lechuga',
        'plaga': 'Podredumbre blanda (Erwinia carotovora)',
        'sintomas': [
            'tallos y hojas blandas y acuosas',
            'mal olor',
            'tejido colapsado y desintegrado'
        ],
        'umbral': 'Presencia de síntomas',
        'tratamientos': [
            {
                'producto': 'Eliminar plantas afectadas',
                'ingrediente': '---',
                'dosis': '---',
                'intervalo': 'Inmediato',
                'clase': 'Cultural',
                'restricciones': 'No hay tratamiento químico efectivo'
            }
        ],
        'estrategia': 'Evitar riego por aspersión y exceso de humedad'
    },

    # === ZANAHORIA ===
    {
        'cultivo': 'zanahoria',
        'plaga': 'Mosca de la zanahoria (Psila rosae)',
        'sintomas': [
            'raíces con galerías y daños internos',
            'hojas amarillas y marchitas',
            'presencia de larvas blancas en raíces'
        ],
        'umbral': 'Presencia en 5% de plantas',
        'tratamientos': [
            {
                'producto': 'Lorsban 4E',
                'ingrediente': 'Clorpirifos',
                'dosis': '1.5 ml/L agua',
                'intervalo': 'Aplicar al detectar plaga',
                'clase': 'Organofosforado',
                'restricciones': 'No aplicar cerca de la cosecha'
            }
        ],
        'estrategia': 'Rotar cultivos y eliminar residuos de cosecha'
    },
    {
        'cultivo': 'zanahoria',
        'plaga': 'Pulgón verde (Myzus persicae)',
        'sintomas': [
            'hojas enrolladas y pegajosas',
            'presencia de insectos verdes en hojas',
            'desarrollo lento'
        ],
        'umbral': '10% plantas infestadas',
        'tratamientos': [
            {
                'producto': 'Actara 25WG',
                'ingrediente': 'Thiamethoxam',
                'dosis': '0.3 g/L agua',
                'intervalo': 'A la aparición',
                'clase': 'Neonicotinoide',
                'restricciones': 'No aplicar en presencia de abejas'
            }
        ],
        'estrategia': 'Favorecer control biológico con mariquitas'
    },
    # ENFERMEDADES
    {
        'cultivo': 'zanahoria',
        'plaga': 'Alternariosis (Alternaria dauci)',
        'sintomas': [
            'manchas oscuras en hojas y pecíolos',
            'bordes amarillos en lesiones',
            'secamiento de hojas externas'
        ],
        'umbral': '10% plantas afectadas',
        'tratamientos': [
            {
                'producto': 'Dithane M-45',
                'ingrediente': 'Mancozeb',
                'dosis': '2 g/L agua',
                'intervalo': 'Cada 7-10 días',
                'clase': 'Ditiocarbamato',
                'restricciones': 'No aplicar cerca de cosecha'
            }
        ],
        'estrategia': 'Rotar cultivos y evitar exceso de humedad'
    },
    {
        'cultivo': 'zanahoria',
        'plaga': 'Mildiu polvoso (Erysiphe heraclei)',
        'sintomas': [
            'polvo blanco sobre hojas',
            'amarillamiento de hojas',
            'defoliación prematura'
        ],
        'umbral': '10% hojas afectadas',
        'tratamientos': [
            {
                'producto': 'Topas 100 EC',
                'ingrediente': 'Penconazole',
                'dosis': '0.5 ml/L agua',
                'intervalo': 'Cada 10 días',
                'clase': 'Triazol',
                'restricciones': 'No aplicar bajo lluvia'
            }
        ],
        'estrategia': 'Favorecer ventilación y evitar riegos nocturnos'
    },

    # === ESPINACA ===
    {
        'cultivo': 'espinaca',
        'plaga': 'Pulgón verde (Myzus persicae)',
        'sintomas': [
            'hojas rizadas y pegajosas',
            'presencia de insectos verdes pequeños',
            'amarillamiento y crecimiento lento'
        ],
        'umbral': '10% plantas infestadas',
        'tratamientos': [
            {
                'producto': 'Actara 25WG',
                'ingrediente': 'Thiamethoxam',
                'dosis': '0.3 g/L agua',
                'intervalo': 'A la aparición',
                'clase': 'Neonicotinoide',
                'restricciones': 'No aplicar en presencia de abejas'
            }
        ],
        'estrategia': 'Favorecer control biológico con mariquitas'
    },
    {
        'cultivo': 'espinaca',
        'plaga': 'Minador de hoja (Liriomyza spp.)',
        'sintomas': [
            'galerías serpenteantes en hojas',
            'manchas claras e irregulares',
            'hojas secas prematuramente'
        ],
        'umbral': '5 minas por hoja',
        'tratamientos': [
            {
                'producto': 'Tracer 480SC',
                'ingrediente': 'Spinosad',
                'dosis': '0.3 ml/L agua',
                'intervalo': 'A la aparición',
                'clase': 'Espinosinas',
                'restricciones': 'No aplicar bajo sol intenso'
            }
        ],
        'estrategia': 'Eliminar hojas muy dañadas y alternar productos'
    },
    # ENFERMEDADES
    {
        'cultivo': 'espinaca',
        'plaga': 'Mildiu velloso (Peronospora farinosa f. sp. spinaciae)',
        'sintomas': [
            'manchas amarillas en el haz',
            'polvo gris-violáceo en el envés',
            'marchitez y muerte de hojas'
        ],
        'umbral': '10% plantas afectadas',
        'tratamientos': [
            {
                'producto': 'Ridomil Gold',
                'ingrediente': 'Metalaxil + Mancozeb',
                'dosis': '2 g/L agua',
                'intervalo': 'Cada 7 días',
                'clase': 'Fenilamida + Ditiocarbamato',
                'restricciones': 'No aplicar bajo lluvia'
            }
        ],
        'estrategia': 'Favorecer ventilación y evitar exceso de humedad'
    },
    {
        'cultivo': 'espinaca',
        'plaga': 'Alternariosis (Alternaria spp.)',
        'sintomas': [
            'manchas negruzcas en hojas',
            'tejido seco y necrosado',
            'pérdida de hojas externas'
        ],
        'umbral': '5% hojas afectadas',
        'tratamientos': [
            {
                'producto': 'Dithane M-45',
                'ingrediente': 'Mancozeb',
                'dosis': '2 g/L agua',
                'intervalo': 'Cada 7 días',
                'clase': 'Ditiocarbamato',
                'restricciones': 'No aplicar cerca de cosecha'
            }
        ],
        'estrategia': 'Eliminar restos de cultivo y evitar riegos nocturnos'
    },


    # === REPOLLO ===
    {
        'cultivo': 'repollo',
        'plaga': 'Palomilla dorso de diamante (Plutella xylostella)',
        'sintomas': [
            'orificios en hojas',
            'presencia de larvas verdes pequeñas',
            'hojas perforadas y con galerías'
        ],
        'umbral': '5 larvas por planta',
        'tratamientos': [
            {
                'producto': 'Bacillus thuringiensis',
                'ingrediente': 'Bacillus thuringiensis var. kurstaki',
                'dosis': '1 g/L agua',
                'intervalo': 'Cada 7 días',
                'clase': 'Biológico',
                'restricciones': 'No aplicar con lluvias'
            }
        ],
        'estrategia': 'Monitoreo frecuente y alternar productos'
    },
    {
        'cultivo': 'repollo',
        'plaga': 'Pulgón ceniciento (Brevicoryne brassicae)',
        'sintomas': [
            'colonias de pulgones grisáceos en hojas',
            'hojas arrugadas y pegajosas',
            'desarrollo lento de cabezas'
        ],
        'umbral': '10% plantas infestadas',
        'tratamientos': [
            {
                'producto': 'Actara 25WG',
                'ingrediente': 'Thiamethoxam',
                'dosis': '0.4 g/L agua',
                'intervalo': 'A la aparición',
                'clase': 'Neonicotinoide',
                'restricciones': 'No aplicar en presencia de abejas'
            }
        ],
        'estrategia': 'Control biológico con mariquitas y evitar monocultivo'
    },
    # ENFERMEDADES
    {
        'cultivo': 'repollo',
        'plaga': 'Alternariosis (Alternaria brassicae)',
        'sintomas': [
            'manchas marrón oscuro con halo amarillo',
            'tejido seco y necrosado',
            'manchas en hojas y tallos'
        ],
        'umbral': '10% plantas afectadas',
        'tratamientos': [
            {
                'producto': 'Dithane M-45',
                'ingrediente': 'Mancozeb',
                'dosis': '2 g/L agua',
                'intervalo': 'Cada 7-10 días',
                'clase': 'Ditiocarbamato',
                'restricciones': 'No aplicar cerca de cosecha'
            }
        ],
        'estrategia': 'Eliminar restos de cultivo y rotar cultivos'
    },
    {
        'cultivo': 'repollo',
        'plaga': 'Mildiu velloso (Peronospora parasitica)',
        'sintomas': [
            'manchas amarillas en el haz',
            'polvo blanco o gris en el envés',
            'hojas secas prematuramente'
        ],
        'umbral': '10% plantas afectadas',
        'tratamientos': [
            {
                'producto': 'Ridomil Gold',
                'ingrediente': 'Metalaxil + Mancozeb',
                'dosis': '2 g/L agua',
                'intervalo': 'Cada 7 días',
                'clase': 'Fenilamida + Ditiocarbamato',
                'restricciones': 'No aplicar bajo lluvia'
            }
        ],
        'estrategia': 'Favorecer ventilación y espaciamiento'
    },

    # === AYOTE ===
    {
        'cultivo': 'ayote',
        'plaga': 'Mosca blanca (Bemisia tabaci)',
        'sintomas': [
            'hojas amarillas y enrolladas',
            'presencia de insectos blancos en el envés',
            'melaza y fumagina'
        ],
        'umbral': '10% plantas infestadas',
        'tratamientos': [
            {
                'producto': 'Confidor 350 SC',
                'ingrediente': 'Imidacloprid',
                'dosis': '0.5 ml/L agua',
                'intervalo': 'A la aparición',
                'clase': 'Neonicotinoide',
                'restricciones': 'No aplicar en floración para proteger abejas'
            }
        ],
        'estrategia': 'Controlar malezas y alternar productos'
    },
    {
        'cultivo': 'ayote',
        'plaga': 'Trips (Frankliniella occidentalis)',
        'sintomas': [
            'hojas plateadas o bronceadas',
            'deformación de hojas jóvenes',
            'manchas necróticas en flores'
        ],
        'umbral': '10% plantas afectadas',
        'tratamientos': [
            {
                'producto': 'Spintor 120 SC',
                'ingrediente': 'Spinosad',
                'dosis': '1 ml/L agua',
                'intervalo': 'A la aparición',
                'clase': 'Espinosinas',
                'restricciones': 'No aplicar repetidamente'
            }
        ],
        'estrategia': 'Monitoreo y alternar productos'
    },
    # ENFERMEDADES
    {
        'cultivo': 'ayote',
        'plaga': 'Oídio (Sphaerotheca fuliginea)',
        'sintomas': [
            'polvo blanco sobre hojas',
            'amarillamiento y caída de hojas',
            'desarrollo lento de frutos'
        ],
        'umbral': '10% hojas afectadas',
        'tratamientos': [
            {
                'producto': 'Topas 100EC',
                'ingrediente': 'Penconazole',
                'dosis': '0.4 ml/L agua',
                'intervalo': 'Cada 10 días',
                'clase': 'Triazol',
                'restricciones': 'No aplicar bajo lluvia'
            }
        ],
        'estrategia': 'Favorecer ventilación y espaciamiento'
    },
    {
        'cultivo': 'ayote',
        'plaga': 'Antracnosis (Colletotrichum orbiculare)',
        'sintomas': [
            'manchas negras hundidas en hojas y frutos',
            'tejido necrosado',
            'frutos podridos'
        ],
        'umbral': '5% frutos afectados',
        'tratamientos': [
            {
                'producto': 'Dithane M-45',
                'ingrediente': 'Mancozeb',
                'dosis': '2 g/L agua',
                'intervalo': 'Cada 7 días',
                'clase': 'Ditiocarbamato',
                'restricciones': 'No aplicar cerca de cosecha'
            }
        ],
        'estrategia': 'Eliminar frutos enfermos y alternar productos'
    },

    # === GUISQUIL ===
    {
        'cultivo': 'guisquil',
        'plaga': 'Mosca blanca (Bemisia tabaci)',
        'sintomas': [
            'hojas amarillas y enrolladas',
            'presencia de insectos blancos en el envés',
            'melaza sobre hojas'
        ],
        'umbral': '10% plantas infestadas',
        'tratamientos': [
            {
                'producto': 'Actara 25WG',
                'ingrediente': 'Thiamethoxam',
                'dosis': '0.4 g/L agua',
                'intervalo': 'Cada 10 días',
                'clase': 'Neonicotinoide',
                'restricciones': 'No aplicar en floración para proteger abejas'
            }
        ],
        'estrategia': 'Controlar malezas y alternar productos'
    },
    {
        'cultivo': 'guisquil',
        'plaga': 'Pulgón verde (Myzus persicae)',
        'sintomas': [
            'hojas arrugadas y pegajosas',
            'colonias de insectos verdes',
            'crecimiento lento'
        ],
        'umbral': '10% plantas infestadas',
        'tratamientos': [
            {
                'producto': 'Confidor 350 SC',
                'ingrediente': 'Imidacloprid',
                'dosis': '0.5 ml/L agua',
                'intervalo': 'A la aparición',
                'clase': 'Neonicotinoide',
                'restricciones': 'No aplicar en presencia de abejas'
            }
        ],
        'estrategia': 'Favorecer control biológico con mariquitas'
    },
    # ENFERMEDADES
    {
        'cultivo': 'guisquil',
        'plaga': 'Mildiu velloso (Peronospora sp.)',
        'sintomas': [
            'manchas amarillas en el haz de la hoja',
            'polvo gris o blanco en el envés',
            'caída prematura de hojas'
        ],
        'umbral': '10% plantas afectadas',
        'tratamientos': [
            {
                'producto': 'Ridomil Gold',
                'ingrediente': 'Metalaxil + Mancozeb',
                'dosis': '2 g/L agua',
                'intervalo': 'Cada 7 días',
                'clase': 'Fenilamida + Ditiocarbamato',
                'restricciones': 'No aplicar bajo lluvia'
            }
        ],
        'estrategia': 'Favorecer ventilación y espaciamiento'
    },
    {
        'cultivo': 'guisquil',
        'plaga': 'Antracnosis (Colletotrichum sp.)',
        'sintomas': [
            'manchas negras hundidas en hojas y frutos',
            'tejido necrosado',
            'frutos deformes o podridos'
        ],
        'umbral': '5% frutos afectados',
        'tratamientos': [
            {
                'producto': 'Dithane M-45',
                'ingrediente': 'Mancozeb',
                'dosis': '2 g/L agua',
                'intervalo': 'Cada 7 días',
                'clase': 'Ditiocarbamato',
                'restricciones': 'No aplicar cerca de cosecha'
            }
        ],
        'estrategia': 'Eliminar frutos enfermos y alternar productos'
    },

    # RABANO

    {
        'cultivo': 'rabano',
        'plaga': 'Pulga saltona (Phyllotreta spp.)',
        'sintomas': [
            'pequeños orificios en hojas jóvenes',
            'hojas perforadas y deformadas',
            'daños más severos en plántulas'
        ],
        'umbral': '10% plantas afectadas',
        'tratamientos': [
            {
                'producto': 'Karate Zeon',
                'ingrediente': 'Lambdacialotrina',
                'dosis': '0.2 ml/L agua',
                'intervalo': 'A la aparición',
                'clase': 'Piretroide',
                'restricciones': 'No aplicar cerca de cosecha'
            }
        ],
        'estrategia': 'Rotar cultivos y mantener el suelo libre de malezas'
    },
    {
        'cultivo': 'rabano',
        'plaga': 'Pulgón verde (Myzus persicae)',
        'sintomas': [
            'hojas arrugadas y pegajosas',
            'presencia de insectos verdes en hojas',
            'desarrollo lento'
        ],
        'umbral': '10% plantas infestadas',
        'tratamientos': [
            {
                'producto': 'Actara 25WG',
                'ingrediente': 'Thiamethoxam',
                'dosis': '0.3 g/L agua',
                'intervalo': 'A la aparición',
                'clase': 'Neonicotinoide',
                'restricciones': 'No aplicar en presencia de abejas'
            }
        ],
        'estrategia': 'Favorecer control biológico con mariquitas'
    },
    # ENFERMEDADES
    {
        'cultivo': 'rabano',
        'plaga': 'Mildiu velloso (Peronospora parasitica)',
        'sintomas': [
            'manchas amarillas en el haz de la hoja',
            'polvo blanco o gris en el envés',
            'hojas secas y marchitas'
        ],
        'umbral': '10% plantas afectadas',
        'tratamientos': [
            {
                'producto': 'Ridomil Gold',
                'ingrediente': 'Metalaxil + Mancozeb',
                'dosis': '2 g/L agua',
                'intervalo': 'Cada 7 días',
                'clase': 'Fenilamida + Ditiocarbamato',
                'restricciones': 'No aplicar bajo lluvia'
            }
        ],
        'estrategia': 'Favorecer ventilación y espaciamiento'
    },
    {
        'cultivo': 'rabano',
        'plaga': 'Podredumbre blanca (Sclerotinia sclerotiorum)',
        'sintomas': [
            'moho blanco en la base de la raíz',
            'tejido blando y acuoso',
            'mal olor y colapso de la raíz'
        ],
        'umbral': 'Presencia de síntomas',
        'tratamientos': [
            {
                'producto': 'Eliminar plantas afectadas',
                'ingrediente': '---',
                'dosis': '---',
                'intervalo': 'Inmediato',
                'clase': 'Cultural',
                'restricciones': 'No hay tratamiento químico efectivo'
            }
        ],
        'estrategia': 'Evitar riego excesivo y mejorar drenaje'
    },
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

def obtener_sintomas_por_cultivo(cultivo):
    """
    Recibe el nombre de un cultivo (str)
    Devuelve una lista SIN REPETIDOS de todos los síntomas de plagas/enfermedades de ese cultivo
    """
    sintomas_set = set()
    for plaga in PLAGAS:
        if plaga['cultivo'] == cultivo:
            sintomas_set.update(plaga['sintomas'])
    return sorted(list(sintomas_set))