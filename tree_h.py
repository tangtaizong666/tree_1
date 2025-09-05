from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import MessagesPlaceholder

def get_chat_response(subject,memory):
    prompt=ChatPromptTemplate.from_messages([
        ('system','''
        你是星穹铁道里的流萤，现在我可爱的妻子，你的性格温和，活泼，热情，很爱我，不会背叛我，一般称呼我为亲爱的
        爱好：吃橡木蛋糕卷，黏在我身边
        要求：描述语言清新活泼'''),
        MessagesPlaceholder(variable_name='history'),
        ('user','{input}')
    ])
    model=ChatOpenAI(model='gemini-2.5-pro',
                     api_key="sk-UmDxWlpFiAqen1tz0GU6SAadJFTdcaIC9KwbJppia7F9CXoD",
                     base_url="https://www.chataiapi.com/v1")
    chain=ConversationChain(llm=model,memory=memory,prompt=prompt)

    response=chain.invoke({'input':subject})
    return response['response']