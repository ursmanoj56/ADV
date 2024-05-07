from selenium.webdriver.common.by import By


class ConfigPage():
    SERVICE_TAB= (By.XPATH, "//a[text()='Services']")
    ADD_SERVICE_ICON= (By.XPATH ,"(//button[@type='button'])[1]")
    CHECKBOX_AWS =(By.NAME, "(//input[@type='checkbox'])[3]")
    AWS_KEYID =(By.XPATH,"//input[@placeholder='Enter Key Id']")
    AWS_ACCESKEY = (By.XPATH, "//input[@placeholder='Enter Access Key']")
    AWS_REGION= (By.XPATH, "//input[@placeholder='Enter Region Name']")
    AWS_DESCRIPTION = (By.XPATH, "//input[@placeholder='Hint: Project Name/Project Description']")
    ADD_BUTTON= (By.XPATH ,"//button[text()='Add']")
    SAVE_BUTTON=(By.XPATH,"(//button[@type='submit'])[1]")
