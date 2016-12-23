from functools import reduce
import math
import matplotlib.pyplot as plt
import numpy as np


while True:

    print("Выберите команду")
    
    print("1. Вычисление суммы")
    print("2. Вычисление степени")
    print("3. Вычислеине среднего арифметического")
    print("4. Проверка на число Фибоначчи")
    print("5. Вычисление факториала")
    print("6. Перестановка максимального и минимального элементов")
    print("7. Расстояние между точками")
    print("8. Построение графика")
    print("0. Выход")
    
    user_input = input(":")
    
    if user_input == "0":
        break
    elif user_input == "1":
      print("Введите числа")
      A = input().split()
      print("1. Способ for")
      print("2. Способ while")
      print("3. Способ рекурсия")
      user_input = input(":")
      
      if user_input == "1":
        s = 0
        for i in range(len(A)):
          A[i]=int(A[i])
          s+=A[i]
        
        print(s)
      
      elif user_input == "2":
        s = 0
        j = len(A)
        i=0
        while i < j:
          A[i] = float(A[i])
          s+=A[i]
          i+=1
        
        print(s)
      elif user_input == "3":
        def summ(p, k=0): 
          k += float(A[p - 1]) 
          if p == 0: 
            return 0 
          
          return summ(p - 1) + k
            
        print(summ(len(A)))
    elif user_input == "2":
      print("Введите число")
      N = input()
      c = 0
      step = 1
      while step < int(N):
        step=step*2
        c+=1
        
      print(int(step/2),',',c-1)
    elif user_input == "3":
      print("Введите числа")
      A = input().split()
      for i in range(len(A)):
          A[i]=int(A[i])
      summ = reduce(lambda a, x: a + x, A)
      print(int(summ)/len(A))
    elif user_input == "4":
      print("Введите число")
      N = input()
      def fibonacci(n): 
        if n <= 2: return 1 
        return fibonacci(n-1) + fibonacci(n-2) 

      fib = 0 
      i=0 
      while fib<int(N): 
        fib=fibonacci(i) 
        i+=1 

      if fib>int(N): 
        print(-1) 
      else: 
        print(i-1) 
    elif user_input == "5":
      print("Введите число")
      N = input() 
      f = 1 
      i = 1 
      while i <= int(N): 
        f*=i 
        i+=1 
      
      print(f)  
    elif user_input == "6":
      print("Введите список")
      A = input().split()
      for i in range(len(A)):
        A[i]=int(A[i])
      mmin=min(A)
      mmax=max(A)
      imin=A.index(mmin)
      imax=A.index(mmax)
      A[imin], A[imax] = A[imax], A[imin]
      print(A)
    elif user_input == "7":
      print("Введите числа x1, y1, x2, y2")
      A = input().split()
      x1 = float(A[0])
      x2 = float(A[1])
      y1 = float(A[2])
      y2 = float(A[3])
      
      print(A)
      d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
      print(d)
    elif user_input == "8":
        v = input("Введите начальную скорость:")
        f1 = v.split()
        b1 = []
        for i in f1:
          b1.append(float(i))
        v = sum(b1)
        g = 3.86
        o = input("Введите угол в градусах:")
        f = o.split()
        b1 = []
        for i in f:
            b1.append(float(i))
        h = sum(b1)
        m = h * math.pi / 180

        lim = 0
        t4 = 1
        t3 = 1
        t2 = 1
        t5 = 1
        while t2 > 0:
            t2 = v * math.sin(m) * t4 - (g * t4 ** 2) / 2
            t4 += 0.01
        t = np.arange(0, t4, 0.01)
        t1 = v * math.cos(m) * t
        t2 = (v * math.sin(m) * t - (g * t ** 2) / 2)
        plt.plot(t1, t2)
        plt.axis('equal')
        plt.xlabel(r'$S,м$')  
        plt.ylabel(r'$H,м$')  
        plt.title(r'$Mars$')  
        plt.grid(True)  
        plt.show()  
