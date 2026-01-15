@echo off
:: バッチファイルのあるディレクトリに移動 (管理者権限などで実行した場合の対策)
cd /d %~dp0

:: ブラウザでURLを開く
echo Opening browser...
start http://127.0.0.1:5000

:: Pythonサーバーを起動
echo Starting Flask server...
python app.py

:: サーバー終了後に画面をすぐ閉じない
pause