
def jumlah_hari(nama_bulan):
    #proses and output
    nm_bulan31=['januari','maret','mei','juli','agustus','oktober','desember']
    nm_bulan30=['april','juni','september','november']
    nm_bulan28=['februari']

    if nama_bulan in nm_bulan31:
        print('jumlah hari : 31 hari ')
    elif nama_bulan in nm_bulan30:
        print('jumlah hari : 30 hari ')
    elif nama_bulan in nm_bulan28:
        print('jumlah hari : 28 hari ')
    else :
        print('Tidak valid')

#input
nama_bulan=input('Masukan nama bulan : ')

jumlah_hari(nama_bulan)
    
