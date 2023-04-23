import modelTraining as mt
from tkinter import *


my_font = ("times new roman", 15)
window = lbl_csv = entry_csv = btn_train = None
lbl_phrase = entry_phrase = btn_test = lbl_perc = None
lbl_resulttest = lbl_efile = lbl_ekey = lbl_eempty = None

def createWindow():
    global window, lbl_csv, entry_csv, btn_train
    global lbl_phrase, entry_phrase, btn_test, lbl_perc
    global lbl_resulttest, lbl_efile, lbl_ekey, lbl_eempty

    window = Tk()
    window.geometry("700x450")
    window.title("MachineLearning")
    window.iconbitmap("icon.ico")
    window.resizable = False, False

    lbl_csv = Label(text="Укажите путь до датасета\n(csv-файл) для обучения:", font=my_font, justify=LEFT)
    lbl_csv.place(x=15, y=15)

    entry_csv = Entry(font=my_font)
    entry_csv.place(x=255, y=20, width=430, height=40)

    btn_train = Button(text="Обучить модель", font=my_font, command=clickBtnTrain)
    btn_train.place(x=15, y=75, width=670, height=40)

    lbl_phrase = Label(text="Введите фразу для про-\nверки модели:", font=my_font, justify=LEFT)
    lbl_phrase.place(x=15, y=125)

    entry_phrase = Entry(font=my_font)
    entry_phrase.place(x=255, y=130, width=430, height=40)

    btn_test = Button(text="Проверить", font=my_font, command=clickBtnTest)
    btn_test.place(x=15, y=185, width=670, height=40)

    lbl_perc = Label(text="Точность модели: ", font=my_font, justify=LEFT)
    # lbl_perc.place(x=15, y=235)

    lbl_resulttest = Label(text="Результат проверки: ", font=my_font, justify=LEFT)
    # lbl_resulttest.place(x=15, y=265)

    lbl_efile = Label(text="Ошибка при чтении с файла", font=my_font, justify=LEFT, foreground="red")
    # lbl_efile.place(x=15, y=295)

    lbl_ekey = Label(text="Файл не соответствует требованиям", font=my_font, justify=LEFT, foreground="red")
    # lbl_ekey.place(x=15, y=355)

    lbl_eempty = Label(text="Текстовое поле должно быть заполнено", font=my_font, justify=LEFT, foreground="red")
    # lbl_eempty.place(x=15, y=355)
    
    window.mainloop()

def clickBtnTrain():
    global window, lbl_csv, entry_csv, btn_train
    global lbl_phrase, entry_phrase, btn_test, lbl_perc
    global lbl_resulttest, lbl_efile, lbl_ekey, lbl_eempty

    lbl_efile.place_forget()
    lbl_ekey.place_forget()
    lbl_eempty.place_forget()

    if entry_csv.get() == "":
        e = mt.initDF()
    else:
        e = mt.initDF(entry_csv.get())

    if type(e) == FileNotFoundError:
        lbl_efile.place(x=15, y=295)
    elif type(e) == KeyError:
        lbl_ekey.place(x=15, y=325)
    else:
        mt.normAndTrain()
        lbl_perc['text'] = "Точность модели: " + str(mt.calculatingPercentage())
        lbl_perc.place(x=15, y=235)

def clickBtnTest():
    global window, lbl_csv, entry_csv, btn_train
    global lbl_phrase, entry_phrase, btn_test, lbl_perc
    global lbl_resulttest, lbl_efile, lbl_ekey, lbl_eempty
    
    lbl_efile.place_forget()
    lbl_ekey.place_forget()
    lbl_eempty.place_forget()

    if entry_phrase.get() == "":
        lbl_eempty.place(x=15, y=355)
    else:
        res = mt.testModel(entry_phrase.get())
        lbl_resulttest['text'] = "Результат проверки: " + str(res)
        lbl_resulttest.place(x=15, y=265)

def main():
    createWindow()

if __name__ == "__main__":
    main()