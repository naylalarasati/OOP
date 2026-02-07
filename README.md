Tugas Analisis 1: • Apa yang terjadi jika kamu mengubah hero1.hp menjadi 500 setelah baris hero1 = Hero...? Coba lakukan print(hero1.hp)

yang terjadi adalah hp nya berubah menjadi 500

Tugas Analisis 2: • Perhatikan parameter lawan pada method serang. Parameter tersebut menerima sebuah objek utuh, bukan hanya string nama. Mengapa ini penting?

karena untuk mendeklarasikan sebuah variabel yang ada dalam bentuk output print

Tugas Analisis 3: • Eksperimen Fungsi super(): Pada class Mage, coba hapus (atau jadikan komentar #) baris kode super().__init__(name, hp, attack_power). Kemudian jalankan programnya.

atribut menjadi error karena tidak bisa mendefinisikan objek mage serta nama

Pertanyaan: Error apa yang muncul saat kamu mencoba melihat info Eudora (eudora.info())? Mengapa error tersebut mengatakan Mage object has no attribute 'name', padahal kita sudah mengirim nama "Eudora" saat pembuatan objek?

karena parameter nama tidak bisa dipanggil, jadi saat di run python tidak bisa menemukan objek yang dimaksud

Jelaskan peran fungsi super() dalam menghubungkan data dari class Anak ke class Induk!

untuk menjembatani antara class induk dan class anak, dipakai untuk constructor dan method lain

Tugas Analisis 4: 
1. Percobaan Hacking: Coba tambahkan baris kode berikut di bagian paling bawah (luar class): print(f"Mencoba akses paksa: {hero1._Hero__hp}") Pertanyaan: Apakah nilai HP muncul atau Error? Jika muncul, diskusikan dengan temanmu mengapa Python masih mengizinkan akses ini (konsep Name Mangling) dan mengapa kita tetap tidak boleh melakukannya dalam standar pemrograman yang baik.

Tidak error, hp tetap muncul. Alasan mengapa tetap tidak boleh melakukannya karena Name Mangling bukan untuk keamanan mutlak, tapi untuk mencegah akses tidak sengaja dan menjaga desain class. Walaupun bisa diakses, hal tersebut melanggar prinsip enkapsulasi dan tidak dianjurkan

2. Uji Validasi: Hapus logika if dan elif di dalam method set_hp, sehingga isinya hanya self.__hp = nilai_baru. Pertanyaan: Kemudian lakukan hero1.set_hp(-100). Apa yang terjadi pada data HP Hero? Jelaskan mengapa keberadaan method Setter sangat penting untuk menjaga integritas data dalam game!

HP menjadi -100 karena setter tidak memiliki validasi sehingga nilai negatif langsung disimpan. Hal ini membuktikan bahwa setter penting untuk menjaga integritas data agar nilai HP tetap logis dalam sistem game.

Tugas Analisis 5: 
1. Melanggar Kontrak: Pada class Hero, hapus (atau jadikan komentar #) seluruh blok method def serang(self, target):. Jalankan programnya. Pertanyaan: Error apa yang muncul? Jelaskan dengan bahasamu sendiri, apa arti pesan error Can't instantiate abstract class Hero with abstract method...? Apa konsekuensinya jika kita lupa membuat method yang sudah dijanjikan di Interface? 

Error ini muncul karena hero  merupakan turunan dari GameUnit, sedangkan GameUnit adalah abstract class yang memiliki method abstract serang(). Method abstract bersifat wajib untuk diimplementasikan oleh semua class turunannya. Jika salah satu method tidak dibuat, maka class tersebut dianggap belum lengkap dan tidak boleh dibuat menjadi objek.
Hal ini menunjukkan bahwa abstract class atau interface berfungsi sebagai kontrak. Kontrak tersebut berisi janji bahwa setiap class turunan harus menyediakan method-method tertentu. Jika janji tersebut tidak dipenuhi, maka program akan dihentikan untuk mencegah kesalahan logika pada sistem.

2. Mencetak Cetakan: Coba aktifkan baris kode unit = GameUnit(). Pertanyaan: Mengapa class GameUnit dilarang untuk dibuat menjadi objek? Apa gunanya ada class GameUnit jika tidak bisa dibuat menjadi objek nyata?

Saat baris kode unit = GameUnit() diaktifkan, program akan menghasilkan error karena GameUnit adalah abstract class. Abstract class tidak boleh dibuat menjadi objek secara langsung karena class tersebut hanya berfungsi sebagai cetakan atau blueprint, bukan sebagai objek nyata yang digunakan di dalam program.

Tugas Analisis 6: 
1. Uji Skalabilitas (Kemudahan Menambah Fitur): Tanpa mengubah satu huruf pun pada kode Looping (for pahlawan in pasukan:), buatlah satu class baru bernama Healer(Hero). Isi method serang milik Healer dengan: print(f"{self.name} tidak menyerang, tapi menyembuhkan teman!"). Masukkan objek Healer ke dalam list pasukan. 
o Pertanyaan: Apakah program berjalan lancar? 
o Kesimpulannya, apa keuntungan Polimorfisme bagi seorang programmer ketika harus mengupdate game dengan karakter baru di masa depan? 

Setelah menambahkan class baru Healer yang mewarisi Hero dan memiliki method serang() sendiri, program tetap berjalan dengan lancar meskipun kode pada bagian looping tidak diubah sama sekali. Hal ini terjadi karena semua objek di dalam list pasukan memiliki method dengan nama yang sama, yaitu serang().
Hal ini menunjukkan bahwa konsep polymorphism memungkinkan satu perintah yang sama dijalankan pada berbagai objek dengan perilaku yang berbeda-beda. Setiap class memiliki cara menyerang atau bertindak sendiri, tetapi sistem tetap dapat memanggilnya secara seragam.
Kesimpulannya, keuntungan polymorphism bagi programmer adalah:
Mudah menambahkan karakter baru
Tidak perlu mengubah kode yang sudah ada
Program menjadi lebih fleksibel dan mudah dikembangkan di masa depan

2. Konsistensi Penamaan: Ubah nama method serang pada class Archer menjadi tembak_panah. Jalankan program. Pertanyaan: Apa yang terjadi? Mengapa dalam konsep Polimorfisme, nama method antara Parent Class dan berbagai Child Class harus persis sama?

Konsistensi Penamaan Method
Ketika nama method serang() pada class Archer diubah menjadi tembak_panah(), program mengalami error saat looping dijalankan. Hal ini terjadi karena loop tetap memanggil method serang(), sedangkan objek Archer tidak lagi memiliki method dengan nama tersebut.
Dalam konsep polymorphism, nama method antara parent class dan seluruh child class harus sama agar sistem dapat memperlakukan semua objek secara seragam. Jika nama method berbeda, maka polymorphism gagal dijalankan karena program tidak menemukan method yang sesuai.

