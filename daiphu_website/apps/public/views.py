from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")

def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")

def service(request: HttpRequest) -> HttpResponse:
    return render(request, "service.html")

def san_pham(request: HttpRequest) -> HttpResponse:
    return render(request, "san_pham.html")

def he_epoxy(request: HttpRequest) -> HttpResponse:
    return render(request, "bot_son/he_epoxy.html")

def he_polyester_epoxy(request: HttpRequest) -> HttpResponse:
    return render(request, "bot_son/he_polyester_epoxy.html")

def he_polyester_tgic(request: HttpRequest) -> HttpResponse:
    return render(request, "bot_son/he_polyester_tgic.html")

def he_polyester_haa(request: HttpRequest) -> HttpResponse:
    return render(request, "bot_son/he_polyester_haa.html")

def he_polyester_urethane(request: HttpRequest) -> HttpResponse:
    return render(request, "bot_son/he_polyester_urethane.html")

def thiet_bi(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/thiet_bi.html")

def equip_auto(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/equip_auto.html")

def auto_booth(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/auto_booth.html")

def auto_injector(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/auto_injector.html")

def enamel_booth(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/enamel_booth.html")

def multistar(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/multistar.html")

def optiflex(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/optiflex.html")

def optigun(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/optigun.html")

def optispray(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/optispray.html")

def optistar(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/optistar.html")

def powder_center(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/powder_center.html")

def powder_hopper(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/powder_hopper.html")

def equip_auto(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/equip_auto.html")

def reciprocator(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/reciprocator.html")

def optimove(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/optimove.html")

def magic_control(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/magic_control.html")

def equip_manual(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/equip_manual.html")

def manual_injector(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/manual_injector.html")

def optiselect(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/optiselect.html")

def manual_booth(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/manual_booth.html")

def manual_optiflex(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/manual_optiflex.html")

def manual_optispray(request: HttpRequest) -> HttpResponse:
    return render(request, "thiet_bi/manual_optispray.html")

def bot_son(request: HttpRequest) -> HttpResponse:
    return render(request, "bot_son/bot_son.html")

def bot_son_trong_nha(request: HttpRequest) -> HttpResponse:
    return render(request, "bot_son/trong_nha.html")

def bot_son_ngoai_troi(request: HttpRequest) -> HttpResponse:
    return render(request, "bot_son/ngoai_troi.html")
