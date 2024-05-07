import os
import openai
import json
openai.api_type = os.getenv("api_type")
openai.api_base = os.getenv("api_base")
openai.api_version = os.getenv("api_version")
openai.api_key = os.getenv("api_key")


############################################# SEO Agent Persona ######################################
persona= '''You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
        and catered to clients across all sectors.
'''


############################################## Similar Keywords ###################################
def similar_k(ref1,ref2,ref3,t):
    system = f''' {persona}\n
        Instructions :
        You have to generate five Similar Keyword on given topic only.
        '''

    user_prompt=f'''

        Extract top five exact matched keywords only for this topic : {t} that are present in these three given article/blog post for SEO: {ref1},{ref2},{ref3}.
        
        '''  
    response_similar = openai.ChatCompletion.create(  
        engine="AIKillsSEO",  
        messages=[{"role":"system","content":system},
        {"role":"user","content":user_prompt}],  
        temperature=0.8,  
        max_tokens=3000,  
        top_p=1,  
        frequency_penalty=0,  
        presence_penalty=0,  
        stop=["#", ";"]  
        )
        
    result=response_similar.choices[0].message['content'].strip()
    return result
    
 
 ############################################# Long Tail Keywords ################################
 
def long_tail(ref1,ref2,ref3,t):
    system = f'''{persona}\n
        Instructions :
        You have to generate five Long Tail Keyword on given topic only.
        '''

    user_prompt=f'''

        Extract top five long tail keywords only for this topic : {t} from these three given article/blog post for SEO: {ref1},{ref2},{ref3}.
        '''  
    response_long_tail = openai.ChatCompletion.create(  
        engine="AIKillsSEO",  
        messages=[{"role":"system","content":system},
        {"role":"user","content":user_prompt}],  
        temperature=0.8,  
        max_tokens=3000,  
        top_p=1,  
        frequency_penalty=0,  
        presence_penalty=0,  
        stop=["#", ";"]  
        )
    results= response_long_tail.choices[0].message['content'].strip()
    return results
 
 
 ########################################### Short Tail Keywords ####################################
 
 
def short_t(ref1,ref2,ref3,t):
    system = f'''{persona}\n
            Instructions :
        You have to generate five Short Tail Keyword on given topic only.
        '''

    user_prompt=f'''

        Extract top five Short Tail keywords only for this topic : {t} from these three given article/blog post for SEO: {ref1},{ref2},{ref3}.
        '''  
    response_short_tail = openai.ChatCompletion.create(  
        engine="AIKillsSEO",  # Use an actual engine  
        messages=[{"role":"system","content":system},
        {"role":"user","content":user_prompt}],  
        temperature=0.8,  
        max_tokens=3000,  
        top_p=1,  
        frequency_penalty=0,  
        presence_penalty=0,  
        stop=["#", ";"]  
        )
    result= response_short_tail.choices[0].message['content'].strip()
    return result
     


############################################## Semantically Related Keywords ############################

def semant_k(ref1,ref2,ref3,t):
    system = f'''{persona}\n
        Instructions :
        You have to generate five Semantically Keyword on given topic only.
        '''
    user_prompt=f'''

        Extract top five Semantically keywords only for this topic : {t} from these three given article/blog post for SEO: {ref1},{ref2},{ref3}. 
        '''  
    response_semantically = openai.ChatCompletion.create(  
        engine="AIKillsSEO",  # Use an actual engine  
        messages=[{"role":"system","content":system},
        {"role":"user","content":user_prompt}],  
        temperature=0.8,  
        max_tokens=3000,  
        top_p=1,  
        frequency_penalty=0,  
        presence_penalty=0,  
        stop=["#", ";"]  
        )
    results=response_semantically.choices[0].message['content'].strip()
    return results
    
######################################################### Checking which functions should be executed according to keywords choice #####################################  
    
def generate_keywords(reference1,reference2,reference3,Topic,Keyword):
    results1={}
    
    try:
        
        
        if "Similar Keywords" in Keyword:
            results1["Similar Keywords"]=similar_k(reference1,reference2,reference3,Topic)
            
        if "Long Tail Keywords" in Keyword:
            results1["Long Tail Keywords"]=long_tail(reference1,reference2,reference3,Topic)
        
        if "Short Tail Keywords" in Keyword:
            results1["Short Tail Keywords"]= short_t(reference1,reference2,reference3,Topic)
        
        if "Semantically Related Keywords" in Keyword:
            results1["Semantically Related Keywords"]= semant_k(reference1,reference2,reference3,Topic)
        
        return results1


####################################### If any function fails then saving the error as exception ################################ 
    except Exception as exc:
        results1["Error"]=str(exc)
        return results1
    
        

 
