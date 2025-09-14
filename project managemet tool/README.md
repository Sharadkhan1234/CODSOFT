PM Tool — Complete Scaffold

Steps to run:
1. python -m venv venv
2. source venv/bin/activate (or venv\Scripts\activate on Windows)
3. pip install -r requirements.txt
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py createsuperuser
7. python manage.py runserver

Notes:
- MEDIA files saved to /media
- Emails are printed to console (development)
- API endpoints available under /api/
