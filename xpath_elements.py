xpath_dict = {
    #general    
    "page_title" : "//page-title",

    #login screen
    "log_input" : "//input[@id='otus-input-1']",
    "password_input" : "//input[@id='otus-input-3']",
    "log_btn" : "//button/span[contains(text(),'Log In')]",

    #side bar nav
    "home_btn" : "//span[contains(text(),'Home')]",
    "classes_btn" : "//span[contains(text(),'Classes')]",
    "lessons_btn" : "//span[contains(text(),'Lessons')]",
    "bookshelf_btn" : "(//span[contains(text(),'Bookshelf')])[1]",
    "assesment_btn" : "//span[contains(text(),'Assessments')]",
    "gradebook_btn" : "//span[contains(text(),'Gradebook')]",
    "reports_btn" : "//span[contains(text(),'Reports')]",
    "poll_btn" : "//span[contains(text(),'Poll')]",
    "blog_btn" : "//span[contains(text(),'Blog')]",

    #assessments
    "status_lbl" : "//div[@id='otus-status-text']",

    #Bookshelf
    "shared_nav" : "//span[contains(text(),'Shared')]",
    "my_bookshelf_nav" : "(//span[contains(text(),'Bookshelf')])[2]",
    "google_drive_nav" : "//ot-icon/following-sibling::span[contains(text(),'Google')]",
    #Bookshelf resources
    "add_resource_btn" : "//ot-icon[@name='plus']/ancestor::button",
        "add_type_resource" : "//span[contains(text(),'Resource')]//ancestor::div[@class='ot-option-container']",
    
    "resource_type_table" : "//div[contains(text(),'Select Resource Type')]",
        "upload_file_btn" : "(//span[contains(text(),'Upload File')])[1]",
        "link_btn" : "(//span[contains(text(),'Link')])[1]",
        "photo_btn" : "(//span[contains(text(),'Photo')])[1]",
        "video_btn" : "(//span[contains(text(),'Video')])[1]",
        "youTube_btn" : "(//span[contains(text(),'YouTube')])[1]",
        "audio_btn" : "(//span[contains(text(),'Audio')])[1]",
        "googleDrive_btn" : "(//img[contains(@src,'drive.png')]/ancestor::div[1])[1]",
        "oneDrive_btn" : "(//img[contains(@src,'360.png')])[1]",
        "Page_btn" : "//i[@class='far fa-file ng-star-inserted']",
        "google_drive_save_btn" : "//div[contains(@class,'small-centered')]//button",

        "add_link_input" : "(//input[contains(@class,'attach-link__input')])[1]",
        "add_link__name_input" : "(//input[contains(@class,'attach-link__input')])[2]",
        "add_Youtube_link_input" : "//div[@class='attach-link__content-input']/input",
        "add_youtube_link__name_input" : "//div[contains(text(),'Video Name')]//ancestor::div/following-sibling::div[@class='row']/input",
        "save_btn" : "(//span[contains(text(),'Save')]/ancestor::button)[1]",
}