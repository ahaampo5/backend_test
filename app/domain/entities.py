# app/domain/entities.py

class User:
    def __init__(self, user_id: int, username: str, email: str):
        self.user_id = user_id
        self.username = username
        self.email = email
    
    def change_email(self, new_email: str):
        # 도메인 내부 로직 예시
        # ex) 이메일 형식 검증, 중복 체크 등
        self.email = new_email
