# Auto Refresh Money Forward
Money Forwardにおける口座情報の更新を一括で行うスクリプトです。
二段階認証にも対応しています。

ログイン情報はインタラクティブに入力でき、ChromeDriverへのパスも自動で取得します。

## Requirements
- Python3
- Selenium
- ChromeDriver
- configparser

(pipがインストールされている場合)

~~~
pip3 install -r requirements.txt
~~~
ですべてインストール可能です。

## 準備

~~~
cd 【moneyforward.pyがあるディレクトリ】
chmod 755 ./moneyforward.py
~~~
で実行権限を付与します。

ログイン情報はconfig.iniに保存されます。

## ChromeDriverが見つからない場合
下記の部分を、ChromeDriverへのパスに書き換えてください。
~~~
path = "ChromeDriverへのパス"
~~~

## 実行
~~~
python3 ./moneyforward.py
~~~
で実行します。

又、定期的に実行する際は、cron等で設定してください。


## 注意事項
このスクリプトを連続して動かすことは、威力業務妨害罪に当たる可能性があります。

また、一括更新機能はプレミアム機能として提供されていますので、このスクリプトは自己責任で使用してください。
