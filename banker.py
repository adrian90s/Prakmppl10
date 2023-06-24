from typing import List

def banker(n: int, m: int, available: List[int], max_req: List[List[int]], allocated: List[List[int]]) -> bool:
    # inisialisasi variabel
    need = [[max_req[i][j] - allocated[i][j] for j in range(m)] for i in range(n)]
    work = available[:]
    finish = [False] * n
    safe_sequence = []
    
    # cek apakah permintaan kurang dari atau sama dengan sumber daya yang tersedia
    def check(request: List[int], i: int) -> bool:
        for j in range(m):
            if request[j] > need[i][j] or request[j] > work[j]:
                return False
        return True
    
    # tambahkan sumber daya yang dialokasikan
    def allocate(i: int):
        for j in range(m):
            work[j] += allocated[i][j]
    
    # lakukan simulasi banker
    while not all(finish):
        found = False
        for i in range(n):
            if not finish[i] and check(need[i], i):
                allocate(i)
                finish[i] = True
                safe_sequence.append(i)
                found = True
        if not found:
            return False
    
    # cetak urutan aman dan kembalikan True jika simulasi berhasil
    print("Safe sequence:", safe_sequence)
    return True

n = 5
m = 3
available = [3, 3, 2]
max_req = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
allocated = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

if banker(n, m, available, max_req, allocated):
    print("Simulasi berhasil")
else:
    print("Simulasi gagal")
