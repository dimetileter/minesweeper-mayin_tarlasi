# Gizli alanı oluştur
game_mod = '1'
size = 14

# Gizli alanı oluştur
if game_mod == '1':
    hidden_area = [['?' for _ in range(size)] for _ in range(size)]

    # Üst başlık (Sütun numaraları 1'den başlayacak)
    print("    ", end="")  # Boşluk bırak
    for col in range(1, size + 1):
        print(f"[{col}]", end=" ")
    print()  # Üst satır tamamlandı

    # Matrisin içeriğini satır numaralarıyla birlikte yazdır
    for i in range(size):
        print(f"[{i+1}]", end=" ")  # Satır numarasını yazdır
        for j in range(size):
            print(f"[{hidden_area[i][j]}]", end=" ")
        print()  # Satır sonu
