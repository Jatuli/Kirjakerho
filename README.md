Kirjakerho

Luodaan sovellus kirjakerhon kotisivun ja tietokannan ylläpitoon

Tällä hetkellä on lisätty toiminnallisuudet:

* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään sovellukseen tietokohteita, tässä tapauksessa kirjoja. Lisäksi käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään kirjoja.
* Käyttäjä näkee sovellukseen lisätyt kirjat.
* Käyttäjä pystyy etsimään kirjoja hakusanalla. 
* Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä kirjoja.
* Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät kirjat.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät kirjat.
* Käyttäjä pystyy valitsemaan tietokohteelle yhden tai useamman luokittelun. (klassikko, moderni, uutuus, scifi, fantasia, tieto, taide yms. 


Jatkossa pyritään lisäämään vielä seuraavat toiminnallisuudet ja muutokset:
* Bugikorjauksia ja yleisen toiminnallisuuden parantamista
* Käyttäjä voi merkata järjestelmässä olevia kirjoja tilaan "haluan lukea" tai "luettu"
* Käyttäjä voi kohdistaa kirjoihin arvosteluja.
* Pyritään tekemään sivusto visuaalisesti miellyttävämmäksi. 
  
Ohjeet testaamiseen linux ympäristössä: 

- Avaa terminaali ja mene kansioon johon haluat ladata sovelluksen tai luo sellainen (esim. cd /polku ja mkdir testi ja cd /testi)

- Lataa sovellus GitHubista git clone komennolla : git clone https://github.com/Jatuli/Kirjakerho.git

- Siirry hakemistoon cd Kirjakerho

- Tämän jälkeen luodaan virtuaaliympäristö. Asenna työkalu (venv-moduuli). sudo apt install python3-venv . Virtuaaliympäristö luodaan käskyllä     python3 - m venv venv ja se aktivoidaan käskyllä source venv/bin/activate

- virtuaaliympäristössä asenna riippuvuudet käskyllä pip install -r requirements.txt

HUOM! softassa on bugi mikä ilmenee itselläni mutta ei toisella testialustalla mitä en onnistunut itseltäni vielä poistamaan. tietokannan luominen ei jostain syystä välttämättä onnistu automaattisesti, jos sinulla on ongelmia sen kanssa ja jotta kuitenkin pääsisit testaamaan ohjelmaa ,alusta tietokanta manuaalisesti käskyillä: 

sqlite3 database.db jonka jälkeen .read schema.sql alustuksen voi testata vielä .tables käskyllä.   Tämän jälkeen .exit ja käynnistä sovellus. 


- Käynnistä sovellus käskyllä python3 app.py

- selaimessa löytyy osoitteesta http://127.0.0.1:5000/

- Kun olet testannut voit sammuttaa virtuaaliympäristön käskyllä deactivate


