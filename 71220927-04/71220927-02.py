def selisih_hari(tgl1, bln1, tgl2, bln2):
    #proses and output
    hari=[31,28,31,30,31,30,31,31,30,31,30,31]
    jmlhri=sum(hari)
    awal=sum(hari[bln1:])-tgl1
    akhr=sum(hari[:bln2])+tgl2
    hsl=jmlhri-akhr-awal
    print(abs(hsl))


#input
tgl1=int(input('Tanggal 1 : '))
bln1=int(input('Bulan 1 : '))
tgl2=int(input('Tanggal 2 : '))
bln2=int(input('Bulan 2 : '))

selisih_hari(tgl1, bln1, tgl2, bln2)




