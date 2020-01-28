# Google Play Store Analytics

## Introduction
The Play Store apps data has enormous potential to drive app-making businesses to success. Actionable insights can be drawn for developers to work on and capture the Android market. Using this dataset we are going to analysis as a developer, we should know the best constraints to focus on when launching our first app. And we definitely have no intention of getting lost in this vast ocean of versatile apps.

## Data Summary
The google play store data consists of the following variables:
- `App` : Application name                
- `Category` : Category the app belongs to
- `Rating` : Overall user rating of the app (as when scraped)
- `Reviews` : Number of user reviews for the app (as when scraped)         
- `Size` : Size of the app (as when scraped)           
- `Installs` : Number of user downloads/installs for the app (as when scraped)     
- `Type` : Paid or Free           
- `Price` : Price of the app (as when scraped)        
- `Content Rating` : Age group the app is targeted at - Children / Mature 21+ / Adult   
- `Genres` : An app can belong to multiple genres (apart from its main category). For eg, a musical family game will belong to Music, Game, Family genres.        
- `Last Updated` : Date when the app was last updated on Play Store (as when scraped) 
- `Current Ver` : Current version of the app available on Play Store (as when scraped)   
- `Android Ver` : Min required Android version (as when scraped)  

## Dependencies
- Flask
- Matplotlib
- Pandas
Semua modul tersebut dapat Anda install pada file `requirements.txt`

## Rubrics
Pada capstone ini, Anda diharapkan untuk dapat membangun sebuah aplikasi Flask yang fokus pada tampilan user interface. Langkah pertama yang harus Anda lakukan adalah silahkan download atau clone repositori ini. File pada repositori ini merupakan sebuah skeleton untuk membuat sebuah dashboard aplikasi Flask. Pada bagian `app.py` dan `templates/index.html` ada beberapa bagian yang rumpang dan harus Anda lengkapi. Beberapa bagian yang harus diperhatikan adalah sebagai berikut:
### Data Preproses and Exploratory Data Analysis
Pada tahap praproses ini, Anda diminta untuk melengkapi praproses data seperti menghapus data yang duplikat, mengubah tipe data dan memodifikasi nilai data. Pada file `app.py` Anda diminta untuk melengkapi data yang rumpang tanpa mengubah alur praproses yang telah ada.
### Data Wrangling
- 

### Data Visualization
- Membuat atau menduplikasi bar plot yang menggambarkan top 5 Category pada Google Playstore
- Membuat atau menduplikasi scatter plot yang menggambarkan sebaran aplikasi jika dilihat berdasarkan Review, Rating, dan jumlah aplikasi yang terinstall.
- Membuat atau menduplikasi histogram plot untuk melihat distribusi ukuran aplikasi 
- Membuat bar plot yang menggambarkan tipe harga aplikasi di Google Playstore

*Notes : Anda dapat melihat contoh plot lain yang hraus dibuat/diduplikat pada repositori ini. Silahkan clone/download repositori ini. 

### Build Flask App

- Demonstrated how to route and make view function for plotting 
- Demonstrated how to render plot to html page
- Demonstrated how to run Flask application in local host
