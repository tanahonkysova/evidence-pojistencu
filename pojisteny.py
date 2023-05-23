class Pojisteny:

    def __init__(self, jmeno, prijmeni, telefonni_cislo, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.telefonni_cislo = telefonni_cislo
        self.vek = vek

    def __str__(self):
        return f"{self.jmeno}  {self.prijmeni}   {self.vek}   {self.telefonni_cislo}"
