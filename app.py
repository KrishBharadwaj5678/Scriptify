from PIL import Image,ImageDraw,ImageFont
import os
import streamlit as st
import textwrap

st.set_page_config(
    page_title="Scriptify",
    page_icon="icon.png",
    menu_items={
        "About":"Unleash the charm of handwritten text with Scriptify! Instantly convert your typed words into beautiful handwriting. Dive into the art of script and make your text stand out with Scriptify's customizable styles and seamless experience. Try it now and add a unique, personal touch to your digital text!"
    }
)

st.write("<h2 style='color:lightgreen;'>Transform Your Text into Handwriting.</h2>",unsafe_allow_html=True)

colors = ["black","white","red","green","blue","yellow","cyan","magenta","gray","lightgray","darkgray","brown","purple","orange","pink","lime","teal","navy","maroon","olive","silver","gold"]

setfontfamily={
    'Aileron Regular':'Aileron-Regular.otf',
    'Aileron Italic':'Aileron-Italic.otf',
    'Aileron Bold':'Aileron-Bold.otf',
    'Acme Regular':'Acme-Regular.ttf',
    'ArimaKoshi Regular':'ArimaKoshi-Regular.otf',
    'Driscutty Signature':'Driscutty_Signature.otf',
    'Workforce Sans':'WorkforceSans.otf',
    'Scratchy Lemon':'Scratchy_Lemon.otf'
}

for i in setfontfamily:
    allfonts=setfontfamily.keys()

fontfamily=st.selectbox("Choose Font",allfonts)

fontsize=st.number_input("Set Font Size",min_value=1,value=20)

font_color=st.selectbox("Choose Font Color",colors,key=1)

back_color=st.selectbox("Choose Background Color",colors,key=2,index=1)

spaceleft=st.radio("Include Left and Top Margins?",['Yes','No'],index=1)

checklineheight=st.radio("Adjust Line Spacing?",['Yes','No'],index=1)
if checklineheight=='Yes':
    line_height=st.number_input("Set Line Height",min_value=1,max_value=40)

alignment=st.selectbox("Choose Alignment",["Left","Center","Right"])

stroke=st.radio("Enable Stroke?",['Yes','No'],index=1)
if stroke=='Yes':
    stroke_width=st.number_input("Set Stroke Width",min_value=1,max_value=5)
    stroke_color=st.selectbox("Set Stroke Color",colors)

text=st.text_area("Enter Text for Handwritten Display")

textWidth=st.number_input("Specify Text Width",min_value=1,value=100)

btn=st.button("Create")
if btn:
    if(len(text)==0):
        st.warning('Text field cannot be empty.')
    else:
        img=Image.new("RGB",(2350,1100),back_color)
        draw=ImageDraw.Draw(img)

        font_name=f'{setfontfamily[fontfamily]}'
        fontPath =os.path.join(os.getcwd(), "fonts", font_name)
        font=ImageFont.truetype(fontPath,fontsize)

        if(spaceleft=='Yes'):
            position=(50,50)
        else:
            position=(0,0)

        if(checklineheight=='Yes'):
            pass
        else:
            line_height=1

        wrapped_text = textwrap.fill(text, textWidth)
        
        if stroke=='Yes':
            pass
        else:
            stroke_width=0
            stroke_color=None

        draw.text(    
            text=wrapped_text,
            xy=position,
            font=font,
            fill=font_color,              
            spacing=line_height,                 
            align=alignment.lower(),              
            stroke_width=stroke_width,          
            stroke_fill=stroke_color
        )  

        img.save("handwriting.png")
        with open("handwriting.png","rb") as img:
            st.download_button("Download",img.read(),'handwriting.png')
        st.image('handwriting.png')
