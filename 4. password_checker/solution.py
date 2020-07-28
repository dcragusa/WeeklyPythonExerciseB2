from string import ascii_uppercase as uppercase, ascii_lowercase as lowercase, punctuation, digits

CATEGORIES = {'uppercase', 'lowercase', 'punctuation', 'digits'}


class PasswordChecker:
    def __init__(self, min_uppercase, min_lowercase, min_punctuation, min_digits):
        for c in CATEGORIES:
            setattr(self, f'min_{c}', locals()[f'min_{c}'])

    @staticmethod
    def check_category(password, category):
        return len([char for char in password if char in globals()[category]])

    def __call__(self, password):
        min_dict = {c: self.check_category(password, c) - getattr(self, f'min_{c}') for c in CATEGORIES}
        return all([num >= 0 for num in min_dict.values()]), min_dict


create_password_checker = PasswordChecker
