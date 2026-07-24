import random
import streamlit as st 
num=0
num1=random.randint(1,20)
num2=random.randint(1,20)
sign=random.choice(['+','-','*','/'])
if sign== '+':
  sc=num1+num2
if sign== '-':
  sc=num1-num2
if sign== '*':
  sc=num1*num2
if sign== '/':
  sc=num1/num2
st.title("أهلاً بك في لعبه الذكاء التابعه لمحمد رياض ")
st.write(num1,sign,num2)
number = st.number_input("أدخل الناتج", step=1.0)
if st.button("تأكيد التخمين "):
 if number==sc:
  st.success("اجابتك صحيحه  ")

if st.button("اعاده الاختبار") :
  def mm():
    return()
 
 

 

   
   
   
   
 
 
