def messageSend(domain,uid64,tokens):
    return f"<The Cake 회원가입 이메일 인증>\n\n\n" \
           f"아래 링크를 클릭하면 회원가입 인증이 완료됩니다.\n\n" \
           f"회원가입 링크 : http://{domain}/baker/activate/{uid64}/{tokens}\n\n감사합니다. :)"

def passwordMessage(domain,userid,temppw):
    return f"<The Cake 임시 비밀번호 발급>\n\n\n" \
           f"{userid}님의 임시 비밀번호는 {temppw}입니다.\n" \
           f"로그인 후 비밀번호를 재설정해주세요.\n\n\n\n" \
           f"로그인하러 가기: http://{domain}/baker/login\n\n"