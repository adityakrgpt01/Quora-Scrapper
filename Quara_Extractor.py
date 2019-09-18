
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import codecs




from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options 

options = Options()
options.binary_location = r'C:\Program Files (x86)\Google\Chrome Dev\Application\chrome.exe'
driver = webdriver.Chrome(chrome_options = options, executable_path=r'D:\Download_New\chromedriver_win32\chromedriver.exe')



def login():

    driver.get('https://www.quora.com/')
    # driver.maximize_window()
    email= driver.find_element_by_xpath("//input[@name='email' and @class='text header_login_text_box ignore_interaction']")
    email.send_keys('aniketgpt04@gmail.com')
    

    # email.send_keys('aniketgpt04@gmail.com')
    time.sleep(0.5)

    password=driver.find_element_by_xpath("//input[@name='password' and @class='text header_login_text_box ignore_interaction']")
    password.send_keys('********')
    time.sleep(0.5)

    # login = driver.find_element_by_xpath("//input[@value='Login' and @class='submit_button ignore_interaction']")
    login = driver.find_element_by_xpath("//input[@class='submit_button ignore_interaction']")
    login.click()

    time.sleep(0.5)

    return driver


login()

from selenium.webdriver.chrome.options import Options

# options = Options()
# options.binary_location = r'C:\Program Files (x86)\Google\Chrome Dev\Application\chrome.exe'
# driver = webdriver.Chrome(chrome_options = options, executable_path=r'D:\Download_New\chromedriver_win32\chromedriver.exe')
# driver.get('https://www.quora.com/topic/Job-Interview-Questions')
# html_doc = driver.page_source


with open('submission2.csv','w') as file:
    file.write("question id,question link,Question,no of follows,no. of answers")

link1 = 'https://www.quora.com/topic/Interviews'
link2 = 'https://www.quora.com/topic/Job-Interview-Questions'
link3= 'https://www.quora.com/topic/Job-Interviews'
link4= 'https://www.quora.com/topic/Programming-Interviews'
link5= 'https://www.quora.com/topic/Facebook-Interviews'
link6= 'https://www.quora.com/topic/Google-Interview-Questions'
link7='https://www.quora.com/topic/Technical-Interview-Questions'
link8='https://www.quora.com/topic/Amazon-Interview-Questions'
link9="https://www.quora.com/topic/Flipkart-Interview-Questions"
link10="https://www.quora.com/topic/Microsoft-Interview-Questions"
link11='https://www.quora.com/topic/Apple-Interview-Questions-1'
link12='https://www.quora.com/topic/Tcs-Technical-Interview-Questions'
link13='https://www.quora.com/topic/Interview-Questions-2'
manylinks = list()
manylinks.append(link3)
manylinks.append(link1)
manylinks.append(link2)
manylinks.append(link4)
manylinks.append(link5)
manylinks.append(link6)
manylinks.append(link7)
manylinks.append(link8)
manylinks.append(link9)
manylinks.append(link10)
manylinks.append(link11)
manylinks.append(link12)
manylinks.append(link13)

for olink in manylinks:
    print(olink)

for olink in manylinks:
    qlinks = list()    
    qids = list()
    # options = Options()
    # options.binary_location = r'C:\Program Files (x86)\Google\Chrome Dev\Application\chrome.exe'
    # browser = webdriver.Chrome(chrome_options = options, executable_path=r'D:\Download_New\chromedriver_win32\chromedriver.exe')
    
    # browser.get(olink)
    driver.get(olink)
    time.sleep(1)
    elem = driver.find_element_by_tag_name("body")


    no_of_pagedowns = 150
    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
        no_of_pagedowns-=1
    post_elems =driver.find_elements_by_xpath("//a[@class='question_link']")
    for post in post_elems:
        qlink = post.get_attribute("href")
        qid = post.get_attribute("id")
        qids.append(qid)
        print(qlink)
        qlinks.append(qlink)
        
    i=0
    for qlink in qlinks:

        append_status=0

        row = list()

        row.append(qids[i])
        i=i+1
        row.append(qlink)
        
        
        try:
            driver.get(qlink)
        except:
            continue
        time.sleep(1)


        elem = driver.find_element_by_tag_name("body")


        # no_of_pagedowns = 1
        # while no_of_pagedowns:
        #     elem.send_keys(Keys.PAGE_DOWN)
        #     time.sleep(0.2)
        #     no_of_pagedowns-=1


        #Question Names
        qname =driver.find_elements_by_xpath("//div[@class='question_text_edit']")
        for q in qname:
            print(q.text)
            # append_status2 = int(q.text[:2])
            # print(append_status2)
            row.append(q.text)


        #follow
        tags = driver.find_elements_by_xpath("//a[@action_click='QuestionFollow']")
        print("\nTag :")
        tag_field = list()
        for t in tags:
            number= t.find_element_by_xpath("//span[@class='ui_button_count_inner']")
            
            print('FOLLOWERS'),

            if(len(number.text)==0):
                number=0

            elif(number.text.find('k')!=-1):
                number=number.text.replace('k','')
                number=float(number)
                number=number*1000
                number=int(number)

            


            else:
                number=int(number.text)

            # num=int(number.text)
            print(number),
            tag_field.append(number)

        row.append(tag_field)




            #Answer Count    
        no_ans = driver.find_elements_by_xpath("//div[@class='answer_count']")
    #    print("No. of ans :")
        for count in no_ans:
            print(count.text)
            append_status = int(count.text[:2])
            print(append_status)

            row.append(count.text)


    #     #All answers
    #     all_ans=driver.find_elements_by_xpath("//div[@class='ui_qtext_expanded']")
    #     i=1
    #     answer_field = list()
    #     for post in all_ans:
    #         if i<=4:
    #             i=i+1
    # #            print("Answer : ")
    # #            print(post.text)
    #             answer_field.append(post.text)
    #         else:
    #             break   
    #     row.append(answer_field)


        print('append_status pppp',append_status)

        if (append_status >10 and number>10):
            with open('submissio2.csv','a') as file:
                writer = csv.writer(file)
                writer.writerow(row)            
            

driver.quit()
