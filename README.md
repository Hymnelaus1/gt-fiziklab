# gt-fiziklab

**English summary:** A small Tkinter GUI tool for Gebze Technical University physics-lab reports. You enter a series of x/y data pairs and it computes Σx, Σy, Σx², Σ(x·y), and the least-squares linear regression slope `a` (via `a = (nΣxy − ΣxΣy) / (nΣx² − (Σx)²)`), which is the standard "seri hesabı" used to fit a line to lab measurements. Only needs Python's built-in `tkinter` — no extra pip packages. A pre-built Windows `.exe` is included for anyone who doesn't have Python set up.

## Ne işe yarar?

Gebze Teknik Üniversitesi fizik laboratuvarı deneylerinde sık kullanılan bir **doğrusal seri hesaplayıcı**dır. Kullanıcıdan bir x veri serisi ve bir y veri serisi alır, bu iki seri arasında en küçük kareler (least squares) yöntemiyle doğrusal ilişki (y ≈ a·x) kurar ve deney raporlarında sıkça istenen ara toplamları hesaplar:

- **Σx** — x değerlerinin toplamı
- **Σy** — y değerlerinin toplamı
- **Σx·y** — x ve y çarpımlarının toplamı
- **Σx²** — x değerlerinin karelerinin toplamı
- **Σx·y / Σx²** — basit oran
- **a (linear fitting formülü)** — en küçük kareler yöntemiyle bulunan doğru eğimi:

  ```
  a = (n·Σxy − Σx·Σy) / (n·Σx² − (Σx)²)
  ```

  burada `n`, serinin uzunluğudur.

Sonuçlar, hesapla butonuna basıldığında ayrı bir pencerede (messagebox) gösterilir.

## Nasıl çalıştırılır?

### Python ile

```bash
python gtufiziklab.py
```

Gereksinimler: sadece Python'un standart kütüphanesindeki `tkinter` modülü yeterlidir (çoğu Windows/Mac Python kurulumunda hazır gelir; bazı Linux dağıtımlarında `sudo apt install python3-tk` gerekebilir). Ekstra bir pip paketi gerekmez.

### Hazır .exe ile (Windows, Python kurmadan)

Python kurulu değilse veya programlamayla uğraşmak istemiyorsanız, depodaki **`gtufiziklab.exe`** dosyasını doğrudan çift tıklayarak çalıştırabilirsiniz.

## Kullanım

1. Programı açın.
2. "Serinin uzunluğunu girin" kutusuna kaç veri noktası gireceğinizi yazın (ör. `3`).
3. x değerlerini virgülle ayırarak girin, ör: `2.31, 45.1234, 35`
4. y değerlerini aynı şekilde girin.
5. "Hesapla" butonuna basın; sonuçlar açılan pencerede listelenir.

> Not: Ondalık ayırıcı olarak nokta (`.`) kullanılmalıdır, virgül değil. Aksi halde hesaplama penceresi açılmaz ve bir hata alırsınız.

Bir örnek çalıştırma görüntüsü için `image.png` dosyasına bakabilirsiniz.
