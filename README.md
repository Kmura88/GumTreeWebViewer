# GumTreeWebViewer

Javaソースコードの変更差分（ASTベースの差分）をWebブラウザ上で視覚的に確認するためのツール．
バックエンドで **GumTree** および **LGMatcher** アルゴリズムを実行し，その結果（Delete, Insert, Move, Update）をモダンなUIでハイライト表示する．

##  起動画面

<img width="1316" height="741" alt="起動画面" src="https://github.com/user-attachments/assets/f686e1a3-ed00-435c-b6b8-adc20ccea3b1" />


## 動作環境

* **OS**: Windows / Mac / Linux
* **Java**: Java 8 以上（`java` コマンドへのパスが通っていること）
* **Python**: Python 3.x

## セットアップ

1. **リポジトリのクローン（またはダウンロード）**
```bash
git clone https://github.com/Kmura88/GumTreeWebViewer.git
cd GumTreeWebViewer
```


2. **依存ライブラリのインストール**
Pythonの軽量Webフレームワーク `Flask` を使用．
```bash
pip install flask
```

## 使い方

### 起動方法

**Windowsの場合:**
同梱の `run.bat` をダブルクリック．

**コマンドラインから起動する場合:**
```bash
python app.py
```

起動後、ブラウザで [http://127.0.0.1:5000](http://127.0.0.1:5000) にアクセス．

### 差分の確認手順

1. **コードの入力**: 左右のテキストエリアに比較したいJavaコードを入力．
* **左側**: 変更前 (Source / Before)
* **右側**: 変更後 (Destination / After)


2. **モード選択**: オプションボタンでアルゴリズムを選択．
* `LGMatcher (-LGM)`: 推奨
* `Default (-M)`: 通常のGumTree

1. **実行**: 「Run Compare」ボタンをクリック．

## ⚠️ 入力コードに関する注意

GumTreeの解析仕様上，入力するコードは完全なクラス構造である必要がある．

メソッドの断片のみでは正しく解析されない．
