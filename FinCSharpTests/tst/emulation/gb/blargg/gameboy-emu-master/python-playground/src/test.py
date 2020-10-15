'''
Created on Jul 2, 2010

@author: bgouveia
'''

if __name__ == '__main__':
 gbDAATable= [
  0x0080,0x0100,0x0200,0x0300,0x0400,0x0500,0x0600,0x0700,
  0x0800,0x0900,0x1020,0x1120,0x1220,0x1320,0x1420,0x1520,
  0x1000,0x1100,0x1200,0x1300,0x1400,0x1500,0x1600,0x1700,
  0x1800,0x1900,0x2020,0x2120,0x2220,0x2320,0x2420,0x2520,
  0x2000,0x2100,0x2200,0x2300,0x2400,0x2500,0x2600,0x2700,
  0x2800,0x2900,0x3020,0x3120,0x3220,0x3320,0x3420,0x3520,
  0x3000,0x3100,0x3200,0x3300,0x3400,0x3500,0x3600,0x3700,
  0x3800,0x3900,0x4020,0x4120,0x4220,0x4320,0x4420,0x4520,
  0x4000,0x4100,0x4200,0x4300,0x4400,0x4500,0x4600,0x4700,
  0x4800,0x4900,0x5020,0x5120,0x5220,0x5320,0x5420,0x5520,
  0x5000,0x5100,0x5200,0x5300,0x5400,0x5500,0x5600,0x5700,
  0x5800,0x5900,0x6020,0x6120,0x6220,0x6320,0x6420,0x6520,
  0x6000,0x6100,0x6200,0x6300,0x6400,0x6500,0x6600,0x6700,
  0x6800,0x6900,0x7020,0x7120,0x7220,0x7320,0x7420,0x7520,
  0x7000,0x7100,0x7200,0x7300,0x7400,0x7500,0x7600,0x7700,
  0x7800,0x7900,0x8020,0x8120,0x8220,0x8320,0x8420,0x8520,
  0x8000,0x8100,0x8200,0x8300,0x8400,0x8500,0x8600,0x8700,
  0x8800,0x8900,0x9020,0x9120,0x9220,0x9320,0x9420,0x9520,
  0x9000,0x9100,0x9200,0x9300,0x9400,0x9500,0x9600,0x9700,
  0x9800,0x9900,0x00B0,0x0130,0x0230,0x0330,0x0430,0x0530,
  0x0090,0x0110,0x0210,0x0310,0x0410,0x0510,0x0610,0x0710,
  0x0810,0x0910,0x1030,0x1130,0x1230,0x1330,0x1430,0x1530,
  0x1010,0x1110,0x1210,0x1310,0x1410,0x1510,0x1610,0x1710,
  0x1810,0x1910,0x2030,0x2130,0x2230,0x2330,0x2430,0x2530,
  0x2010,0x2110,0x2210,0x2310,0x2410,0x2510,0x2610,0x2710,
  0x2810,0x2910,0x3030,0x3130,0x3230,0x3330,0x3430,0x3530,
  0x3010,0x3110,0x3210,0x3310,0x3410,0x3510,0x3610,0x3710,
  0x3810,0x3910,0x4030,0x4130,0x4230,0x4330,0x4430,0x4530,
  0x4010,0x4110,0x4210,0x4310,0x4410,0x4510,0x4610,0x4710,
  0x4810,0x4910,0x5030,0x5130,0x5230,0x5330,0x5430,0x5530,
  0x5010,0x5110,0x5210,0x5310,0x5410,0x5510,0x5610,0x5710,
  0x5810,0x5910,0x6030,0x6130,0x6230,0x6330,0x6430,0x6530,
  0x6010,0x6110,0x6210,0x6310,0x6410,0x6510,0x6610,0x6710,
  0x6810,0x6910,0x7030,0x7130,0x7230,0x7330,0x7430,0x7530,
  0x7010,0x7110,0x7210,0x7310,0x7410,0x7510,0x7610,0x7710,
  0x7810,0x7910,0x8030,0x8130,0x8230,0x8330,0x8430,0x8530,
  0x8010,0x8110,0x8210,0x8310,0x8410,0x8510,0x8610,0x8710,
  0x8810,0x8910,0x9030,0x9130,0x9230,0x9330,0x9430,0x9530,
  0x9010,0x9110,0x9210,0x9310,0x9410,0x9510,0x9610,0x9710,
  0x9810,0x9910,0xA030,0xA130,0xA230,0xA330,0xA430,0xA530,
  0xA010,0xA110,0xA210,0xA310,0xA410,0xA510,0xA610,0xA710,
  0xA810,0xA910,0xB030,0xB130,0xB230,0xB330,0xB430,0xB530,
  0xB010,0xB110,0xB210,0xB310,0xB410,0xB510,0xB610,0xB710,
  0xB810,0xB910,0xC030,0xC130,0xC230,0xC330,0xC430,0xC530,
  0xC010,0xC110,0xC210,0xC310,0xC410,0xC510,0xC610,0xC710,
  0xC810,0xC910,0xD030,0xD130,0xD230,0xD330,0xD430,0xD530,
  0xD010,0xD110,0xD210,0xD310,0xD410,0xD510,0xD610,0xD710,
  0xD810,0xD910,0xE030,0xE130,0xE230,0xE330,0xE430,0xE530,
  0xE010,0xE110,0xE210,0xE310,0xE410,0xE510,0xE610,0xE710,
  0xE810,0xE910,0xF030,0xF130,0xF230,0xF330,0xF430,0xF530,
  0xF010,0xF110,0xF210,0xF310,0xF410,0xF510,0xF610,0xF710,
  0xF810,0xF910,0x00B0,0x0130,0x0230,0x0330,0x0430,0x0530,
  0x0090,0x0110,0x0210,0x0310,0x0410,0x0510,0x0610,0x0710,
  0x0810,0x0910,0x1030,0x1130,0x1230,0x1330,0x1430,0x1530,
  0x1010,0x1110,0x1210,0x1310,0x1410,0x1510,0x1610,0x1710,
  0x1810,0x1910,0x2030,0x2130,0x2230,0x2330,0x2430,0x2530,
  0x2010,0x2110,0x2210,0x2310,0x2410,0x2510,0x2610,0x2710,
  0x2810,0x2910,0x3030,0x3130,0x3230,0x3330,0x3430,0x3530,
  0x3010,0x3110,0x3210,0x3310,0x3410,0x3510,0x3610,0x3710,
  0x3810,0x3910,0x4030,0x4130,0x4230,0x4330,0x4430,0x4530,
  0x4010,0x4110,0x4210,0x4310,0x4410,0x4510,0x4610,0x4710,
  0x4810,0x4910,0x5030,0x5130,0x5230,0x5330,0x5430,0x5530,
  0x5010,0x5110,0x5210,0x5310,0x5410,0x5510,0x5610,0x5710,
  0x5810,0x5910,0x6030,0x6130,0x6230,0x6330,0x6430,0x6530,
  0x0600,0x0700,0x0800,0x0900,0x0A00,0x0B00,0x0C00,0x0D00,
  0x0E00,0x0F00,0x1020,0x1120,0x1220,0x1320,0x1420,0x1520,
  0x1600,0x1700,0x1800,0x1900,0x1A00,0x1B00,0x1C00,0x1D00,
  0x1E00,0x1F00,0x2020,0x2120,0x2220,0x2320,0x2420,0x2520,
  0x2600,0x2700,0x2800,0x2900,0x2A00,0x2B00,0x2C00,0x2D00,
  0x2E00,0x2F00,0x3020,0x3120,0x3220,0x3320,0x3420,0x3520,
  0x3600,0x3700,0x3800,0x3900,0x3A00,0x3B00,0x3C00,0x3D00,
  0x3E00,0x3F00,0x4020,0x4120,0x4220,0x4320,0x4420,0x4520,
  0x4600,0x4700,0x4800,0x4900,0x4A00,0x4B00,0x4C00,0x4D00,
  0x4E00,0x4F00,0x5020,0x5120,0x5220,0x5320,0x5420,0x5520,
  0x5600,0x5700,0x5800,0x5900,0x5A00,0x5B00,0x5C00,0x5D00,
  0x5E00,0x5F00,0x6020,0x6120,0x6220,0x6320,0x6420,0x6520,
  0x6600,0x6700,0x6800,0x6900,0x6A00,0x6B00,0x6C00,0x6D00,
  0x6E00,0x6F00,0x7020,0x7120,0x7220,0x7320,0x7420,0x7520,
  0x7600,0x7700,0x7800,0x7900,0x7A00,0x7B00,0x7C00,0x7D00,
  0x7E00,0x7F00,0x8020,0x8120,0x8220,0x8320,0x8420,0x8520,
  0x8600,0x8700,0x8800,0x8900,0x8A00,0x8B00,0x8C00,0x8D00,
  0x8E00,0x8F00,0x9020,0x9120,0x9220,0x9320,0x9420,0x9520,
  0x9600,0x9700,0x9800,0x9900,0x9A00,0x9B00,0x9C00,0x9D00,
  0x9E00,0x9F00,0x00B0,0x0130,0x0230,0x0330,0x0430,0x0530,
  0x0610,0x0710,0x0810,0x0910,0x0A10,0x0B10,0x0C10,0x0D10,
  0x0E10,0x0F10,0x1030,0x1130,0x1230,0x1330,0x1430,0x1530,
  0x1610,0x1710,0x1810,0x1910,0x1A10,0x1B10,0x1C10,0x1D10,
  0x1E10,0x1F10,0x2030,0x2130,0x2230,0x2330,0x2430,0x2530,
  0x2610,0x2710,0x2810,0x2910,0x2A10,0x2B10,0x2C10,0x2D10,
  0x2E10,0x2F10,0x3030,0x3130,0x3230,0x3330,0x3430,0x3530,
  0x3610,0x3710,0x3810,0x3910,0x3A10,0x3B10,0x3C10,0x3D10,
  0x3E10,0x3F10,0x4030,0x4130,0x4230,0x4330,0x4430,0x4530,
  0x4610,0x4710,0x4810,0x4910,0x4A10,0x4B10,0x4C10,0x4D10,
  0x4E10,0x4F10,0x5030,0x5130,0x5230,0x5330,0x5430,0x5530,
  0x5610,0x5710,0x5810,0x5910,0x5A10,0x5B10,0x5C10,0x5D10,
  0x5E10,0x5F10,0x6030,0x6130,0x6230,0x6330,0x6430,0x6530,
  0x6610,0x6710,0x6810,0x6910,0x6A10,0x6B10,0x6C10,0x6D10,
  0x6E10,0x6F10,0x7030,0x7130,0x7230,0x7330,0x7430,0x7530,
  0x7610,0x7710,0x7810,0x7910,0x7A10,0x7B10,0x7C10,0x7D10,
  0x7E10,0x7F10,0x8030,0x8130,0x8230,0x8330,0x8430,0x8530,
  0x8610,0x8710,0x8810,0x8910,0x8A10,0x8B10,0x8C10,0x8D10,
  0x8E10,0x8F10,0x9030,0x9130,0x9230,0x9330,0x9430,0x9530,
  0x9610,0x9710,0x9810,0x9910,0x9A10,0x9B10,0x9C10,0x9D10,
  0x9E10,0x9F10,0xA030,0xA130,0xA230,0xA330,0xA430,0xA530,
  0xA610,0xA710,0xA810,0xA910,0xAA10,0xAB10,0xAC10,0xAD10,
  0xAE10,0xAF10,0xB030,0xB130,0xB230,0xB330,0xB430,0xB530,
  0xB610,0xB710,0xB810,0xB910,0xBA10,0xBB10,0xBC10,0xBD10,
  0xBE10,0xBF10,0xC030,0xC130,0xC230,0xC330,0xC430,0xC530,
  0xC610,0xC710,0xC810,0xC910,0xCA10,0xCB10,0xCC10,0xCD10,
  0xCE10,0xCF10,0xD030,0xD130,0xD230,0xD330,0xD430,0xD530,
  0xD610,0xD710,0xD810,0xD910,0xDA10,0xDB10,0xDC10,0xDD10,
  0xDE10,0xDF10,0xE030,0xE130,0xE230,0xE330,0xE430,0xE530,
  0xE610,0xE710,0xE810,0xE910,0xEA10,0xEB10,0xEC10,0xED10,
  0xEE10,0xEF10,0xF030,0xF130,0xF230,0xF330,0xF430,0xF530,
  0xF610,0xF710,0xF810,0xF910,0xFA10,0xFB10,0xFC10,0xFD10,
  0xFE10,0xFF10,0x00B0,0x0130,0x0230,0x0330,0x0430,0x0530,
  0x0610,0x0710,0x0810,0x0910,0x0A10,0x0B10,0x0C10,0x0D10,
  0x0E10,0x0F10,0x1030,0x1130,0x1230,0x1330,0x1430,0x1530,
  0x1610,0x1710,0x1810,0x1910,0x1A10,0x1B10,0x1C10,0x1D10,
  0x1E10,0x1F10,0x2030,0x2130,0x2230,0x2330,0x2430,0x2530,
  0x2610,0x2710,0x2810,0x2910,0x2A10,0x2B10,0x2C10,0x2D10,
  0x2E10,0x2F10,0x3030,0x3130,0x3230,0x3330,0x3430,0x3530,
  0x3610,0x3710,0x3810,0x3910,0x3A10,0x3B10,0x3C10,0x3D10,
  0x3E10,0x3F10,0x4030,0x4130,0x4230,0x4330,0x4430,0x4530,
  0x4610,0x4710,0x4810,0x4910,0x4A10,0x4B10,0x4C10,0x4D10,
  0x4E10,0x4F10,0x5030,0x5130,0x5230,0x5330,0x5430,0x5530,
  0x5610,0x5710,0x5810,0x5910,0x5A10,0x5B10,0x5C10,0x5D10,
  0x5E10,0x5F10,0x6030,0x6130,0x6230,0x6330,0x6430,0x6530,
  0x00C0,0x0140,0x0240,0x0340,0x0440,0x0540,0x0640,0x0740,
  0x0840,0x0940,0x0440,0x0540,0x0640,0x0740,0x0840,0x0940,
  0x1040,0x1140,0x1240,0x1340,0x1440,0x1540,0x1640,0x1740,
  0x1840,0x1940,0x1440,0x1540,0x1640,0x1740,0x1840,0x1940,
  0x2040,0x2140,0x2240,0x2340,0x2440,0x2540,0x2640,0x2740,
  0x2840,0x2940,0x2440,0x2540,0x2640,0x2740,0x2840,0x2940,
  0x3040,0x3140,0x3240,0x3340,0x3440,0x3540,0x3640,0x3740,
  0x3840,0x3940,0x3440,0x3540,0x3640,0x3740,0x3840,0x3940,
  0x4040,0x4140,0x4240,0x4340,0x4440,0x4540,0x4640,0x4740,
  0x4840,0x4940,0x4440,0x4540,0x4640,0x4740,0x4840,0x4940,
  0x5040,0x5140,0x5240,0x5340,0x5440,0x5540,0x5640,0x5740,
  0x5840,0x5940,0x5440,0x5540,0x5640,0x5740,0x5840,0x5940,
  0x6040,0x6140,0x6240,0x6340,0x6440,0x6540,0x6640,0x6740,
  0x6840,0x6940,0x6440,0x6540,0x6640,0x6740,0x6840,0x6940,
  0x7040,0x7140,0x7240,0x7340,0x7440,0x7540,0x7640,0x7740,
  0x7840,0x7940,0x7440,0x7540,0x7640,0x7740,0x7840,0x7940,
  0x8040,0x8140,0x8240,0x8340,0x8440,0x8540,0x8640,0x8740,
  0x8840,0x8940,0x8440,0x8540,0x8640,0x8740,0x8840,0x8940,
  0x9040,0x9140,0x9240,0x9340,0x9440,0x9540,0x9640,0x9740,
  0x9840,0x9940,0x3450,0x3550,0x3650,0x3750,0x3850,0x3950,
  0x4050,0x4150,0x4250,0x4350,0x4450,0x4550,0x4650,0x4750,
  0x4850,0x4950,0x4450,0x4550,0x4650,0x4750,0x4850,0x4950,
  0x5050,0x5150,0x5250,0x5350,0x5450,0x5550,0x5650,0x5750,
  0x5850,0x5950,0x5450,0x5550,0x5650,0x5750,0x5850,0x5950,
  0x6050,0x6150,0x6250,0x6350,0x6450,0x6550,0x6650,0x6750,
  0x6850,0x6950,0x6450,0x6550,0x6650,0x6750,0x6850,0x6950,
  0x7050,0x7150,0x7250,0x7350,0x7450,0x7550,0x7650,0x7750,
  0x7850,0x7950,0x7450,0x7550,0x7650,0x7750,0x7850,0x7950,
  0x8050,0x8150,0x8250,0x8350,0x8450,0x8550,0x8650,0x8750,
  0x8850,0x8950,0x8450,0x8550,0x8650,0x8750,0x8850,0x8950,
  0x9050,0x9150,0x9250,0x9350,0x9450,0x9550,0x9650,0x9750,
  0x9850,0x9950,0x9450,0x9550,0x9650,0x9750,0x9850,0x9950,
  0xA050,0xA150,0xA250,0xA350,0xA450,0xA550,0xA650,0xA750,
  0xA850,0xA950,0xA450,0xA550,0xA650,0xA750,0xA850,0xA950,
  0xB050,0xB150,0xB250,0xB350,0xB450,0xB550,0xB650,0xB750,
  0xB850,0xB950,0xB450,0xB550,0xB650,0xB750,0xB850,0xB950,
  0xC050,0xC150,0xC250,0xC350,0xC450,0xC550,0xC650,0xC750,
  0xC850,0xC950,0xC450,0xC550,0xC650,0xC750,0xC850,0xC950,
  0xD050,0xD150,0xD250,0xD350,0xD450,0xD550,0xD650,0xD750,
  0xD850,0xD950,0xD450,0xD550,0xD650,0xD750,0xD850,0xD950,
  0xE050,0xE150,0xE250,0xE350,0xE450,0xE550,0xE650,0xE750,
  0xE850,0xE950,0xE450,0xE550,0xE650,0xE750,0xE850,0xE950,
  0xF050,0xF150,0xF250,0xF350,0xF450,0xF550,0xF650,0xF750,
  0xF850,0xF950,0xF450,0xF550,0xF650,0xF750,0xF850,0xF950,
  0x00D0,0x0150,0x0250,0x0350,0x0450,0x0550,0x0650,0x0750,
  0x0850,0x0950,0x0450,0x0550,0x0650,0x0750,0x0850,0x0950,
  0x1050,0x1150,0x1250,0x1350,0x1450,0x1550,0x1650,0x1750,
  0x1850,0x1950,0x1450,0x1550,0x1650,0x1750,0x1850,0x1950,
  0x2050,0x2150,0x2250,0x2350,0x2450,0x2550,0x2650,0x2750,
  0x2850,0x2950,0x2450,0x2550,0x2650,0x2750,0x2850,0x2950,
  0x3050,0x3150,0x3250,0x3350,0x3450,0x3550,0x3650,0x3750,
  0x3850,0x3950,0x3450,0x3550,0x3650,0x3750,0x3850,0x3950,
  0x4050,0x4150,0x4250,0x4350,0x4450,0x4550,0x4650,0x4750,
  0x4850,0x4950,0x4450,0x4550,0x4650,0x4750,0x4850,0x4950,
  0x5050,0x5150,0x5250,0x5350,0x5450,0x5550,0x5650,0x5750,
  0x5850,0x5950,0x5450,0x5550,0x5650,0x5750,0x5850,0x5950,
  0x6050,0x6150,0x6250,0x6350,0x6450,0x6550,0x6650,0x6750,
  0x6850,0x6950,0x6450,0x6550,0x6650,0x6750,0x6850,0x6950,
  0x7050,0x7150,0x7250,0x7350,0x7450,0x7550,0x7650,0x7750,
  0x7850,0x7950,0x7450,0x7550,0x7650,0x7750,0x7850,0x7950,
  0x8050,0x8150,0x8250,0x8350,0x8450,0x8550,0x8650,0x8750,
  0x8850,0x8950,0x8450,0x8550,0x8650,0x8750,0x8850,0x8950,
  0x9050,0x9150,0x9250,0x9350,0x9450,0x9550,0x9650,0x9750,
  0x9850,0x9950,0x9450,0x9550,0x9650,0x9750,0x9850,0x9950,
  0xFA60,0xFB60,0xFC60,0xFD60,0xFE60,0xFF60,0x00C0,0x0140,
  0x0240,0x0340,0x0440,0x0540,0x0640,0x0740,0x0840,0x0940,
  0x0A60,0x0B60,0x0C60,0x0D60,0x0E60,0x0F60,0x1040,0x1140,
  0x1240,0x1340,0x1440,0x1540,0x1640,0x1740,0x1840,0x1940,
  0x1A60,0x1B60,0x1C60,0x1D60,0x1E60,0x1F60,0x2040,0x2140,
  0x2240,0x2340,0x2440,0x2540,0x2640,0x2740,0x2840,0x2940,
  0x2A60,0x2B60,0x2C60,0x2D60,0x2E60,0x2F60,0x3040,0x3140,
  0x3240,0x3340,0x3440,0x3540,0x3640,0x3740,0x3840,0x3940,
  0x3A60,0x3B60,0x3C60,0x3D60,0x3E60,0x3F60,0x4040,0x4140,
  0x4240,0x4340,0x4440,0x4540,0x4640,0x4740,0x4840,0x4940,
  0x4A60,0x4B60,0x4C60,0x4D60,0x4E60,0x4F60,0x5040,0x5140,
  0x5240,0x5340,0x5440,0x5540,0x5640,0x5740,0x5840,0x5940,
  0x5A60,0x5B60,0x5C60,0x5D60,0x5E60,0x5F60,0x6040,0x6140,
  0x6240,0x6340,0x6440,0x6540,0x6640,0x6740,0x6840,0x6940,
  0x6A60,0x6B60,0x6C60,0x6D60,0x6E60,0x6F60,0x7040,0x7140,
  0x7240,0x7340,0x7440,0x7540,0x7640,0x7740,0x7840,0x7940,
  0x7A60,0x7B60,0x7C60,0x7D60,0x7E60,0x7F60,0x8040,0x8140,
  0x8240,0x8340,0x8440,0x8540,0x8640,0x8740,0x8840,0x8940,
  0x8A60,0x8B60,0x8C60,0x8D60,0x8E60,0x8F60,0x9040,0x9140,
  0x9240,0x9340,0x3450,0x3550,0x3650,0x3750,0x3850,0x3950,
  0x3A70,0x3B70,0x3C70,0x3D70,0x3E70,0x3F70,0x4050,0x4150,
  0x4250,0x4350,0x4450,0x4550,0x4650,0x4750,0x4850,0x4950,
  0x4A70,0x4B70,0x4C70,0x4D70,0x4E70,0x4F70,0x5050,0x5150,
  0x5250,0x5350,0x5450,0x5550,0x5650,0x5750,0x5850,0x5950,
  0x5A70,0x5B70,0x5C70,0x5D70,0x5E70,0x5F70,0x6050,0x6150,
  0x6250,0x6350,0x6450,0x6550,0x6650,0x6750,0x6850,0x6950,
  0x6A70,0x6B70,0x6C70,0x6D70,0x6E70,0x6F70,0x7050,0x7150,
  0x7250,0x7350,0x7450,0x7550,0x7650,0x7750,0x7850,0x7950,
  0x7A70,0x7B70,0x7C70,0x7D70,0x7E70,0x7F70,0x8050,0x8150,
  0x8250,0x8350,0x8450,0x8550,0x8650,0x8750,0x8850,0x8950,
  0x8A70,0x8B70,0x8C70,0x8D70,0x8E70,0x8F70,0x9050,0x9150,
  0x9250,0x9350,0x9450,0x9550,0x9650,0x9750,0x9850,0x9950,
  0x9A70,0x9B70,0x9C70,0x9D70,0x9E70,0x9F70,0xA050,0xA150,
  0xA250,0xA350,0xA450,0xA550,0xA650,0xA750,0xA850,0xA950,
  0xAA70,0xAB70,0xAC70,0xAD70,0xAE70,0xAF70,0xB050,0xB150,
  0xB250,0xB350,0xB450,0xB550,0xB650,0xB750,0xB850,0xB950,
  0xBA70,0xBB70,0xBC70,0xBD70,0xBE70,0xBF70,0xC050,0xC150,
  0xC250,0xC350,0xC450,0xC550,0xC650,0xC750,0xC850,0xC950,
  0xCA70,0xCB70,0xCC70,0xCD70,0xCE70,0xCF70,0xD050,0xD150,
  0xD250,0xD350,0xD450,0xD550,0xD650,0xD750,0xD850,0xD950,
  0xDA70,0xDB70,0xDC70,0xDD70,0xDE70,0xDF70,0xE050,0xE150,
  0xE250,0xE350,0xE450,0xE550,0xE650,0xE750,0xE850,0xE950,
  0xEA70,0xEB70,0xEC70,0xED70,0xEE70,0xEF70,0xF050,0xF150,
  0xF250,0xF350,0xF450,0xF550,0xF650,0xF750,0xF850,0xF950,
  0xFA70,0xFB70,0xFC70,0xFD70,0xFE70,0xFF70,0x00D0,0x0150,
  0x0250,0x0350,0x0450,0x0550,0x0650,0x0750,0x0850,0x0950,
  0x0A70,0x0B70,0x0C70,0x0D70,0x0E70,0x0F70,0x1050,0x1150,
  0x1250,0x1350,0x1450,0x1550,0x1650,0x1750,0x1850,0x1950,
  0x1A70,0x1B70,0x1C70,0x1D70,0x1E70,0x1F70,0x2050,0x2150,
  0x2250,0x2350,0x2450,0x2550,0x2650,0x2750,0x2850,0x2950,
  0x2A70,0x2B70,0x2C70,0x2D70,0x2E70,0x2F70,0x3050,0x3150,
  0x3250,0x3350,0x3450,0x3550,0x3650,0x3750,0x3850,0x3950,
  0x3A70,0x3B70,0x3C70,0x3D70,0x3E70,0x3F70,0x4050,0x4150,
  0x4250,0x4350,0x4450,0x4550,0x4650,0x4750,0x4850,0x4950,
  0x4A70,0x4B70,0x4C70,0x4D70,0x4E70,0x4F70,0x5050,0x5150,
  0x5250,0x5350,0x5450,0x5550,0x5650,0x5750,0x5850,0x5950,
  0x5A70,0x5B70,0x5C70,0x5D70,0x5E70,0x5F70,0x6050,0x6150,
  0x6250,0x6350,0x6450,0x6550,0x6650,0x6750,0x6850,0x6950,
  0x6A70,0x6B70,0x6C70,0x6D70,0x6E70,0x6F70,0x7050,0x7150,
  0x7250,0x7350,0x7450,0x7550,0x7650,0x7750,0x7850,0x7950,
  0x7A70,0x7B70,0x7C70,0x7D70,0x7E70,0x7F70,0x8050,0x8150,
  0x8250,0x8350,0x8450,0x8550,0x8650,0x8750,0x8850,0x8950,
  0x8A70,0x8B70,0x8C70,0x8D70,0x8E70,0x8F70,0x9050,0x9150,
  0x9250,0x9350,0x9450,0x9550,0x9650,0x9750,0x9850,0x9950]
 
 meu=[0x80, 0x100, 0x200, 0x300, 0x400, 0x500, 0x600, 0x700, 
    0x800, 0x900, 0x1020, 0x1120, 0x1220, 0x1320, 0x1420, 0x1520, 
    0x1000, 0x1100, 0x1200, 0x1300, 0x1400, 0x1500, 0x1600, 0x1700, 
    0x1800, 0x1900, 0x2020, 0x2120, 0x2220, 0x2320, 0x2420, 0x2520, 
    0x2000, 0x2100, 0x2200, 0x2300, 0x2400, 0x2500, 0x2600, 0x2700, 
    0x2800, 0x2900, 0x3020, 0x3120, 0x3220, 0x3320, 0x3420, 0x3520, 
    0x3000, 0x3100, 0x3200, 0x3300, 0x3400, 0x3500, 0x3600, 0x3700, 
    0x3800, 0x3900, 0x4020, 0x4120, 0x4220, 0x4320, 0x4420, 0x4520, 
    0x4000, 0x4100, 0x4200, 0x4300, 0x4400, 0x4500, 0x4600, 0x4700, 
    0x4800, 0x4900, 0x5020, 0x5120, 0x5220, 0x5320, 0x5420, 0x5520, 
    0x5000, 0x5100, 0x5200, 0x5300, 0x5400, 0x5500, 0x5600, 0x5700, 
    0x5800, 0x5900, 0x6020, 0x6120, 0x6220, 0x6320, 0x6420, 0x6520, 
    0x6000, 0x6100, 0x6200, 0x6300, 0x6400, 0x6500, 0x6600, 0x6700, 
    0x6800, 0x6900, 0x7020, 0x7120, 0x7220, 0x7320, 0x7420, 0x7520, 
    0x7000, 0x7100, 0x7200, 0x7300, 0x7400, 0x7500, 0x7600, 0x7700, 
    0x7800, 0x7900, 0x8020, 0x8120, 0x8220, 0x8320, 0x8420, 0x8520, 
    0x8000, 0x8100, 0x8200, 0x8300, 0x8400, 0x8500, 0x8600, 0x8700, 
    0x8800, 0x8900, 0x9020, 0x9120, 0x9220, 0x9320, 0x9420, 0x9520, 
    0x9000, 0x9100, 0x9200, 0x9300, 0x9400, 0x9500, 0x9600, 0x9700, 
    0x9800, 0x9900, 0xa030, 0xa130, 0xa230, 0xa330, 0xa430, 0xa530, 
    0x90, 0x110, 0x210, 0x310, 0x410, 0x510, 0x610, 0x710, 
    0x810, 0x910, 0x1030, 0x1130, 0x1230, 0x1330, 0x1430, 0x1530, 
    0x1010, 0x1110, 0x1210, 0x1310, 0x1410, 0x1510, 0x1610, 0x1710, 
    0x1810, 0x1910, 0x2030, 0x2130, 0x2230, 0x2330, 0x2430, 0x2530, 
    0x2010, 0x2110, 0x2210, 0x2310, 0x2410, 0x2510, 0x2610, 0x2710, 
    0x2810, 0x2910, 0x3030, 0x3130, 0x3230, 0x3330, 0x3430, 0x3530, 
    0x3010, 0x3110, 0x3210, 0x3310, 0x3410, 0x3510, 0x3610, 0x3710, 
    0x3810, 0x3910, 0x4030, 0x4130, 0x4230, 0x4330, 0x4430, 0x4530, 
    0x4010, 0x4110, 0x4210, 0x4310, 0x4410, 0x4510, 0x4610, 0x4710, 
    0x4810, 0x4910, 0x5030, 0x5130, 0x5230, 0x5330, 0x5430, 0x5530, 
    0x5010, 0x5110, 0x5210, 0x5310, 0x5410, 0x5510, 0x5610, 0x5710, 
    0x5810, 0x5910, 0x6030, 0x6130, 0x6230, 0x6330, 0x6430, 0x6530, 
    
    0x6010, 0x6110, 0x6210, 0x6310, 0x6410, 0x6510, 0x6610, 0x6710, 
    0x6810, 0x6910, 0x7030, 0x7130, 0x7230, 0x7330, 0x7430, 0x7530, 
    0x7010, 0x7110, 0x7210, 0x7310, 0x7410, 0x7510, 0x7610, 0x7710, 
    0x7810, 0x7910, 0x8030, 0x8130, 0x8230, 0x8330, 0x8430, 0x8530, 
    0x8010, 0x8110, 0x8210, 0x8310, 0x8410, 0x8510, 0x8610, 0x8710, 
    0x8810, 0x8910, 0x9030, 0x9130, 0x9230, 0x9330, 0x9430, 0x9530, 
    0x9010, 0x9110, 0x9210, 0x9310, 0x9410, 0x9510, 0x9610, 0x9710, 
    0x9810, 0x9910, 0xa030, 0xa130, 0xa230, 0xa330, 0xa430, 0xa530, 
    0xa010, 0xa110, 0xa210, 0xa310, 0xa410, 0xa510, 0xa610, 0xa710, 
    0xa810, 0xa910, 0xb030, 0xb130, 0xb230, 0xb330, 0xb430, 0xb530, 
    0xb010, 0xb110, 0xb210, 0xb310, 0xb410, 0xb510, 0xb610, 0xb710, 
    0xb810, 0xb910, 0xc030, 0xc130, 0xc230, 0xc330, 0xc430, 0xc530, 
    0xc010, 0xc110, 0xc210, 0xc310, 0xc410, 0xc510, 0xc610, 0xc710, 
    0xc810, 0xc910, 0xd030, 0xd130, 0xd230, 0xd330, 0xd430, 0xd530, 
    0xd010, 0xd110, 0xd210, 0xd310, 0xd410, 0xd510, 0xd610, 0xd710, 
    0xd810, 0xd910, 0xe030, 0xe130, 0xe230, 0xe330, 0xe430, 0xe530, 
    0xe010, 0xe110, 0xe210, 0xe310, 0xe410, 0xe510, 0xe610, 0xe710, 
    0xe810, 0xe910, 0xf030, 0xf130, 0xf230, 0xf330, 0xf430, 0xf530, 
    0xf010, 0xf110, 0xf210, 0xf310, 0xf410, 0xf510, 0xf610, 0xf710, 
    0xf810, 0xf910, 0xb0, 0x130, 0x230, 0x330, 0x430, 0x530, 
    0x90, 0x110, 0x210, 0x310, 0x410, 0x510, 0x610, 0x710, 
    0x810, 0x910, 0x1030, 0x1130, 0x1230, 0x1330, 0x1430, 0x1530, 
    0x1010, 0x1110, 0x1210, 0x1310, 0x1410, 0x1510, 0x1610, 0x1710, 
    0x1810, 0x1910, 0x2030, 0x2130, 0x2230, 0x2330, 0x2430, 0x2530, 
    0x2010, 0x2110, 0x2210, 0x2310, 0x2410, 0x2510, 0x2610, 0x2710, 
    0x2810, 0x2910, 0x3030, 0x3130, 0x3230, 0x3330, 0x3430, 0x3530, 
    0x3010, 0x3110, 0x3210, 0x3310, 0x3410, 0x3510, 0x3610, 0x3710, 
    0x3810, 0x3910, 0x4030, 0x4130, 0x4230, 0x4330, 0x4430, 0x4530, 
    0x4010, 0x4110, 0x4210, 0x4310, 0x4410, 0x4510, 0x4610, 0x4710, 
    0x4810, 0x4910, 0x5030, 0x5130, 0x5230, 0x5330, 0x5430, 0x5530, 
    0x5010, 0x5110, 0x5210, 0x5310, 0x5410, 0x5510, 0x5610, 0x5710, 
    0x5810, 0x5910, 0x6030, 0x6130, 0x6230, 0x6330, 0x6430, 0x6530, 
    
    0x600, 0x700, 0x800, 0x900, 0xa00, 0xb00, 0xc00, 0xd00, 
    0xe00, 0xf00, 0x1020, 0x1120, 0x1220, 0x1320, 0x1420, 0x1520, 
    0x1600, 0x1700, 0x1800, 0x1900, 0x1a00, 0x1b00, 0x1c00, 0x1d00, 
    0x1e00, 0x1f00, 0x2020, 0x2120, 0x2220, 0x2320, 0x2420, 0x2520, 
    0x2600, 0x2700, 0x2800, 0x2900, 0x2a00, 0x2b00, 0x2c00, 0x2d00, 
    0x2e00, 0x2f00, 0x3020, 0x3120, 0x3220, 0x3320, 0x3420, 0x3520, 
    0x3600, 0x3700, 0x3800, 0x3900, 0x3a00, 0x3b00, 0x3c00, 0x3d00, 
    0x3e00, 0x3f00, 0x4020, 0x4120, 0x4220, 0x4320, 0x4420, 0x4520, 
    0x4600, 0x4700, 0x4800, 0x4900, 0x4a00, 0x4b00, 0x4c00, 0x4d00, 
    0x4e00, 0x4f00, 0x5020, 0x5120, 0x5220, 0x5320, 0x5420, 0x5520, 
    0x5600, 0x5700, 0x5800, 0x5900, 0x5a00, 0x5b00, 0x5c00, 0x5d00, 
    0x5e00, 0x5f00, 0x6020, 0x6120, 0x6220, 0x6320, 0x6420, 0x6520, 
    0x6600, 0x6700, 0x6800, 0x6900, 0x6a00, 0x6b00, 0x6c00, 0x6d00, 
    0x6e00, 0x6f00, 0x7020, 0x7120, 0x7220, 0x7320, 0x7420, 0x7520, 
    0x7600, 0x7700, 0x7800, 0x7900, 0x7a00, 0x7b00, 0x7c00, 0x7d00, 
    0x7e00, 0x7f00, 0x8020, 0x8120, 0x8220, 0x8320, 0x8420, 0x8520, 
    0x8600, 0x8700, 0x8800, 0x8900, 0x8a00, 0x8b00, 0x8c00, 0x8d00, 
    0x8e00, 0x8f00, 0x9020, 0x9120, 0x9220, 0x9320, 0x9420, 0x9520, 
    0x9600, 0x9700, 0x9800, 0x9900, 0x9a00, 0x9b00, 0x9c00, 0x9d00, 
    0x9e00, 0x9f00, 0xa030, 0xa130, 0xa230, 0xa330, 0xa430, 0xa530, 
    0x610, 0x710, 0x810, 0x910, 0xa10, 0xb10, 0xc10, 0xd10, 
    0xe10, 0xf10, 0x1030, 0x1130, 0x1230, 0x1330, 0x1430, 0x1530, 
    0x1610, 0x1710, 0x1810, 0x1910, 0x1a10, 0x1b10, 0x1c10, 0x1d10, 
    0x1e10, 0x1f10, 0x2030, 0x2130, 0x2230, 0x2330, 0x2430, 0x2530, 
    0x2610, 0x2710, 0x2810, 0x2910, 0x2a10, 0x2b10, 0x2c10, 0x2d10, 
    0x2e10, 0x2f10, 0x3030, 0x3130, 0x3230, 0x3330, 0x3430, 0x3530, 
    0x3610, 0x3710, 0x3810, 0x3910, 0x3a10, 0x3b10, 0x3c10, 0x3d10, 
    0x3e10, 0x3f10, 0x4030, 0x4130, 0x4230, 0x4330, 0x4430, 0x4530, 
    0x4610, 0x4710, 0x4810, 0x4910, 0x4a10, 0x4b10, 0x4c10, 0x4d10, 
    0x4e10, 0x4f10, 0x5030, 0x5130, 0x5230, 0x5330, 0x5430, 0x5530, 
    0x5610, 0x5710, 0x5810, 0x5910, 0x5a10, 0x5b10, 0x5c10, 0x5d10, 
    0x5e10, 0x5f10, 0x6030, 0x6130, 0x6230, 0x6330, 0x6430, 0x6530, 
    
    0x6610, 0x6710, 0x6810, 0x6910, 0x6a10, 0x6b10, 0x6c10, 0x6d10, 
    0x6e10, 0x6f10, 0x7030, 0x7130, 0x7230, 0x7330, 0x7430, 0x7530, 
    0x7610, 0x7710, 0x7810, 0x7910, 0x7a10, 0x7b10, 0x7c10, 0x7d10, 
    0x7e10, 0x7f10, 0x8030, 0x8130, 0x8230, 0x8330, 0x8430, 0x8530, 
    0x8610, 0x8710, 0x8810, 0x8910, 0x8a10, 0x8b10, 0x8c10, 0x8d10, 
    0x8e10, 0x8f10, 0x9030, 0x9130, 0x9230, 0x9330, 0x9430, 0x9530, 
    0x9610, 0x9710, 0x9810, 0x9910, 0x9a10, 0x9b10, 0x9c10, 0x9d10, 
    0x9e10, 0x9f10, 0xa030, 0xa130, 0xa230, 0xa330, 0xa430, 0xa530, 
    0xa610, 0xa710, 0xa810, 0xa910, 0xaa10, 0xab10, 0xac10, 0xad10, 
    0xae10, 0xaf10, 0xb030, 0xb130, 0xb230, 0xb330, 0xb430, 0xb530, 
    0xb610, 0xb710, 0xb810, 0xb910, 0xba10, 0xbb10, 0xbc10, 0xbd10, 
    0xbe10, 0xbf10, 0xc030, 0xc130, 0xc230, 0xc330, 0xc430, 0xc530, 
    0xc610, 0xc710, 0xc810, 0xc910, 0xca10, 0xcb10, 0xcc10, 0xcd10, 
    0xce10, 0xcf10, 0xd030, 0xd130, 0xd230, 0xd330, 0xd430, 0xd530, 
    0xd610, 0xd710, 0xd810, 0xd910, 0xda10, 0xdb10, 0xdc10, 0xdd10, 
    0xde10, 0xdf10, 0xe030, 0xe130, 0xe230, 0xe330, 0xe430, 0xe530, 
    0xe610, 0xe710, 0xe810, 0xe910, 0xea10, 0xeb10, 0xec10, 0xed10, 
    0xee10, 0xef10, 0xf030, 0xf130, 0xf230, 0xf330, 0xf430, 0xf530, 
    0xf610, 0xf710, 0xf810, 0xf910, 0xfa10, 0xfb10, 0xfc10, 0xfd10, 
    0xfe10, 0xff10, 0xb0, 0x130, 0x230, 0x330, 0x430, 0x530, 
    0x610, 0x710, 0x810, 0x910, 0xa10, 0xb10, 0xc10, 0xd10, 
    0xe10, 0xf10, 0x1030, 0x1130, 0x1230, 0x1330, 0x1430, 0x1530, 
    0x1610, 0x1710, 0x1810, 0x1910, 0x1a10, 0x1b10, 0x1c10, 0x1d10, 
    0x1e10, 0x1f10, 0x2030, 0x2130, 0x2230, 0x2330, 0x2430, 0x2530, 
    0x2610, 0x2710, 0x2810, 0x2910, 0x2a10, 0x2b10, 0x2c10, 0x2d10, 
    0x2e10, 0x2f10, 0x3030, 0x3130, 0x3230, 0x3330, 0x3430, 0x3530, 
    0x3610, 0x3710, 0x3810, 0x3910, 0x3a10, 0x3b10, 0x3c10, 0x3d10, 
    0x3e10, 0x3f10, 0x4030, 0x4130, 0x4230, 0x4330, 0x4430, 0x4530, 
    0x4610, 0x4710, 0x4810, 0x4910, 0x4a10, 0x4b10, 0x4c10, 0x4d10, 
    0x4e10, 0x4f10, 0x5030, 0x5130, 0x5230, 0x5330, 0x5430, 0x5530, 
    0x5610, 0x5710, 0x5810, 0x5910, 0x5a10, 0x5b10, 0x5c10, 0x5d10, 
    0x5e10, 0x5f10, 0x6030, 0x6130, 0x6230, 0x6330, 0x6430, 0x6530, 
    
    0xc0, 0x140, 0x240, 0x340, 0x440, 0x540, 0x640, 0x740, 
    0x840, 0x940, 0xa40, 0xb40, 0xc40, 0xd40, 0xe40, 0xf40, 
    0x1040, 0x1140, 0x1240, 0x1340, 0x1440, 0x1540, 0x1640, 0x1740, 
    0x1840, 0x1940, 0x1a40, 0x1b40, 0x1c40, 0x1d40, 0x1e40, 0x1f40, 
    0x2040, 0x2140, 0x2240, 0x2340, 0x2440, 0x2540, 0x2640, 0x2740, 
    0x2840, 0x2940, 0x2a40, 0x2b40, 0x2c40, 0x2d40, 0x2e40, 0x2f40, 
    0x3040, 0x3140, 0x3240, 0x3340, 0x3440, 0x3540, 0x3640, 0x3740, 
    0x3840, 0x3940, 0x3a40, 0x3b40, 0x3c40, 0x3d40, 0x3e40, 0x3f40, 
    0x4040, 0x4140, 0x4240, 0x4340, 0x4440, 0x4540, 0x4640, 0x4740, 
    0x4840, 0x4940, 0x4a40, 0x4b40, 0x4c40, 0x4d40, 0x4e40, 0x4f40, 
    0x5040, 0x5140, 0x5240, 0x5340, 0x5440, 0x5540, 0x5640, 0x5740, 
    0x5840, 0x5940, 0x5a40, 0x5b40, 0x5c40, 0x5d40, 0x5e40, 0x5f40, 
    0x6040, 0x6140, 0x6240, 0x6340, 0x6440, 0x6540, 0x6640, 0x6740, 
    0x6840, 0x6940, 0x6a40, 0x6b40, 0x6c40, 0x6d40, 0x6e40, 0x6f40, 
    0x7040, 0x7140, 0x7240, 0x7340, 0x7440, 0x7540, 0x7640, 0x7740, 
    0x7840, 0x7940, 0x7a40, 0x7b40, 0x7c40, 0x7d40, 0x7e40, 0x7f40, 
    0x8040, 0x8140, 0x8240, 0x8340, 0x8440, 0x8540, 0x8640, 0x8740, 
    0x8840, 0x8940, 0x8a40, 0x8b40, 0x8c40, 0x8d40, 0x8e40, 0x8f40, 
    0x9040, 0x9140, 0x9240, 0x9340, 0x9440, 0x9540, 0x9640, 0x9740, 
    0x9840, 0x9940, 0x9a50, 0x9b50, 0x9c50, 0x9d50, 0x9e50, 0x9f50, 
    0xa050, 0xa150, 0xa250, 0xa350, 0xa450, 0xa550, 0xa650, 0xa750, 
    0xa850, 0xa950, 0xaa50, 0xab50, 0xac50, 0xad50, 0xae50, 0xaf50, 
    0xb050, 0xb150, 0xb250, 0xb350, 0xb450, 0xb550, 0xb650, 0xb750, 
    0xb850, 0xb950, 0xba50, 0xbb50, 0xbc50, 0xbd50, 0xbe50, 0xbf50, 
    0xc050, 0xc150, 0xc250, 0xc350, 0xc450, 0xc550, 0xc650, 0xc750, 
    0xc850, 0xc950, 0xca50, 0xcb50, 0xcc50, 0xcd50, 0xce50, 0xcf50, 
    0xd050, 0xd150, 0xd250, 0xd350, 0xd450, 0xd550, 0xd650, 0xd750, 
    0xd850, 0xd950, 0xda50, 0xdb50, 0xdc50, 0xdd50, 0xde50, 0xdf50, 
    0xe050, 0xe150, 0xe250, 0xe350, 0xe450, 0xe550, 0xe650, 0xe750, 
    0xe850, 0xe950, 0xea50, 0xeb50, 0xec50, 0xed50, 0xee50, 0xef50, 
    0xf050, 0xf150, 0xf250, 0xf350, 0xf450, 0xf550, 0xf650, 0xf750, 
    0xf850, 0xf950, 0xfa50, 0xfb50, 0xfc50, 0xfd50, 0xfe50, 0xff50, 
    
    0xa050, 0xa150, 0xa250, 0xa350, 0xa450, 0xa550, 0xa650, 0xa750, 
    0xa850, 0xa950, 0xaa50, 0xab50, 0xac50, 0xad50, 0xae50, 0xaf50, 
    0xb050, 0xb150, 0xb250, 0xb350, 0xb450, 0xb550, 0xb650, 0xb750, 
    0xb850, 0xb950, 0xba50, 0xbb50, 0xbc50, 0xbd50, 0xbe50, 0xbf50, 
    0xc050, 0xc150, 0xc250, 0xc350, 0xc450, 0xc550, 0xc650, 0xc750, 
    0xc850, 0xc950, 0xca50, 0xcb50, 0xcc50, 0xcd50, 0xce50, 0xcf50, 
    0xd050, 0xd150, 0xd250, 0xd350, 0xd450, 0xd550, 0xd650, 0xd750, 
    0xd850, 0xd950, 0xda50, 0xdb50, 0xdc50, 0xdd50, 0xde50, 0xdf50, 
    0xe050, 0xe150, 0xe250, 0xe350, 0xe450, 0xe550, 0xe650, 0xe750, 
    0xe850, 0xe950, 0xea50, 0xeb50, 0xec50, 0xed50, 0xee50, 0xef50, 
    0xf050, 0xf150, 0xf250, 0xf350, 0xf450, 0xf550, 0xf650, 0xf750, 
    0xf850, 0xf950, 0xfa50, 0xfb50, 0xfc50, 0xfd50, 0xfe50, 0xff50, 
    0xd0, 0x150, 0x250, 0x350, 0x450, 0x550, 0x650, 0x750, 
    0x850, 0x950, 0xa50, 0xb50, 0xc50, 0xd50, 0xe50, 0xf50, 
    0x1050, 0x1150, 0x1250, 0x1350, 0x1450, 0x1550, 0x1650, 0x1750, 
    0x1850, 0x1950, 0x1a50, 0x1b50, 0x1c50, 0x1d50, 0x1e50, 0x1f50, 
    0x2050, 0x2150, 0x2250, 0x2350, 0x2450, 0x2550, 0x2650, 0x2750, 
    0x2850, 0x2950, 0x2a50, 0x2b50, 0x2c50, 0x2d50, 0x2e50, 0x2f50, 
    0x3050, 0x3150, 0x3250, 0x3350, 0x3450, 0x3550, 0x3650, 0x3750, 
    0x3850, 0x3950, 0x3a50, 0x3b50, 0x3c50, 0x3d50, 0x3e50, 0x3f50, 
    0x4050, 0x4150, 0x4250, 0x4350, 0x4450, 0x4550, 0x4650, 0x4750, 
    0x4850, 0x4950, 0x4a50, 0x4b50, 0x4c50, 0x4d50, 0x4e50, 0x4f50, 
    0x5050, 0x5150, 0x5250, 0x5350, 0x5450, 0x5550, 0x5650, 0x5750, 
    0x5850, 0x5950, 0x5a50, 0x5b50, 0x5c50, 0x5d50, 0x5e50, 0x5f50, 
    0x6050, 0x6150, 0x6250, 0x6350, 0x6450, 0x6550, 0x6650, 0x6750, 
    0x6850, 0x6950, 0x6a50, 0x6b50, 0x6c50, 0x6d50, 0x6e50, 0x6f50, 
    0x7050, 0x7150, 0x7250, 0x7350, 0x7450, 0x7550, 0x7650, 0x7750, 
    0x7850, 0x7950, 0x7a50, 0x7b50, 0x7c50, 0x7d50, 0x7e50, 0x7f50, 
    0x8050, 0x8150, 0x8250, 0x8350, 0x8450, 0x8550, 0x8650, 0x8750, 
    0x8850, 0x8950, 0x8a50, 0x8b50, 0x8c50, 0x8d50, 0x8e50, 0x8f50, 
    0x9050, 0x9150, 0x9250, 0x9350, 0x9450, 0x9550, 0x9650, 0x9750, 
    0x9850, 0x9950, 0x9a50, 0x9b50, 0x9c50, 0x9d50, 0x9e50, 0x9f50, 
    
    0xfa60, 0xfb60, 0xfc60, 0xfd60, 0xfe60, 0xff60, 0xc0, 0x140, 
    0x240, 0x340, 0x440, 0x540, 0x640, 0x740, 0x840, 0x940, 
    0xa60, 0xb60, 0xc60, 0xd60, 0xe60, 0xf60, 0x1040, 0x1140, 
    0x1240, 0x1340, 0x1440, 0x1540, 0x1640, 0x1740, 0x1840, 0x1940, 
    0x1a60, 0x1b60, 0x1c60, 0x1d60, 0x1e60, 0x1f60, 0x2040, 0x2140, 
    0x2240, 0x2340, 0x2440, 0x2540, 0x2640, 0x2740, 0x2840, 0x2940, 
    0x2a60, 0x2b60, 0x2c60, 0x2d60, 0x2e60, 0x2f60, 0x3040, 0x3140, 
    0x3240, 0x3340, 0x3440, 0x3540, 0x3640, 0x3740, 0x3840, 0x3940, 
    0x3a60, 0x3b60, 0x3c60, 0x3d60, 0x3e60, 0x3f60, 0x4040, 0x4140, 
    0x4240, 0x4340, 0x4440, 0x4540, 0x4640, 0x4740, 0x4840, 0x4940, 
    0x4a60, 0x4b60, 0x4c60, 0x4d60, 0x4e60, 0x4f60, 0x5040, 0x5140, 
    0x5240, 0x5340, 0x5440, 0x5540, 0x5640, 0x5740, 0x5840, 0x5940, 
    0x5a60, 0x5b60, 0x5c60, 0x5d60, 0x5e60, 0x5f60, 0x6040, 0x6140, 
    0x6240, 0x6340, 0x6440, 0x6540, 0x6640, 0x6740, 0x6840, 0x6940, 
    0x6a60, 0x6b60, 0x6c60, 0x6d60, 0x6e60, 0x6f60, 0x7040, 0x7140, 
    0x7240, 0x7340, 0x7440, 0x7540, 0x7640, 0x7740, 0x7840, 0x7940, 
    0x7a60, 0x7b60, 0x7c60, 0x7d60, 0x7e60, 0x7f60, 0x8040, 0x8140, 
    0x8240, 0x8340, 0x8440, 0x8540, 0x8640, 0x8740, 0x8840, 0x8940, 
    0x8a60, 0x8b60, 0x8c60, 0x8d60, 0x8e60, 0x8f60, 0x9040, 0x9140, 
    0x9240, 0x9340, 0x9450, 0x9550, 0x9650, 0x9750, 0x9850, 0x9950, 
    0x9a70, 0x9b70, 0x9c70, 0x9d70, 0x9e70, 0x9f70, 0xa050, 0xa150, 
    0xa250, 0xa350, 0xa450, 0xa550, 0xa650, 0xa750, 0xa850, 0xa950, 
    0xaa70, 0xab70, 0xac70, 0xad70, 0xae70, 0xaf70, 0xb050, 0xb150, 
    0xb250, 0xb350, 0xb450, 0xb550, 0xb650, 0xb750, 0xb850, 0xb950, 
    0xba70, 0xbb70, 0xbc70, 0xbd70, 0xbe70, 0xbf70, 0xc050, 0xc150, 
    0xc250, 0xc350, 0xc450, 0xc550, 0xc650, 0xc750, 0xc850, 0xc950, 
    0xca70, 0xcb70, 0xcc70, 0xcd70, 0xce70, 0xcf70, 0xd050, 0xd150, 
    0xd250, 0xd350, 0xd450, 0xd550, 0xd650, 0xd750, 0xd850, 0xd950, 
    0xda70, 0xdb70, 0xdc70, 0xdd70, 0xde70, 0xdf70, 0xe050, 0xe150, 
    0xe250, 0xe350, 0xe450, 0xe550, 0xe650, 0xe750, 0xe850, 0xe950, 
    0xea70, 0xeb70, 0xec70, 0xed70, 0xee70, 0xef70, 0xf050, 0xf150, 
    0xf250, 0xf350, 0xf450, 0xf550, 0xf650, 0xf750, 0xf850, 0xf950, 
    
    0x9a70, 0x9b70, 0x9c70, 0x9d70, 0x9e70, 0x9f70, 0xa050, 0xa150, 
    0xa250, 0xa350, 0xa450, 0xa550, 0xa650, 0xa750, 0xa850, 0xa950, 
    0xaa70, 0xab70, 0xac70, 0xad70, 0xae70, 0xaf70, 0xb050, 0xb150, 
    0xb250, 0xb350, 0xb450, 0xb550, 0xb650, 0xb750, 0xb850, 0xb950, 
    0xba70, 0xbb70, 0xbc70, 0xbd70, 0xbe70, 0xbf70, 0xc050, 0xc150, 
    0xc250, 0xc350, 0xc450, 0xc550, 0xc650, 0xc750, 0xc850, 0xc950, 
    0xca70, 0xcb70, 0xcc70, 0xcd70, 0xce70, 0xcf70, 0xd050, 0xd150, 
    0xd250, 0xd350, 0xd450, 0xd550, 0xd650, 0xd750, 0xd850, 0xd950, 
    0xda70, 0xdb70, 0xdc70, 0xdd70, 0xde70, 0xdf70, 0xe050, 0xe150, 
    0xe250, 0xe350, 0xe450, 0xe550, 0xe650, 0xe750, 0xe850, 0xe950, 
    0xea70, 0xeb70, 0xec70, 0xed70, 0xee70, 0xef70, 0xf050, 0xf150, 
    0xf250, 0xf350, 0xf450, 0xf550, 0xf650, 0xf750, 0xf850, 0xf950, 
    0xfa70, 0xfb70, 0xfc70, 0xfd70, 0xfe70, 0xff70, 0xd0, 0x150, 
    0x250, 0x350, 0x450, 0x550, 0x650, 0x750, 0x850, 0x950, 
    0xa70, 0xb70, 0xc70, 0xd70, 0xe70, 0xf70, 0x1050, 0x1150, 
    0x1250, 0x1350, 0x1450, 0x1550, 0x1650, 0x1750, 0x1850, 0x1950, 
    0x1a70, 0x1b70, 0x1c70, 0x1d70, 0x1e70, 0x1f70, 0x2050, 0x2150, 
    0x2250, 0x2350, 0x2450, 0x2550, 0x2650, 0x2750, 0x2850, 0x2950, 
    0x2a70, 0x2b70, 0x2c70, 0x2d70, 0x2e70, 0x2f70, 0x3050, 0x3150, 
    0x3250, 0x3350, 0x3450, 0x3550, 0x3650, 0x3750, 0x3850, 0x3950, 
    0x3a70, 0x3b70, 0x3c70, 0x3d70, 0x3e70, 0x3f70, 0x4050, 0x4150, 
    0x4250, 0x4350, 0x4450, 0x4550, 0x4650, 0x4750, 0x4850, 0x4950, 
    0x4a70, 0x4b70, 0x4c70, 0x4d70, 0x4e70, 0x4f70, 0x5050, 0x5150, 
    0x5250, 0x5350, 0x5450, 0x5550, 0x5650, 0x5750, 0x5850, 0x5950, 
    0x5a70, 0x5b70, 0x5c70, 0x5d70, 0x5e70, 0x5f70, 0x6050, 0x6150, 
    0x6250, 0x6350, 0x6450, 0x6550, 0x6650, 0x6750, 0x6850, 0x6950, 
    0x6a70, 0x6b70, 0x6c70, 0x6d70, 0x6e70, 0x6f70, 0x7050, 0x7150, 
    0x7250, 0x7350, 0x7450, 0x7550, 0x7650, 0x7750, 0x7850, 0x7950, 
    0x7a70, 0x7b70, 0x7c70, 0x7d70, 0x7e70, 0x7f70, 0x8050, 0x8150, 
    0x8250, 0x8350, 0x8450, 0x8550, 0x8650, 0x8750, 0x8850, 0x8950, 
    0x8a70, 0x8b70, 0x8c70, 0x8d70, 0x8e70, 0x8f70, 0x9050, 0x9150, 
    0x9250, 0x9350, 0x9450, 0x9550, 0x9650, 0x9750, 0x9850, 0x9950]
 
 print len(gbDAATable)
 print len(meu)
 print gbDAATable == meu
 for i in range (len(meu)):
     if gbDAATable[i] != meu[i]:
         print " %d meu : %x gba: %x"% (i,meu [i],gbDAATable[i]) 
        
 
