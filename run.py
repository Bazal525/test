from app import app, db

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Tworzenie tabel, jeśli jeszcze nie istnieją
    app.run(debug=True)
