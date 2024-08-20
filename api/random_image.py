from flask import Flask, send_file, jsonify, make_response
import os
import random

app = Flask(__name__)

# 图片目录路径
IMAGE_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'images')

# 获取图片列表
image_list = [f for f in os.listdir(IMAGE_FOLDER) if os.path.isfile(os.path.join(IMAGE_FOLDER, f))]

@app.route('/api/random', methods=['GET'])
def random_image():
    if not image_list:
        return jsonify({"error": "No images found"}), 404

    # 随机选择一张图片
    image_name = random.choice(image_list)
    image_path = os.path.join(IMAGE_FOLDER, image_name)

    # 使用send_file发送图片
    response = make_response(send_file(image_path))

    # 设置HTTP头来防止浏览器缓存
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

    return response

if __name__ == '__main__':
    app.run(debug=True)
