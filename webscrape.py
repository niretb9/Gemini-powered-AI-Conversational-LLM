from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

service = Service(r"C:\Users\Niret\Downloads\edgedriver_win64\msedgedriver.exe")

driver = webdriver.Edge(service=service)

links = [
    "https://kiit.ac.in/sap/",
    "http://library.kiit.ac.in/",
    "https://kiit.ac.in/notices/",
    "https://alumni.kiit.ac.in/",
    "https://kiit.ac.in/academics/faculty-kiit-university/",
    "https://kiit.ac.in/campuslife/sports/",
    "http://coe.kiit.ac.in/",
    "https://kiit.ac.in/training-placement/",
    "https://kiit.ac.in/career/",
    "https://achyutasamanta.com/",
    "https://kiit.ac.in/a-z-listing/",
    "https://kiit.ac.in/brochure/",
    "https://kiitee.kiit.ac.in/",
    "https://form.kiit.ac.in/payment/",
    "https://kiit.ac.in/sap/",
    "http://library.kiit.ac.in/",
    "https://kiit.ac.in/notices/",
    "https://alumni.kiit.ac.in/",
    "https://kiit.ac.in/academics/faculty-kiit-university/",
    "https://kiit.ac.in/campuslife/sports/",
    "http://coe.kiit.ac.in/",
    "https://kiit.ac.in/training-placement/",
    "https://kiit.ac.in/career/",
    "https://achyutasamanta.com/",
    "https://kiit.ac.in/a-z-listing/",
    "https://kiit.ac.in/brochure/",
    "https://kiitee.kiit.ac.in/",
    "https://form.kiit.ac.in/payment/",
    "https://www.facebook.com/KIITUniversity",
    "https://www.linkedin.com/school/kiituniversity/",
    "https://www.instagram.com/KIITUniversity",
    "https://www.youtube.com/channel/UC2x7DxsTyZj7XBa3hlLVPCQ",
    "https://www.twitter.com/KIITUniversity",
    "https://kiit.ac.in/",
    "https://kiit.ac.in/about/",
    "https://kiit.ac.in/about/#",
    "https://kiit.ac.in/about/kiit-edge/",
    "https://kiit.ac.in/about/ranking-recognition/",
    "https://kiit.ac.in/about/history/",
    "https://kiit.ac.in/about/global-footprint/",
    "https://kiit.ac.in/about/founder/",
    "https://kiit.ac.in/academics/",
    "https://kiit.ac.in/academics/#",
    "https://kiit.ac.in/academics/schools/",
    "https://kiit.ac.in/academics/courses/",
    "http://coe.kiit.ac.in/",
    "https://kiit.ac.in/academics/faculty-kiit-university/",
    "https://kiit.ac.in/academics/scholarships-fellowships/",
    "https://kiit.ac.in/research/",
    "https://news.kiit.ac.in/",
    "https://kiit.ac.in/explore/",
    "https://kiit.ac.in/tour/",
    "https://kiit.ac.in/contact/",
    "https://kiit.ac.in/admission/",
    "https://kiitee.kiit.ac.in/",
    "https://international.kiit.ac.in/",
    "https://kiit.ac.in/#",
    "https://kiit.ac.in/about/",
    "https://kiit.ac.in/about/#",
    "https://kiit.ac.in/about/kiit-edge/",
    "https://kiit.ac.in/about/ranking-recognition/",
    "https://kiit.ac.in/about/history/",
    "https://kiit.ac.in/about/global-footprint/",
    "https://kiit.ac.in/about/founder/",
    "https://kiit.ac.in/academics/",
    "https://kiit.ac.in/academics/#",
    "https://kiit.ac.in/academics/schools/",
    "https://kiit.ac.in/academics/courses/",
    "http://coe.kiit.ac.in/",
    "https://kiit.ac.in/academics/faculty-kiit-university/",
    "https://kiit.ac.in/academics/scholarships-fellowships/",
    "https://kiit.ac.in/research/",
    "https://news.kiit.ac.in/",
    "https://kiit.ac.in/explore/",
    "https://kiit.ac.in/tour/",
    "https://kiit.ac.in/contact/",
    "https://kiit.ac.in/admission/",
    "https://kiitee.kiit.ac.in/",
    "https://international.kiit.ac.in/",
    "https://kiit.ac.in/#pro",
    "https://kiitee.kiit.ac.in/",
    "https://sustainability.kiit.ac.in/",
    "https://kiit.ac.in/campuslife/sports/",
    "https://achyutasamanta.com/",
    "https://international.kiit.ac.in/",
    "https://koc.kiit.ac.in/",
    "https://kiitonline.ac.in/",
    "https://kiitincubator.in/boeing-3-0/",
    "https://kiit.ac.in/convocation/20th-convocation-2024/",
    "https://www.kiitonline.ac.in/?utm_source=kiit.ac.in&utm_medium=slider&utm_campaign=KIITWebsite",
    "https://koc.kiit.ac.in/",
    "https://kiitincubator.in/boeing-3-0/",
    "https://international.kiit.ac.in/",
    "https://library.kiit.ac.in/courses-offered/",
    "https://electronics.kiit.ac.in/programme/",
    "https://yoga.kiit.ac.in/programme/",
    "https://cse.kiit.ac.in/programme/",
    "https://civil.kiit.ac.in/programme/",
    "https://electronics.kiit.ac.in/programme/",
    "https://electrical.kiit.ac.in/programme/",
    "https://kiit.ac.in/about/ranking-recognition/",
    "https://news.kiit.ac.in/",
    "https://news.kiit.ac.in/achievements/achyuta-samanta-receives-national-recognition-for-notable-contributions-to-the-health-sector/",
    "https://news.kiit.ac.in/achievements/achyuta-samanta-receives-national-recognition-for-notable-contributions-to-the-health-sector/",
    "https://news.kiit.ac.in/kims/mega-rangoli-competition-organized-by-pharmacology-department-kims/",
    "https://news.kiit.ac.in/kims/mega-rangoli-competition-organized-by-pharmacology-department-kims/",
    "https://news.kiit.ac.in/achievements/dr-achyuta-samanta-awarded-fellowship-by-institution-of-fire-engineers/",
    "https://news.kiit.ac.in/achievements/dr-achyuta-samanta-awarded-fellowship-by-institution-of-fire-engineers/",
    "https://news.kiit.ac.in/achievements/achyuta-samanta-awarded-60th-honorary-doctorate/",
    "https://news.kiit.ac.in/achievements/achyuta-samanta-awarded-60th-honorary-doctorate/",
    "https://news.kiit.ac.in/kims/pcos-awareness-month-observed-by-kims-department-of-og/",
    "https://news.kiit.ac.in/kims/pcos-awareness-month-observed-by-kims-department-of-og/",
    "https://news.kiit.ac.in/kiit-events/talk/director-rd-kiit-du-delivers-talk-at-louisiana-state-university-health-sciences-center-usa/",
    "https://news.kiit.ac.in/kiit-events/talk/director-rd-kiit-du-delivers-talk-at-louisiana-state-university-health-sciences-center-usa/",
    "https://news.kiit.ac.in/kiitnews/kiit-du-professor-appointed-associate-editor-of-prestigious-elsevier-journal/",
    "https://news.kiit.ac.in/kiitnews/kiit-du-professor-appointed-associate-editor-of-prestigious-elsevier-journal/",
    "https://news.kiit.ac.in/kiitnews/weather-and-climate-hackathon-concludes-at-kiit/",
    "https://news.kiit.ac.in/kiitnews/weather-and-climate-hackathon-concludes-at-kiit/",
    "https://kiit.ac.in/event/",
    "https://kiit.ac.in/event/arsenic-in-the-environment-arsenic-and-other-pollutants-water-security-and-one-health-under-global-climate-change-scenario/",
    "https://kiit.ac.in/event/arsenic-in-the-environment-arsenic-and-other-pollutants-water-security-and-one-health-under-global-climate-change-scenario/",
    "https://kiit.ac.in/event/40th-international-value-engineering-conference-ai-and-the-future-of-ve/",
    "https://kiit.ac.in/event/40th-international-value-engineering-conference-ai-and-the-future-of-ve/",
    "https://kiit.ac.in/event/ieee-4th-international-conference-on-applied-electromagnetics-signal-processing-2024/",
    "https://kiit.ac.in/event/ieee-4th-international-conference-on-applied-electromagnetics-signal-processing-2024/",
    "https://kiit.ac.in/event/kims-won-the-rolling-trophy-in-inter-college-basketball-tournament-2024/",
    "https://kiit.ac.in/event/kims-won-the-rolling-trophy-in-inter-college-basketball-tournament-2024/",
    "https://kiit.ac.in/event/kiit-fresher-party-2024/",
    "https://kiit.ac.in/event/kiit-fresher-party-2024/",
    "https://kiit.ac.in/event/alumni-meet-2024/",
    "https://kiit.ac.in/event/alumni-meet-2024/"
]

with open("scraped_links_content.txt", "w", encoding="utf-8") as txt_file:

    def scrape_text_from_link(link):
        try:
            driver.get(link)
            time.sleep(5)  

            elements = driver.find_elements(By.TAG_NAME, 'p')
            page_text = ""
            for element in elements:
                page_text += element.text + "\n"
            return page_text

        except Exception as e:
            print(f"Failed to scrape {link}: {e}")
            return ""

    for i, link in enumerate(links, 1):
        text = scrape_text_from_link(link)
        
        if text:
            txt_file.write(f"Content from link {i}: {link}\n")
            txt_file.write(text)
            txt_file.write("\n\n")  

driver.quit()
