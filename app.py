import os
import subprocess
import json
import uuid
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 設定
WORKSPACE_DIR = os.path.join(os.getcwd(), 'workspace')
JAR_PATH = os.path.join(os.getcwd(), 'LGMatcherJsonExporter.jar')
JAVA_CMD = 'java' 

if not os.path.exists(WORKSPACE_DIR):
    os.makedirs(WORKSPACE_DIR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    data = request.json
    src_code = data.get('src_code', '')
    dst_code = data.get('dst_code', '')
    
    # オプションを取得 (デフォルトは -LGM)
    option = data.get('option', '-LGM')
    
    # セキュリティ対策: 意図しないコマンド注入を防ぐため、許可された値かチェック
    if option not in ['-LGM', '-M']:
        option = '-LGM'
    
    unique_id = str(uuid.uuid4())
    src_path = os.path.join(WORKSPACE_DIR, f'src_{unique_id}.java')
    dst_path = os.path.join(WORKSPACE_DIR, f'dst_{unique_id}.java')
    json_path = os.path.join(WORKSPACE_DIR, f'output_{unique_id}.json')
    
    try:
        with open(src_path, 'w', encoding='utf-8',newline='\n') as f:
            f.write(src_code)
        with open(dst_path, 'w', encoding='utf-8',newline='\n') as f:
            f.write(dst_code)

        # 形式: java -jar LGMatcher.jar [OPTION] [JSON_PATH] [SRC_PATH] [DST_PATH]
        cmd = [JAVA_CMD, '-jar', JAR_PATH, option, json_path, src_path, dst_path]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            return jsonify({'error': 'Java execution failed', 'details': result.stderr}), 500

        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8') as f:
                diff_data = json.load(f)
            return jsonify({'success': True, 'data': diff_data})
        else:
            return jsonify({'error': 'Output JSON not found'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        for p in [src_path, dst_path, json_path]:
            if os.path.exists(p):
                try:
                    os.remove(p)
                except:
                    pass

if __name__ == '__main__':
    app.run(debug=True, port=5000)