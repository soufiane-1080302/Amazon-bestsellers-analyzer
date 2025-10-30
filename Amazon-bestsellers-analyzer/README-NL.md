# Amazon Bestsellers Data-analyse met Pandas

Een uitgebreid data-analyseproject dat de bestsellers van Amazon uit 2009-2019 onderzoekt met behulp van Python en Pandas.

## Projectoverzicht

Dit project analyseert een dataset van Amazon-bestsellers over een periode van 11 jaar (2009-2019). De analyse onderzoekt verschillende aspecten, waaronder:

- **Genreverdeling**: Trends in fictie versus non-fictie
- **Prijsanalyse**: Prijspatronen en trends in de loop der tijd
- **Beoordelingsanalyse**: Verdelingen en correlaties van gebruikersbeoordelingen
- **Inzichten van auteurs**: Meest productieve en populaire auteurs
- **Tijdelijke trends**: Veranderingen van jaar tot jaar in de boekenmarkt

## Dataset

**Bestand**: `bestsellers.csv`

**Structuur**:
- **Naam**: Boektitel
- **Auteur**: Auteur
- **Gebruikersbeoordeling**: Gemiddelde beoordeling (schaal van 0 tot 5)
- **Recensies**: Aantal gebruikersrecensies
- **Prijs**: Boekprijs in USD
- **Jaar**: Jaar van bestsellervermelding (2009-2019)
- **Genre**: Fictie of non-fictie

**Omvang**: 550 items (boeken)


### Vereisten

- Python 3.7 of hoger
- pip pakketbeheerder

### Installatie

1. **Kloon de repository**:
```bash
git clone https://github.com/uwgebruikersnaam/amazon-bestsellers-analysis.git
cd amazon-bestsellers-analysis
```

2. **Installeer afhankelijkheden**:
```bash
pip install -r requirements.txt
```


### Uitvoeren van de Analyse

Voer het hoofdscript uit:

```bash
python analyze_bestsellers.py
```

Het script zal:
1. De gegevens laden
2. Een uitgebreide analyse uitvoeren
3. De resultaten weergeven in de terminal
4. Een samenvattingsbestand genereren (`analysis_summary.txt`)

## Analysefuncties

### 1. Gegevensverkenning
- Datasetdimensies en -structuur
- Gegevenstypen en ontbrekende waarden
- Duplicaatdetectie

### 2. Statistische samenvatting
- Beschrijvende statistieken voor alle numerieke kolommen
- Gemiddelde, mediaan, minimum, maximum en standaarddeviatie
- Prijs-, beoordelings- en recensiestatistieken

### 3. Genreanalyse
- Verdeling fictie versus non-fictie
- Gemiddelde prijzen per genre
- Gemiddelde beoordelingen per genre
- Aantal recensies per genre

### 4. Topboeken en auteurs
- Meest gerecenseerde boeken
- Hoogst gewaardeerde boeken
- Meest productieve auteurs
- Duurste boeken

### 5. Jaar-op-jaar analyse
- Boeken gepubliceerd per jaar
- Prijsontwikkelingen in de loop der tijd
- Beoordelingstrends in de loop der tijd
- Veranderingen in genreverdeling

### 6. Prijsanalyse
- Prijsklasseverdelingen
- Veelvoorkomende prijspunten
- Prijs per genre en jaar

### 7. Beoordelingsanalyse
- Beoordelingsverdeling met visuele balken
- Boeken met een perfecte beoordeling van 4,9
- Boeken met de laagste beoordeling

### 8. Correlatieanalyse
- Relaties tussen variabelen
- Prijs versus beoordelingen
- Recensies versus beoordelingen
- Tijdelijke correlaties

### 9. Belangrijkste inzichten
- Geautomatiseerde generatie van inzichten
- Identificatie van markttrends
- Samenvattende statistieken

## Voorbeelduitvoer

```
DATA-ANALYSE VAN AMAZON BESTSELLERS (2009-2019)
========================================================================

Gegevens van Amazon Bestsellers laden...
Succesvol geladen 550 records

=======================================================================
GEGEVENSVERKENNING
=========================================================================

1️ Datasetvorm:
Rijen: 550
Kolommen: 7

2️ Kolomnamen en -typen:
Naam object
Auteur object
Gebruikersbeoordeling float64
Reviews int64
Prijs int64
Jaar int64
Genre object

...
```

## Gebruikte technologieën

- **Python 3.x**: Kernprogrammeertaal
- **Pandas**: Datamanipulatie en -analyse
- **NumPy**: Numerieke berekeningen
- **Ingebouwde bibliotheken**: datum/tijd, waarschuwingen

## Belangrijkste bevindingen

Na het uitvoeren van de analyse ontdekt u inzichten zoals:

- De populairste genres van de afgelopen tien jaar
- Prijstrends op de boekenmarkt
- Correlatie tussen recensies en beoordelingen
- Meest succesvolle auteurs en titels
- Veranderingen in consumentenvoorkeuren in de loop der tijd

## Code Walkthrough

### Belangrijkste functies

1. **`load_data(bestandspad)`**: Laadt CSV-gegevens in een Pandas DataFrame
2. **`explore_data(df)`**: Initiële dataverkenning en -validatie
3. **`statistical_summary(df)`**: Genereert uitgebreide statistieken
4. **`genre_analysis(df)`**: Analyseert boeken op genre
5. **`top_books_and_authors(df)`**: Identificeert toppresteerders
6. **`year_analysis(df)`**: Onderzoekt tijdstrends
7. **`price_analysis(df)`**: Gedetailleerde prijsspecificatie
8. **`rating_analysis(df)`**: Analyse van beoordelingsverdeling
9. **`correlation_analysis(df)`**: Variabele correlaties
10. **`generate_insights(df)`**: Geautomatiseerde generatie van inzichten
11. **`export_summary(df)`**: Exporteert bevindingen naar een tekstbestand

### Analysestroom

```python
df = load_data('bestsellers.csv')
↓
explore_data(df)
↓
statistical_summary(df)
↓
[Meerdere analysefuncties]
↓
export_summary(df)
```

## Uitvoerbestanden

- **`analysis_summary.txt`**: Tekstbestand met de belangrijkste bevindingen en statistieken

## Bijdragen

Bijdragen zijn welkom! Bijdragen:

1. Fork de repository
2. Maak een feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit je wijzigingen (`git commit -m 'Add some AmazingFeature'`)
4. Push naar de branch (`git push origin feature/AmazingFeature`)
5. Open een Pull Request

## 📧 Contact

Soufiane Tarifit ~ Soufiane.tarifit@gmail.com

Projectlink: [https://github.com/soufiane-1080302/amazon-bestsellers-analyzer](https://github.com/soufiane-1080302/amazon-bestsellers-analyzer)

## Dankbetuiging

- Dataset afkomstig uit Kaggle's Amazon Bestsellers-dataset
- Geïnspireerd door tutorials over data-analyse van Codedex.io
- Gebouwd als onderdeel van een portfolioproject voor het demonstreren van data-analysevaardigheden

## Bronvermelding

- [Panda's Documentatie](https://pandas.pydata.org/docs/)
- [Python-gegevensanalyse](https://www.python.org/)
- [Best practices voor datavisualisatie](https://www.tableau.com/learn/articles/data-visualization)
- [Github Amazon Bestsellers-dataset source](https://github.com/codedex-io/projects/blob/main/projects/analyze-spreadsheet-data-with-pandas-chatgpt/amazon-best-sellers-analysis/bestsellers.csv)
- [License-project](https://choosealicense.com/)