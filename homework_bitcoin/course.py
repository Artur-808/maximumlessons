import bs4
import requests
import tkinter

def getcontent(valute):
    url= "https://myfin.by/crypto-rates/" + valute
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, "lxml")
    return soup
def getcourse(soup):
    result = soup.find("div", {"class": "birzha_info_head_rates"})
    return result.text
def main(valute):
    soup= getcontent(valute)
    return getcourse(soup)
main("bitcoin")
rub = main("bitcoin")
def rubbles(none):
    rub2 = rub.split(".")
    return rub2[0]
rub3 = rubbles(rub)
rub4 = int(rub3) * 60
rub5 = "(или ~{} российских рублей)".format(rub4)
window = tkinter.Tk()
window.geometry("450x500")
window.title("bitcoin")
logo = tkinter.PhotoImage(file= "bitcoin.png")
pic = tkinter.Label(image= logo)
pic.place (x=100, y=0)
label = tkinter.Label(text= "1 BitCoin стоит" + main("bitcoin"), font= "Arial 18")
label.place(x=0, y= 300)
label = tkinter.Label(text= rub5, font= "Arial 18")
label.place(x= 40, y= 380)
window.mainloop()