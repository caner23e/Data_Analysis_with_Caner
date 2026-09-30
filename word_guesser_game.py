import streamlit as st 
import random
words = ["lecture", "library", "seminar", "campus", "zurich"]
secret = random.choice(words)  
secret = "tram"
guessed = ""
mistakes = 0
visible = " _ " * len(secret)  

st.title("Welcome to the Word Guesser Game")


start_button = st.button("click here to start the game")
if start_button:
    st.session_state = True
    st.write("You can guess up to 6 letter, each time when you guess the right letter the letter will show up. You can guess up to max 6 wrong letter. GOOD LUCK")
    
if st.session_state == True and mistakes <= 6:
    start_button = True
    letter = st.text_input("Guess a letter")
    if letter not in guessed: 
        guessed = guessed + letter + " "  
    if letter not in secret:
        mistakes += 1
    
with st.container(border=True):
    st.write("Your word: " , visible)
    st.write("Your guessed Letters:" + guessed)
    st.write("Mistakes count:", mistakes)

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
#    if visible == secret:
#        print("Congrats you have won")
#        break
#
#if mistakes == 6:
#    print("The word was:", secret)
