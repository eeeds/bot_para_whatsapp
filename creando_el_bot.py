from selenium import webdriver
import time
import os, time
#Obtención del path de chromedriver
driver = webdriver.Chrome(executable_path=r"C:\Users\Encin\Dropbox\My PC (LAPTOP-QC4SVF2M)\Desktop\Github\Curso-Bot de Whatsapp\chromedriver.exe")

driver.get("https://web.whatsapp.com/")
time.sleep(10)
#Ejemplo con número y mensaje
celular = "595982355439"

mensaje = "Hola, soy un bot"
driver.get("https://wa.me/" + celular +  "?text=" + mensaje)

time.sleep(5)

#Obtención de elementos por su xpath
btn = driver.find_elements_by_xpath("//*[@id='action-button']")[0]
btn.click()
time.sleep(5)

btn= driver.find_elements_by_xpath("//*[@id='fallback_block']/div/div/a")[0]
btn.click()
time.sleep(30)
#Este es el botón de envío de Whatsapp
btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[3]")[0]

btn.click()
time.sleep(5)


driver.close()