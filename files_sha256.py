#################################
# 3-12-23                       # 
# Antonio Russoniello           #
# get SHA256 folder and files   #
################################# 

import hashlib, os

def get_directories():
    f_dict = {}
    dirs =[x[0] for x in os.walk('./')]
    for d in dirs:
        #print(d)
        f_names =[x[2] for x in os.walk(d)]
        #print(f_names)
        f_dict[d] = f_names[0]
    return f_dict

def get_dict_path_files(f_dict):
    f_path = {}    
    for f in f_dict:
        #print(f, f_dict[f])
        f_path[str(f)] = f_dict[f]
        #print(f_path)
    return f_path

def get_full_path(f_path):
    return_path_list = []
    for k in f_path:
        #print(f_path[k])
        if len(f_path[k]) != 0:
            for i in range(len(f_path[k])):
                full_path = str(k) + '/'+ str(f_path[k][i])
                full_path = full_path.replace('\\','/')
                return_path_list.append(full_path)
    return return_path_list


def files_hash(f_path):
    hash_result = {}
    file_and_hash = {}
    for each in f_path:
        with open(each, 'rb') as f:
            # digest = hashlib.file_digest(f, "sha256") # uncomment this line for windows
            # linux #
            file_contents = f.read() # uncomment for linux
            digest = hashlib.sha256(file_contents) # uncomment this line for linux
            
        file_and_hash[each] = digest.hexdigest() 
    return file_and_hash

def get_hash_per_folder(dirs, files_hashed):
    current_path = ''
    result_dict = {}
    for d in dirs:
        d = d.replace('\\','/')
        current_path = d
        hash_sum = []
        hash_text = ''
        for i in files_hashed:
            index = i.find(d)

            if (index != -1):
                hash_sum.append(files_hashed[i])
                #print(hash_sum)
                hash_text += files_hashed[i]         
        
        # remove from the report the folders without files 
        # Folder with subdirectories will be hashed with the hash of the subdirs contained inside
        if hash_text != "":
            mesg = hashlib.sha256()
            mesg.update(hash_text.encode('utf-8'))
            #print(mesg.hexdigest(),d)
            #print(hash_text)
            result_dict[d] = mesg.hexdigest()

        current_path = ''
    return result_dict
    
def write_to_txt_file(f_hash, folder):
    file_name = os.getcwd().split('\\')[-1]
    date_time = time_date()
    with open("" + file_name + '_SHA256.txt', 'w') as f:     #define here the path for save the result
        f.write('Fecha y Hora: ' + date_time + '\n')            
        f.write(55*'*' + ' SHA256 POR ARCHIVOS: ' + 55*'*' + '\n')        
        for h in f_hash:
            #print(h, f_hash[h])
            f.write(f_hash[h]  + '\t' + str(h)  +'\n')
        f.write('\n'+ 55*'*' + ' SHA256 POR CARPETAS: ' + 55*'*' + '\n')        
        #f.write('SHA256:' + 16*'\t' + 'RUTA:\n')
        for h in folder:
            f.write(folder[h]  + '\t' + str(h)  +'\n')           

def time_date():
    from datetime import datetime
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    #print("date and time =", dt_string)
    return dt_string

def remove_duplicated_hash(hash_result): # remove duplicated hash, just show hash for subdirs with files inside it
    h_tmp = ''
    for d in hash_result:
        if(hash_result[d] != h_tmp):
            print(d, hash_result[d])
        h_tmp = hash_result[d]


if __name__ == "__main__":
    directories = get_directories()
    files_path_dict = get_dict_path_files(directories)
    files_to_hash = get_full_path(files_path_dict)
    files_hash = files_hash(files_to_hash)
    folder_hash = get_hash_per_folder(directories, files_hash)
    write_to_txt_file(files_hash, folder_hash)
    #remove_duplicated_hash(folder_hash)







