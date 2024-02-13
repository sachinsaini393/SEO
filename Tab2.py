import os
import openai
openai.api_type = "azure"
openai.api_base = "https://seorevolution-gpt4.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "2acafeb8501f41e2a7f3cf3c5854287a"


def generate_keywords(reference1,reference2,reference3,Topic,Keyword):
    results1={}
    
    try:
        
        if "Similar Keywords" in Keyword:
            system = ''' 
        You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
        and catered to clients across all sectors.

        Instructions :
        You have to generate five Similar Keyword on given topic only.
        '''

            user_prompt=f'''

        Extract top five exact matched keywords only for this topic : {Topic} that are present in these three given article/blog post for SEO: {reference1},{reference2},{reference3}.
        
        '''  
            response_similar = openai.ChatCompletion.create(  
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
        
            #results1.append ("Similar Keywords:\n"+  response_similar.choices[0].message['content']  )
        results1["Similar Keywords"]=response_similar.choices[0].message['content'].strip()
    
    

        if "Long Tail Keywords" in Keyword:
            system = '''
        You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
        and catered to clients across all sectors.

        Instructions :
        You have to generate five Long Tail Keyword on given topic only.
        '''

            user_prompt=f'''

        Extract  top five long tail keywords only for this topic : {Topic} from these three given article/blog post for SEO: {reference1},{reference2},{reference3}.
        '''  
            response_long_tail = openai.ChatCompletion.create(  
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
            results1["Long Tail Keywords"]=response_long_tail.choices[0].message['content'].strip()
        #results1.append ("Long Tail Keywords :\n"+  response_long_tail.choices[0].message['content']  )
        
        
        if "Short Tail Keywords" in Keyword:
            system = '''
        You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
        and catered to clients across all sectors.

        Instructions :
        You have to generate five Short Tail Keyword on given topic only.
        '''

            user_prompt=f'''

        Extract top five Short Tail keywords only for this topic : {Topic} from these three given article/blog post for SEO: {reference1},{reference2},{reference3}.
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
            results1["Short Tail Keywords"]= response_short_tail.choices[0].message['content'].strip()
        #results1.append ("Short Tail Keywords :\n"+  response_short_tail.choices[0].message['content']  )
    

        if "Semantically Related Keywords" in Keyword:
            system = '''
        You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
        and catered to clients across all sectors.

        Instructions :
        You have to generate five Semantically Keyword on given topic only.
        '''

            user_prompt=f'''

        Extract top five Semantically keywords only for this topic : {Topic} from these three given article/blog post for SEO: {reference1},{reference2},{reference3}. 
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
            results1["Semantically Related Keywords"]=response_semantically.choices[0].message['content'].strip()
        #results1.append ("Semantically Related Keywords :\n"+  response_semantically.choices[0].message['content']  )

    #return results1["Similar Keyword"],results1["Long Tail Keyword"],results1["Short Tail Keyword"],results1["Semantically Related"]
    #return "\n\n".join(results1)
        return results1
    
    except Exception as exc:
        results1["Error"]=str(exc)
        return results1
    
        

 