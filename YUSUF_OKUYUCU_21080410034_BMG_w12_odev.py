
# Lessons exams result dictionary
exam_sonuclar = {'isimler': ['Ayşe K.', 'Ahmet M.', 'Nuri C.', 'Nawar T.', 'Suzan T.', 'Ala B.'],
                'cinsiyet': ['K', 'E', 'E', 'E', 'K', 'K'],
                'matematik': [60, 40, 97, 45, 56, 95],
                'turkce': [70, 30, 23, 80, 78, 46]}
count_erkek = 0
count_kadın = 0
sum_math_sonuc_erkek = 0
sum_math_sonuc_kadın = 0
sum_turkish_sonuc = 0
max_turkish_sonuc_erkek = 0
max_turkish_sonuc_kadın = 0
for i in range(len(exam_sonuclar["matematik"])):
    if exam_sonuclar["cinsiyet"][i] == "E":
        count_erkek += 1
        sum_math_sonuc_erkek += exam_sonuclar["matematik"][i]
        sum_turkish_sonuc += exam_sonuclar["turkce"][i]
        if max_turkish_sonuc_erkek < exam_sonuclar["turkce"][i]:
            max_turkish_sonuc_erkek = exam_sonuclar["turkce"][i]
    else:
        count_kadın += 1
        sum_math_sonuc_kadın += exam_sonuclar["matematik"][i]
        sum_turkish_sonuc += exam_sonuclar["turkce"][i]
        if max_turkish_sonuc_kadın < exam_sonuclar["turkce"][i]:
            max_turkish_sonuc_kadın = exam_sonuclar["turkce"][i]
print("Kadınların matematik not ortalamaları : {:.2f}".format(sum_math_sonuc_kadın / count_kadın))
print("Erkeklerin matematik not ortalamaları : {:.2f}".format(sum_math_sonuc_erkek / count_erkek))
print("Sınıfın türkçe not ortalaması : {:.2f}".format(sum_turkish_sonuc / (count_erkek + count_kadın)))
print("Kadınların en yüksek Türkçe not : {}".format(max_turkish_sonuc_kadın))
print("Erkeklerin en yüksek Türkçe not : {}".format(max_turkish_sonuc_erkek))
