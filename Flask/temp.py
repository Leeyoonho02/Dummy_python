from flask import Flask

app = Flask(__name__) # 이 모듈이 애플리케이션의 진입점임을 나타냄

@app.route('/')
def home():
    hello = "This is my first project! hooray!"
    return hello

if __name__ == '__main__':
    app.run(debug=True)