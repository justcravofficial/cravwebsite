from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Serve the main landing page
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve the APK file directly
@app.route('/CRAV1.apk')
def download_apk():
    return send_from_directory('.', 'CRAV1.apk', as_attachment=True)

if __name__ == '__main__':
    # Use environment port for Render
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
