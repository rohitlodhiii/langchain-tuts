from flask import Flask , render_template , jsonify , request
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
app = Flask(__name__)

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate" , methods = ['GET' , 'POST'])
def generate():
    if request.method == 'POST':
        prompt = PromptTemplate.from_template("Write a blog on title {title}")
        llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3 ,google_api_key=api_key)
        chain = prompt | llm 
        mains = request.json.get('prompt')
        output = chain.invoke(mains).content
        return output




app.run(host = '0.0.0.0' , port=81)