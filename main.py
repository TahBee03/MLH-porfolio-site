from website import create_app

app = create_app() # Create Flask app

if __name__ == '__main__':
    app.run(debug=True) # Run Flask app