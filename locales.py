import re
from dataclasses import dataclass


@dataclass
class zh_CN:
    UPLOAD_COMPLETE = '上传完成。'
    UPLOAD_COMPLETE_NON_ASCII = '上传完成，但关卡中含有特殊字符，仅对电脑版可见。'
    FILE_TOO_LARGE = '文件大于 4MB。'


@dataclass
class es_ES:
    UPLOAD_COMPLETE = 'Publicar completado.'
    UPLOAD_COMPLETE_NON_ASCII = 'Publicar completo, pero con caracteres especiales, solo será visible para PC.'
    FILE_TOO_LARGE = 'El archivo tiene más de 4 MB.'


@dataclass
class en_US:
    UPLOAD_COMPLETE = 'Upload completed.'
    UPLOAD_COMPLETE_NON_ASCII = 'Upload completed, but name with special characters, will only be visible on PC.'
    FILE_TOO_LARGE = 'File is bigger than 4MB.'


def convert_tags(locale_from: str, locale_to: str, tags):
    # The server stores Chinese tag names, so it needs to be converted
    tags_es_to_cn = {
        "Tradicional": "标准",
        "Puzles": "解谜",
        "Contrarreloj": "计时挑战",
        "Autoavance": "自卷轴",
        "Automatismos": "自动图",
        "Corto pero intenso": "一次通过",
        "Competitivo": "对战",
        "Tematico": "机关",
        "Música": "音乐",
        "Artístico": "美术",
        "Habilidad": "技巧",
        "Disparos": "射击",
        "Contra jefes": "BOSS战",
        "En solitario": "单人"
    }
    tags_en_to_cn = {
        "Standard": "标准",
        "Puzzle": "解谜",
        "Speedrun": "计时挑战",
        "Autoscroll": "自卷轴",
        "Auto-mario": "自动图",
        "Short and Sweet": "一次通过",
        "Multiplayer": "对战",
        "Themed": "机关",
        "Music": "音乐",
        "Art": "美术",
        "Technical": "技巧",
        "Shooter": "射击",
        "Boss battle": "BOSS战",
        "Singleplayer": "单人"
    }

    # Because the translation script fills in extra characters with spaces, they need to be dealt here with regex
    if locale_from == 'ES' and locale_to == 'CN':
        for item in tags_es_to_cn:
            tags = tags.replace(item, tags_es_to_cn[item])
    elif locale_from == 'CN' and locale_to == 'ES':
        tags = re.sub(r'/ +,/', ',', tags).rstrip(' ')
        for item in tags_es_to_cn:
            tags = tags.replace(tags_es_to_cn[item], item)
    elif locale_from == 'EN' and locale_to == 'CN':
        tags = re.sub(r'/ +,/', ',', tags).rstrip(' ')
        for item in tags_en_to_cn:
            tags = tags.replace(item, tags_en_to_cn[item])
    elif locale_from == 'CN' and locale_to == 'EN':
        tags = re.sub(r'/ +,/', ',', tags).rstrip(' ')
        for item in tags_en_to_cn:
            tags = tags.replace(tags_en_to_cn[item], item)

    return tags
