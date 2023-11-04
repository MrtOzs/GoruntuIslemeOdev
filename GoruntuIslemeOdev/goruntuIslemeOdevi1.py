
import cv2
#Görüntünün geri seviyede siyah beyaz okunmasını sağlar
resim = cv2.imread('resim.png', cv2.IMREAD_GRAYSCALE)
#Histogram ı tutmak için dizi oluşturduk
histogram_tutucu = [0] * 256
#Histogramı döner her döndüğünde bir arttırma yaparız
for satir in resim:
    for pixelDegeri in satir:
     histogram_tutucu[pixelDegeri] += 1
#Histogram piksel değerini döner ve sayısını buluruz
for i in range(len(histogram_tutucu)):
      sayi =  histogram_tutucu [i]
    print(f'Piksel değeri {i}: {sayi} piksel')