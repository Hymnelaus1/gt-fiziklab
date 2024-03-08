import tkinter as tk
from tkinter import messagebox

def calculate():
    # inputs
    serielong = int(entry_length.get())

    #
    stack = []
    stack1 = []


    data1 = entry_data1.get()
    stack = [float(x) for x in data1.split(",")]

    data2 = entry_data2.get()
    stack1 = [float(x) for x in data2.split(",")]

    # calculations
    result1 = sum(stack)
    result2 = sum(stack1)
    result3 = sum(x ** 2 for x in stack)
    result4 = sum(stack[i] * stack1[i] for i in range(serielong))
    result5 = result4/result3
    result6 = (serielong * result4 - result1 * result2) / (serielong * result3 - result1 ** 2)

    # results
    result_message = f"Σx: {result1}\n" \
                     f"Σy: {result2}\n" \
                     f"Σx*y: {result4}\n" \
                     f"Σx**2: {result3}\n" \
                     f"Σx*y/Σx**2: {result5}\n" \
                     f"a hesabı(linear fitting formulae): {result6} \n \n"\
                     "Orhan Haluk Taşcıoğlu"   
                     
    messagebox.showinfo("Sonuçlar", result_message)

# tkinter cart curt
root = tk.Tk()
root.title("Fiziklab")

# Seri uzunluğu girişi
label_length = tk.Label(root, text="Serinin uzunluğunu girin:")
label_length.pack()

entry_length = tk.Entry(root)
entry_length.pack()


label_data1 = tk.Label(root, text="x değerlerini giriniz örnek 2.31, 45.1234, 35 (dataların arasına virgül koymayı unutmayın):")
label_data1.pack()

entry_data1 = tk.Entry(root)
entry_data1.pack()


label_data2 = tk.Label(root, text="y değerlerini giriniz örnek 2.31, 45.1234, 35 (dataların arasına virgül koymayı unutmayın):")
label_data2.pack()

entry_data2 = tk.Entry(root)
entry_data2.pack()

explanation_text = "Yukarıdaki örnekler 3 uzunluğundaki bir seri için verilmiştir, ancak kod tüm seriler için çalışıyor \nEğer hesapla butonuna bastıktan sonra karşınıza hesapların olduğu farklı bir sekme açılmıyorsa virgül nokta kullanımına dikkat edin."
explanation_label = tk.Label(root, text=explanation_text)
explanation_label.pack()


calculate_button = tk.Button(root, text="Hesapla", command=calculate)
calculate_button.pack()

root.mainloop()