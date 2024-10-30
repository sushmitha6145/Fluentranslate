import streamlit as st
from googletrans import Translator as GoogleTranslator
from gtts import gTTS
import os
import base64
from docx import Document

language_mapping = {
    "en": "English",
    "hi": "Hindi",
    "gu": "Gujarati",
    "mr": "Marathi",
    "ta": "Tamil",
    "te": "Telugu",
    "ur": "Urdu",
    "bn": "Bengali",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "nl": "Dutch",
    "ja": "Japanese",
    "ko": "Korean",
    "ru": "Russian",
    "ar": "Arabic",
    "th": "Thai",
    "tr": "Turkish",
    "pl": "Polish",
    "cs": "Czech",
    "sv": "Swedish",
    "da": "Danish",
    "fi": "Finnish",
    "el": "Greek",
    "hu": "Hungarian",
    "uk": "Ukrainian",
    "no": "Norwegian",
    "id": "Indonesian",
    "vi": "Vietnamese",
    "ro": "Romanian",
    "fa": "Persian",
    "iw": "Hebrew",
    "bg": "Bulgarian",
    "ca": "Catalan",
    "hr": "Croatian",
    "sr": "Serbian",
    "sk": "Slovak",
    "sl": "Slovenian",
    "lt": "Lithuanian",
    "lv": "Latvian",
    "et": "Estonian",
    "is": "Icelandic",
    "ga": "Irish",
    "sq": "Albanian",
    "mk": "Macedonian",
    "hy": "Armenian",
    "ka": "Georgian",
    "ne": "Nepali",
    "si": "Sinhala",
    "km": "Khmer",
    "jw": "Javanese"
}

# Function to translate text using Google Translate
def translate_text_with_google(text, target_language):
    google_translator = GoogleTranslator()

    max_chunk_length = 500
    translated_text = ""

    for i in range(0, len(text), max_chunk_length):
        chunk = text[i:i + max_chunk_length]
        translated_chunk = google_translator.translate(chunk, dest=target_language).text
        translated_text += translated_chunk

    return translated_text

# Function to convert text to speech and save as an MP3 file
def convert_text_to_speech(text, output_file, language='en'):
    if text:
        supported_languages = list(language_mapping.keys())  # Add more supported languages as needed
        if language not in supported_languages:
            st.warning(f"Unsupported language: {language}")
            return

        tts = gTTS(text=text, lang=language)
        tts.save(output_file)

# Function to generate a download link for a file
def get_binary_file_downloader_html(link_text, file_path, file_format):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    b64_file = base64.b64encode(file_data).decode()
    download_link = f'<a href="data:{file_format};base64,{b64_file}" download="{os.path.basename(file_path)}">{link_text}</a>'
    return download_link

# Function to convert translated text to a Word document
def convert_text_to_word_doc(text, output_file):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_file)

# Function to translate text with fallback to Google Translate on error
def translate_text_with_fallback(text, target_language):
    try:
        return translate_text_with_google(text, target_language)
    except Exception as e:
        st.warning(f"Google Translate error: {str(e)}")

# Function to count words in the text
def count_words(text):
    words = text.split()
    return len(words)

def main():
    st.image("jangirii.png", width=300)
    st.title("Text Translation and Conversion to Speech (MultiLingual)")
    
    # Get user input
    text = st.text_area("Enter text to translate and convert to speech:", height=300)

    # Show word count as soon as the text is entered
    word_count = count_words(text)
    st.subheader(f"Word Count: {word_count} words")

    target_language = st.selectbox("Select target language:", list(language_mapping.values()))

    # Add a button to trigger the translation and text-to-speech conversion
    if st.button("Translate - Convert to Speech and get Translated document"):
        # Define target_language_code within this scope
        target_language_code = [code for code, lang in language_mapping.items() if lang == target_language][0]

        # Translate text using Google Translate with error handling
        translated_text = translate_text_with_fallback(text, target_language_code)

        # Display translated text
        if translated_text:
            st.subheader(f"Translated text ({target_language}):")
            st.write(translated_text)
        else:
            st.warning("Translation result is empty. Please check your input text.")

        if translated_text:
            # Convert translated text to speech
            output_file = "translated_speech.mp3"
            convert_text_to_speech(translated_text, output_file, language=target_language_code)

            # Play the generated speech
            audio_file = open(output_file, 'rb')
            st.audio(audio_file.read(), format='audio/mp3')

            # Play the generated speech (platform-dependent)
            if os.name == 'posix':  # For Unix/Linux
                os.system(f"xdg-open {output_file}")
            elif os.name == 'nt':  # For Windows
                os.system(f"start {output_file}")
            else:
                st.warning("Unsupported operating system")

            # Provide a download link for the MP3 file
            st.markdown(get_binary_file_downloader_html("Download Audio File", output_file, 'audio/mp3'), unsafe_allow_html=True)

            # Convert the translated text to a DOCX document
            docx_output_file = "translated_text.docx"
            convert_text_to_word_doc(translated_text, docx_output_file)

            # Provide a download link for the DOCX document
            st.markdown(get_binary_file_downloader_html("Download DOCX Document", docx_output_file, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
