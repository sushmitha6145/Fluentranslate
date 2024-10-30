import streamlit as st
def get_method_code(method_name):
    if method_name == "translate_text_with_google":
        return '''
        def translate_text_with_google(text, target_language):
            google_translator = GoogleTranslator()
            max_chunk_length = 500
            translated_text = ""
            for i in range(0, len(text), max_chunk_length):
                chunk = text[i:i + max_chunk_length]
                translated_chunk = google_translator.translate(chunk, dest=target_language).text
                translated_text += translated_chunk
            return translated_text
        '''
    elif method_name == "convert_text_to_speech":
        return '''
        def convert_text_to_speech(text, output_file, language='en'):
            if text:
                supported_languages = list(language_mapping.keys())
                if language not in supported_languages:
                    st.warning(f"Unsupported language: {language}")
                    return
                tts = gTTS(text=text, lang=language)
                tts.save(output_file)
        '''
    elif method_name == "get_binary_file_downloader_html":
        return '''
        def get_binary_file_downloader_html(link_text, file_path, file_format):
            with open(file_path, 'rb') as f:
                file_data = f.read()
            b64_file = base64.b64encode(file_data).decode()
            download_link = f'<a href="data:{file_format};base64,{b64_file}" download="{os.path.basename(file_path)}">{link_text}</a>'
            return download_link
        '''
    elif method_name == "convert_text_to_word_doc":
        return '''
        def convert_text_to_word_doc(text, output_file):
            doc = Document()
            doc.add_paragraph(text)
            doc.save(output_file)
        '''



def display_method_info(method_info):
    st.header("Method Functionality")
    for method_name, details in method_info.items():
        st.subheader(method_name)
        for key, value in details.items():
            st.text(f"{key}: {value}")
        st.text("\n")

def display_method_code(method_names):
    st.header("code of the method")
    for method_name in method_names:
        method_code = get_method_code(method_name)
        st.code(method_code, language='python')


def display_method_info():
    st.header("Method Functionality")

    method_info = {
        "convert_text_to_speech": {
            "Functionality": "Converts text to speech (MP3 format).",
            "Parameters": "text (text to convert), output_file (output file path), language (language code for speech synthesis)",
            "Output": "MP3 audio file with the generated speech"
        },
        "get_binary_file_downloader_html": {
            "Functionality": "Generates a download link for a file.",
            "Parameters": "link_text (text for the download link), file_path (file path), file_format (file format)",
            "Output": "HTML download link for the file"
        },
        "convert_text_to_word_doc": {
            "Functionality": "Converts translated text to a Word document.",
            "Parameters": "text (translated text to convert), output_file (output file path)",
            "Output": "Word document containing the translated text"
        },
         "translate_text_with_google": {
            "Functionality": "Translates text using Google Translate.",
            "Parameters": "text (text to translate), target_language (language code for translation)",
            "Output": "Translated text"
        }
    }

    for method_name, details in method_info.items():
        st.subheader(method_name)
        for key, value in details.items():
            st.text(f"{key}: {value}")
        st.text("\n")

def main():
    # Split the page into two columns
    st.title("About the Application")
    project_description = '''
"Imagine a tool that effortlessly translates text, speaks in multiple languages,
and transforms documents into speech—all at your fingertips! Our Streamlit-powered app
is a language wizard: upload DOCX, PDFs to extract and edit text.
Not only does it translate text using Google's magic, but it also converts it into
spoken words with stunning accuracy. Whether you're editing uploaded files or
directly entering text, our app's got you covered—word counts, language selection,
and flawless audio generation. Experience the future of text transformation with our intuitive,
multilingual, and vibrant app—your go-to for seamless translation and speech conversion."
'''
    st.markdown(project_description, unsafe_allow_html=True)
    
    '''---'''
    st.header("How to Use :")

    project_description1 = '''
    ---
    
    To use the our Streamlit app, follow these steps:
    
    ### Page 1: Document and PDF Translation
    1. **Upload a File**:
       - Use the file uploader to upload a DOCX or PDF. The uploaded file should contain text that you want to translate and convert to speech.
      
    2. **View Extracted Text**:
       - Once the file is uploaded, the app will extract the text from the file.
       - If it's a DOCX file, it removes lists (bullets) and displays the extracted text.
       - For PDFs, it extracts the text without lists.
    
    3. **Edit Text**:
       - The extracted text is displayed in an editable text area where you can modify the text if needed.
    
    4. **Word Count Check**:
       - The app checks the word count of the edited text. If it's over 50,000 words, it warns that it might be too large for translation.
    
    5. **Translate and Generate**:
       - Select a target language from the dropdown.
       - Click the "Translate and Generate Audio/Video Download Links" button.
       - This translates the edited text to the chosen language using Google Translate.
       - It generates a downloadable MP3 audio file of the translated text.
       - Provides a download link for the translated text as a Word document.
    
    ### Page 2: Text Translation
    1. **Enter Text**:
       - Enter or paste text into the text area to translate and convert to speech.
    
    2. **Word Count Check**:
       - Similar to Page 1, it displays the word count of the entered text.
    
    3. **Select Target Language**:
       - Choose the target language from the dropdown.
    
    4. **Translate and Convert**:
       - Click the "Translate - Convert to Speech and get Translated document" button.
       - This translates the entered text to the chosen language using Google Translate.
       - Generates a downloadable MP3 audio file of the translated text.
       - Provides a download link for the translated text as a Word document.
    
    ### General Steps:
    - **Translation Output**:
      - The translated text and audio can be listened to directly in the app.
      - Download the translated text as a Word document.
      
    - **Audio Playback**:
      - Click the audio player to listen to the generated speech.
      
    - **Downloads**:
      - Use the provided download links to save the translated text and audio files.
    
    That's the basic usage flow of the provided Streamlit app across its two pages.
    
    --- 
    '''
        
    st.markdown(project_description1, unsafe_allow_html=True)
    '''---'''
    st.header("Info of the methods used in the code")
    '''---'''
    left_column, right_column = st.columns(2)

    # List of method names
    method_names = [
        "convert_text_to_speech",
        "get_binary_file_downloader_html",
        "convert_text_to_word_doc",
        "translate_text_with_google"
    ]

    # Add content to the left column
    with left_column:
        display_method_code(method_names)
        # Add your content for the left side here

    # Add content to the right column
    with right_column:
        display_method_info()

if __name__ == "__main__":
    main()
