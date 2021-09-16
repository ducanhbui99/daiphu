from django.urls import path
from . import views



app_name = "public"
urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path('service', views.service, name="service"),
    path('san_pham', views.san_pham, name="san_pham"),
    path('bot_son/bot_son_trong_nha/he_epoxy', views.he_epoxy, name="he_epoxy"),
    path('bot_son/bot_son_trong_nha/he_polyester_epoxy', views.he_polyester_epoxy, name="he_polyester_epoxy"),
    path('bot_son/bot_son_ngoai_troi/he_polyester_tgic', views.he_polyester_tgic, name="he_polyester_tgic"),
    path('bot_son/bot_son_ngoai_troi/he_polyester_haa', views.he_polyester_haa, name="he_polyester_haa"),
    path('bot_son/bot_son_ngoai_troi/he_polyester_urethane', views.he_polyester_urethane, name="he_polyester_urethane"),
    path('san_pham/thiet_bi', views.thiet_bi, name="thiet_bi"),
    path('san_pham/thiet_bi_phun_son/thiet_bi_tu_dong', views.equip_auto, name="equip_auto"),
    path('san_pham/thiet_bi_phun_son/thiet_bi_tu_dong/auto_booth', views.auto_booth, name="auto_booth"),
    path('san_pham/thiet_bi_phun_son/thiet_bi_tu_dong/auto_injector', views.auto_injector, name="auto_injector"),
    path('san_pham/thiet_bi_phun_son/thiet_bi_tu_dong/enamel_booth', views.enamel_booth, name="enamel_booth"),
    path('san_pham/thiet_bi_phun_son/thiet_bi_tu_dong/multistar', views.multistar, name="multistar"),
    path('san_pham/thiet_bi_phun_son/thiet_bi_tu_dong/optiflex', views.optiflex, name="optiflex"),
    path('san_pham/thiet_bi_phun_son/thiet_bi_tu_dong/optigun', views.optigun, name="optigun"),
    path('san_pham/thiet_bi_phun_son/thiet_bi_tu_dong/optispray', views.optispray, name="optispray"),
    path('san_pham/thiet_bi_phun_son/thiet_bi_tu_dong/optistar', views.optistar, name="optistar"),
    path('san_pham/thiet_bi_phun_son/thiet_bi_tu_dong/powder_center', views.powder_center, name="powder_center"),
    path('san_pham/thiet_bi_phun_son/thiet_bi_tu_dong/reciprocator', views.reciprocator, name="reciprocator"),
    path('san_pham/thiet_bi_phun_son/thiet_bi_tu_dong/optimove', views.optimove, name="optimove"),
    path('san_pham/thiet_bi_phun_son/thiet_bi_tu_dong/magic_control', views.magic_control, name="magic_control"),
    path('san_pham/thiet_bi_phun_son/thiet_bi_tu_dong/powder_hopper', views.powder_hopper, name="powder_hopper"),
    path('san_pham/thiet_bi_phun_son/thiet_bi_phun_tay', views.equip_manual, name="equip_manual"),
    path('san_pham/thiet_bi_phun_son/thiet_bi_phun_tay/optiselect', views.optiselect, name="optiselect"),
    path('san_pham/thiet_bi_phun_son/thiet_bi_phun_tay/manual_booth', views.manual_booth, name="manual_booth"),
    path('san_pham/thiet_bi_phun_son/thiet_bi_phun_tay/manual_injector', views.manual_injector, name="manual_injector"),
    path('san_pham/thiet_bi_phun_son/equp_manual/manual_optiflex', views.manual_optiflex, name="manual_optiflex"),
    path('san_pham/thiet_bi_phun_son/equp_manual/manual_optispray', views.manual_optispray, name="manual_optispray"),
    path('san_pham/bot_son', views.bot_son, name="bot_son"),
    path('san_pham/bot_son/bot_son_trong_nha', views.bot_son_trong_nha, name="bot_son_trong_nha"),
    path('san_pham/bot_son/bot_son_ngoai_troi', views.bot_son_ngoai_troi, name="bot_son_ngoai_troi"),
    
]
