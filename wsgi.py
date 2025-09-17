from app import app

# 同时提供标准的WSGI应用名称
application = app

if __name__ == "__main__":
    app.run()