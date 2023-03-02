def ratarata(n1,n2,n3,n4,n5,n6,n7,n8):
    #proses and output
    l_nilai=[n1,n2,n3,n4,n5,n6,n7,n8]
    l_nilai.sort()
    x_nilai=min(l_nilai)
    l_nilai.remove(x_nilai)
    y_nilai=min(l_nilai)
    l_nilai.remove(y_nilai)
    totalnilai=sum(l_nilai)
    rtrt=totalnilai/6
    print('Rata-rata : ',+(round(rtrt)))

#input
n1=int(input('n1 = '))
n2=int(input('n2 = '))
n3=int(input('n3 = '))
n4=int(input('n4 = '))
n5=int(input('n5 = '))
n6=int(input('n6 = '))
n7=int(input('n7 = '))
n8=int(input('n8 = '))

ratarata(n1,n2,n3,n4,n5,n6,n7,n8)


