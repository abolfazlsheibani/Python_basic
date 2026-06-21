# برنامه‌ای بنویسید که از کاربر یک عدد بگیرد و با استفاده از حلقه for، مجموع اعداد از 1 تا آن عدد را محاسبه و چاپ کند.

vorodi = int(input("لطفا عدد مورد نظر خود را وارد کنید: "))
motaghayerjam_ke_bayad_biroon_bashe = 0
for i in range(1, vorodi + 1):
    motaghayerjam_ke_bayad_biroon_bashe += i
print(motaghayerjam_ke_bayad_biroon_bashe)
