import os
import torch
import tkinter as tk
import numpy as np
from google import genai
from google.genai import types
from google.genai.errors import APIError
from transformers import AutoTokenizer, AutoModelForSequenceClassification

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, 'cyber_detector_model')
lib_path = os.path.join(BASE_DIR, 'classes.npy')
lib = np.load(lib_path, allow_pickle=True)
lib_list = lib.tolist()

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)


def ambil_kode():
    global kode_simpan

    #untuk mengambil input kode
    kode_simpan = text.get("1.0", "end").strip()

    print("--CODE SUCCEDD TO LOAD")
    print(kode_simpan)

    inputs = tokenizer(kode_simpan, return_tensors='pt', truncation=True, max_length=512)

    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)
        prediction = torch.nn.functional.softmax(outputs.logits, dim=-1)
    
    answer = prediction.numpy()
    result_label.config(text=lib_list[np.argmax(answer, axis=1)])

def api_process():
    success_api = False
    api = api_code.get()
    try:
        api_check = genai.Client(api_key=api)

        api_check.models.list()

        print("The API Key is functioned well")

        success_api = True
    except APIError as a:
        print("API Key is invalid")
        print(f"The detail: {a}")
        return False
    
    except Exception as e:
        print("Something was unbehaviour")
        print(f"The Detail: {e}")
        return False
    
    if success_api:
        switch_to_second_frame()

def switch_to_second_frame():
    first_frame.pack_forget()
    second_frame.pack(fill="both", expand=True)

#membuat bingkai aplikasi
root = tk.Tk()
root.title("AI Code Analizer")
root.geometry('500x500')

#create the API key menu
first_frame = tk.Frame(root, bg="#90ee90")
first_frame.pack(fill='both', expand=True)

#create the label for put API code instruction
label_api = tk.Label(first_frame, text='Paste your API GenAI Here')
label_api.pack(padx=10,pady=10)

#create the box for inputing the API
api_code = tk.Entry(first_frame, width=100)
api_code.pack(padx=10,pady=10)

#create the button to process the API
button_api = tk.Button(first_frame, text="Process", command=api_process, bg="#006400", fg="white")
button_api.pack(padx=10,pady=10)

#create exit button
exit_first_frame = tk.Button(first_frame, text="Exit", command=root.destroy, bg="#006400", fg="white")
exit_first_frame.pack(padx=10,pady=10)

#create the second frame
second_frame = tk.Frame(root)

#membuat petunjuk
label = tk.Label(second_frame, text="Paste your C code below")
label.pack(pady=10, padx=10)

#membuat text box
text = tk.Text(second_frame, width=50, height=15)
text.pack(pady=10)

#membua tombol untuk menyimpan
button_sending = tk.Button(second_frame, text="Check Code", command=ambil_kode, bg='green', fg='white', width=25)
button_sending.pack(pady=10)

#show the result of analizing
result_label = tk.Label(second_frame, text='', bg='white', fg='black')
result_label.pack(padx=10,pady=10) 

#membuat tombol untuk exit
button_exit = tk.Button(second_frame, text='Exit', command=root.destroy, bg='red', fg='black')
button_exit.pack(pady=10)
root.mainloop()