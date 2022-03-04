# Cirmos Titkosító
Egy egyszerű titkosító és dekódoló program Pythonban írva. 

A program képes szöveget titkosítani, majd azt visszafejteni. Minden egyes támogatott karakterhez tartozik egy 10 betűből és számból álló karaktersorozat. A program linuxos terminálban (Debian) való futtatásra lett tervezve. 

A futtatáshoz szükséges Python 3 (3.8.10-es verzió volt használva a fejlesztéshez), valamint  bizonyos Python könyvtárak (requirements.txt):
- termcolor
- pyperclip

A követelmények telepítéséhez:

```pip install -r requirements.txt```

A program elindításához nyissunk meg egy terminált a mappában, ahol van a programfájlunk, majd szimplán írjuk be:

```python3 titkosito.py```


A program elindulása után egy menü fogad minket:
- Titkosítás: az általunk beírt szöveget átalakítja titkosított szöveggé.
- Dekódolás: az általunk beírt titkosított szöveget átalakítja  szöveggé.
- Kilépés: kilép a programból.

Támogatott karakterek: 
0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[]^_`{|}~

A titkosítás és dekódolás végeredményéül kapott szöveg automatikusan kimásolódik a vágólapra. Ezt a funkciót a programkód 9. sorában lehet ki/bekapcsolni.
- ```masolasVagolapra = True```  Másolás vágólapra bekapcsolva (alapértelmezett).
- ```masolasVagolapra = False``` Másolás vágólapra kikapcsolva. 

</br>

A program egy kezdetleges stádiumban van, rengeteg helyen lehet még fejleszteni. Ilyen lehet például: 
- Kompatibilissá tevés más rendszerekkel. Megváltoztatni a felhasználóval való kommunikációnak a módját egy grafikus interfésszé. Ez javítana a felhasználói élményen, valamint egy cross-platform UI keretrendszer lehetővé tenné a más operációs rendszereken való futtatást.
- Javítani a titkosítási algoritmuson, hogy nehezebben visszafejthető karaktersorozatot generáljon, valamint a titkosított szöveg létrehozásához mindig más szöveg és számkombináció kerüljön felhasználásra. 
- Támogatott karakterek bővítése.


Szívesen fogadok bármilyen észrevételt, vagy építő jellegű kritikát. </br>
✉️ histvan.public@gmail.com
