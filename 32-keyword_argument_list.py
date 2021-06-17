#Belajar Keyword Argument List (**)

#disini ada sebuah method bernama create_html
 #1. membuat tag html pada parameter pertama
 #2. membuat text sebagai parameter kedua

#cara pertama menggunakan manual yang masih memiliki banyak kesalahan
""" def create_html(tag, text, href=""):
    html = f"<{tag} href='{href}'>{text}</{tag}>"
    return html

html = create_html("p","Hello Reza")
print(html)
html = create_html("a", "Ini Link", href="www.google.com")
print(html) """ #kita hanya ingin tag html ada di a saja tapi malah masuk di p juga

#cara kedua memiliki cara otomatisasi menggunakan keyword_argument_list
 #di python memiliki feature yang bernama keyword argument, dimana kita dapat memasukan argument
 #tapi harus disebutkan nama argumentnya/nama parameternya yang nanti akan otomatis dicombine menjadi sebuah dictionary
def create_html(tag, text, **attributes):
    html = f"<{tag}" #tag masih terbuka belum ditutup karena ingin dilakukan pengulangan didalamnya

    for key, value in attributes.items(): # (.items) untuk memanggil tuple key-value
        html = html + f" {key}='{value}'" #tanda petik satu pada value ('') untuk menambahkan format penulisan html

    html = html + f">{text}</{tag}>" #penutup tag
    return html #mengembalikan html agar dapat dipanggil diluar def function

html = create_html("p","Hello Reza", style="paragraf") #memanggil html diluar def function #tanda peti dua merupakan format penulisan value
print(html)
html = create_html("a", "Ini Link", href="www.google.com", style="link") #tanda peti dua merupakan format penulisan value
print(html)
html = create_html("div", "Ini Div", style="Contoh")
print(html)

# <a href="">Ini Link</a>