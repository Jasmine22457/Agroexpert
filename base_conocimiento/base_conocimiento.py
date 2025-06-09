# base_conocimiento.py

# --- REGLAS DE FERTILIZANTE: grano básico y hortalizas principales ---
FERTILIZANTES = [
    # MAÍZ
    {'cultivo': 'maiz', 'suelo': 'arcilloso', 'clima': 'seco',     'recomendacion': "120 kg N/ha, 60 kg P₂O₅/ha, 40 kg K₂O/ha. Mejorar drenaje y riego frecuente."},
    {'cultivo': 'maiz', 'suelo': 'arcilloso', 'clima': 'humedo',   'recomendacion': "120 kg N/ha, 60 kg P₂O₅/ha, 40 kg K₂O/ha. Aplicar fungicida preventivo."},
    {'cultivo': 'maiz', 'suelo': 'arcilloso', 'clima': 'tropical', 'recomendacion': "110 kg N/ha, 60 kg P₂O₅/ha, 40 kg K₂O/ha. Vigilar malezas."},
    {'cultivo': 'maiz', 'suelo': 'arenoso',   'clima': 'seco',     'recomendacion': "150 kg N/ha, 60 kg P₂O₅/ha, 60 kg K₂O/ha. Riego frecuente y materia orgánica."},
    {'cultivo': 'maiz', 'suelo': 'arenoso',   'clima': 'humedo',   'recomendacion': "150 kg N/ha, 60 kg P₂O₅/ha, 60 kg K₂O/ha. Buen drenaje."},
    {'cultivo': 'maiz', 'suelo': 'arenoso',   'clima': 'tropical', 'recomendacion': "130 kg N/ha, 60 kg P₂O₅/ha, 55 kg K₂O/ha."},
    {'cultivo': 'maiz', 'suelo': 'volcanico', 'clima': 'seco',     'recomendacion': "100 kg N/ha, 45 kg P₂O₅/ha, 35 kg K₂O/ha. Vigilar pH."},
    {'cultivo': 'maiz', 'suelo': 'volcanico', 'clima': 'humedo',   'recomendacion': "105 kg N/ha, 50 kg P₂O₅/ha, 40 kg K₂O/ha."},
    {'cultivo': 'maiz', 'suelo': 'volcanico', 'clima': 'tropical', 'recomendacion': "100 kg N/ha, 48 kg P₂O₅/ha, 38 kg K₂O/ha."},

    # FRIJOL
    {'cultivo': 'frijol', 'suelo': 'arcilloso', 'clima': 'seco',   'recomendacion': "60 kg N/ha, 70 kg P₂O₅/ha, 30 kg K₂O/ha. Mejorar ventilación."},
    {'cultivo': 'frijol', 'suelo': 'arcilloso', 'clima': 'humedo', 'recomendacion': "70 kg N/ha, 80 kg P₂O₅/ha, 40 kg K₂O/ha."},
    {'cultivo': 'frijol', 'suelo': 'arenoso',   'clima': 'seco',   'recomendacion': "80 kg N/ha, 80 kg P₂O₅/ha, 50 kg K₂O/ha. Abono orgánico."},
    {'cultivo': 'frijol', 'suelo': 'arenoso',   'clima': 'humedo', 'recomendacion': "90 kg N/ha, 90 kg P₂O₅/ha, 50 kg K₂O/ha."},
    {'cultivo': 'frijol', 'suelo': 'volcanico', 'clima': 'seco',   'recomendacion': "70 kg N/ha, 60 kg P₂O₅/ha, 30 kg K₂O/ha. Vigilar pH."},
    {'cultivo': 'frijol', 'suelo': 'volcanico', 'clima': 'humedo', 'recomendacion': "75 kg N/ha, 65 kg P₂O₅/ha, 32 kg K₂O/ha."},

    # ARROZ
    {'cultivo': 'arroz', 'suelo': 'franco',    'clima': 'humedo',   'recomendacion': "90 kg N/ha, 50 kg P₂O₅/ha, 50 kg K₂O/ha. Mantener riego por inundación."},
    {'cultivo': 'arroz', 'suelo': 'franco',    'clima': 'tropical', 'recomendacion': "95 kg N/ha, 55 kg P₂O₅/ha, 48 kg K₂O/ha."},
    {'cultivo': 'arroz', 'suelo': 'arcilloso', 'clima': 'humedo',   'recomendacion': "80 kg N/ha, 40 kg P₂O₅/ha, 40 kg K₂O/ha."},
    {'cultivo': 'arroz', 'suelo': 'arcilloso', 'clima': 'tropical', 'recomendacion': "85 kg N/ha, 43 kg P₂O₅/ha, 43 kg K₂O/ha."},

    # SORGO
    {'cultivo': 'sorgo', 'suelo': 'arcilloso', 'clima': 'seco',   'recomendacion': "75 kg N/ha, 35 kg P₂O₅/ha, 28 kg K₂O/ha."},
    {'cultivo': 'sorgo', 'suelo': 'arcilloso', 'clima': 'humedo', 'recomendacion': "80 kg N/ha, 36 kg P₂O₅/ha, 32 kg K₂O/ha."},
    {'cultivo': 'sorgo', 'suelo': 'arenoso',   'clima': 'seco',   'recomendacion': "90 kg N/ha, 40 kg P₂O₅/ha, 35 kg K₂O/ha."},
    {'cultivo': 'sorgo', 'suelo': 'arenoso',   'clima': 'humedo', 'recomendacion': "100 kg N/ha, 45 kg P₂O₅/ha, 40 kg K₂O/ha."},

    # TOMATE
    {'cultivo': 'tomate', 'suelo': 'franco',    'clima': 'templado', 'recomendacion': "200 kg N/ha, 150 kg P₂O₅/ha, 100 kg K₂O/ha. Riego cada 2 días."},
    {'cultivo': 'tomate', 'suelo': 'franco',    'clima': 'tropical', 'recomendacion': "180 kg N/ha, 140 kg P₂O₅/ha, 110 kg K₂O/ha. Revisar plagas."},
    {'cultivo': 'tomate', 'suelo': 'arcilloso', 'clima': 'humedo',   'recomendacion': "180 kg N/ha, 120 kg P₂O₅/ha, 90 kg K₂O/ha. Fungicida preventivo."},
    {'cultivo': 'tomate', 'suelo': 'arcilloso', 'clima': 'seco',     'recomendacion': "160 kg N/ha, 100 kg P₂O₅/ha, 80 kg K₂O/ha. Aporte de materia orgánica."},

    # CHILE
    {'cultivo': 'chile', 'suelo': 'arenoso', 'clima': 'seco',   'recomendacion': "110 kg N/ha, 70 kg P₂O₅/ha, 90 kg K₂O/ha. Riego frecuente."},
    {'cultivo': 'chile', 'suelo': 'arenoso', 'clima': 'humedo', 'recomendacion': "120 kg N/ha, 80 kg P₂O₅/ha, 95 kg K₂O/ha. Control de malezas."},
    {'cultivo': 'chile', 'suelo': 'franco',  'clima': 'tropical', 'recomendacion': "115 kg N/ha, 75 kg P₂O₅/ha, 92 kg K₂O/ha. Fertilización dividida."},

    # PEPINO
    {'cultivo': 'pepino', 'suelo': 'franco',  'clima': 'templado', 'recomendacion': "85 kg N/ha, 60 kg P₂O₅/ha, 95 kg K₂O/ha. Riego por goteo."},
    {'cultivo': 'pepino', 'suelo': 'franco',  'clima': 'tropical', 'recomendacion': "90 kg N/ha, 65 kg P₂O₅/ha, 100 kg K₂O/ha."},
    {'cultivo': 'pepino', 'suelo': 'arenoso', 'clima': 'seco',     'recomendacion': "95 kg N/ha, 70 kg P₂O₅/ha, 110 kg K₂O/ha. Materia orgánica."},

    # CEBOLLA
    {'cultivo': 'cebolla', 'suelo': 'limo',  'clima': 'humedo',   'recomendacion': "100 kg N/ha, 50 kg P₂O₅/ha, 80 kg K₂O/ha. Evitar inundaciones."},
    {'cultivo': 'cebolla', 'suelo': 'limo',  'clima': 'templado', 'recomendacion': "105 kg N/ha, 55 kg P₂O₅/ha, 85 kg K₂O/ha."},

    # REPOLLO
    {'cultivo': 'repollo', 'suelo': 'franco',  'clima': 'tropical', 'recomendacion': "130 kg N/ha, 70 kg P₂O₅/ha, 110 kg K₂O/ha. Riego regular."},
    {'cultivo': 'repollo', 'suelo': 'franco',  'clima': 'humedo',   'recomendacion': "135 kg N/ha, 75 kg P₂O₅/ha, 115 kg K₂O/ha. Revisar drenaje."},

    # ZANAHORIA
    {'cultivo': 'zanahoria', 'suelo': 'limo',  'clima': 'humedo',   'recomendacion': "90 kg N/ha, 40 kg P₂O₅/ha, 50 kg K₂O/ha. Riego regular."},
    {'cultivo': 'zanahoria', 'suelo': 'limo',  'clima': 'templado', 'recomendacion': "95 kg N/ha, 45 kg P₂O₅/ha, 55 kg K₂O/ha."},

    # LECHUGA
    {'cultivo': 'lechuga', 'suelo': 'franco',  'clima': 'tropical', 'recomendacion': "60 kg N/ha, 30 kg P₂O₅/ha, 70 kg K₂O/ha. Mantener suelo húmedo."},
    {'cultivo': 'lechuga', 'suelo': 'franco',  'clima': 'templado', 'recomendacion': "65 kg N/ha, 32 kg P₂O₅/ha, 75 kg K₂O/ha."},

    # AYOTE
    {'cultivo': 'ayote', 'suelo': 'arcilloso', 'clima': 'seco',   'recomendacion': "70 kg N/ha, 45 kg P₂O₅/ha, 60 kg K₂O/ha. Drenaje fundamental."},
    {'cultivo': 'ayote', 'suelo': 'arcilloso', 'clima': 'humedo', 'recomendacion': "75 kg N/ha, 50 kg P₂O₅/ha, 65 kg K₂O/ha."},

    # RÁBANO
    {'cultivo': 'rabano', 'suelo': 'franco',  'clima': 'tropical', 'recomendacion': "40 kg N/ha, 20 kg P₂O₅/ha, 40 kg K₂O/ha."},
    {'cultivo': 'rabano', 'suelo': 'franco',  'clima': 'humedo',   'recomendacion': "42 kg N/ha, 22 kg P₂O₅/ha, 42 kg K₂O/ha."},

    # PIPIAN
    {'cultivo': 'pipian', 'suelo': 'franco',    'clima': 'tropical', 'recomendacion': "65 kg N/ha, 35 kg P₂O₅/ha, 65 kg K₂O/ha."},
    {'cultivo': 'pipian', 'suelo': 'arcilloso', 'clima': 'humedo',   'recomendacion': "70 kg N/ha, 38 kg P₂O₅/ha, 68 kg K₂O/ha."},

    # ESPINACA
    {'cultivo': 'espinaca', 'suelo': 'arenoso', 'clima': 'templado', 'recomendacion': "85 kg N/ha, 40 kg P₂O₅/ha, 80 kg K₂O/ha. Controlar malezas."},
    {'cultivo': 'espinaca', 'suelo': 'arenoso', 'clima': 'humedo',   'recomendacion': "87 kg N/ha, 41 kg P₂O₅/ha, 85 kg K₂O/ha."},

    # GUISQUIL
    {'cultivo': 'guisquil', 'suelo': 'volcanico', 'clima': 'humedo',   'recomendacion': "65 kg N/ha, 28 kg P₂O₅/ha, 70 kg K₂O/ha."},
    {'cultivo': 'guisquil', 'suelo': 'volcanico', 'clima': 'tropical', 'recomendacion': "68 kg N/ha, 29 kg P₂O₅/ha, 74 kg K₂O/ha."},
]

# --- REGLAS DE DIAGNÓSTICO: síntomas por cultivo ---
DIAGNOSTICOS = [
    # MAÍZ
    {'cultivo': 'maiz', 'sintomas': ['manchas amarillas', 'pudricion tallo'], 'diagnostico': 'Hongo Fusarium', 'recomendacion': 'Rotar cultivos, aplicar benomilo.'},
    {'cultivo': 'maiz', 'sintomas': ['hojas enrolladas', 'gusanos'], 'diagnostico': 'Gusano cogollero', 'recomendacion': 'Aplicar insecticida biológico.'},
    {'cultivo': 'maiz', 'sintomas': ['puntos blancos', 'telaraña'], 'diagnostico': 'Araña roja', 'recomendacion': 'Liberar enemigos naturales, aplicar azufre.'},
    {'cultivo': 'maiz', 'sintomas': ['marchitez', 'raices negras'], 'diagnostico': 'Pythium', 'recomendacion': 'Mejorar drenaje, fungicida para suelo.'},
    {'cultivo': 'maiz', 'sintomas': ['hojas amarillas', 'manchas marrones'], 'diagnostico': 'Mancha foliar', 'recomendacion': 'Eliminar residuos, usar semilla resistente.'},
    {'cultivo': 'maiz', 'sintomas': ['hojas blancas', 'crecimiento detenido'], 'diagnostico': 'Mildiu', 'recomendacion': 'Fungicida específico, eliminar plantas infectadas.'},

    # FRIJOL
    {'cultivo': 'frijol', 'sintomas': ['manchas marrones', 'hojas'], 'diagnostico': 'Antracnosis', 'recomendacion': 'Aplicar fungicida, usar semillas certificadas.'},
    {'cultivo': 'frijol', 'sintomas': ['hojas amarillas', 'insectos pequeños'], 'diagnostico': 'Pulgón', 'recomendacion': 'Jabón potásico, control biológico.'},
    {'cultivo': 'frijol', 'sintomas': ['hojas deformes', 'necrosis'], 'diagnostico': 'Virus del mosaico', 'recomendacion': 'Remover plantas afectadas.'},
    {'cultivo': 'frijol', 'sintomas': ['manchas negras', 'tallo quebradizo'], 'diagnostico': 'Bacteriosis', 'recomendacion': 'Eliminar restos de cultivo, rotación de cultivos.'},
    {'cultivo': 'frijol', 'sintomas': ['flores caídas', 'vainas vacías'], 'diagnostico': 'Deficiencia de micronutrientes', 'recomendacion': 'Fertilizante con micronutrientes.'},

    # ARROZ
    {'cultivo': 'arroz', 'sintomas': ['puntas secas', 'manchas grises'], 'diagnostico': 'Mancha marrón', 'recomendacion': 'Reducir nitrógeno, fungicida.'},
    {'cultivo': 'arroz', 'sintomas': ['tallos negros', 'mal olor'], 'diagnostico': 'Tizón por Rhizoctonia', 'recomendacion': 'Secar campos, fungicida específico.'},
    {'cultivo': 'arroz', 'sintomas': ['plantas caídas', 'base podrida'], 'diagnostico': 'Podredumbre del tallo', 'recomendacion': 'Mejorar drenaje, fungicida de suelo.'},
    {'cultivo': 'arroz', 'sintomas': ['hojas enrolladas', 'maleza presente'], 'diagnostico': 'Daño por chinche', 'recomendacion': 'Control de malezas, insecticida selectivo.'},

    # SORGO
    {'cultivo': 'sorgo', 'sintomas': ['manchas rojizas', 'hojas secas'], 'diagnostico': 'Antracnosis', 'recomendacion': 'Aplicar fungicida.'},
    {'cultivo': 'sorgo', 'sintomas': ['hojas enrolladas', 'insectos'], 'diagnostico': 'Mosca del sorgo', 'recomendacion': 'Control biológico, eliminar malezas.'},
    {'cultivo': 'sorgo', 'sintomas': ['tallos blandos', 'pudricion en la base'], 'diagnostico': 'Podredumbre del tallo', 'recomendacion': 'Mejorar aireación.'},

    # TOMATE
    {'cultivo': 'tomate', 'sintomas': ['manchas oscuras', 'hojas'], 'diagnostico': 'Tizón temprano', 'recomendacion': 'Aplicar mancozeb, eliminar hojas afectadas.'},
    {'cultivo': 'tomate', 'sintomas': ['tallos podridos'], 'diagnostico': 'Pudrición bacteriana', 'recomendacion': 'Mejorar drenaje, usar semillas tratadas.'},
    {'cultivo': 'tomate', 'sintomas': ['frutos con agujeros', 'larvas dentro'], 'diagnostico': 'Mosca de la fruta', 'recomendacion': 'Colocar trampas, recoger frutos caídos.'},
    {'cultivo': 'tomate', 'sintomas': ['hojas enrolladas', 'crecimiento lento'], 'diagnostico': 'Virus del rizado amarillo', 'recomendacion': 'Eliminar plantas afectadas.'},

    # CHILE
    {'cultivo': 'chile', 'sintomas': ['manchas blancas', 'hojas caídas'], 'diagnostico': 'Oídio', 'recomendacion': 'Aplicar azufre mojable.'},
    {'cultivo': 'chile', 'sintomas': ['hojas deformes', 'manchas amarillas'], 'diagnostico': 'Trips', 'recomendacion': 'Control biológico, insecticida selectivo.'},
    {'cultivo': 'chile', 'sintomas': ['frutos podridos', 'moho blanco'], 'diagnostico': 'Moho blanco', 'recomendacion': 'Eliminar frutos afectados.'},

    # PEPINO
    {'cultivo': 'pepino', 'sintomas': ['manchas amarillas', 'hojas secas'], 'diagnostico': 'Mildiu', 'recomendacion': 'Mejorar ventilación, fungicida adecuado.'},
    {'cultivo': 'pepino', 'sintomas': ['tallos blandos', 'pudricion'], 'diagnostico': 'Podredumbre blanda', 'recomendacion': 'Reducir riego, evitar daños mecánicos.'},
    {'cultivo': 'pepino', 'sintomas': ['frutos curvos', 'hojas pálidas'], 'diagnostico': 'Deficiencia de potasio', 'recomendacion': 'Fertilizante potásico.'},

    # CEBOLLA
    {'cultivo': 'cebolla', 'sintomas': ['bulbo blando', 'mal olor'], 'diagnostico': 'Podredumbre bacteriana', 'recomendacion': 'Mejorar drenaje, evitar riego excesivo.'},
    {'cultivo': 'cebolla', 'sintomas': ['hojas amarillas', 'caídas'], 'diagnostico': 'Mosca de la cebolla', 'recomendacion': 'Aplicar insecticida, eliminar restos de cosecha.'},

    # REPOLLO
    {'cultivo': 'repollo', 'sintomas': ['manchas negras', 'hojas perforadas'], 'diagnostico': 'Plaga de gusanos', 'recomendacion': 'Control biológico, eliminar larvas.'},
    {'cultivo': 'repollo', 'sintomas': ['manchas circulares', 'hojas húmedas'], 'diagnostico': 'Bacteriosis', 'recomendacion': 'Eliminar hojas afectadas.'},

    # ZANAHORIA
    {'cultivo': 'zanahoria', 'sintomas': ['raices deformes', 'manchas marrones'], 'diagnostico': 'Nemátodos', 'recomendacion': 'Rotar cultivos, solarización.'},
    {'cultivo': 'zanahoria', 'sintomas': ['hojas amarillas', 'crecimiento lento'], 'diagnostico': 'Deficiencia de nutrientes', 'recomendacion': 'Fertilizar con compost.'},

    # LECHUGA
    {'cultivo': 'lechuga', 'sintomas': ['manchas cafes', 'bordes quemados'], 'diagnostico': 'Tipburn', 'recomendacion': 'Evitar estrés hídrico, mejorar ventilación.'},
    {'cultivo': 'lechuga', 'sintomas': ['hojas blandas', 'mal olor'], 'diagnostico': 'Podredumbre blanda', 'recomendacion': 'Reducir riego, evitar daño mecánico.'},

    # ESPINACA
    {'cultivo': 'espinaca', 'sintomas': ['hojas amarillas', 'manchas marrones'], 'diagnostico': 'Mancha foliar', 'recomendacion': 'Mejorar ventilación, eliminar hojas infectadas.'},
    {'cultivo': 'espinaca', 'sintomas': ['tallos podridos'], 'diagnostico': 'Pythium', 'recomendacion': 'Fungicida de suelo, evitar exceso de agua.'},

    # AYOTE
    {'cultivo': 'ayote', 'sintomas': ['frutos blandos', 'olor ácido'], 'diagnostico': 'Podredumbre', 'recomendacion': 'Mejorar drenaje, eliminar frutos afectados.'},
    {'cultivo': 'ayote', 'sintomas': ['hojas secas', 'tallo agrietado'], 'diagnostico': 'Estrés hídrico', 'recomendacion': 'Aumentar riego.'},

    # GUISQUIL
    {'cultivo': 'guisquil', 'sintomas': ['manchas blancas', 'hojas enrolladas'], 'diagnostico': 'Oídio', 'recomendacion': 'Fungicida, podar brotes afectados.'},
    {'cultivo': 'guisquil', 'sintomas': ['hojas deformes', 'coloración violeta'], 'diagnostico': 'Virus', 'recomendacion': 'Eliminar plantas afectadas, controlar vectores.'},
]

# === ACUAPONIA ===
ACUAPONIA = [
    {'pez': 'tilapia', 'cultivo': 'lechuga', 'recomendacion': 'pH 6.5-7.5, nitritos <0.5 ppm, recambio semanal, buena oxigenación, luz suficiente.'},
    {'pez': 'tilapia', 'cultivo': 'tomate',  'recomendacion': 'pH 6.8-7.5, suplemento Ca/Mg, oxigenación alta, monitorear nutrientes.'},
    {'pez': 'tilapia', 'cultivo': 'albahaca', 'recomendacion': 'pH 6.5-7.2, control de amonio, sombra parcial.'},
    {'pez': 'tilapia', 'cultivo': 'espinaca', 'recomendacion': 'pH 6.2-7.0, recambio parcial semanal, sombra parcial.'},
    {'pez': 'tilapia', 'cultivo': 'menta',    'recomendacion': 'pH 6.7-7.4, cambio de agua cada 10 días, podar raíces.'},

    {'pez': 'bagre',   'cultivo': 'albahaca', 'recomendacion': 'pH 7-8, NO2 <0.3 ppm, circulación buena, sombra parcial.'},
    {'pez': 'bagre',   'cultivo': 'lechuga',  'recomendacion': 'pH 7-7.5, buena aireación, cambio de agua cada semana.'},
    {'pez': 'bagre',   'cultivo': 'espinaca', 'recomendacion': 'pH 7-8, recambio parcial frecuente, iluminación media.'},

    {'pez': 'carpa',   'cultivo': 'espinaca', 'recomendacion': 'pH 6.5-7.2, NO3 <50 ppm, control de algas, buena iluminación.'},
    {'pez': 'carpa',   'cultivo': 'tomate',   'recomendacion': 'pH 6.8-7.2, filtro biológico, buena aireación, suplemento de Ca.'},
    {'pez': 'carpa',   'cultivo': 'lechuga',  'recomendacion': 'pH 7.0-7.5, recambio parcial de agua, buena luz.'},

    {'pez': 'dorado',  'cultivo': 'albahaca', 'recomendacion': 'pH 7.5, recambio cada 10 días, nutrientes bien balanceados.'},
    {'pez': 'dorado',  'cultivo': 'tomate',   'recomendacion': 'pH 7.5-8, excelente oxigenación, monitoreo frecuente.'},
    {'pez': 'dorado',  'cultivo': 'espinaca', 'recomendacion': 'pH 7.2-7.8, recambio parcial cada semana.'},
]

# === Listas para selects frontend ===
CULTIVOS = sorted(list(set([r['cultivo'] for r in FERTILIZANTES])))
SUELOS = sorted(list(set([r['suelo'] for r in FERTILIZANTES])))
CLIMAS = sorted(list(set([r['clima'] for r in FERTILIZANTES])))

PECES = sorted(list(set([r['pez'] for r in ACUAPONIA])))
CULTIVOS_ACUA = sorted(list(set([r['cultivo'] for r in ACUAPONIA])))

# Lista única de síntomas para el frontend
SINTOMAS = sorted(list(set(s for r in DIAGNOSTICOS for s in r['sintomas'])))