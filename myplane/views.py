from django.shortcuts import render
import math


def index(request):
    return render(request, "input.html")


def weightBalance(request):
    depart = "depart" in request.POST and request.POST["depart"]
    dest = "dest" in request.POST and request.POST["dest"]
    marks = "marks" in request.POST and request.POST["marks"]
    tipo = "tipo" in request.POST and request.POST["tipo"]
    bow = "bow" in request.POST and request.POST["bow"]
   
    pax1 = "pax1" in request.POST and request.POST["pax1"]
    pax2 = "pax2" in request.POST and request.POST["pax2"]
    pax3 = "pax3" in request.POST and request.POST["pax3"]
    pax4 = "pax4" in request.POST and request.POST["pax4"]
    pax5 = "pax5" in request.POST and request.POST["pax5"]
    pax6 = "pax6" in request.POST and request.POST["pax6"]
    pax7 = "pax7" in request.POST and request.POST["pax7"]
    pax8 = "pax8" in request.POST and request.POST["pax8"]
    pax9 = "pax9" in request.POST and request.POST["pax9"]
    # baggage
    bgg1 = "bgg1" in request.POST and request.POST["bgg1"]
    bgg2 = "bgg2" in request.POST and request.POST["bgg2"]

    b = int(bow)
    p1 = int(pax1)
    p2 = int(pax2)
    p3 = int(pax3)
    p4 = int(pax4)
    p5 = int(pax5)
    p6 = int(pax6)
    p7 = int(pax7)
    p8 = int(pax8)
    p9 = int(pax9)
    b1 = int(bgg1)
    b2 = int(bgg2)

    pax = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9
    cargo = b1 + b2
    zfw = b + pax + cargo

    fueled = "fueled" in request.POST and request.POST["fueled"]
    ventral = "ventral" in request.POST and request.POST["ventral"]

    myFuel = list(range(120, 1270, 1))
    minus_wing_parcial_mom = 0
    plus_wing_parcial_mom = 0
    wing_parcial = 0

    if int(fueled) == 120 or int(fueled) < 140:
        minus_wing_parcial_mom = -196
    elif int(fueled) == 140 or int(fueled) < 160:
        minus_wing_parcial_mom = -338
    elif int(fueled) == 160 or int(fueled) < 180:
        minus_wing_parcial_mom = -479
    elif int(fueled) == 180 or int(fueled) < 200:
        minus_wing_parcial_mom = -578
    elif int(fueled) == 200 or int(fueled) < 220:
        minus_wing_parcial_mom = -677
    elif int(fueled) == 220 or int(fueled) < 240:
        minus_wing_parcial_mom = -792
    elif int(fueled) == 240 or int(fueled) < 260:
        minus_wing_parcial_mom = -907
    elif int(fueled) == 260 or int(fueled) < 280:
        minus_wing_parcial_mom = -985
    elif int(fueled) == 280 or int(fueled) < 300:
        minus_wing_parcial_mom = -1063
    elif int(fueled) == 300 or int(fueled) < 320:
        minus_wing_parcial_mom = -1127
    elif int(fueled) == 320 or int(fueled) < 340:
        minus_wing_parcial_mom = -1190
    elif int(fueled) == 340 or int(fueled) < 360:
        minus_wing_parcial_mom = -1248
    elif int(fueled) == 360 or int(fueled) < 380:
        minus_wing_parcial_mom = -1307
    elif int(fueled) == 380 or int(fueled) < 400:
        minus_wing_parcial_mom = -1352
    elif int(fueled) == 400 or int(fueled) < 420:
        minus_wing_parcial_mom = -1397
    elif int(fueled) == 420 or int(fueled) < 460:
        minus_wing_parcial_mom = -1434
    elif int(fueled) == 460 or int(fueled) < 480:
        minus_wing_parcial_mom = -1484
    elif int(fueled) == 480 or int(fueled) < 500:
        minus_wing_parcial_mom = -1497
    elif int(fueled) == 500 or int(fueled) < 520:
        minus_wing_parcial_mom = -1503
    elif int(fueled) == 520 or int(fueled) < 540:
        minus_wing_parcial_mom = -1510
    elif int(fueled) == 540 or int(fueled) < 560:
        minus_wing_parcial_mom = -1506
    elif int(fueled) == 560 or int(fueled) < 580:
        minus_wing_parcial_mom = -1503
    elif int(fueled) == 580 or int(fueled) < 600:
        minus_wing_parcial_mom = -1479
    elif int(fueled) == 600 or int(fueled) < 620:
        minus_wing_parcial_mom = -1455
    elif int(fueled) == 620 or int(fueled) < 640:
        minus_wing_parcial_mom = -1406
    elif int(fueled) == 640 or int(fueled) < 660:
        minus_wing_parcial_mom = -1358
    elif int(fueled) == 660 or int(fueled) < 680:
        minus_wing_parcial_mom = -1298
    elif int(fueled) == 680 or int(fueled) < 700:
        minus_wing_parcial_mom = -1239
    elif int(fueled) == 700 or int(fueled) < 720:
        minus_wing_parcial_mom = -1175
    elif int(fueled) == 720 or int(fueled) < 740:
        minus_wing_parcial_mom = -1110
    elif int(fueled) == 740 or int(fueled) < 760:
        minus_wing_parcial_mom = -1035
    elif int(fueled) == 760 or int(fueled) < 780:
        minus_wing_parcial_mom = -959
    elif int(fueled) == 780 or int(fueled) < 800:
        minus_wing_parcial_mom = -862
    elif int(fueled) == 800 or int(fueled) < 820:
        minus_wing_parcial_mom = -764
    elif int(fueled) == 820 or int(fueled) < 840:
        minus_wing_parcial_mom = -655
    elif int(fueled) == 840 or int(fueled) < 860:
        minus_wing_parcial_mom = --545
    elif int(fueled) == 860 or int(fueled) < 880:
        minus_wing_parcial_mom = -420
    elif int(fueled) == 880 or int(fueled) < 900:
        minus_wing_parcial_mom = -295
    elif int(fueled) == 900 or int(fueled) < 920:
        minus_wing_parcial_mom = -149
    elif int(fueled) == 920 or int(fueled) < 940:
        minus_wing_parcial_mom = -3
    elif int(fueled) == 940 or int(fueled) < 960:
        plus_wing_parcial_mom = 165
    elif int(fueled) == 960 or int(fueled) < 980:
        plus_wing_parcial_mom = 333
    elif int(fueled) == 980 or int(fueled) < 1000:
        plus_wing_parcial_mom = 528
    elif int(fueled) == 1000 or int(fueled) < 1020:
        plus_wing_parcial_mom = 722
    elif int(fueled) == 1020 or int(fueled) < 1040:
        plus_wing_parcial_mom = 959
    elif int(fueled) == 1040 or int(fueled) < 1060:
        plus_wing_parcial_mom = 1195
    elif int(fueled) == 1060 or int(fueled) < 1080:
        plus_wing_parcial_mom = 1479
    elif int(fueled) == 1080 or int(fueled) < 1100:
        plus_wing_parcial_mom = 1763
    elif int(fueled) == 1100 or int(fueled) < 1120:
        plus_wing_parcial_mom = 2086
    elif int(fueled) == 1120 or int(fueled) < 1140:
        plus_wing_parcial_mom = 2409
    elif int(fueled) == 1140 or int(fueled) < 1150:
        plus_wing_parcial_mom = 2743
    elif int(fueled) == 1153:
        plus_wing_parcial_mom = 2930
    elif int(fueled) == 1160 or int(fueled) < 1180:
        plus_wing_parcial_mom = 3077
    elif int(fueled) == 1180 or int(fueled) < 1200:
        plus_wing_parcial_mom = 3480
    elif int(fueled) == 1200 or int(fueled) < 1220:
        plus_wing_parcial_mom = 3883
    elif int(fueled) == 1220 or int(fueled) < 1240:
        plus_wing_parcial_mom = 4443
    elif int(fueled) == 1240 or int(fueled) < 1260:
        plus_wing_parcial_mom = 5002
    elif int(fueled) == 1263:
        plus_wing_parcial_mom = 5737

    trip = "trip" in request.POST and request.POST["trip"]
    trip = int(trip)
    wing_parcial = round(int(fueled) * float(6.66))
    ventral = int(ventral)
    to_fuel = wing_parcial + ventral
    to_weight = to_fuel + zfw
    ld_fuel = to_fuel - trip
    ld_weight = to_weight - trip

    lh_row_one_arm = float(-8.80)
    rh_row_one_arm = float(-8.80)
    lh_row_two_arm = float(-5.68)
    rh_row_two_arm = float(-5.68)
    lh_sette_front_arm = float(-3.48)
    rh_row_four_arm = float(-0.64)
    lh_settee_center_arm = float(-0.70)
    lh_settee_rear_arm = float(1.16)
    qtu_arm = float(1.46)
    front_baggage_arm = float(-12.10)
    rear_baggage_arm = float(5.50)

    PAX1_mom = int(pax1) * lh_row_one_arm
    PAX2_mom = int(pax2) * rh_row_one_arm
    PAX3_mom = int(pax3) * lh_row_two_arm
    PAX4_mom = int(pax4) * rh_row_two_arm
    PAX5_mom = int(pax5) * lh_sette_front_arm
    PAX6_mom = int(pax6) * rh_row_four_arm
    PAX7_mom = int(pax7) * lh_settee_center_arm
    PAX8_mom = int(pax8) * lh_settee_rear_arm
    PAX9_mom = int(pax9) * qtu_arm

    bagg1_mom = int(bgg1) * front_baggage_arm
    bagg2_mom = int(bgg2) * rear_baggage_arm

    ventral_fuel_mom = 0
    if ventral:
        ventral_fuel_mom = 12.514

    minus_moments = (
        float(minus_wing_parcial_mom)
        + float(PAX1_mom)
        + float(PAX2_mom)
        + float(PAX3_mom)
        + float(PAX4_mom)
        + float(PAX5_mom)
        + float(PAX6_mom)
        + float(PAX7_mom)
        + float(bagg1_mom)
    )

    before_round = b * float(0.6614)
    bow_mom = round(before_round)

    plus_moments = (
        float(plus_wing_parcial_mom)
        + float(ventral_fuel_mom)
        + float(PAX8_mom)
        + float(PAX9_mom)
        + float(bagg2_mom)
        + float(bow_mom)
    )

    total_mom = float(minus_moments + plus_moments)

    cg = total_mom / to_weight
    trim = round(((cg + 1.308) * 100) / 7.263)

    def truncate(n, decimals=2):
        multiplier = 10**decimals
        return int(n * multiplier) / multiplier

    to_cg = truncate(cg)

    context = {
        "marks": marks,
        "tipo": tipo,
        "bow": bow,
        #"bow_mom": bow_mom,
        "zfw": zfw,
        "fueled": fueled,
        "ventral": ventral,
        "trip": trip,
        "to_fuel": to_fuel,
        "to_weight": to_weight,
        "ld_fuel": ld_fuel,
        "ld_weight": ld_weight,
        "to_cg": to_cg,
        "trim": trim,
        "depart": depart,
        "dest": dest,
        "total_mom": total_mom,
        "minus_moments": minus_moments,
        "plus_moments": plus_moments,
        "bagg1_mom": bagg1_mom,
        "bagg2_mom": bagg2_mom,
        "pax": pax,
        "cargo": cargo,
        "plus_wing_parcial_mom": plus_wing_parcial_mom,
        "minus_wing_parcial_mom": minus_wing_parcial_mom,
        "bgg1": bgg1,
        "bgg2": bgg2,
        "wing_parcial": wing_parcial,
    }
    return render(request, "result.html", context)
