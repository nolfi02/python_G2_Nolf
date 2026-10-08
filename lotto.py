import random


class Lotto:
    def __init__(self):
        # Dictionary: Jede Zahl von 1 bis 45 beginnt mit dem Zähler 0.
        self.statistik = {zahl: 0 for zahl in range(1, 46)}

    def lottoziehung(self, anzahl_zahlen=6):
        """Zieht unterschiedliche Zahlen aus dem Bereich 1 bis 45."""
        if not 1 <= anzahl_zahlen <= 45:
            raise ValueError("Die Anzahl der Zahlen muss zwischen 1 und 45 liegen.")

        verfuegbare_zahlen = list(range(1, 46))
        gezogene_zahlen = []

        for _ in range(anzahl_zahlen):
            # Genau ein Zufallsaufruf pro gezogener Zahl.
            index = random.randrange(len(verfuegbare_zahlen))

            # Entfernte Zahlen können nicht erneut gezogen werden.
            zahl = verfuegbare_zahlen.pop(index)
            gezogene_zahlen.append(zahl)

        return gezogene_zahlen

    def statistik_aktualisieren(self, gezogene_zahlen):
        """Erhöht die Zähler nach einer vollständigen Lottoziehung."""
        for zahl in gezogene_zahlen:
            self.statistik[zahl] += 1

    def lottoziehung_statistik(self, anzahl_ziehungen):
        """Führt mehrere Ziehungen durch und erfasst deren Statistik."""
        if anzahl_ziehungen < 1:
            raise ValueError("Es muss mindestens eine Ziehung stattfinden.")

        # Statistik für diesen Durchlauf zurücksetzen.
        self.statistik = {zahl: 0 for zahl in range(1, 46)}

        for _ in range(anzahl_ziehungen):
            gezogene_zahlen = self.lottoziehung()
            self.statistik_aktualisieren(gezogene_zahlen)

        self.statistik_ausgeben(anzahl_ziehungen)

    def statistik_ausgeben(self, anzahl_ziehungen):
        """Gibt die Häufigkeit jeder Zahl am Bildschirm aus."""
        print(f"\nStatistik für {anzahl_ziehungen:,} Lottoziehungen:")
        print(f"{'Zahl':>4} | {'Häufigkeit':>10} | {'Anteil der Ziehungen':>20}")
        print("-" * 42)

        for zahl, haeufigkeit in self.statistik.items():
            prozent = haeufigkeit / anzahl_ziehungen * 100
            print(f"{zahl:>4} | {haeufigkeit:>10} | {prozent:>19.2f}%")

        print(f"\nInsgesamt gezogene Zahlen: {sum(self.statistik.values()):,}")


def main():
    lotto = Lotto()

    # Eine einzelne Ziehung mit sechs Zahlen anzeigen.
    gezogene_zahlen = lotto.lottoziehung()
    print("Die sechs Lottozahlen:", sorted(gezogene_zahlen))

    # Für jede Anzahl eine eigene Statistik erstellen.
    for anzahl_ziehungen in (1000, 10000, 100000):
        lotto.lottoziehung_statistik(anzahl_ziehungen)


if __name__ == "__main__":
    main()