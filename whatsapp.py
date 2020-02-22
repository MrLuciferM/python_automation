from selenium import webdriver
driver = webdriver.Chrome(executable_path = 'D:\Themes\Applications\chromedriver.exe')
driver.get('https://web.whatsapp.com/')

name = input("Enter name of the user or group: ")
msg = input("Enter the message to be sent: ")
count = int(input("How many times u wanna send it? "))

input("Enter anything after scanning the QR ")
user = driver.find_element_by_xpath(f'//span[@title = "{name}"]')
user.click()
msgBox = driver.find_element_by_class_name('_13mgZ')

for i in range(count):
    msgBox.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
    