
from selenium import webdriver
from shutil import which
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
import pandas as pd
import time


def fetch_jobs(keyword, num_pages):
    options = Options()
    options.add_argument("window-size=1920,1080")
    #Enter your chromedriver.exe path below
    path = "/mnt/D/Tech Projects/DS-Salary-Project/India-Data-Science/chromedriver"
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)
    
    url = "https://www.glassdoor.co.in/Job/Home/recentActivity.htm"
    # url = "https://www.glassdoor.co.in/Job/data-scientist-jobs-SRCH_KO0,14_IP5.htm"
    driver.get(url)
    search_input = driver.find_element_by_id("sc.keyword")
    search_input.send_keys(keyword)
    search_input.send_keys(Keys.ENTER)
    time.sleep(2)
    
    
    
    
    company_name = []
    job_title = []
    salary_est = []
    location = []
    job_description = []
    salary_estimate = []
    company_size = []
    company_type = []
    company_sector = []
    company_industry = []
    company_founded = []
    company_revenue = []
    company_rating = []
    
    df = pd.DataFrame({
    'Job Title': job_title,
    'Salary Estimate': salary_estimate,
    'Job Description': job_description,
    'Rating' : company_rating,
    'Company Name"': company_name, 
    'Location': location,
    'Size': company_size,
    'Founded' : company_founded,
    'Type of ownership': company_type,
    'Industry' : company_industry,
    'Sector': company_sector,
    'Revenue': company_revenue
    })
    
    
    
    
    #Set current page to 1
    current_page = 1     
        
        
    time.sleep(3)
    
    while current_page <= num_pages:   
        
        done = False
        while not done:
            job_cards = driver.find_elements_by_xpath("//article[@id='MainCol']//ul/li[@data-adv-type='GENERAL']")
            for card in job_cards:
                card.click()
                time.sleep(1)

                #Closes the signup prompt
                try:
                    driver.find_element_by_xpath(".//span[@class='SVGInline modal_closeIcon']").click()
                    time.sleep(2)
                except NoSuchElementException:
                    time.sleep(2)
                    pass

                #Expands the Description section by clicking on Show More
                try:
                    driver.find_element_by_xpath("//div[@class='css-t3xrds e856ufb2']").click()
                    time.sleep(1)
                except NoSuchElementException:
                    card.click()
                    print(str(current_page) + '#ERROR: no such element')
                    time.sleep(30)
                    driver.find_element_by_xpath("//div[@class='css-t3xrds e856ufb2']").click()
                except ElementNotInteractableException:
                    card.click()
                    driver.implicitly_wait(30)
                    print(str(current_page) + '#ERROR: not interactable')
                    driver.find_element_by_xpath("//div[@class='css-t3xrds e856ufb2']").click()

                #Scrape 

                try:
                    company_name.append(driver.find_element_by_xpath("//div[@class='css-xuk5ye e1tk4kwz5']").text)
                except:
                    company_name.append("#N/A")
                    pass
                
                try:
                    company_rating.append(driver.find_element_by_xpath("//div[@class='mr-sm css-ey2fjr e1pr2f4f3']").text)
                except:
                    company_rating.append("#N/A")
                    pass

                try:
                    job_title.append(driver.find_element_by_xpath("//div[@class='css-1j389vi e1tk4kwz2']").text)
                except:
                    job_title.append("#N/A")
                    pass

                try:
                    location.append(driver.find_element_by_xpath("//div[@class='css-56kyx5 e1tk4kwz1']").text)
                except:
                    location.append("#N/A")
                    pass

                try:
                    job_description.append(driver.find_element_by_xpath("//div[@id='JobDescriptionContainer']").text)
                except:
                    job_description.append("#N/A")
                    pass

                try:
                    salary_estimate.append(driver.find_element_by_xpath("//div[@class='css-y2jiyn e2u4hf18']").text)
                except:
                    salary_estimate.append("#N/A")
                    pass
                            
                try:
                    company_size.append(driver.find_element_by_xpath("//div[@id='CompanyContainer']//span[text()='Size']//following-sibling::*").text)
                except:
                    company_size.append("#N/A")
                    pass
                
                try:
                    company_type.append(driver.find_element_by_xpath("//div[@id='CompanyContainer']//span[text()='Type']//following-sibling::*").text)
                except:
                    company_type.append("#N/A")
                    pass
                    
                try:
                    company_sector.append(driver.find_element_by_xpath("//div[@id='CompanyContainer']//span[text()='Sector']//following-sibling::*").text)
                except:
                    company_sector.append("#N/A")
                    pass
                    
                try:
                    company_industry.append(driver.find_element_by_xpath("//div[@id='CompanyContainer']//span[text()='Industry']//following-sibling::*").text)
                except:
                    company_industry.append("#N/A")
                    pass
                    
                try:
                    company_founded.append(driver.find_element_by_xpath("//div[@id='CompanyContainer']//span[text()='Founded']//following-sibling::*").text)
                except:
                    company_founded.append("#N/A")
                    pass
                    
                try:
                    company_revenue.append(driver.find_element_by_xpath("//div[@id='CompanyContainer']//span[text()='Revenue']//following-sibling::*").text)
                except:
                    company_revenue.append("#N/A")
                    pass
                    
                    
                    
                    
                done = True
                
       # Moves to the next page         
        if done:
            print(str(current_page) + ' ' + 'out of' +' '+ str(num_pages) + ' ' + 'pages done')
            driver.find_element_by_xpath("//span[@alt='next-icon']").click()   
            df = pd.DataFrame({
            'Job Title': job_title,
            'Salary Estimate': salary_estimate,
            'Job Description': job_description,
            'Rating' : company_rating,
            'Company Name"': company_name, 
            'Location': location,
            'Size': company_size,
            'Founded' : company_founded,
            'Type of ownership': company_type,
            'Industry' : company_industry,
            'Sector': company_sector,
            'Revenue': company_revenue
            })
            df.to_csv(keyword + '.csv')
    
            current_page = current_page + 1
            time.sleep(4)
            
    driver.close()

  
    df.to_csv(keyword + '.csv')
    
                       