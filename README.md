## Author
- 13519084 - Rhapsodya Piedro Asmorobangun
- 13519176 - Made Kharisma Jagaddhita

## Algoritma A*
Algoritma A* juga merupakan algoritma traversal graf terinformasi sehingga algoritma ini memakai graf dengan bobot (weighted graph). Pencarian dimulai dari node awal tertentu dari grafik. Tujuan pencarian adalah untuk menemukan jalur ke node tujuan tertentu yang memiliki cost terkecil (jarak tempuh terkecil, waktu terpendek, dll.). Berikut merupakan langkah-langkah dari algoritma A*:
1. Inisialisasi open list dan closed list. Open list nantinya akan berisi simpul-simpul yang masih hidup. Closed list akan berisi simpul-simpul yang telah dikunjungi.
2. Masukkan simpul awal ke dalam open list.
3. Iterasi semua simpul pada open list dan pilih simpul yang memiliki estimasi cost paling kecil. Perhitungan simpul yang ingin diekspansi menggunakan rumus f(n) = g(n) + h(n) dimana f(n) adalah estimasi cost dengan melalui jalur n ke tujuan, g(n) adalah cost sejauh ini untuk mencapai n, dan h(n) adalah perkiraan biaya n ke tujuan. Perhitungan h(n) dapat dilakukan secara heuristik. Dalam tugas ini akan menggunakan jarak euclidean. 
4. Masukkan simpul yang dipilih tadi ke dalam closed list.
5. Ekspansi simpul yang dipilih. jika hasil ekspansi dari simpul tidak berada di closed list, maka masukkan simpul tersebut ke open list.
6. Ulangi langkah 3 sampai 5. Jika simpul yang diekspansi ternyata merupakan simpul tujuan, maka path telah ditemukan. Jika tidak ada lagi simpul di open list dan path belum ditemukan, maka simpul tujuan tidak dapat tercapai dari simpul awal.

## Setup
Program dapat dijalankan pada sistem operasi Windows. Pastikan sudah menginstall python dan pip

## Cara Menjalankan
- Install jupyter notebook versi terbaru dengan menjalankan command `pip install jupyter notebook` pada cmd
- Install ipyleaflet dengan menjalankan command `pip install ipyleaflet` pada cmd
- Install ipywidgets dengan menjalankan command `pip install ipywidgets` pada cmd
- Buka cmd di folder src
- Jalankan command `jupyter notebook` pada cmd
- Buka URL yang muncul pada cmd
- Pada jupyter notebook, buka Tucil.ipynb
- Klik 'Cell' dan pilih 'Run All'
- Ketik nama file yang ada pada folder test
- Ketik nomor simpul asal dan tujuan
