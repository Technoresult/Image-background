import streamlit as st
from rembg import remove
from PIL import Image
import numpy as np
import io

def main():
    st.title("Image Background Remover")
    st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        
        st.write("")
        st.write("Removing background...")
        
        with st.spinner('Processing...'):
            input_image = np.array(image)
            output_image = remove(input_image)
            output_image = Image.fromarray(output_image)
            
            st.image(output_image, caption='Background Removed.', use_column_width=True)
            
            buf = io.BytesIO()
            output_image.save(buf, format="PNG")
            byte_im = buf.getvalue()
            
            st.download_button(label="Download Image", data=byte_im, file_name="output.png", mime="image/png")

if __name__ == '__main__':
    main()
