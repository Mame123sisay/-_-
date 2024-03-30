import json
from difflib import get_close_matches
from typing import Optional
from flask import Flask,redirect,render_template,request


app= Flask('chatbot')
app=Flask(__name__,template_folder='template')



def load_knowledge_base(file_path)->dict:
    with open(file_path,'r') as files:
        data=json.load(files)
        return data
    
    
def save_knowledge_base(file_path,data):
    with open(file_path,'w') as files:
        json.dump(data, files,indent=2)
        
def find_best_match(user_question,questions)->Optional[str] :
    matchs=get_close_matches(user_question,questions,n=1,cutoff=0.6) 
    return matchs[0] if matchs else None


def get_answer_for_question(question,knowledge_base)->Optional[str]:
     
    for q in knowledge_base['questions']:
        if q['question'] == question:
            
            return q['answer']
        
        
        
def chat_bot(user_query):
    knowledge_base=load_knowledge_base("knowledge_base.json")
   
    user_input=user_query.lower()
    if user_input== "quit":
        
        exit()
    '''for question in knowledge_base["questions"]:
        if question["question"].lower()==user_input:
            answer=question["answer"]
            return answer
        
    return" Bot: I don't know about "+  user_input'''
        
    best_match=find_best_match(user_input,[q["question"] for q in knowledge_base["questions"]])
    if best_match:
        answer=get_answer_for_question(best_match,knowledge_base)
        return answer
      
        
            
    else:
        
        return( 'Bot: I don\'t know the answer . ')
        '''new_answer=input("type the answer or 'skip' to skip :")
        if new_answer.lower() =='skip':
            
            exit()
        elif new_answer.lower() !='skip':
            knowledge_base["questions"].append({"question":user_input,"answer":new_answer})
            save_knowledge_base('knowledge_base.json',knowledge_base)
            return('Bot: Thank you!   I learned  a new response!!')'''
            
                
                
                
    
    

       
                
                



@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/query',methods=['POST'])

def get_query():
     user_query=request.form['query']
     prev_response = request.form.get('prev_response', '')
     prev_query = request.form.get('prev_query')
     response=chat_bot(user_query)
     if user_query=='yes':
         
       
        return('Bot: Thank you!   I learned  a new response!!')
         
    
     
     combined_query = prev_query + '<br><br>YOU: ' +user_query+'<br>' if prev_query else "You: " + user_query
     combined_response = prev_response + '<br><br>Bot: ' + response + '<br><br><br><br>' if prev_query else "Bot: " + response
     prev=response


     return render_template('index.html', query=combined_query,response=combined_response)
    
   
   
    
    
    
        
        
             
              
              

          
       
            
         
         
        
         
         
        
            
           
        
    
                
                
               
               
    
    

if __name__ == '__main__':
    app.run(debug=True)
            



