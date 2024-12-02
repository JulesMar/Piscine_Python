class calculator:
    #your code here

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        res = 0
        for i in V1:
             res += i * V2[V1.index(i)]
        print("Dot product is: ", res)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        res = []
        for i in V1:
             res.append(i + V2[V1.index(i)] + 0.0)
        print("Add Vector is: ", res)
    
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        res = []
        for i in V1:
             res.append(i - V2[V1.index(i)] + 0.0)
        print("Sous Vector is: ", res)
