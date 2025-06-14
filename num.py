from checks import check_pos_odd_int, check_pos_int


class Num:
    
    def __init__(self, n):
        check_pos_odd_int(n)

        self.__data = {'n' : n, 
                       'path' : None,         
                       'path_length' : None,
                       'path_max' : None,
                       'path_ratio' : None,
                       'is_tail' : None}

    @staticmethod
    def col(n):
        if n % 2:
            return 3 * n + 1
        return n // 2

    def data(self):
        return self.__data

    def path(self):
        if self.__data['path'] is None:
            current_num = self.__data['n']
            pth = []
       
            while current_num != 1:
                if current_num % 2:
                    pth.append(current_num)

                current_num = Num.col(current_num)

            pth.append(1)
            self.__data['path'] = pth 
            self.__data['path_length'] = len(pth)
            self.__data['path_max'] = max(pth)
            self.__data['path_ratio'] = max(pth) / self.__data['n']
            self.__data['is_tail'] = max(pth) <= self.__data['n']    

        return self.__data['path']

    def path_length(self):
        if self.__data['path_length'] is None:
            self.path()

        return self.__data['path_length'] 

    def path_max(self):
        if self.__data['path_max'] is None:
            self.path()

        return self.__data['path_max']

    def path_ratio(self):
        if self.__data['path_ratio'] is None:
            self.path()

        return self.__data['path_ratio']

    def is_tail(self):
        if self.__data['is_tail'] is None:
            self.path()

        return self.__data['is_tail']


def tails(n):
    check_pos_int(n)

    num_tails = 0
    for i in range(1, n + 1, 2):
        num_tails += int(Num(i).is_tail())

    return num_tails
