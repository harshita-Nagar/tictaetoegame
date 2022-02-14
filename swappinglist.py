# swappipng using   class
class Swapping:

    #@@staticmethod
    def swap_list(self, sl):
            n = len(sl)

            # Swapping
            temp = sl[0]
            sl[0] = sl[n - 1]
            sl[n - 1] = temp

            return sl


list_r=[10, 14, 5, 9, 56, 12]
swapping=Swapping()
k=swapping.swap_list(list_r)
print(k)


