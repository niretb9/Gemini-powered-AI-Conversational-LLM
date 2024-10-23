"""
KIIT 7th Semester Minor Project

Title: Gemini-Powered LLM Conversational AI Platform with Integrated College Data and Faculty Database

Authors: 
    Mayank Gajwe    - 21052080
    Niret Badgire   - 2105385
    Ketan Kumar     - 21051823

Mentor/Faculty: Sarita Tripathy
"""
import json
import os
import re
import webbrowser
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai

import asciiprint as asc
import gemini_trainer as train #todo

"""
[*] A token is equivalent to about 4 characters for Gemini models. 100 tokens are about 60-80 English words.

[**] RPM: Requests per minute
TPM: Tokens per minute
RPD: Requests per day
TPD: Tokens per day

# use Dev for testing and training - utilizes limited tokens
# use Prod for final deliverable
"""
varModelDev = asc.dev_credentials
varModelProd = asc.prod_credentials

forceTokenLimit = 10001


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(varModelProd)

chat = model.start_chat(history=[])

def format_double_stars(text):
    orange_color = '\033[38;5;208m'
    reset_color = '\033[0m'
    pattern = r'\*\*(.*?)\*\*'

    # Check if text is a string
    if not isinstance(text, str):
        return text

    # Use re.DOTALL to match across multiple lines
    formatted_text = re.sub(pattern, lambda match: f"{orange_color}**{match.group(1)}**{reset_color}", text, flags=re.DOTALL)

    return formatted_text

def tune_gemini(question):
    response = chat.send_message(question, stream=False)  
    return response

training_data = './scraped_links_content.txt' # no formatting req
def initialize():
    print("[+] INITIALIZING")
    bias = train.loadTrainer(training_data)
    if(bias==''):
        bias = asc.redactData
    tune_gemini(asc.initprompt)
    tune_gemini(bias[:forceTokenLimit])

def talk(query):
    response = tune_gemini(query)
    res = format_double_stars(response.text)
    print(res)
    while True:
        print("\033[92m[+]\033[0m Enter your query (type 'exit' to quit): ", end='')
        q = input()
        if q.lower() == 'exit':
            break 
        response = tune_gemini(q)
        print(response.text)
def open_link(url):
    webbrowser.open(url)

def print_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  
    art = asc.art
                                                           

    print(f"\033[95m{art}\033[0m\n\033[93m")
    print("[1] SHOW ALL TEACHERS\n")
    print("[2] INFORMATION ABOUT TEACHERS\n")
    print("[3] ABOUT KIIT\n")
    print("[4] WHO IS THE BEST TEACHER ?\n")
    print("[5] CUSTOM QUERY\n")
    print("[6] EXIT\033[0m\n")

def show_teachers():
    with open('./teacher.jsonl', 'r') as json_file:
        json_list = list(json_file)
    count = 0
    for json_str in json_list:
        result = json.loads(json_str)
        count += 1
        print(f"\033[92m[+]\033[0m {count}. {result['NAME']}")

def show_teacher_profile(id):
    with open('./teacher.jsonl', 'r') as json_file:
        json_list = list(json_file)

    for json_str in json_list:
        result = json.loads(json_str)
        if result['id'] == id:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"NAME: {result['NAME']}")
            print(f"DEPARTMENT: {result['DEPARTMENT']}")
            print(f"EMAIL: {result['EMAIL']}")
            print("\nDo you want more information? y/n, Y/n")
            ans = input().lower()
            if ans == 'y':
                open_link(result['LINK'])
                continue
            else:
                print("[-] exiting !!")
            break

def main():
    initialize()
    exit_flag = 0
    while exit_flag != 1:
        print_menu()
        print("query-> ", end='')
        query = input()
        if query == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            show_teachers()

        elif query == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            show_teachers()
            print("[?] Enter teacher index ?")
            print("query-> ", end='')
            query = input()
            show_teacher_profile(query)

        elif query == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            kiit = asc.kiit
            print('\033[92m', kiit, '\033[0m')
            talk('Tell us about Kalinga Institute of Industrial Technology within 150 words')
            print("\nDo you want more information? y/n, Y/n")
            ans = input().lower()
            if ans == 'y':
                open_link('https://cse.kiit.ac.in/')
                continue
            else:
                print("[-] exiting !!")
            continue

        elif query == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            open_link('https://cse.kiit.ac.in/wp-content/uploads/2019/01/Sarita-Tripathy-1.jpg')

        elif query == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[92m[+]\033[0m Enter your query-> ", end='')
            q = input()
            talk(q)

        elif query == '6':
            exit_flag = 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print("CREATED BY-".center(60))
            
            mayank = asc.mayank
            a = asc.a
            print(mayank, asc.niret, asc.ketan)

            print("\033[35m 21052080, 2105385, 2101823\033[0m".center(60))
            os.system("pause")
            break

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("[!] USE CUSTOM QUERY !!")
            print("\033[92[+]\033[0m Enter your query-> ", end='')
            q = input()
            talk(q)

if __name__ == '__main__':
    main()
