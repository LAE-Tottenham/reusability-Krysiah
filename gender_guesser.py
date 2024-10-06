import requests

def guess_gender(name):
    gender_resp = requests.get(f"https://api.genderize.io/?name={name}").json()
    gender = gender_resp["gender"]
    prob_percent = gender_resp["probability"] * 100
    return [gender, prob_percent]

def gen_guess():
    print("Welcome to the weird weather bot :)")
    print("-----------------------------------\n")
    name = input("May I take your first name please? ")
    gender_result = guess_gender(name)
    gender = gender_result[0]
    prob_percent = gender_result[1]
    print(f"\nHmmm, I'm {prob_percent}% sure you are a {gender}.")
    
    gender_correct = input("Am I right? :) (Y/n)")
    if gender_correct.lower() in ["", "yes", "y", "ye"]:
        print("Wooooooh! Computer 1, Human 0.")
    else:
        print("Ahhhh, sorry! :(")