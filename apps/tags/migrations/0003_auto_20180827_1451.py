# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-27 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_auto_20180827_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='proxy',
            field=models.CharField(blank=True, choices=[('Afghanistan(AF)', 'Afghanistan(AF)'), ('Aland(AX)', 'Aland(AX)'), ('Albania(AL)', 'Albania(AL)'), ('Algeria(DZ)', 'Algeria(DZ)'), ('AmericanSamoa(AS)', 'AmericanSamoa(AS)'), ('Andorra(AD)', 'Andorra(AD)'), ('Angola(AO)', 'Angola(AO)'), ('Anguilla(AI)', 'Anguilla(AI)'), ('Antarctica(AQ)', 'Antarctica(AQ)'), ('AntiguaandBarbuda(AG)', 'AntiguaandBarbuda(AG)'), ('Argentina(AR)', 'Argentina(AR)'), ('Armenia(AM)', 'Armenia(AM)'), ('Aruba(AW)', 'Aruba(AW)'), ('Australia(AU)', 'Australia(AU)'), ('Austria(AT)', 'Austria(AT)'), ('Azerbaijan(AZ)', 'Azerbaijan(AZ)'), ('Bahamas(BS)', 'Bahamas(BS)'), ('Bahrain(BH)', 'Bahrain(BH)'), ('Bangladesh(BD)', 'Bangladesh(BD)'), ('Barbados(BB)', 'Barbados(BB)'), ('Belarus(BY)', 'Belarus(BY)'), ('Belgium(BE)', 'Belgium(BE)'), ('Belize(BZ)', 'Belize(BZ)'), ('Benin(BJ)', 'Benin(BJ)'), ('Bermuda(BM)', 'Bermuda(BM)'), ('Bhutan(BT)', 'Bhutan(BT)'), ('Bolivia(BO)', 'Bolivia(BO)'), ('Bonaire,SintEustatius,andSaba(BQ)', 'Bonaire,SintEustatius,andSaba(BQ)'), ('BosniaandHerzegovina(BA)', 'BosniaandHerzegovina(BA)'), ('Botswana(BW)', 'Botswana(BW)'), ('Brazil(BR)', 'Brazil(BR)'), ('BritishIndianOceanTerritory(IO)', 'BritishIndianOceanTerritory(IO)'), ('BritishVirginIslands(VG)', 'BritishVirginIslands(VG)'), ('Brunei(BN)', 'Brunei(BN)'), ('Bulgaria(BG)', 'Bulgaria(BG)'), ('BurkinaFaso(BF)', 'BurkinaFaso(BF)'), ('Burundi(BI)', 'Burundi(BI)'), ('Cambodia(KH)', 'Cambodia(KH)'), ('Cameroon(CM)', 'Cameroon(CM)'), ('Canada(CA)', 'Canada(CA)'), ('CapeVerde(CV)', 'CapeVerde(CV)'), ('CaymanIslands(KY)', 'CaymanIslands(KY)'), ('CentralAfricanRepublic(CF)', 'CentralAfricanRepublic(CF)'), ('Chad(TD)', 'Chad(TD)'), ('Chile(CL)', 'Chile(CL)'), ('China(CN)', 'China(CN)'), ('ChristmasIsland(CX)', 'ChristmasIsland(CX)'), ('Cocos[Keeling]Islands(CC)', 'Cocos[Keeling]Islands(CC)'), ('Colombia(CO)', 'Colombia(CO)'), ('Comoros(KM)', 'Comoros(KM)'), ('Congo(CD)', 'Congo(CD)'), ('CookIslands(CK)', 'CookIslands(CK)'), ('CostaRica(CR)', 'CostaRica(CR)'), ('Croatia(HR)', 'Croatia(HR)'), ('Cuba(CU)', 'Cuba(CU)'), ('Cura\xe7ao(CW)', 'Cura\xe7ao(CW)'), ('Cyprus(CY)', 'Cyprus(CY)'), ('Czechia(CZ)', 'Czechia(CZ)'), ('Denmark(DK)', 'Denmark(DK)'), ('Djibouti(DJ)', 'Djibouti(DJ)'), ('Dominica(DM)', 'Dominica(DM)'), ('DominicanRepublic(DO)', 'DominicanRepublic(DO)'), ('EastTimor(TL)', 'EastTimor(TL)'), ('Ecuador(EC)', 'Ecuador(EC)'), ('Egypt(EG)', 'Egypt(EG)'), ('ElSalvador(SV)', 'ElSalvador(SV)'), ('EquatorialGuinea(GQ)', 'EquatorialGuinea(GQ)'), ('Eritrea(ER)', 'Eritrea(ER)'), ('Estonia(EE)', 'Estonia(EE)'), ('Ethiopia(ET)', 'Ethiopia(ET)'), ('FalklandIslands(FK)', 'FalklandIslands(FK)'), ('FaroeIslands(FO)', 'FaroeIslands(FO)'), ('FederatedStatesofMicronesia(FM)', 'FederatedStatesofMicronesia(FM)'), ('Fiji(FJ)', 'Fiji(FJ)'), ('Finland(FI)', 'Finland(FI)'), ('France(FR)', 'France(FR)'), ('FrenchGuiana(GF)', 'FrenchGuiana(GF)'), ('FrenchPolynesia(PF)', 'FrenchPolynesia(PF)'), ('FrenchSouthernTerritories(TF)', 'FrenchSouthernTerritories(TF)'), ('Gabon(GA)', 'Gabon(GA)'), ('Gambia(GM)', 'Gambia(GM)'), ('Georgia(GE)', 'Georgia(GE)'), ('Germany(DE)', 'Germany(DE)'), ('Ghana(GH)', 'Ghana(GH)'), ('Gibraltar(GI)', 'Gibraltar(GI)'), ('Greece(GR)', 'Greece(GR)'), ('Greenland(GL)', 'Greenland(GL)'), ('Grenada(GD)', 'Grenada(GD)'), ('Guadeloupe(GP)', 'Guadeloupe(GP)'), ('Guam(GU)', 'Guam(GU)'), ('Guatemala(GT)', 'Guatemala(GT)'), ('Guernsey(GG)', 'Guernsey(GG)'), ('Guinea(GN)', 'Guinea(GN)'), ('Guinea-Bissau(GW)', 'Guinea-Bissau(GW)'), ('Guyana(GY)', 'Guyana(GY)'), ('Haiti(HT)', 'Haiti(HT)'), ('HashemiteKingdomofJordan(JO)', 'HashemiteKingdomofJordan(JO)'), ('Honduras(HN)', 'Honduras(HN)'), ('HongKong(HK)', 'HongKong(HK)'), ('Hungary(HU)', 'Hungary(HU)'), ('Iceland(IS)', 'Iceland(IS)'), ('India(IN)', 'India(IN)'), ('Indonesia(ID)', 'Indonesia(ID)'), ('Iran(IR)', 'Iran(IR)'), ('Iraq(IQ)', 'Iraq(IQ)'), ('Ireland(IE)', 'Ireland(IE)'), ('IsleofMan(IM)', 'IsleofMan(IM)'), ('Israel(IL)', 'Israel(IL)'), ('Italy(IT)', 'Italy(IT)'), ('IvoryCoast(CI)', 'IvoryCoast(CI)'), ('Jamaica(JM)', 'Jamaica(JM)'), ('Japan(JP)', 'Japan(JP)'), ('Jersey(JE)', 'Jersey(JE)'), ('Kazakhstan(KZ)', 'Kazakhstan(KZ)'), ('Kenya(KE)', 'Kenya(KE)'), ('Kiribati(KI)', 'Kiribati(KI)'), ('Kosovo(XK)', 'Kosovo(XK)'), ('Kuwait(KW)', 'Kuwait(KW)'), ('Kyrgyzstan(KG)', 'Kyrgyzstan(KG)'), ('Laos(LA)', 'Laos(LA)'), ('Latvia(LV)', 'Latvia(LV)'), ('Lebanon(LB)', 'Lebanon(LB)'), ('Lesotho(LS)', 'Lesotho(LS)'), ('Liberia(LR)', 'Liberia(LR)'), ('Libya(LY)', 'Libya(LY)'), ('Liechtenstein(LI)', 'Liechtenstein(LI)'), ('Luxembourg(LU)', 'Luxembourg(LU)'), ('Macao(MO)', 'Macao(MO)'), ('Macedonia(MK)', 'Macedonia(MK)'), ('Madagascar(MG)', 'Madagascar(MG)'), ('Malawi(MW)', 'Malawi(MW)'), ('Malaysia(MY)', 'Malaysia(MY)'), ('Maldives(MV)', 'Maldives(MV)'), ('Mali(ML)', 'Mali(ML)'), ('Malta(MT)', 'Malta(MT)'), ('MarshallIslands(MH)', 'MarshallIslands(MH)'), ('Martinique(MQ)', 'Martinique(MQ)'), ('Mauritania(MR)', 'Mauritania(MR)'), ('Mauritius(MU)', 'Mauritius(MU)'), ('Mayotte(YT)', 'Mayotte(YT)'), ('Mexico(MX)', 'Mexico(MX)'), ('Monaco(MC)', 'Monaco(MC)'), ('Mongolia(MN)', 'Mongolia(MN)'), ('Montenegro(ME)', 'Montenegro(ME)'), ('Montserrat(MS)', 'Montserrat(MS)'), ('Morocco(MA)', 'Morocco(MA)'), ('Mozambique(MZ)', 'Mozambique(MZ)'), ('Myanmar[Burma](MM)', 'Myanmar[Burma](MM)'), ('Namibia(NA)', 'Namibia(NA)'), ('Nauru(NR)', 'Nauru(NR)'), ('Nepal(NP)', 'Nepal(NP)'), ('Netherlands(NL)', 'Netherlands(NL)'), ('NewCaledonia(NC)', 'NewCaledonia(NC)'), ('NewZealand(NZ)', 'NewZealand(NZ)'), ('Nicaragua(NI)', 'Nicaragua(NI)'), ('Niger(NE)', 'Niger(NE)'), ('Nigeria(NG)', 'Nigeria(NG)'), ('Niue(NU)', 'Niue(NU)'), ('NorfolkIsland(NF)', 'NorfolkIsland(NF)'), ('NorthKorea(KP)', 'NorthKorea(KP)'), ('NorthernMarianaIslands(MP)', 'NorthernMarianaIslands(MP)'), ('Norway(NO)', 'Norway(NO)'), ('Oman(OM)', 'Oman(OM)'), ('Pakistan(PK)', 'Pakistan(PK)'), ('Palau(PW)', 'Palau(PW)'), ('Palestine(PS)', 'Palestine(PS)'), ('Panama(PA)', 'Panama(PA)'), ('PapuaNewGuinea(PG)', 'PapuaNewGuinea(PG)'), ('Paraguay(PY)', 'Paraguay(PY)'), ('Peru(PE)', 'Peru(PE)'), ('Philippines(PH)', 'Philippines(PH)'), ('PitcairnIslands(PN)', 'PitcairnIslands(PN)'), ('Poland(PL)', 'Poland(PL)'), ('Portugal(PT)', 'Portugal(PT)'), ('PuertoRico(PR)', 'PuertoRico(PR)'), ('Qatar(QA)', 'Qatar(QA)'), ('RepublicofKorea(KR)', 'RepublicofKorea(KR)'), ('RepublicofLithuania(LT)', 'RepublicofLithuania(LT)'), ('RepublicofMoldova(MD)', 'RepublicofMoldova(MD)'), ('RepublicoftheCongo(CG)', 'RepublicoftheCongo(CG)'), ('R\xe9union(RE)', 'R\xe9union(RE)'), ('Romania(RO)', 'Romania(RO)'), ('Russia(RU)', 'Russia(RU)'), ('Rwanda(RW)', 'Rwanda(RW)'), ('SaintHelena(SH)', 'SaintHelena(SH)'), ('SaintKittsandNevis(KN)', 'SaintKittsandNevis(KN)'), ('SaintLucia(LC)', 'SaintLucia(LC)'), ('SaintMartin(MF)', 'SaintMartin(MF)'), ('SaintPierreandMiquelon(PM)', 'SaintPierreandMiquelon(PM)'), ('SaintVincentandtheGrenadines(VC)', 'SaintVincentandtheGrenadines(VC)'), ('Saint-Barth\xe9lemy(BL)', 'Saint-Barth\xe9lemy(BL)'), ('Samoa(WS)', 'Samoa(WS)'), ('SanMarino(SM)', 'SanMarino(SM)'), ('S\xe3oTom\xe9andPr\xedncipe(ST)', 'S\xe3oTom\xe9andPr\xedncipe(ST)'), ('SaudiArabia(SA)', 'SaudiArabia(SA)'), ('Senegal(SN)', 'Senegal(SN)'), ('Serbia(RS)', 'Serbia(RS)'), ('Seychelles(SC)', 'Seychelles(SC)'), ('SierraLeone(SL)', 'SierraLeone(SL)'), ('Singapore(SG)', 'Singapore(SG)'), ('SintMaarten(SX)', 'SintMaarten(SX)'), ('SlovakRepublic(SK)', 'SlovakRepublic(SK)'), ('Slovenia(SI)', 'Slovenia(SI)'), ('SolomonIslands(SB)', 'SolomonIslands(SB)'), ('Somalia(SO)', 'Somalia(SO)'), ('SouthAfrica(ZA)', 'SouthAfrica(ZA)'), ('SouthGeorgiaandtheSouthSandwichIslands(GS)', 'SouthGeorgiaandtheSouthSandwichIslands(GS)'), ('SouthSudan(SS)', 'SouthSudan(SS)'), ('Spain(ES)', 'Spain(ES)'), ('SriLanka(LK)', 'SriLanka(LK)'), ('Sudan(SD)', 'Sudan(SD)'), ('Suriname(SR)', 'Suriname(SR)'), ('SvalbardandJanMayen(SJ)', 'SvalbardandJanMayen(SJ)'), ('Swaziland(SZ)', 'Swaziland(SZ)'), ('Sweden(SE)', 'Sweden(SE)'), ('Switzerland(CH)', 'Switzerland(CH)'), ('Syria(SY)', 'Syria(SY)'), ('Taiwan(TW)', 'Taiwan(TW)'), ('Tajikistan(TJ)', 'Tajikistan(TJ)'), ('Tanzania(TZ)', 'Tanzania(TZ)'), ('Thailand(TH)', 'Thailand(TH)'), ('Togo(TG)', 'Togo(TG)'), ('Tokelau(TK)', 'Tokelau(TK)'), ('Tonga(TO)', 'Tonga(TO)'), ('TrinidadandTobago(TT)', 'TrinidadandTobago(TT)'), ('Tunisia(TN)', 'Tunisia(TN)'), ('Turkey(TR)', 'Turkey(TR)'), ('Turkmenistan(TM)', 'Turkmenistan(TM)'), ('TurksandCaicosIslands(TC)', 'TurksandCaicosIslands(TC)'), ('Tuvalu(TV)', 'Tuvalu(TV)'), ('U.S.MinorOutlyingIslands(UM)', 'U.S.MinorOutlyingIslands(UM)'), ('U.S.VirginIslands(VI)', 'U.S.VirginIslands(VI)'), ('Uganda(UG)', 'Uganda(UG)'), ('Ukraine(UA)', 'Ukraine(UA)'), ('UnitedArabEmirates(AE)', 'UnitedArabEmirates(AE)'), ('UnitedKingdom(GB)', 'UnitedKingdom(GB)'), ('UnitedStates(US)', 'UnitedStates(US)'), ('Uruguay(UY)', 'Uruguay(UY)'), ('Uzbekistan(UZ)', 'Uzbekistan(UZ)'), ('Vanuatu(VU)', 'Vanuatu(VU)'), ('VaticanCity(VA)', 'VaticanCity(VA)'), ('Venezuela(VE)', 'Venezuela(VE)'), ('Vietnam(VN)', 'Vietnam(VN)'), ('WallisandFutuna(WF)', 'WallisandFutuna(WF)'), ('Yemen(YE)', 'Yemen(YE)'), ('Zambia(ZM)', 'Zambia(ZM)'), ('Zimbabwe(ZW)', 'Zimbabwe(ZW)')], max_length=20, null=True, verbose_name='\u4ee3\u7406'),
        ),
    ]
