import os
import openai
import json

openai.api_type = os.getenv("api_type")
openai.api_base = os.getenv("api_base")
openai.api_version = os.getenv("api_version")
openai.api_key = os.getenv("api_key")

persona='''
You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
and catered to clients across all sectors.
'''

def content_generation(r1,r2,r3,Topic, finalized_keyword, content_type):
    results = {}
    try:
        
        
    #results=[]
    
        if 'Title' in content_type:
            system = f'''{persona}\n
        Instruction : You have to strictly generate only one title.
        
        '''
            user_prompt_title = f'Write one descriptive title for the topic {Topic} and optimize it for keywords {finalized_keyword} with character limit of 50-60 characters.'
            response_title = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_prompt_title}
            ],
            temperature=0.8,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
            r_title=response_title.choices[0].message['content'].strip()
            results['Title'] =r_title 
        #results.append(r_title)
        
        
        
        if "Meta Description" in content_type:
            system = f'''{persona}\n
        Instructions: You have to strictly generate only one meta description.
        
        '''
            user_prompt_meta = f'Write one descriptive Meta Description for the topic {Topic} and optimize it for keywords {finalized_keyword} with character limit of 150 -160 characters.'
            response_meta = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_prompt_meta}
            ],
            temperature=0.8,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
            r_meta=response_meta.choices[0].message['content'].strip()
            results["Meta Description"] = r_meta
        #results.append(r_meta)
        
    
    
        if "Image Prompt" in content_type:
            system = f'''{persona}'''
            user_prompt = f'''Generate 5 ideas only for images with ALT text that can be added on blog post for the topic : {Topic} And optimize it for the keyword : {finalized_keyword} for SEO.
            Give output in JSON format only with key name as Idea , Idea Description and ALT text.
            Example: "{\n\"Idea 1\": {\n    \"Idea Description\": \"Image showcasing the clean streets of Indore, highlighting its cleanliness.\",\n    \"ALT text\": \"Clean streets of Indore reflecting Indore as one of India's cleanest cities\"\n},\n\"Idea 2\": {\n    \"Idea Description\": \"Photo collage of various sanitation activities like street sweeping, waste collection in Surat.\",\n    \"ALT text\": \"Sanitation activities in Surat, showcasing Surat as one of India's cleanest cities\"\n},\n\"Idea 3\": {\n    \"Idea Description\": \"Infographic depicting the transformation of Indore and Surat into clean cities due to IT infrastructure services.\",\n    \"ALT text\": \"Indore and Surat transformation into cleanest cities in India due to IT infrastructure services\"\n},\n\"Idea 4\": {\n    \"Idea Description\": \"Side by side images of Indore and Surat showcasing their clean public spaces like parks, markets, etc.\",\n    \"ALT text\": \"Public spaces of Indore and Surat reflecting their status as India's cleanest cities\"\n},\n\"Idea 5\": {\n    \"Idea Description\": \"Image of a computer screen showing data analytics related to the cleanliness index of Indore and Surat.\",\n    \"ALT text\": \"Data analytics showcasing Indore and Surat as India's cleanest cities\"\n}\n}"
            
            '''
        #Give me a table with column names as Idea, Idea Description and ALT text.
              
            
            response_alt = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
            r_alt=response_alt.choices[0].message['content'].strip()
            results["Image Prompt"] = r_alt
        #results.append(r_alt)
        
    
    
    
    #return {results["Title"], results["Meta Description"], results["Alt Text"]}
    #final_results=json.dumps(results)
        return results
    
    except Exception as exe:
        results["Error"]=str(exe)
        return results

