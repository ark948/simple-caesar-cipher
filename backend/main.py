from flask import Flask, render_template, request, flash, Response, url_for
from dotenv import load_dotenv
import os

from cipher import caesar_cipher_encrypt, caesar_cipher_decrypt

app = Flask(__name__)
load_dotenv()

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/encrypt/', methods=('POST',))
def encrypt():
    if request.method == "POST":
        text = request.form['input-text']
        key = request.form['key']
        if not text or not key:
            flash("Input text or key is missing.")
        else:
            encrypted_text = caesar_cipher_encrypt(s=text, key=int(key))
            return Response(f"ENCRYPTED TEXT => {encrypted_text}", status=200)
        

@app.route('/decrypt/', methods=('POST',))
def decrypt():
    if request.method == "POST":
        text = request.form['input-text']
        key = request.form['key']
        if not text or not key:
            flash("Input text or key is missing.")
        else:
            decrypted_text = caesar_cipher_decrypt(s=text, key=int(key))
            return Response(f"DECRYPTED TEXT => {decrypted_text}", status=200)


if __name__ == "__main__":
    app.run()