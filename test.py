from PIL import Image, ImageDraw, ImageFont

# Configuración inicial
width = 1200
height = 2500  # Ajusta según el contenido
background_color = (255, 255, 255)  # Blanco
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# Fuentes (asegúrate de tener una fuente que soporte cirílico)
font_path = "arial.ttf"  # Usa Arial o descarga una fuente como "NotoSans-Regular.ttf"
title_font = ImageFont.truetype(font_path, 40)
subtitle_font = ImageFont.truetype(font_path, 30)
bold_font = ImageFont.truetype(font_path, 25)
text_font = ImageFont.truetype(font_path, 20)

# Coordenadas iniciales
x, y = 50, 50

# Función para agregar texto con saltos de línea
def add_text(text, font, y_offset=20):
    global y
    draw.text((x, y), text, font=font, fill=(0, 0, 0))
    y += font.getsize(text)[1] + y_offset

# Contenido en ruso (texto completo)
content = """
# ВТОРАЯ МИРОВАЯ ВОЙНА

## 1 сентября 1939 г. — 2 сентября 1945 г.  
Глобальный военный конфликт, в котором участвовали ведущие мировые державы. Боевые действия велись на множестве фронтов и привели к беспрецедентным человеческим и материальным потерям.

### СТРАНЫ ОСИ  
**Германия** **Италия** **Япония**

## ПРИЧИНЫ  

#### Версальский договор  
Жёсткие условия, наложенные на Германию после Первой мировой войны, способствовали росту нацизма.  

#### Великая депрессия  
Экономический кризис усилил националистические и милитаристские настроения в Европе.  

#### Экспансионизм  
Нацистская Германия, фашистская Италия и Япония стремились к территориальному расширению.  

#### Пакт Молотова-Риббентропа  
Договор о ненападении между Германией и СССР облегчил вторжение в Польшу.  

## ПОСЛЕДСТВИЯ  

#### Разрушения  
Массированные бомбардировки уничтожили целые города в Европе и Японии.  

#### Изменение границ  
Территории стран-агрессоров были сокращены.  

#### ООН  
Создана Организация Объединённых Наций для обеспечения международной безопасности.  

#### Деколонизация  
Ослабление Европы ускорило деколонизацию Азии и Африки.  

#### Холодная война  
Европа разделилась на два блока: западный (под руководством США) и восточный (под руководством СССР).  

**Статистика войны**  

## УЧАСТНИКИ  

#### СОЮЗНИКИ (победители)  
**Великобритания** **Франция** **СССР** **США** **Китай**  

Война началась с вторжения Германии в Польшу  
и распространилась на весь мир.  

Основные фронты находились в Европе,  
Средиземноморье и Тихом океане.  

Вступление в войну СССР и США стало  
решающим фактором победы Союзников.  

Это единственная война, в которой применялось ядерное оружие —  
атомные бомбардировки Хиросимы и Нагасаки.  

Война завершилась безоговорочной капитуляцией  
Германии и Японии.  

### Союзнические конференции  

Во время войны Союзники проводили встречи для согласования  
стратегических решений и условий послевоенного мира.  

**КАСАБЛАНКСКАЯ**                **ТЕГЕРАНСКАЯ**  
**КОНФЕРЕНЦИЯ**                  **КОНФЕРЕНЦИЯ**  
Требовалась безоговорочная      Решено открыть второй фронт  
капитуляция стран Оси.          во Франции.  

**ЯЛТИНСКАЯ**                    **ПОТСДАМСКАЯ**  
**КОНФЕРЕНЦИЯ**                  **КОНФЕРЕНЦИЯ**  
Определены новые границы        Германия и Австрия разделены  
и условия для Германии.         на четыре оккупационные зоны.  

#### Холокост  

Нацисты реализовали план уничтожения еврейского населения Европы,  
известный как «окончательное решение». В Польше были построены лагеря смерти,  
где применялись массовые убийства — расстрелы и газовые камеры.  
Концентрационные лагеря использовались для заключения групп,  
считавшихся врагами государства, в бесчеловечных условиях.  
Жертвами стали 11 миллионов человек, включая 6 миллионов евреев.  
"""

# Procesar el texto línea por línea
lines = content.strip().split("\n")
for line in lines:
    if line.startswith("# "):
        add_text(line[2:], title_font)
    elif line.startswith("## "):
        add_text(line[3:], subtitle_font)
    elif line.startswith("### "):
        add_text(line[4:], bold_font)
    elif line.startswith("**"):
        add_text(line, bold_font)
    else:
        add_text(line, text_font, y_offset=15)

# Guardar la imagen
image.save("segunda_guerra_mundial_ruso.png")
print("Imagen generada: segunda_guerra_mundial_ruso.png")