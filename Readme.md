# Auto Refresh Money Forward
Money Forwardにおける口座情報の更新を一括で行うスクリプトです。
二段階認証にも対応しています。

## Requirements
- Python (2 or 3)
- Selenium
- ChromeDriver


## Preparing to run

~~~
cd 【moneyforward.pyがあるディレクトリ】
chmod 755 ./moneyforward.py
~~~
で実行権限を付与します。

次に、下記の部分を、自分のログイン情報、ChromeDriverのパスに書き換えてください。
~~~
email = 'YOUR_EMAIL_ADDRESS'
password = 'YOUR_PASSWORD'
path = '/usr/lib/chromium-browser/chromedriver'
~~~

## How to run
~~~
python3 ./moneyforward.py
~~~
で実行します。

又、定期的に実行する際は、cron等で設定してください。


## Caution
このスクリプトを連続して動かすことは、威力業務妨害罪に当たる可能性があります。
また、一括更新機能はプレミアム機能として提供されていますので、このスクリプトは自己責任で使用してください。
