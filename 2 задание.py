from math import comb

print((comb(10,6)*comb(15,4) + comb(10,7)*comb(15,3) + comb(10,8) * comb(15,2) + comb(10,9)*comb(15,1)+comb(10,10)*comb(15,0))/ comb(25,10) * 100)