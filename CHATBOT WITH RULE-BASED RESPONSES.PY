data={
  "Hii":"Hello! My day is going great!! How about yours?",
 "Whats your name":"Im MECHDROID AI BOT! Whats your name?",
 "My name is Sree":"What a beautiful name!!  How may I assist you today?",
  "What do you do to relax?":"To relax  probably enjoy listening to some calming music or maybe watching a good show. watch a feel-good series or listening to nature sounds helps people unwind.",
 "Any Movie suggestions":"Yeh Jawaani Hai Deewani, Wake Up Sid, Zindagi Na Milegi Dobara, Ee Nagaraniki Emaindi, MAD, Pelli Choopulu, Dear Zindagi.",
  "Where are these movies available":"Netflix ",
 "Any Songs suggestions":"Tum Hi Ho (Aashiqui 2),Kabira (Yeh Jawaani Hai Deewani),Naatu Naatu (RRR), Butta Bomma (Ala Vaikunthapurramuloo), Tujh Mein Rab Dikhta Hai (Rab Ne Bana Di Jodi.)",
  "Where are these songs available":"Spotify",
  "Any Thriller Book suggestions": "You might love *The Silent Patient* by Alex Michaelides, *Verity* by Colleen Hoover, *The Housemaid* by Frieda McFadden, or the *A Good Girl's Guide to Murder* series by Holly Jackson (all books in the series).",
  "Where can I find these Thriller books?": "These books are available on Amazon, Flipkart, or your local bookstores.",
  "Any Thriller Podcasts suggestions": "For thriller fans, try *My Favorite Murder*, *Serial*, or *Criminal* for real-life thrillers. If you like comedy, *Conan O'Brien Needs a Friend* is a great choice.",
  "Where are these Thriller podcasts available?": "You can listen to these podcasts on Spotify, Apple Podcasts, or Google Podcasts.",
 "Any Rom-Com Book suggestions": "If you're into romantic comedies, you might enjoy *The Rosie Project* by Graeme Simsion, *To All the Boys I've Loved Before* by Jenny Han, *The Hating Game* by Sally Thorne, *Beach Read* by Emily Henry, or *Red, White & Royal Blue* by Casey McQuiston.",
  "Where can I find these rom-com books?": "These rom-com books are available on Amazon, Flipkart, or your local bookstores.",
  "Any Rom-Com Podcasts suggestions": "For romantic comedy lovers, check out *Romance University Podcast*, *The Popcast*, *Call Your Girlfriend*, or *Dating Straight* for fun rom-com discussions.",
  "Where are these rom-com podcasts available?": "You can listen to these rom-com podcasts on Spotify, Apple Podcasts, or Google Podcasts.",
  "Thankyou":"You're welcome! Enjoy",
 "Bye":"Bye! Take care and have a great day!",
 
}
def get_response(user_input):
    for pattern, response in data.items():
        if pattern in user_input:
            return response
    return "I'm sorry, I didn't understand that. "

print("Chatbot: Hi! I'm  MECHDROID AI BOT, I'm happy to assist you!")

while True:
    user_input = input("Me: ")
    if user_input == "Bye":
        print("Chatbot: Goodbye! Have a great day 🙋😊!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)