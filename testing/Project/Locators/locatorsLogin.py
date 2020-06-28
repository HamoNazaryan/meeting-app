class LocatorsLogin:
    body_selector = "body"
    username_textbox_id = "email"
    password_textbox_id = "passLogin"
    login_button_id = "submit"
    flash_message_selector = ".flash-block>p"
    login_title_selector = "#signin h1"
    remember_id = "remember"
    need_account_selector = ".need-account>p"
    forgot_block_selector = ".forgot-block>p"
    email_error_text_selector = '#email+span.helper-text'
    password_error_text_selector = '#passLogin+span.helper-text'
    password_character_counter = "#passLogin~.character-counter"
    signup_link_selector = "a[href='signup']"
    forgot_password_link_selector = "a[href='/reset_password']"
