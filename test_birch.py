import unittest
from birch import Birch

class TestBirch(unittest.TestCase):
    def test_initialization(self):
        # Test poprawności inicjalizacji parametrów klasy Birch
        birch = Birch(threshold=0.3, branching_factor=40)
        self.assertEqual(birch.threshold, 0.3)
        self.assertEqual(birch.branching_factor, 40)
    
    def test_fit_creates_clusters(self):
        # Test, czy metoda fit tworzy oczekiwaną liczbę klastrów
        X = [
            [0, 0], [0, 1], [1, 0],  # Punkty w pierwszym klastrze
            [10, 10], [10, 11], [11, 10]  # Punkty w drugim klastrze
        ]
        
        birch = Birch(threshold=2, branching_factor=50)
        birch.fit(X)
        
        # Sprawdzamy, czy zostały utworzone dwa klastry
        self.assertEqual(len(birch.clusters), 2)

    def test_predict_assigns_to_existing_clusters(self):
        # Test, czy metoda predict poprawnie przypisuje punkty do istniejących klastrów
        X_train = [
            [0, 0], [0, 1], [1, 0],
            [10, 10], [10, 11], [11, 10]
        ]
        
        birch = Birch(threshold=2, branching_factor=50)
        birch.fit(X_train)
        
        X_test = [
            [0, 0.5],  # Punkt blisko pierwszego klastra
            [10, 10.5] # Punkt blisko drugiego klastra
        ]
        
        labels = birch.predict(X_test)
        
        # Sprawdzamy, czy punkty testowe zostały przypisane do odpowiednich klastrów
        self.assertEqual(labels[0], 0)  # Punkt przypisany do klastra 0
        self.assertEqual(labels[1], 1)  # Punkt przypisany do klastra 1

if __name__ == "__main__":
    unittest.main()
