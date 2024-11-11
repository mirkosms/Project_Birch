import unittest
from birch import Birch

class TestBirch(unittest.TestCase):
    def test_initialization(self):
        birch = Birch(threshold=0.3, branching_factor=40)
        self.assertEqual(birch.threshold, 0.3)
        self.assertEqual(birch.branching_factor, 40)
    
    def test_fit_creates_clusters(self):
        # Przykładowe dane (prosty zestaw, aby łatwo było zweryfikować wynik)
        X = [
            [0, 0], [0, 1], [1, 0],  # Te punkty powinny utworzyć jeden klaster
            [10, 10], [10, 11], [11, 10]  # Te punkty powinny utworzyć drugi klaster
        ]
        
        # Ustawienie algorytmu z odpowiednim threshold, aby utworzyć dwa klastry
        birch = Birch(threshold=2, branching_factor=50)
        birch.fit(X)
        
        # Sprawdzenie liczby klastrów
        # Możesz użyć metody wewnętrznej klasy, jeśli przechowujesz klastry w sposób, który pozwala to łatwo sprawdzić.
        self.assertEqual(len(birch.clusters), 2)

    def test_predict_assigns_to_existing_clusters(self):
        # Dane treningowe, na których algorytm utworzy klastry
        X_train = [
            [0, 0], [0, 1], [1, 0],
            [10, 10], [10, 11], [11, 10]
        ]
        
        birch = Birch(threshold=2, branching_factor=50)
        birch.fit(X_train)
        
        # Nowe punkty, które powinny zostać przypisane do istniejących klastrów
        X_test = [
            [0, 0.5],  # Blisko pierwszego klastra
            [10, 10.5] # Blisko drugiego klastra
        ]
        
        labels = birch.predict(X_test)
        
        # Sprawdzenie, czy punkty testowe zostały przypisane do odpowiednich klastrów
        # (Zakładamy, że klastry są ponumerowane np. 0, 1 itp.)
        self.assertEqual(labels[0], 0)  # Pierwszy punkt powinien trafić do klastra 0
        self.assertEqual(labels[1], 1)  # Drugi punkt powinien trafić do klastra 1

    # Dodaj kolejne testy dla innych funkcji w przyszłości

if __name__ == "__main__":
    unittest.main()
