def messageSend(domain,uid64,tokens):
    return f"<The Cake 회원가입 이메일 인증>\n\n\n" \
           f"아래 링크를 클릭하면 회원가입 인증이 완료됩니다.\n\n" \
           f"회원가입 링크 : http://{domain}/fuser/activate/{uid64}/{tokens}\n\n감사합니다. :)"