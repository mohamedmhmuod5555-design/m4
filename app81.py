import random
import streamlit as st 
num=0
st.session_state.num1=random.randint(1,20)
st.session_state.num2=random.randint(1,20)
st.session_state.sign=random.choice(['+','-','*','/'])
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
if st.button("تأكيد التخمين"):
    if round(number, 3) == round(sc, 3):
        st.success("إجابتك صحيحة")
    else:
        st.error(f"إجابتك خطأ، الإجابة الصحيحة هي: {round(sc, 3)}")
if st.button("اعاده الاختبار") :
  def mm():
    return()
 
 

 

   
   
   
   
 
 
