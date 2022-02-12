# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 14:12:31 2022

@author: Marcos
"""

#Importação de bibliotecas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class main:
    def __init__(self, city):
        self.browser = webdriver.Chrome(executable_path=r'/home/marcos/Documentos/chromedriver_linux64/chromedriver') #Conecta o chrome com python
        self.browser.maximize_window() #Maximizar a tela do Chrome
        self.browser.get('https://www.cptec.inpe.br/') #Site que o Chrome vai abrir
        sleep(3.5)
        self.search = self.browser.find_element_by_id('search').send_keys(city) #Digita a cidade na barra de peesquisa
        sleep(2)
        self.search = self.browser.find_element_by_id('search').send_keys(Keys.ARROW_DOWN + Keys.ENTER) #Pressiona para baixo e dar ENTER
        sleep(3.5)
        self.browser.find_element_by_css_selector('#home > span > button').click() #Clica no botão de Previsão Horáaria 
        sleep(2)
        
    def extract(self, city):
        city = city.lower() #Converteu toda a palavra da cidade para minúsculo
        if(city == 'natal'): #Se a cidade for Natal use essas posições 
            self.city = self.browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/h4').text
            self.temp = self.browser.find_element_by_xpath('/html/body/div[2]/div[5]/div[1]/div/div[3]').text
            self.data = self.browser.find_element_by_xpath('/html/body/div[2]/div[5]/div[1]/div/div[4]').text
            sleep(3.5)
        else: 
            self.city = self.browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/h4').text
            self.temp = self.browser.find_element_by_xpath('/html/body/div[2]/div[5]/div[1]/div/div[2]').text
            self.data = self.browser.find_element_by_xpath('/html/body/div[2]/div[5]/div[1]/div/div[3]').text
            sleep(3.5)

        self.browser.close()
        

       
