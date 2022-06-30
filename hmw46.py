import re

# 1.Aşağıdakı listdə düzgün formada ad və soyad yazılmayan sözləri çıxarın:
# ad_soyad = ['Aygun Kazimova', 'fermer Həsən', 'Namiq Qaracuxurlu', 'Rehim Rehimli', 'roya Ayxan', 'Eynulla']
# 
# 
# for ad in ad_soyad:
#     correct = re.match('[A-Z].* [A-Z].*' , ad)
#     if correct:
#         print(ad)


# 3. Aşağdakı mətindəki bütün saytları list şəklində çıxarın.      
# sentence = """Dünyada bir çox saytlar mövcuddur. Bunların bir çoxu fərqli məqsədlərə xidmət edirlər. Müsal üçün http://www.google.com saytı axtarış üçün istifadə olunur. Digər yandan https://facebook.com və http://www.instagram.com saytları sosial şəbəkə kimi fəaliyyət göstərirlər"""
# 
# site = 'https?://(www.)?[a-z]+\.[a-z]+'
# sites = re.findall(pattern, data)