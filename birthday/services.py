from django.conf import settings
from django.utils import timezone
from .models import Birthdays
import requests


def get_today_birthdays():
    today = timezone.localdate()
    return Birthdays.objects.filter(
        birth_date__month=today.month,
        birth_date__day=today.day,
    )


def build_message(birthdays):
    birthdays = list(birthdays)
    if not birthdays:
        return None
    nomes = ", ".join(b.name for b in birthdays)
    return f"Hoje é aniversário de: {nomes}! 🎉🎂"


def send_whatsapp_group_message(text: str):
    cfg = settings.EVOLUTION_API
    if not text:
        return {"sent": False, "reason": "empty_text"}

    # Padrão comum do Evolution API (ajuste se sua instância usar outro path/headers)
    url = f"{cfg['BASE_URL'].rstrip('/')}/message/sendText/{cfg['INSTANCE']}"
    headers = {"Content-Type": "application/json", "apikey": cfg["TOKEN"]}
    payload = {
        "number": cfg["GROUP_JID"],  # ex.: "1203630...@g.us"
        "text": text,

    }

    resp = requests.post(url, headers=headers, json=payload, timeout=20)
    resp.raise_for_status()
    return {"sent": True, "response": resp.json()}


def send_today_birthdays():
    bdays = get_today_birthdays()
    msg = build_message(bdays)
    if not msg:
        return {"sent": False, "reason": "no_birthdays_today"}
    return send_whatsapp_group_message(msg)
