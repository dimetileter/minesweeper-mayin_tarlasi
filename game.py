import random

game_mod = '0'
bomb_lst = []
safe_area_lst = []
game_area = []
bomb_area = []
score = 0
used_crdnt_lst = []
win = True
k = 0.3 # Katsayı olsun, default olara orta zorlukta gelsin

# Oyun modu seçimi
while True :
    print()
    print("1-) ---Gizli Mod----")
    print("2-) ---Şeffaf Mod---")
    game_mod = input("Oyun modunuzu seçin: ")

    if game_mod == '1' :
        print("Gizli mod seçildi")
        break
    elif game_mod == '2' :
        print("Şeffaf mod seçildi")
        break

    print("Geçersiz seçim!")

while True :
    print()
    print("1-) ---Kolay Seviye---")
    print("2-) ---Orta Seviye----")
    print("3-) ---Zor Seviye-----")
    print("4-) ---Özel Mod-------")
    level = input("Seviyenizi seçin: ")

    if level == '1' :
        print("Kolay seviye seçildi")
        k = 0.20
        break
    elif level == '2' :
        print("Orta seviye seçildi")
        k = 0.30
        break
    elif level == '3' :
        print("Zor seviye seçildi")
        k = 0.40
        break
    elif level == '4' :
        print("Özel mod seçildi \n")
        print("(i): Mayın oranını 0.X cinsinden yazınız ve oran 1.0 dan büyük olamaz")

        while True :
            k = float(input("Lütfen mayın oranını belirleyinz (Oranı 0.X cinsinden yazın - 1.0 dan): "))
            if (k > 1.0) or (k < 0.0):
                print("Geçersiz giriş!")
            else:
                break
        break
    print("Geçersiz seçim!")

while True :
    print()
    size = int(input("Oyun alanı boyutunu girini -> "))
    if size < 10 :
        print("Oyun alanı en az 10 birim olabilir!")
        continue
    else :
        print("Oyun başlatılıyor...\n")
        break

# Bomba Alanını oluştur
bomb_area = [[' ' for _ in range(size)] for _ in range(size)]
bomb_size = int((size*size)*k)

# Bombaları oluştur
while len(bomb_lst) < bomb_size :
    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)

    # Bombaların aynı koordinatlara eklenmesini önle
    if (x,y) not in bomb_lst :
        bomb_lst.append((x, y))
        bomb_area[x][y] = 'X'

# Gizli alanı oluştur
game_area = [['?' for _ in range(size)] for _ in range(size)]

# Şeffaf mod seçildiyse alanı bitiştir
if game_mod == '2':
    game_area = [[bomb_area[i][j] for j in range(size)] for i in range(size)]

# Oyun alanını ekrana yazdır
for i in range(size):
    for j in range(size):
        print("[{}]".format(game_area[i][j]), end=" ")
    print()

# Oyunu başlat
while score < (size*size - bomb_size) :
    # Kooridnatları al ve doğruluğunu kontrol et
    while True :
        cell = input("Açmak istediğiniz alanın koordinatını giriniz: ").split(",")
        x = int(cell[0]) - 1
        y = int(cell[1]) - 1

        if (x,y) in used_crdnt_lst :
            print("Bu alan açıldı!")
            print()
            continue
        elif 0 <= x < size and 0 <= y < size :
            used_crdnt_lst.append((x,y))
            print()
            break
        else :
            print("Geçersiz koordinat girdisi!\n")
            continue

    # Koordinatı konrol et
    if bomb_area[x][y] == 'X' :
        print("GAME OVER *_*")
        win = False
        # Alanı yazdır
        for i in range(size):
            for j in range(size):
                cell = bomb_area[i][j]
                print("[{}]".format(cell), end=" ")
            print()
        print("Puanınız: {}".format(score))
        break
    elif bomb_area[x][y] == " " :
        game_area[x][y] = ' '

        # Çevre kolon ve sütunları tek tek kontrol et
        bomb_count = 0
        for i in [-1, 0, 1]:  # x için: -1 (üst), 0 (aynı sıra), 1 (alt)
            for j in [-1, 0, 1]:  # y için: -1 (sol), 0 (aynı sütun), 1 (sağ)
                x2 = x + i
                y2 = y + j  # Yeni koordinatlar
                if 0 <= x2 < size and 0 <= y2 < size and bomb_area[x2][y2] == 'X':  # Matris sınırlarını aşmıyorsa
                    bomb_count +=1

        # Bomba sayınsını kutuya ekle
        if bomb_count > 0 :
            game_area[x][y] = bomb_count
        else :
            game_area[x][y] = '0'

        score += 1
        # Yeni alanı yazdır
        for i in range(size):
            for j in range(size):
                cell = game_area[i][j]
                print("[{}]".format(cell), end=" ")
            print()

if win :
    print("Tebrikler hiçbir mayına yakalnmadınız. Skorunuz: {}".format(score))
    for i in range(size):
        for j in range(size):
            cell = bomb_area[i][j]
            print("[{}]".format(cell), end=" ")
        print()

"""
# Alanı yazdır
for i in range(size):
    for j in range(size):
        cell = hidden_area[i][j]
        print("[{}]".format(cell), end=" ")
    print()

print("\n")

# Alanı yazdır
for i in range(size):
    for j in range(size):
        cell = area[i][j]
        print("[{}]".format(cell), end=" ")
    print()
"""



