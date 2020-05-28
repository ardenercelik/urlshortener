#python-dotenv ile başlattığımız env değerlerini bu dosyadan çağırıyoruz.
import os #environ env değerlerini alıyor.

SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
ADMIN_USERNAME=os.environ.get("ADMIN_USERNAME")
ADMIN_PASSWORD=os.environ.get("ADMIN_PASSWORD")
port=3000
