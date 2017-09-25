cursus = {'student1':9.5,'student2':8.0,'student3':7.5,'student4':9.2,'student5':8.5,'student6':4.0,'student7':6.0,'student8':6.5}
for student,score in cursus.items():
    if score > 9.0:
        print(student,score)