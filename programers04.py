def solution(phone_number):
    num_length = len(phone_number)
    back_num = phone_number[-4:]
    return "*"*(num_length-4)+back_num