medida = float(input("uma distancai em metros: "))
cm = medida * 100
mm = medida * 1000
dm = medida / 10
dam = medida * 1000000
hm = medida / 100
km = medida * 0.001
ml = medida * 0.000621371
m = medida * 100000

print("A medida de {:.0f}m corresponde a {:.0f} mm \n{:.0f} cm \n{:.0f} dm \n{:.0f} dam \n{:.0f} hm \n{:.2f} km \n{:.2f} ml" .format (medida, cm, mm, dm, dam, hm, km, ml))

