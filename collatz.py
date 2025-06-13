class Num:
    
    def __init__(self, n):
        if not (isinstance(n, int) and n > 0 and n % 2):
            raise ValueError('n needs to be a positive odd integer')

        self.__n = n
        self.__path = None

    @staticmethod
    def col(n):
        if n % 2:
            return 3 * n + 1
        return n // 2

    def path(self):
        if self.__path is not None:
            return self.__path

        current_num = self.__n
        self.__path = []
       
        while current_num != 1:
            if current_num % 2:
                self.__path.append(current_num)

            current_num = Num.col(current_num)

        self.__path.append(1)        
        return self.__path

    def path_length(self):
        return len(self.path())

    def path_max(self):
        return max(self.path())

    def path_ratio(self):
        return self.path_max() / self.__n

    def is_tail(self):
        return self.path_max() <=  self.__n             
