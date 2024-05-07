import os
import openai
openai.api_type = os.getenv("api_type")
openai.api_base = os.getenv("api_base")
openai.api_version = os.getenv("api_version")
openai.api_key = os.getenv("api_key")

############# weekly tech blog format ##################
tech_format=''' 
##Given Title

##Blog Subtitle
   
##Headshot of Digitally Cognizant author Tech to Watch
##Tech to Watch Blog

##Visit our [Relevant Webpage Here]

##In the news
   Detailed content discussing the blog .

 
##The Cognizant take
   Insights, opinions, and expert analysis related to the blog topic, given by a representative from Cognizant.
    [Additional paragraphs as needed]
    
##Digital Business & Technology , [Relevant tags and keywords here]

'''

####################### Tech style guide ###############
tech_style='''Unified Style Guide:

1. Voice and Tone: 
Adopt a formal yet accessible tone. The narrative voice should be authoritative and knowledgeable, striking a balance between being informative and conversational. Your objective should be to educate the reader, with a confident tone that demonstrates your command over the subject.

2. Mood: 
The mood should strike a balance between realism and optimism. While exploring possibilities and showing enthusiasm for the future, also acknowledge existing challenges. This should create an atmosphere of anticipation coupled with pragmatism.

3. Sentence Structure: 
Primarily use complex and compound sentences. Your sentences should be rich, often tackling multiple ideas or points of information, but should not deter from clarity. Employ parenthetical phrases for additional context or explanations, and use relative clauses to provide more information on the subject.

4. Transition Style: 
Seamlessly transition from one idea to the next using a variety of styles. Use logical transition words like 'moreover', 'however', 'and', and delve deeper into the topic for a gradual reveal of details.

5. Rhythm and Pacing: 
Maintain a moderate pace, with a rhythm driven by a balance of long, descriptive sentences and short, conclusive statements. Layer your information, starting broadly and gradually narrowing down to specifics.

6. Signature Styles: 
Frequently employ technical terms relevant to the topic, reflecting your expertise and deep understanding. Use direct quotes from experts to lend credibility. Provide balanced views by highlighting both promising prospects and potential challenges. Engage the reader with rhetorical questions, stimulating thought and encouraging active participation in the topic.

7. Stylistic Nuances: 
Your distinct writing style should be characterized by expert references, a balance of factual and emotive language, and strategic use of rhetorical questions. Use metaphors and analogies to explain complex concepts, making the text more relatable and easier to understand.

In summary, to maintain the original style, the writing should be authoritative yet accessible, optimistic yet realistic. It should be dense with information and insights, employing complex sentences, smooth transitions, and direct reader address. It should engage the audience by posing and answering questions, referencing expert opinions, and balancing facts with emotional language.
'''





#################### descriptive style guide ######################

descriptive_style='''Style Guide:

1. Voice and Tone: The language used in the text should be formal, authoritative, informative, and slightly conversational, demonstrating a high level of expertise in the subject matter. The tone should be professional and approachable, yet not overly technical, aimed at an educated, technologically aware audience. The use of specific tech-related terminology is encouraged but should be balanced with accessible language to ensure the content is comprehensible to a broader audience.

2. Mood: The overall mood of the text should be optimistic, explorative, investigative, and inquisitive. The content should delve into the potential of the topic, highlighting both the opportunities and challenges, maintaining a hopeful, curious, and forward-looking atmosphere.

3. Sentence Structure: The text should utilize a mix of simple, compound, and complex sentences. While the length may vary, a majority of sentences should be medium to long, offering detailed information, explanations, and implications of the discussed topic. The active voice is preferred.

4. Transition Style: The writer should transition smoothly between ideas using a logical progression of thought. Employ phrases like "Moreover", "However", "By contrast", "Nevertheless", "But the challenges are as clear as the potential" and rhetorical questions to navigate from one idea to another. The use of conjunctions, adverbs, and ellipsis ("…") are also encouraged to bridge two separate ideas or sections.

5. Rhythm and Pacing: The rhythm of the text should be steady, neither too fast nor slow. The pacing should be deliberate, providing enough information for the reader to understand the complexities of the topic without overwhelming them. Longer sentences can be used to provide in-depth information and provoke thought, while shorter sentences should serve to punctuate key points and maintain reader interest.

6. Signature Styles: The use of expert quotes should be a standout feature, lending credibility and depth to the article. The author should frequently address the reader directly, fostering a sense of dialogue and engagement. Repetition can be used effectively to underscore important points. The author should consistently use specific, tangible examples to illustrate abstract concepts. The use of speculative phrases like "Imagine if" and parenthetical clauses for additional information or context are also encouraged.

7. Distinctive Elements: The ability to present both sides of an argument or discussion, the consistent use of expert quotes, and the use of tangible examples to illustrate abstract concepts should be distinctive elements in the author's style. The language should strike a balance between professional and accessible, ensuring both complexity and readability. Thought-provoking questions, colloquial similes, and the dash (—) should be used for providing context or clarification.
'''

def gpt4(prompt,persona=None):
    if persona is None:
        messages=[
                {"role": "user", "content": prompt}
            ]
    else:
        messages=[
                {"role": "system", "content": persona},
                {"role": "user", "content": prompt}
            ]
    response = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=messages,
            temperature=0.8,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
    result=response.choices[0].message['content'].strip()
    return result

############# Weekly Tech Blog Generation #######################
def article_style_guide(r1,r2,r3,format_blog,style,Title,finalized_keyword):
    system2=f'''
        You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
        and catered to clients across all sectors.
        '''
        
    user_prompt2 = f'''Write a painfully detailed blog post in approximately 1000 words using these three reference content \n\n 1:{r1}\n\n2:{r2}\n\n3:{r3} and this style guide: \n {style} only \n on this Title: {Title} and optimize it for these following keywords : {finalized_keyword} for SEO.
    Note:
        - You have to strictly use this format :{format_blog} while writting new blog post.
        - Refer to the detailed style guide provided previously to ensure a consistent and professional voice throughout the article.
        - Don't write any conclusion. Just stick to given format only.
        - 
    '''
    response = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system2},
                {"role": "user", "content": user_prompt2}
            ],
            temperature=0.8,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
    result=response.choices[0].message['content']  
    
    return result
###################### Weekly Tech Blog ###############
def descriptive_blog(Title,finalized_keyword):
    
    user_prompt = f''' Write table content consisting of 3 sections only for this title : {Title}.
This table of content will be used for writting a article in 2000-3000 words.
Note:
    1.Give Table of Content only.
    2. Don't give any reference or conclusion section and about authors.
    3. Start all headings and subhedings with double '##'only.
    Example: ## Heading1
    ## Subheading1
    ## Subheading1.2
    4. Each section will contains only 2-3 points only.
    '''
    
    tocc=gpt4(user_prompt)
    aa=tocc.split('\n')
    filtered_list = [i for i in aa if i]
    # Verifications and content for each point in the table of contents
    verifications = []
    for point in filtered_list:
    # Generate verification
        prompt_ver = f'''Generate only one verification question for this: {point} using this title :'GenAI in High Tech: Transforming Quality Assurance & Business Process Outsourcing'
                Note : These questions will be used to write a blog post.'''
        response2 = gpt4(prompt_ver)
        verifications.append(response2)
    
    contents=[]
    for question in verifications :
        prompt_con = f'''Using this style guide :\n{descriptive_style}\nAnswer the following question in 200-300 words only :\n {question} .
    Note :
    1.The answer will be used for writting a comprehensive descriptive blog post.
    2. Don't give any conclusion but you can give case studies if required.

    '''
        response_con = gpt4(prompt_con)
        contents.append(response_con)
    
    
    
    optimized_answer=[]
    for index,questions in enumerate(verifications):
        prompt_opt = f'''Using this style guide :\n{descriptive_style}\n  Optimize the Answer of given question for these following keywords only: {finalized_keyword} for SEO.
    Question : {questions}
    Answer  : {contents[index]}
    Note :
    1.The answer will be used for writting a comprehensive descriptive blog post.
    2. Don't give any conclusion but you can give case studies if required.
    3. Write in 2 paragraphs only.
    4. You will use exact given keywords only.
    '''
        response_opt = gpt4(prompt_opt)
        optimized_answer.append(response_opt)
    # Print final formatted article
    article=[]
    for i in range(len(filtered_list)):
        article.append(f"{filtered_list[i]}\n{optimized_answer[i]}\n")
    final_article='\n'.join(article)
    return final_article
    
    
######################## Glossary ######################
def glossary(Topic,keyword):
    
    system = '''

        You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
            and catered to clients across all sectors.
            
        '''
    user_prompt = f'Generate 5 FAQs on {Topic} and optimize it for {keyword} for SEO. Explain FAQs in 100-150 words.'
    response = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=3000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
           
    result=response.choices[0].message['content']
    return result


##################################################

def content(ref1,ref2,ref3,topic,title,keywords,style):
    results={}
    try:
        if "Weekly Tech Blog" in style:
            results["Weekly Tech Blog"]=article_style_guide(ref1,ref2,ref3,tech_format,tech_style,title,keywords)
        if "Descriptive Blog" in style:
            results["Descriptive Blog"]=descriptive_blog(title,keywords)                                   
        if "Glossary" in style:
            results["Glossary"]=glossary(topic,keywords)
        
        return results
    except Exception as exc:
        results["Error"]=str(exc)
        return results
