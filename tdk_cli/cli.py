# -*- coding: utf-8 -*-
from urllib.parse import quote
from urllib.request import urlopen
from json import loads

from rich import box
from rich.table import Table
from rich.console import Console
from rich import print


class TDKDict:
    def __init__(self, word):
        self.word = word
        # gts, bati, tarama, derleme, atasozu, kilavuz, lehceler
        url = "https://sozluk.gov.tr/gts?ara=" + quote(word)
        self.data = loads(urlopen(url).read())
        if "error" in self.data:
            print("Error")
            exit()

    def rich(self):
        data = self.data
        word = self.word
        table = Table(title=word + " - TDK", show_header=False, box=box.SQUARE)
        for i in range(len(data)):
            # lang
            if data[i]["lisan"] != "":
                table.add_row(data[i]["lisan"] + ":")
            else:
                # suffix
                if data[i]["taki"] != None:
                    table.add_row(word + ", " + data[i]["taki"] + ":")
                else:
                    table.add_row(word + ":")
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
            if len(data) > 1 and i != range(len(data))[1]:
                table.add_row("")
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
