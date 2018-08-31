# CodeSH

[![N|Solid](https://emregeldegul.net/wp-content/uploads/2018/09/codeshUsage.png)]( https://emregeldegul.net/2018/09/codesh-v2-kod-paylasma-modulu)

CodeSH, kaynak kodları hızlı bir biçimde paste.ubuntu.com üzerinde paylaşmaya olanak sağlayan bir modül/programdır. Program olarak kullanılabildiği gibi bir python modülü olarakta kullanılabilir.

  - Paylaşılan kodların listesini json formatında saklar
  - Paylaşılan kodları copyboarda ekler
  - Kodların dilini otomatik olarak tespit eder
  - Python modülü olarak kullanılabilir

[![N|Solid](https://emregeldegul.net/wp-content/uploads/2018/09/codeshShare.png)]( https://emregeldegul.net/2018/09/codesh-v2-kod-paylasma-modulu)

# Program Kurulum
```sh
~$ git clone https://github.com/MuReCoder/codesh.git && cd codesh
~$ pip install -r requirements.txt
~$ sudo mv codesh.py /usr/bin/codesh
~$ sudo chmod +x /usr/bin/codesh
```

# Modül Kurulum
```sh
~$ pip install codesh
```

# Program Kullanım
Programın kullanımı için kurulumdan sonra komut satırında **codesh** komutunun verilmesi yeterlidir. Argüman olarak ise kaynak kodu paylaşılacak argümanlar girilir.

```sh
~$ codesh file1.txt file2.py file3.php ... .. .
```

Paylaşılan son kodların listesi için **--list** argümanının gönderilmesi yeterli.

```sh
~$ codesh --list
```

Bu komut paylaşılan programların sıralı tam listesini ayrıntıları ile verecektir.
# Modül Kullanımı
Modül olarak yüklendikten sonra **sh** sınıfı ile işlemler yapılabilir. Main fonksiyonuna dosya ismi gönderildiğinde paste.ubuncu.com üzerinde kaynak koda ait ID geri döner.

```py
from codesh import sh
app = sh(nickname='username')
app.main('filename')
```

Paylaşılan kodlara jData nesnesi üzerinden ulaşılabilir.

```py
from codesh import sh
app = sh(nickname='username')
app.main('filename')

print(app.jData)
```

# Ek Bilgiler
- Paylaşılan kodlara ait veriler (id, tarih, paylaşan) ev dizininde "codesh.json" formatında saklanır.
- Sadece linux ortamında test edilmiştir.


Programı yazarken çok kastığımın farkındayım, gerekli yerlerde pull req atarak destek verebilir, hatalarımı giderebilirsiniz. Yeni özellikler için issuse açabilirsiniz.