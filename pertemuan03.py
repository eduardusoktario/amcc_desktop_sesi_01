#LIST
# # #ini membuat list yang kosong
# # list1 = []
# # print(list1)

# # list2 = ["Oktario","Salsabila","Yanuar"]
# # print(list2)

# # list3 = [[1,2,3,4,5], 100, "Oktario"]
# # print(list3)
# #bacanya  0,1,2,3,4,5,6,7,8,9
# list4 = [1,2,3,4,5,6,7,8,9,10]
# # print("Hasil dari print(list4[2]) = ", list4[2])
# # print("Hasil dari negatif indeks [-3] =", list4[-3])
# # print("Range indeks 1:6 = ", list4[1:6])

# #mengubah data pada list
# print(list4)
# list4[9] = "Oktario"
# print(list4)

# #menghapus data pada list
# del list4[8]
# print(list4)
# #menghapus list secara keseluruhan
# list4.clear()
# print(list4)

# #menambah data pada list
# list4.append("Desktop")
# print(list4)
# #menambah banyak data pada list
# list4.extend(["Programming","AMCC","2020/2021"])
# print(list4)

#TUPLE
# tuple1 = (1,)
# print(tuple1)

# tuple2 = (1,2,3)
# print(tuple2)

# tuple3 = ("hello",[1,2,3])
# print(tuple3)

# tuple4 = 1,2,3
# a,b,c = tuple4
# print(a,b,c)

# my_tuple = ('Hallo beb')
# print(my_tuple[1])
# print(my_tuple[-1])
# print(my_tuple[:5])
# print(my_tuple[5:])
# print(my_tuple[2:5])

# tuple5 = (1,2,3,[6,5])
# print(tuple5)

# tuple5[3][0] = 4
# print(tuple5)

# del tuple5
# print(tuple5)

# tuple6 = ('Hai sayang')
# print(tuple6.count('a'))
# print(tuple6.index('y'))

#SET
# set1 = {1,2,3,4,5}
# print(set1)

# list2 = ['a','b','c','d']
# list3 = [1,2,3,4,5]
# set2 = set(list2)
# set3 = set(list3)
# print(set2)
# print(set3)

# set4 = {100,200,300,400,500}
# print(set4)

# #penambahan data tunggal
# set4.add(600)
# print(set4)

# #penambahan banyak data
# set4.update([700,800,900])
# print(set4)

# #menghapus keseluruhan set
# set4.clear()
# print(set4)

# #operasi himpunan matematika
# set4 = {10,20,30,40,50}
# set5 = {50,60,70,80,90}

# print(set4 | set5)
# print(set5.union(set4))

#DICTIONARY
# dict1 = {"yk":"Yogyakarta","jkt":"Jakarta"}
# print("Hai, namaku Rio aku asalnya ", dict1["yk"])
# print("Hai, namaku Okta aku asalnya ", dict1.get("jkt"))

# #tambah dictionary
# dict1["mgl"] = "Magelang"
# print(dict1)

# #ganti value dict
# dict1["mgl"] = "Magetan"
# print(dict1)

# del dict1["mgl"]
# print(dict1)
# dict1["mgl"].clear()
# print(dict1)

list1=[1,2,3]

list1.append(4)
print(list1)
list1.extend([5,6,7])
print(list1)