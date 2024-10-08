{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a392d5df-3729-40b5-97e5-1a85cc563f6a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'John', 'age': 30, 'city': {'name': 'New York', 'country': 'USA'}}\n"
     ]
    }
   ],
   "source": [
    "#Dictionaries\n",
    "person = {\n",
    "    'name': 'John',\n",
    "    'age': 30,\n",
    "    'city': {\n",
    "        'name': 'New York',\n",
    "        'country': 'USA'\n",
    "    }\n",
    "}\n",
    "print(person)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fa0bbfe4-8b06-46be-8bcf-5e29e8439f02",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'name': 'John', 'age': 31, 'city': {'name': 'New York', 'country': 'USA'}, 'gender': 'male', 'education': {'degree': 'Bachelor of Science', 'major': 'Computer Science'}}\n"
     ]
    }
   ],
   "source": [
    "#To Add KEY \n",
    "person['gender'] = 'male'\n",
    "person['age'] = 31\n",
    "person['education'] = {\n",
    "    'degree': 'Bachelor of Science',\n",
    "    'major': 'Computer Science'\n",
    "}\n",
    "print(person)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "88f8c479-632a-4578-b665-02be1801f6e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "31\n"
     ]
    }
   ],
   "source": [
    "##TO UPDATE VALUE \n",
    "print(person['age'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "49943a87-e78d-4fe9-bc8e-b1ff4416957c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "New York\n"
     ]
    }
   ],
   "source": [
    "person = {\n",
    "    'name': 'John',\n",
    "    'age': 30,\n",
    "    'city': {\n",
    "        'name': 'New York',\n",
    "        'country': 'USA'\n",
    "   }\n",
    "}\n",
    "print(person['city']['name'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d18e74d8-2d44-4672-beb8-bdc6299f9a02",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0: {'name': 'John', 'age': 20, 'grade': 'A'}, 1: {'name': 'Jane', 'age': 21, 'grade': 'B'}, 3: {'name': 'Bob', 'age': 22, 'grade': 'C'}, 4: 'none'}\n"
     ]
    }
   ],
   "source": [
    "##CAN NAME DICTIONARY ANYTHING\n",
    "students = {\n",
    "    0: {\n",
    "        'name': 'John',\n",
    "        'age': 20,\n",
    "        'grade': 'A'\n",
    "    },\n",
    "    1: {\n",
    "        'name': 'Jane',\n",
    "        'age': 21,\n",
    "        'grade': 'B'\n",
    "    },\n",
    "    3: {\n",
    "        'name': 'Bob',\n",
    "        'age': 22,\n",
    "        'grade': 'C'\n",
    "    },\n",
    "    4: 'none'\n",
    "}\n",
    "print(students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ce83ba13-6752-49dd-a4ab-73a4f40192fd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jane\n"
     ]
    }
   ],
   "source": [
    "print(students[1]['name'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "2a1b2079-7195-4fc4-9d0e-7fcbf8f02683",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0: {'name': 'John', 'age': 20, 'grade': 'A'}, 3: {'name': 'Bob', 'age': 22, 'grade': 'C'}, 4: 'none'}\n"
     ]
    }
   ],
   "source": [
    "#TO DELETE \n",
    "del students[1]\n",
    "print(students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "e09e9c52-8fb1-425d-b15e-5fb7e4c1415c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "John\n",
      "30\n",
      "{'name': 'New York', 'country': 'USA'}\n"
     ]
    }
   ],
   "source": [
    "for xyz in person.values():\n",
    "  print(xyz)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "bf9fbc25-4591-412e-b49e-9b7a8c2061c6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 {'name': 'John', 'age': 20, 'grade': 'A'}\n",
      "3 {'name': 'Bob', 'age': 22, 'grade': 'C'}\n",
      "4 none\n"
     ]
    }
   ],
   "source": [
    "for each_key in students:\n",
    "  print(str(each_key), students[each_key])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "abf3ae25-c8f5-436f-aaa3-a2ec856362d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 {'name': 'John', 'age': 20, 'grade': 'A'}\n",
      "3 {'name': 'Bob', 'age': 22, 'grade': 'C'}\n",
      "4 none\n"
     ]
    }
   ],
   "source": [
    "for a, b in students.items():\n",
    "  print(a, b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "2c920eed-782a-4e7b-a74f-f4bf64a6ca87",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "John\n"
     ]
    }
   ],
   "source": [
    "student_list = [\n",
    "    {\n",
    "        'name': 'John',\n",
    "        'age': 20,\n",
    "        'grade': 'A'\n",
    "    },\n",
    "    {\n",
    "        'name': 'Jane',\n",
    "        'age': 21,\n",
    "        'grade': 'B'\n",
    "    },\n",
    "    {\n",
    "        'name': 'Bob',\n",
    "        'age': 22,\n",
    "        'grade': 'C'\n",
    "    },\n",
    "    {\n",
    "        'name': 'Alice',\n",
    "        'age': 23,\n",
    "        'grade': 'D'\n",
    "    }\n",
    "]\n",
    "print(student_list[0]['name'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "d2c980fb-74c8-41b2-b49d-598256ca6460",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'name': 'John', 'age': 20, 'grade': 'A'}, {'name': 'Jane', 'age': 21, 'grade': 'B'}, {'name': 'Bob', 'age': 22, 'grade': 'C'}, {'name': 'Alice', 'age': 23, 'grade': 'D'}, {'name': 'Eve', 'age': 24, 'grade': 'E'}]\n"
     ]
    }
   ],
   "source": [
    "new_dictionary = {\n",
    "    'name': 'Eve',\n",
    "    'age': 24,\n",
    "    'grade': 'E'\n",
    "}\n",
    "student_list.append(new_dictionary)\n",
    "print(student_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": "null",
   "id": "a78abf12-1754-4ea7-b4e4-dc2a917aed33",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
