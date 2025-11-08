import librosa
import numpy as np
import soundfile as sf
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
TARGET_SR = 16000 #tan so lay mau 16k hz
SILENCE_THRESHOLD_DB = 20
def preprocess_audio(file_path):
    y, sr = librosa.load(file_path, sr=TARGET_SR, mono=True)
    y_trimmed, index = librosa.effects.trim(y, top_db=SILENCE_THRESHOLD_DB)
    return y_trimmed

N_MFCC = 13 
def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=16000)
    f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))
    mean_f0 = np.nanmean(f0)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=N_MFCC)
    mean_mfccs = np.mean(mfccs, axis=1)
    return mean_f0, mean_mfccs

def predict_gender(file_path):
    lr = joblib.load('model.pkl')
    le = joblib.load('label_encoder.pkl')
    processed_audio = 'processed_audio.wav'
    y = preprocess_audio(file_path)
    sf.write(processed_audio, y, 16000)
    mean_f0, mean_mfccs = extract_features(processed_audio)
    features = [mean_f0]
    
    for mfcc in mean_mfccs:
        features.append(mfcc)
    features = np.array([features])
    y_proba = lr.predict_proba(features)[0]
    
    classes = le.inverse_transform([0, 1])
    
    plt.figure(figsize=(8, 6))
    sns.barplot(x=classes, y=y_proba, hue=classes)
    plt.ylabel('Probability')
    plt.xlabel('Gender')
    plt.title(f'Gender Prediction Probabilities for {file_path}')    
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()
        

    