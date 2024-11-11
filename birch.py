import numpy as np

class Birch:
    def __init__(self, threshold=0.5, branching_factor=50):
        self.threshold = threshold
        self.branching_factor = branching_factor
        self.clusters = []  # Inicjalizacja listy klastrów jako lista centroidów

    def fit(self, X):
        # X - zbiór danych
        for point in X:
            # Szukaj najbliższego centroidu w istniejących klastrach
            if len(self.clusters) == 0:
                # Jeśli nie ma klastrów, dodaj pierwszy punkt jako centroid pierwszego klastra
                self.clusters.append(point)
            else:
                distances = [np.linalg.norm(np.array(point) - np.array(centroid)) for centroid in self.clusters]
                min_distance = min(distances)
                min_index = distances.index(min_distance)
                
                if min_distance < self.threshold:
                    # Punkt jest wystarczająco blisko istniejącego centroidu, więc przypisz go do tego klastra
                    self.clusters[min_index] = np.mean([self.clusters[min_index], point], axis=0)
                else:
                    # Punkt nie pasuje do żadnego istniejącego centroidu, więc stwórz nowy klaster
                    self.clusters.append(point)
    
    def predict(self, X):
        labels = []
        for point in X:
            distances = [np.linalg.norm(np.array(point) - np.array(centroid)) for centroid in self.clusters]
            min_index = distances.index(min(distances))
            labels.append(min_index)  # Przypisujemy indeks najbliższego klastra jako etykietę
        return labels


