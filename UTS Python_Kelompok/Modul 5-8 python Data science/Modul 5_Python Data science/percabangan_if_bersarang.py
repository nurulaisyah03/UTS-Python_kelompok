gaji=10000000
berkeluarga=True
punyarumah=True
if gaji>3000000:
    print("gaji sudah diatas umr")
    if berkeluarga:
        print("wajib ikut asuransi dan menabung untuk pensiun")
    else:
        print("tidak perlu ikut asuransi")
    if punyarumah:
        print("wajib bayar pajak rumah")
    else:
        print("tidak wajib bayar pajak rumah")
else:
    print("gaji belum umr")