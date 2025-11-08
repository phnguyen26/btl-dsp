import pandas as pd
import os
import glob
from utils import extract_features, N_MFCC

if __name__ == '__main__':

    INPUT_DIR = "du_lieu_da_xu_ly" 

    OUTPUT_FILE = "features.csv" 
    genders = ['female', 'male']
    all_features_data = []
    for gender in genders:
        files = glob.glob(os.path.join(os.path.join(INPUT_DIR, gender), '*.wav'))
        for file_path in files:
            print(file_path)
            base_name = os.path.basename(file_path)
            mean_f0, mean_mfccs = extract_features(file_path)
            feature_dict = {
                "filename": base_name,
                "label": gender,
                "mean_f0": mean_f0
            }
            for i in range(N_MFCC):
                feature_dict[f"mfcc_{i+1}"] = mean_mfccs[i]
            
            all_features_data.append(feature_dict)

    df = pd.DataFrame(all_features_data)        
    df.to_csv(OUTPUT_FILE, index=False)
        
    print("HOÀN TẤT")