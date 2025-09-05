import streamlit as st
from tree_h import get_chat_response
from langchain.memory import ConversationBufferMemory



st.image('img.png',width=300)
#标题
st.header('桦树皮画小助手🗒️')


#初始化memory和messages
if 'memory' not in st.session_state:
    st.session_state['memory']=ConversationBufferMemory(return_messages=True)

    st.session_state['messages']=[{'role':'ai','content':'hi朋友，想走进桦树皮画的世界吗🌞'}]

#st.chat_message(role).write(content)，streamlit的聊天样式组件，根据role显示不同的聊天气泡
#这里遍历所有的消息并渲染到页面上，让用户可以看到之前的消息
for message in st.session_state['messages']:
    if message['role']=='ai':
        avatar='🌲'
    else:
        avatar='🎃'
    # st.chat_message(message['role']).write(message['content'])
    # with st.chat_message(message['role'],avatar=avatar):


    with st.chat_message(message['role'], avatar=avatar):
        st.write(message['content'])
    #     st.write(message['content'])
subject=st.chat_input()
if subject:
    #保存用户消息到历史消息储存，并打印
    st.session_state['messages'].append({'role':'human','content':subject})
    st.chat_message('human',avatar='🎃').write(subject)

    with st.spinner('AI正在努力思考，清稍等...'):
        response=get_chat_response(subject,st.session_state['memory'])
        msg={'role':'ai','content':response}
        #保存ai回复的消息到历史消息并打印
        st.session_state['messages'].append(msg)
        st.chat_message('ai',avatar='🌲').write(response)