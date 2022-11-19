from pprint import pprint

class Profile:
    def __init__(self):
        self.profile = {
            "name": "-",
            "gender": "-",
            "birthday": "-",
            "age": "-",
            "phone": "-",
            "email": "-",
        }
    
    def set_profile(self, profile):
        self.profile = profile
        
    def get_profile(self):
        return self.profile
    
    def get_name(self):
        return self.profile.get('name')
    
    def get_gender(self):
        return self.profile.get('gender')
    
    def get_birthday(self):
        return self.profile.get('birthday')
    
    def get_age(self):
        return self.profile.get('age')
    
    def get_phone(self):
        return self.profile.get('phone')
    
    def get_email(self):
        return self.profile.get('email')
    
    
    
profile = Profile()


profile.set_profile({
    "name": "lee",
    "gender": "man",
    "birthday": "01/01",
    "age": 32,
    "phone": "01012341234",
    "email": "python@sparta.com",
})

information = input("궁금하신 정보를 입력하세요. (ex): 이름, 성별, 생일, 나이, 핸드폰번호, 이메일) ※전체를 보시려면 전체 를 입력해주세요 : ")

if information == "이름":
    print(profile.get_name()) # 이름 출력
elif information == "성별":
    print(profile.get_gender()) # 성별 출력
elif information == "생일":
    print(profile.get_birthday()) # 생일 출력
elif information == "나이":
    print(profile.get_age()) # 나이 출력
elif information == "핸드폰번호":
    print(profile.get_phone()) # 핸드폰번호 출력
elif information == "이메일":
    print(profile.email()) # 이메일 출력
elif information == "전체":
    pprint(profile.get_profile())
else:
    print("잘못 입력하셨습니다.")