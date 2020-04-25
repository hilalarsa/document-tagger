import difflib
from difflib import SequenceMatcher

fullWords = ['kementerian', 'riset,', 'teknologi', 'dan', 'pendidikan', 'tinggi', 'politeknik', 'negeri', 'malang', 'jalan', 'soekarno', 'hatta', 'no.9', 'malang', '65141', 'telepon', '(0341)', '404424', '-', '404425.', 'fax', '(oja1)', '404420', 'sid', 'ti', 'surat', 'tugas', 'nomor:', '10116/pl2/kp/2019', 'direktur', 'politeknik', 'negeri', 'malang', 'memberi', 'tugas', 'kepada:', 'nama', 'peneliti', 'nidn', 'jabatan', 'putra', 'prima', 'arhandi,', 's.t.,', 'mkom', '0003118602', '\xe2\x80\x94', '|', 'ketua', 'luoman', 'affandi,', 's.kom.,', 'm.msi', '0730118201', 'anggota', 'dimas', 'wahyu', 'wibowo,', 's.t,', 'm.t', '0009108402', 'anggota', 'untuk', 'melaksanakan', 'kegiatan', 'penelitian', 'reguler', 'kompetisi', 'yang', 'dibiayai', 'dengan', 'dana', 'dipa', 'nomor:', 'sp', 'dipa-042.01-2401004/2019', 'dengan', 'surat', 'perjanjian', 'no:', '9675/pl2.1/hk/2019.', 'dengan', 'judul', ':', 'aplikasi', 'whatsapp', 'gateway', 'dengan', 'nomor', 'kontak', 'otomatis', 'untuk', 'notifikasi', 'surat', 'peringatan', 'mahasiswa', 'menggunakan', 'metode', 'mesin', 'turing', 'dan', 'rest', 'politeknik', 'negeri', 'malang', '1', 'april', 's/d', '31', 'oktober', '2019', 'tempat', 'pelaksanaan', 'waktu', 'pelaksanaan', 'demikian', 'surat', 'tugas', 'ini', 'dibuat', 'untuk', 'dilaksanakan', 'dengan', 'sebaik-baiknya.', 'setiawan,', 'mmt.,', 'mm', 'nip.1195909101986031002', 'tembusan:', '1.', 'pembantu', 'direktur', 'i:', '2.', 'pembantu', 'direktur', 'il:', '3.', 'ketua', 'jurusar/', 'program', 'studi', 'teknologi', 'informasi']
dictFromApi = ['putra prima arhandi', 'luqman affandi', 'dimas wahyu wibowo']

# for item in dictFromApi:
    # print(item.split())

for word in fullWords:
    #get each word from datastring
    for individualName in dictFromApi:
        #get per name/rows from api
        partName = individualName.split()
        for part in partName:
            #get per name word from splitted name/row from api
            seq = SequenceMatcher(a=word,b=part)
            if(seq.ratio() > 0.8):
                print(part + " " + word)
                print(seq.ratio())
            # print(seq.real_quick_ratio())
            # print(seq.quick_ratio())


# str1 = 'abcd'
# str2 = 'abcde'
# seq = SequenceMatcher(a=str1, b=str2)
# print(seq.ratio())