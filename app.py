from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import random
import os
from werkzeug.utils import secure_filename
import uuid

# 创建一个Flask网站实例
app = Flask(__name__)

# 设置密钥，用于flash消息
app.config['SECRET_KEY'] = 'your-secret-key-here'

# 静态文件夹配置
UPLOAD_FOLDER = 'static/images'

# 确保上传目录存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 准备美食列表
foods = [
    "五食学子套餐", "五食鸭腿饭", "五食三鲜米线", "六食金陵小炒", "八食鸡排饭",
    "八食牛排饭", "八食鱼排饭", "北京烤鸭", "火锅", "小笼包",
    "红烧肉", "回锅肉", "麻婆豆腐", "香辣蟹", "夫妻肺片",
    "口水鸡", "酸辣粉", "担担面", "锅贴", "生煎包"
]

# 准备文案列表
quotes = [
    "如果上帝把你的门关上了，你就再打开，因为门就是这么用的。",
    "如果世界是一头大象，那么抽象是否是对世界的反抗。",
    "我不再讨厌星期一了，我已经是个成熟的孩子了，我讨厌整个星期",
    "对不起，我不是一个好丈夫，也不是一个好儿子，那又怎样呢，我是一个女孩子",
    "我好像得了自闭症，坐在教室和图书馆眼睛自然而然就会闭起来",
    "为什么会食欲不振啊，我开心了就吃顿好的，不开心了更想吃顿好的安慰安慰自己。",
    "生活就像一盒巧克力，你永远不知道下一块会是什么味道。",
    "你若盛开，清风自来。",
    "每一次的跌倒，都是为了更好的站起来。"
]

# 云类型和描述
cloud_types = {
    "积云": {
        "description": "积云是最常见的云之一，通常呈白色、蓬松的棉花状，底部平坦，顶部凸起。它们通常表明天气晴朗稳定，但如果发展旺盛可能会形成积雨云。",
        "image": "积云通常在阳光明媚的日子里出现，形状像棉花团。"
    },
    "层云": {
        "description": "层云是均匀、灰色的云幕，通常覆盖整个天空，但不会带来降雨。层云形成时往往伴随着阴天或雾天，常见于清晨或寒冷天气。",
        "image": "层云看起来像一层灰色的毯子覆盖在天空中。"
    },
    "卷云": {
        "description": "卷云是高空中的冰晶云，呈白色、羽毛状或纤维状。它们通常出现在晴朗的天空中，预示着天气可能会变化。",
        "image": "卷云在高空中形成，看起来像白色的羽毛或丝线。"
    },
    "积雨云": {
        "description": "积雨云是巨大的、垂直发展的云，顶部通常呈砧状。它们是雷暴、暴雨、冰雹和龙卷风的发源地，属于非常不稳定的云系。",
        "image": "积雨云是雷暴云，顶部像铁砧，底部常常暗黑。"
    },
    "雨层云": {
        "description": "雨层云是暗灰色的云层，通常会带来持续的降雨或降雪。它们覆盖范围广，厚度大，常由层云或高层云发展而来。",
        "image": "雨层云会带来持续的降雨，天空呈暗灰色。"
    },
    "卷积云": {
        "description": "卷积云是高空中的小云块，通常呈鱼鳞状排列。它们是由高空中的气流波动形成的，常被称为\"鱼鳞天\"。",
        "image": "卷积云像天空中的鱼鳞，排列整齐。"
    }
}

# 获取随机美食
@app.route('/random_food')
def random_food():
    food = random.choice(foods)
    return jsonify({'food': food})

# 获取随机文案
@app.route('/random_quote')
def random_quote():
    quote = random.choice(quotes)
    return jsonify({'quote': quote})

# 云识别路由
@app.route('/identify_cloud', methods=['POST'])
def identify_cloud():
    # 在实际应用中，这里应该调用云识别API
    # 目前我们使用随机模拟识别结果
    cloud_types_list = list(cloud_types.keys())
    identified_cloud = random.choice(cloud_types_list)
    cloud_info = cloud_types[identified_cloud]
    
    # 检查是否有文件上传
    if 'cloud_image' in request.files:
        file = request.files['cloud_image']
        if file.filename != '':
            try:
                # 保存上传的云图片
                filename = f"cloud_{uuid.uuid4()}.{file.filename.rsplit('.', 1)[1].lower()}"
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                flash('云图片上传成功！')
            except Exception as e:
                flash(f'图片上传失败：{str(e)}')
    
    return jsonify({
        'cloud_type': identified_cloud,
        'description': cloud_info['description']
    })



# 定义网站的首页
@app.route('/')
def home():
    # 获取第一句美食和文案作为初始显示
    initial_food = random.choice(foods)
    initial_quote = random.choice(quotes)
    
    # 传递初始内容给网页显示
    return render_template('index.html', 
                           initial_food=initial_food, 
                           initial_quote=initial_quote)

# 启动网站（允许外部设备访问）
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')