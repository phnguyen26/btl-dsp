import soundfile as sf
import os
import glob
from utils import preprocess_audio, TARGET_SR

if __name__ ==  '__main__':
    INPUT_DIR = "du_lieu_goc" 
    OUTPUT_DIR = "du_lieu_da_xu_ly"
    
    # tao thu muc
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, 'female'), exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, 'male'), exist_ok=True)
    
    genders = ['female', 'male']
    
    # vong lap tien xu li tat ca file
    for gender in genders:
        files = glob.glob(os.path.join(os.path.join(INPUT_DIR, gender), '*.wav'))
        for file_path in files:
            print(file_path)
            base_name = os.path.basename(file_path)
            
            processed_audio = preprocess_audio(file_path)
            
            # neu file khong im lang hoan toan 
            if processed_audio is not None:
                output_path = os.path.join(os.path.join(OUTPUT_DIR,gender), base_name)                
                sf.write(output_path, processed_audio, TARGET_SR)

    print("HOÀN TẤT")