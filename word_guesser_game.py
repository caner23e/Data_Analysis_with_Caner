import streamlit as st 
import random

words = ["lecture", "library", "seminar", "campus", "zurich"]
secret = random.choice(words)  
secret = "tram"
#guessed = "" => After each if statement when i click to write something the code starts from the beginning
#mistakes = 0 => THus we need to change this
#visible = " _ " * len(secret)  THis code would run evertime 
st.title("Welcome to the Word Guesser Game")

if "started" not in st.session_state: #This is only fun ONCE when i type somthing for the first time
    st.session_state.started = False  #I have to use st.session_state since if I only used "mistake" streamlit would compute mistake once and then delete it when it runs the code again, that why we store it outside 
    st.session_state.guessed = ""
    st.session_state.mistakes = 0
    start_button = False
    
    #st.session_state


start_button = st.button("click here to start the game")
if start_button:
    st.session_state.started = True
    #st.session_state = True THis is apperently wrong
    st.write("You can guess up to 6 letter, each time when you guess the right letter the letter will show up. You can guess up to max 6 wrong letter. GOOD LUCK")
    
#if st.session_state == True and mistakes <= 6: => THis code is wrong since i used state.started
 #   start_button = True
if st.session_state.started and st.session_state.mistakes < 6:
    letter = st.text_input("Guess a letter")
    if len(letter) >1:
        st.write("You can only guess one letter")
    if letter in st.session_state.guessed:
            st.write("You have already guessed this letter, try again")
    else: 
        if letter not in st.session_state.guessed:  #it was just "guess" before
            st.session_state.guessed = st.session_state.guessed + letter + " "  
        if letter not in secret:
            st.session_state.mistakes += 1 #it was just "mistake" before
    
visible = ""
for character in secret:
    if character in st.session_state.guessed:
        visible += character
    else:
        visible += "_" #THIS is like Bulls and Cows solution
    
with st.container(border=True):
    st.write("Your word: " , visible)
    st.write("Your guessed Letters:" + st.session_state.guessed)
    st.write("Mistakes count:", st.session_state.mistakes)


#    for character in secret:
#        if character in guessed:
#            # Add character to visible.
#            visible = visible + character
#                
#                
#        else:
#            # Add an underscore to visible.
#            visible = visible + "-"
#
#    print("Word:", visible)
#    print("Mistakes left:", 6 - mistakes)
#
if visible == secret:
       st.title("Congrats you have won")
if st.session_state.mistakes == 6:
    st.title("Sorry you have lost!")
    retry_button = st.button("Try again")
    if retry_button:
        del st.session_state.started
#
#if mistakes == 6:
#    print("The word was:", secret)o
