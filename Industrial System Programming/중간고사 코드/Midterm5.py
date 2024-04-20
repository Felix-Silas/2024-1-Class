import time

input("엔터 누르고 20초 세보세요")


start = time.time()


input("20초 후에 다시 엔터를 누르세요.")


end = time.time()

et = end - start
print('실제 시간:', et)
print('차이: ',abs(20-et))
