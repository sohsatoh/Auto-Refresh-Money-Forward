# Auto Refresh Money Forward
Money Forwardにおける口座情報の更新を一括で行うスクリプトです。
二段階認証にも対応しています。

## Requirements
- Python3
- Selenium
- ChromeDriver


## How to use
### 1
~~~
cd 【moneyforward.pyがあるディレクトリ】
chmod 755 ./moneyforward.py
~~~
で実行権限を付与。

### 2
~~~
email = 'YOUR_EMAIL_ADDRESS'
password = 'YOUR_PASSWORD'
path = '/usr/lib/chromium-browser/chromedriver'
~~~
の部分を、自分のログイン情報、ChromeDriverのパスに書き換える。

### 3
~~~
python3 ./moneyforward.py
~~~
で実行。

又、定期的に実行する際は、cron等で設定してください。
