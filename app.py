from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


keywords = {
    "hello": "Hey (ਹੈਲੋ)",
    "can you help me?": "Ki tusi meri madad kar sakde ho? (ਕੀ ਤੁਸੀਂ ਮੇਰੀ ਮਦਦ ਕਰ ਸਕਦੇ ਹੋ?)",
    "what is your name?": "Tuhada naam ki hai? (ਤੁਹਾਡਾ ਨਾਂ ਕੀ ਹੈ?)",
    "how are you?": "Tusi kiven ho? (ਤੁਸੀਂ ਕਿਵੇਂ ਹੋ?)",
    "i am learning Punjabi.": "Main Punjabi sikh reha haan. (ਮੈਂ ਪੰਜਾਬੀ ਸਿੱਖ ਰਿਹਾ ਹਾਂ)", 
    "it is raining today": "Aaj mihaan peh reha hai. (ਅੱਜ ਮੀਂਹ ਪੈ ਰਿਹਾ ਹੈ)",
    "i am very happy today": "Main aaj bahut khush haan! (ਮੈਂ ਅੱਜ ਬਹੁਤ ਖੁਸ਼ ਹਾਂ)",
    "where is the nearest bus stop?": "Sabh ton najdeek bus stop kithhe hai? (ਸਭ ਤੋਂ ਨੇੜਲੇ ਬੱਸ ਸਟਾਪ ਕਿੱਥੇ ਹਨ?)",
    "i want to go to Amritsar": "Main Amritsar jana chaunda haan. (ਮੈਂ ਅੰਮ੍ਰਿਤਸਰ ਜਾਣਾ ਚਾਹੁੰਦਾ ਹਾਂ)",  
    "how much does this cost?": "Is di keemat kinni hai? (ਇਹ ਦੀ ਕੀਮਤ ਕਿੰਨੀ ਹੈ?)",
    "goodbye": "Alvida (ਅਲਵਿਦਾ)",
    "thank you": "Dhanvaad (ਧੰਨਵਾਦ)"


} 



default_response = "Sorry, I don't know that sentance."


@app.route("/")
def home():
    return render_template("Home.html")





@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower().strip()
    if not user_input:
        return jsonify({"error": "Please enter a valid message."})
    
    reply = default_response
    for keyword in keywords:
        if keyword in user_input:
            reply = f"The meaning of {keyword} is {keywords[keyword]}."
            break

    return jsonify({"reply": reply})




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

