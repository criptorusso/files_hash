# files_hash
Get the hash sha256 from files inside directories and subdirectories.

Execute the script out the directory to get the hashes, a txt file will be created with the following rule dir_Name_SHA256.txt

The file with the result will contain the hash for each file inside any subdirectory in the main directory and also a hash for each subdirectory, this is obtained calculating the hash for each files inside the directory and concatenating the hashes in alphabetical ascendent order and finally getting the sha256 for the concatenation. The subdirectories without any file inside would be excluded. Directories that contains other folder without

Example:


![alt text](https://github.com/criptorusso/files_hash/blob/main/example.png?raw=true)
