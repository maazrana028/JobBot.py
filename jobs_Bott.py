from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class LinkedinJobBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-webrtc")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("window-size=1200,800")
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.latest_jobs = []

    def login_linkedin(self):
        self.driver.get("https://www.linkedin.com/login")
        wait = WebDriverWait(self.driver, 10)
        try:
            email_input = wait.until(EC.presence_of_element_located((By.ID, 'username')))
            email_input.send_keys(self.email)

            password_input = wait.until(EC.presence_of_element_located((By.ID, 'password')))
            password_input.send_keys(self.password)
            password_input.send_keys(Keys.RETURN)
            time.sleep(random.randint(5, 10))

            # Mask Selenium detection
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

            print("Login successful!")
        except Exception as e:
            print(f"Login failed: {e}")
            self.driver.save_screenshot('login_error.png')

    def search_jobs_linkedin(self, keywords, location):
        self.driver.get(f"https://www.linkedin.com/jobs/search/?keywords={keywords}&location={location}&f_TPR=r604800")
        time.sleep(random.randint(5, 10))
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.randint(3, 6))

    def evaluate_jobs_linkedin(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            job_cards = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'job-card-container')))
        except:
            print("No jobs found for this search.")
            return

        job_counter = 1
        for card in job_cards[:10]:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", card)
                time.sleep(random.randint(3, 6))
                card.click()
                time.sleep(random.randint(4, 8))

                job_title_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'top-card-layout__title')))
                job_title = job_title_element.text

                job_link_element = self.driver.find_element(By.CLASS_NAME, 'top-card-layout__cta')
                job_link = job_link_element.find_element(By.TAG_NAME, 'a').get_attribute('href')

                date_element = self.driver.find_element(By.CLASS_NAME, 'posted-time-ago__text')
                date_posted = date_element.text.lower()

                if 'just now' in date_posted or 'hour' in date_posted or 'day' in date_posted and int(date_posted.split()[0]) <= 7:
                    description_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'description__text')))
                    description = description_element.text

                    score = self.evaluate_fit(description)
                    print(f"Job Title: {job_title}\nScore: {score}\nLink: {job_link}\n")
                    self.latest_jobs.append(f"{job_counter}. {job_title} - {job_link}")
                    job_counter += 1

                    user_input = input(f"Would you like to apply for {job_title}? (yes/no): ")
                    if user_input.lower() == 'yes':
                        message = input("Write a short message for the hiring manager: ")
                        print(f"Message to hiring manager: {message}")
                    else:
                        print("Skipping this job.")
                else:
                    print(f"Skipping {job_title}, posted on: {date_posted}")

            except Exception as e:
                print(f"Skipping job, issue encountered: {e}")

    def evaluate_fit(self, description):
        keywords = [
            'Network Configuration', 'Technical Support', 'Remote Desktop Support', 'Microsoft Office 365', 'Server Administration',
            'Cloud Services', 'Ticketing', 'Incident Management', 'Active Directory', 'System Diagnostics', 'Hardware Support',
            'Printer Configuration', 'Wi-Fi Router Setup', 'Windows OS', 'Linux', 'TCP/IP', 'VLANs', 'DNS', 'DHCP', 'VPN',
            'Routers', 'Switches', 'ServiceNow', 'Zendesk', 'Incident Management', 'Antivirus', 'Malware Removal',
            'Patch Management', 'Azure Portal', 'Virtual Machines', 'Role-Based Access Control', 'RBAC', 'Ubuntu', 'Kali Linux',
            'Parrot OS', 'Oracle VirtualBox', 'VMware Workstation Pro', 'Python', 'Visual Studio'
        ]
        score = sum(1 for word in keywords if word.lower() in description.lower())
        return score

    def search_and_evaluate_multiple(self):
        roles = [
            "IT Technician", "IT Support Analyst", "IT Helpdesk", "Information Technology Analyst", "Cybersecurity Intern", 
            "Junior IT Analyst", "System Administration", "Service Desk analyst", "IT Helpdesk", "Support Desk IT", "Junior Cybersecurity Analyst" 
        ]
        locations = ["London", "Greater London", "Surrey", "Guildford", "Woking", "Egham", "Croydon", "Kingston upon Thames", "Richmond upon Thames", "Southampton", "Northampton", "Reading", "Slough", "Basingstoke", "Portsmouth", "Brighton", "Manchester", "Birmingham", "Bristol", "Leeds", "Liverpool", "Cambridge", "Oxford"]

        for role in roles:
            for location in locations:
                print(f"Searching for {role} in {location}...")
                self.search_jobs_linkedin(role, location)
                self.evaluate_jobs_linkedin()
                time.sleep(random.randint(8, 15))

        with open('latest_jobs.txt', 'w') as file:
            for job in self.latest_jobs:
                file.write(job + '\n')

    def quit(self):
        self.driver.quit()

bot = LinkedinJobBot(
    email='username@example.com',
    password='P@ssword1234'
)

try:
    bot.login_linkedin()
    bot.search_and_evaluate_multiple()
    input("Press Enter to quit...")
finally:
    bot.quit()
