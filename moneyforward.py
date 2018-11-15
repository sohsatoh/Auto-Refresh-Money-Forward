#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver

url = "https://moneyforward.com/accounts"
email = "YOUR_EMAIL_ADDRESS"
password = "YOUR_PASSWORD"
path = '/usr/local/bin/chromedriver'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=path, chrome_options=options)
driver.implicitly_wait(5)
print("実行中...")

#ログイン処理
driver.get(url)
driver.find_element_by_id("sign_in_session_service_email").send_keys(email)
driver.find_element_by_id("sign_in_session_service_password").send_keys(password)
driver.find_element_by_id("login-btn-sumit").submit()
print("ログイン中...")

#ログインメッセージ関連
if email == "YOUR_EMAIL_ADDRESS" or password == "YOUR_PASSWORD":
	print("メールアドレスとパスワード両方をスクリプトファイルに入力してください。\n終了します...")
	driver.quit()
	exit()
elif driver.find_elements_by_xpath("//*[contains(text(), 'メールアドレスもしくはパスワードが間違っています')]"):
	print("メールアドレスもしくはパスワードが間違っています。\n終了します...")
	driver.quit()
	exit()
elif driver.find_elements_by_xpath("//*[contains(text(), 'マネーフォワードに登録されていない端末・ブラウザからのログインです。')]"):
	print("二段階認証が必要です。メールを確認し、10分以内に認証コードを入力してください。")
	two_factor_auth_code = input("認証コード: ")
	driver.find_element_by_id("verification_code").send_keys(two_factor_auth_code)
	driver.find_element_by_class_name("form-submit-code").submit()
	if driver.find_elements_by_xpath("//*[contains(text(), '認証コードが無効です。')]"):
		print("認証コードが無効です。\n終了します...")
		driver.quit()
		exit()
	else:
		print("ログインに成功しました!")
		driver.get(url)
		pass
else:
	print("ログインに成功しました!")

#二段階認証設定画面の回避
try:
	not_now_button = str("javascript:document.getElementByClassName('not-now').click();")
	driver.execute_script(not_now_button)
except:
	pass

#更新すべき対象の数を計算
account = len(driver.find_elements_by_xpath("//form[starts-with(@action, '/faggregation_queue2/')]"))
needauth = len(driver.find_elements_by_link_text("要画像認証") + driver.find_elements_by_link_text("要ワンタイムパスワード") + driver.find_elements_by_xpath("//*[contains(text(), '重要なお知らせ')]"))

if account == 0:
	print("口座が一つもないか、ログインできませんでした。\n終了します...")
	driver.quit()
	exit()
elif needauth != 0:
	print("認証が必要な口座が" + str(needauth) + "つあります。これらは更新されません。\n" + str(account) + "つの口座情報を更新します...")
else:
	print(str(account) + "つの口座情報を更新します...")

#更新処理
refreshed = 0
for i in range(account):
	refreshed += 1
	remaining = account - refreshed
	if remaining == 0:
		remaining = "なし"
	print(str(refreshed) + "番目を更新中..." + "(残り" + str(remaining) + ")")
	driver.find_elements_by_xpath("//form[starts-with(@action, '/faggregation_queue2/')]")[refreshed-1].submit()
print("更新が完了しました!")
driver.quit()
