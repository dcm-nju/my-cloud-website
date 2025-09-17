# Flask网站项目

这是一个基于Flask框架开发的简单网站，提供随机美食推荐、随机文案生成和云识别功能。该项目可以部署到Vercel平台上。

## 功能特点

- 🎲 **随机美食推荐** - 从预设的美食列表中随机推荐一款美食
- 💬 **随机文案生成** - 生成有趣或富有哲理的随机文案
- ☁️ **云识别功能** - 上传图片后随机返回一种云的类型和描述（模拟AI识别）

## 技术栈

- **后端**：Python, Flask
- **前端**：HTML, CSS, JavaScript
- **部署**：Vercel

## 项目结构

```
my-flask-site/
├── app.py                # Flask应用主文件
├── wsgi.py               # WSGI入口文件，用于Vercel部署
├── requirements.txt      # 项目依赖
├── vercel.json           # Vercel配置文件
├── .gitignore            # Git忽略文件配置
├── templates/            # Flask模板目录
│   └── index.html        # 主页面模板
└── static/               # 静态文件目录
    └── images/           # 图片资源
```

## 本地开发

1. 确保安装了Python 3.7+和pip
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 运行应用：
   ```bash
   python app.py
   ```
4. 在浏览器中访问 http://localhost:5000

## Vercel部署说明

本项目已经配置好了Vercel部署所需的文件：
- `vercel.json` - Vercel项目配置
- `wsgi.py` - 标准WSGI入口点
- `requirements.txt` - 项目依赖声明

部署到Vercel时，系统会自动检测这些文件并正确配置环境。