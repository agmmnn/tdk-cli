# -*- coding: utf-8 -*-
from urllib.parse import quote
from urllib.request import Request, urlopen
from json import loads

from rich import box
from rich.table import Table
from rich import print


class TDKDict:
    def __init__(self, word):
        self.word = word
        # gts, bati, tarama, derleme, atasozu, kilavuz, lehceler
        url = "https://sozluk.gov.tr/gts?ara=" + quote(word)
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        self.data = loads(urlopen(req).read())
        # print(self.data)
        if "error" in self.data:
            print(self.data["error"])
            exit()

    def rich(self):
        data = self.data
        word = self.word
        for i in range(len(data)):
            table = Table(
                box=box.ROUNDED,
                show_footer=(
                    True
                    if ("atasozu" in data[i]) or (data[i]["birlesikler"] != None)
                    else False
                ),
                footer_style="grey62",
            )
            table.add_column(
                "[cyan]❯ "
                + data[i]["madde"]
                + (
                    " (" + data[i]["anlam_gor"] + ")"
                    if (len(data) > 1 and data[i]["anlam_gor"] != "0")
                    else ""
                )
                + "[/cyan]",
                (
                    (
                        "Atasözleri, Deyimler veya Birleşik Fiiller:\n"
                        + str([i["madde"] for i in data[i]["atasozu"]])[1:-1]
                        if "atasozu" in data[i]
                        else ""
                    )
                    + (
                        "\n\n"
                        if ("atasozu" in data[i]) and (data[i]["birlesikler"] != None)
                        else ""
                    )
                    + (
                        ("Birleşik Kelimeler:\n") + data[i]["birlesikler"]
                        if data[i]["birlesikler"] != None
                        else ""
                    )
                ),
            )
            # lang
            if data[i]["lisan"] != "":
                table.add_row(data[i]["lisan"])
            else:
                # suffix
                if data[i]["taki"] != None:
                    table.add_row(word + ", " + data[i]["taki"])
                elif (data[i]["telaffuz"] != None) and (data[i]["ozel_mi"] == "1"):
                    table.add_row("özel, " + data[i]["telaffuz"])
            for j in range(len(data[i]["anlamlarListe"])):
                # meaning
                table.add_row(
                    str(j + 1) + ". [cyan]" + data[i]["anlamlarListe"][j]["anlam"] + "."
                )
                # sample sentences
                if "orneklerListe" in data[i]["anlamlarListe"][j] != "":
                    table.add_row(
                        "    [grey62]“"
                        + data[i]["anlamlarListe"][j]["orneklerListe"][0]["ornek"]
                        + "."
                        + "”"
                    )
            # space after each item except last one
            # if len(data) > 1 and i != range(len(data))[1]:
            #     table.add_row("")
            print(table)

    def plain(self):
        data = self.data
        word = self.word
        for i in range(len(data)):
            # lang
            if data[i]["lisan"] != "":
                print(data[i]["lisan"] + ":")
            else:
                # suffix
                if data[i]["taki"] != None:
                    print(word + ", " + data[i]["taki"] + ":")
                else:
                    print(word + ":")
            for j in range(len(data[i]["anlamlarListe"])):
                # meaning
                print(str(j + 1) + ". " + data[i]["anlamlarListe"][j]["anlam"] + ".")
                # sample sentences
                if "orneklerListe" in data[i]["anlamlarListe"][j] != "":
                    print(
                        "    “"
                        + data[i]["anlamlarListe"][j]["orneklerListe"][0]["ornek"]
                        + "."
                        + "”"
                    )
            # space after each item except last one
            if len(data) > 1 and i != range(len(data))[1]:
                print("")
