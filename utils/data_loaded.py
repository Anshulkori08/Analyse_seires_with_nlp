import glob
import pandas as pd

def load_subtitles_dataset(dataset_path):
    # Find all .ass files in the dataset directory
    subtitles_paths = glob.glob(dataset_path + '/*.ass')

    scripts = []
    episode_num = []

    for path in subtitles_paths:
        
            
            with open(path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                lines = lines[27:]          
                processed_lines = []
                for line in lines:
                    parts = line.split(',')
                    if len(parts) > 9:
                        processed_lines.append(",".join(parts[9:]))

                script = " ".join([line.replace('\\N', ' ') for line in processed_lines])

                
                file_name = path.split('/')[-1]  
                episode = int(file_name.split('-')[-1].split('.')[0].strip())

                scripts.append(script)
                episode_num.append(episode)
        

    
    df = pd.DataFrame.from_dict({"episode": episode_num, "script": scripts})
    return df