"""
"หากผู้เรียนกำลังศึกษาอยู่ในชั้นปีที่ 2 มหาวิทยาลัยชื่อดังย่านกลางเมืองที่ตอนนี้กำลังสอบเก็บคะแนนกันอย่างสนุกสนาน แล้ววันนึงได้รับมอบหมายจากอาจารย์ที่ปรึกษาให้พัฒนาโปรแกรมให้กับทางคณะ โดย ระบบดังกล่าวจะมีการเก็บคะแนนรายบุคคลของผู้เรียนแต่ละท่าน ของนักศึกษาชั้นปีที่ 2 เทอม 1" โดยมีรายชื่อวิชาดังนี้

Foundation English
General Business
Introduction to Computer Systems
Computer Programming


โดยให้ผู้เรียนพัฒนาโปรแกรมโดยสร้างตัวแปรสำหรับเก็บคะแนนผู้เรียนในรายวิชาดังกล่าว โดยคะแนนจะสามารถเป็นตัวเลขทศนิยมได้ และ เมื่อได้ตัวแปรมาแล้วให้ทำการแสดงผลออกมาให้ผู้ใช้งานได้เห็นในรูปแบบ

--- Your Score ---

Foundation English : คะแนนที่ได้

General Business : คะแนนที่ได้

Introduction to Computer Systems : คะแนนที่ได้

Computer Programming : คะแนนที่ได้

*การตั้งชื่อตัวแปรควรสื่อความหมาย ผู้อ่าน หรือ นักพัฒนาโปรแกรมท่านอื่นสามารถอ่านเข้าใจได้
"""

foundation_english_scores = float(input("Enter your Foundation English score: "))
general_business_scores = float(input("Enter your General Business score: "))
introduction_to_computer_systems_scores = float(input("Enter your Introduction to Computer Systems score: "))
computer_programming_scores = float(input("Enter your Computer Programming score: "))

print("--- Your score ---")
print("Foundation English:", foundation_english_scores)
print("General Business:", general_business_scores)
print("Introduction to Computer Systems:", introduction_to_computer_systems_scores)
print("Computer Programming:", computer_programming_scores)
