# GumTreeWebViewer

Javaソースコードの変更差分（ASTベースの差分）をWebブラウザ上で視覚的に確認するツール．
バックエンドで **GumTree** および **LGMatcher** アルゴリズムを実行し，その結果を表示する．

[内部の処理](https://github.com/Kmura88/LGMatcherJsonExporter)

##  起動画面

<img width="1316" height="741" alt="起動画面" src="https://github.com/user-attachments/assets/f686e1a3-ed00-435c-b6b8-adc20ccea3b1" />


## 動作環境

* **OS**: Windows / Mac / Linux
* **Java**: Java 8 以上（`java` コマンドへのパスが通っていること）
* **Python**: Python 3.x

## セットアップ

`Flask`のインストール
```bash
pip install flask
```

## How to use

### 起動方法-Windows
`run.bat` をダブルクリック．

### 起動方法-コマンドライン
```bash
python app.py
```
起動後、 [http://127.0.0.1:5000](http://127.0.0.1:5000) にアクセス．

## 注意

GumTreeの解析仕様上，入力するコードは完全なクラス構造である必要がある．
メソッドの断片のみでは正しく解析されない．


