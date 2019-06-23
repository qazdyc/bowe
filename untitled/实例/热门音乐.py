from selenium import webdriver
url = "163muisc"
browser = webdriver.chrome()
while url != "javacript:void(0)":
    browser.get(url)
    browser.switch_to.frame("")
    data =
browser.find_element_by_id("").find_elements_by_tag_name("")
for i in range(len(data)):
    num = data[i].find_element_by_class_name("nb").text
    if "万" in num and int(num.split("万")[0])>1000:
        msk = data[i].find_element_by_css_selector("")
        with open("163playlist.txt","a") as f:
            f.write(["msk.title","msk.num","msk.href"])
url = browser.find_element_by_css_selector("").get_attribute("")
browser.close()