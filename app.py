from flask import Flask, request, jsonify, render_template
import openai
import os
from openai import OpenAI

app = Flask(__name__)

# 设置OpenAI API密钥
openai.api_key = "test"
BASE_URL = "https://openai.api2d.net/v1/chat/completions"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_formula():
    user_input = request.json.get('input')
    if not user_input:
        return jsonify({'error': '无效的输入'}), 400
    
    try:
        # 创建OpenAI客户端
        client = OpenAI(api_key="fk201061-8XCrzLWCSLY99itAWOvWiTkrn8tkdf9M|ck545-c4fde9d", base_url="https://openai.api2d.net/v1")
        
        # 调用GPT API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一个专业的数学公式生成器。"},
                {"role": "user", "content": f"请根据以下描述生成一个数学公式: {user_input}"}
            ]
        )
        
        # 从API响应中提取生成的公式
        generated_formula = response.choices[0].message.content.strip()
        
        return jsonify({'formula': generated_formula})
    except Exception as e:
        return jsonify({'error': f'生成公式时出错: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)

# 注视一条


