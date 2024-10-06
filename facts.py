import requests
import os, time

def funfact():
    input("\nWould you like a cat fact while you wait? ")
    print("Doesn't matter what you think, I'm going to give you one anyway :)")
    time.sleep(3)
    joke_resp = requests.get("https://catfact.ninja/fact").json()
    joke = joke_resp['fact']
    print("\n###########################")
    print("CAT FACT:")
    print(f"\n{joke}\n")
    print("So interesting isn't it!")
    print("###########################")

    print("\nWaiting 5 seconds for you to read the fact...")
    time.sleep(5)
    print("\nNow, back to getting the weather...")

    for i in range(3):
        time.sleep(1)
        print("...")
