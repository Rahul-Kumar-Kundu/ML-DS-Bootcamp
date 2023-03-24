{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ff3a198e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7.45\n"
     ]
    }
   ],
   "source": [
    "a=float(input())\n",
    "print('%.2f' %a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "1e430269",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[7.3, 4.5, 3.2, 4.6, 4.3]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lst=[]\n",
    "for i in range (0,5):\n",
    "    a=float(input())\n",
    "    lst.append(a)\n",
    "lst"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b7f0c7f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3 4 5 6 7 8 9 10 "
     ]
    }
   ],
   "source": [
    "a=int(input())\n",
    "n=1\n",
    "while(n <= a):\n",
    "    print(n,end=\" \")\n",
    "    n=n+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d4eef21a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 "
     ]
    }
   ],
   "source": [
    "a=int(input())\n",
    "for i in range (a,0):\n",
    "        print(a,end=\" \")\n",
    "        a=a+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "aa2d7635",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a=int(input())\n",
    "count=0\n",
    "while a>0:\n",
    "    count=count+1\n",
    "    a//=10\n",
    "count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "a509f531",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "120"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n=int(input())\n",
    "c=1\n",
    "while n>1:\n",
    "    c =c* n\n",
    "    n=n-1\n",
    "c\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "d0d3ae69",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 \n",
      "\n",
      "1 2 \n",
      "\n",
      "1 2 3 \n",
      "\n",
      "1 2 3 4 \n",
      "\n",
      "1 2 3 4 5 \n",
      "\n"
     ]
    }
   ],
   "source": [
    "for i in range(1,6):\n",
    "    for j in range(1,i+1):\n",
    "        print(j,end=' ')\n",
    "    print('\\n')   "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
