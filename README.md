# files_hash
Get the hash sha256 from files inside directories and subdirectories.

Execute the script out the directory to get the hashes, a txt file will be created with the following rule dir_Name_SHA256.txt

The file with the result will contain the hash for each file inside any subdirectory in the main directory and also a hash for each subdirectory, this is obtained calculating the hash for each files inside the directory and concatenating the hashes in alphabetical ascendent order and finally getting the sha256 for the concatenation. The subdirectories without any file inside would be excluded. Directories that contains other folder without

Example:

folder1:
      |---doc1
      |---folder2:
                |---doc2
      |---folder3:
                |---folder4:
                          |---doc4

Fecha y Hora: 26/12/2023 11:39:40
******************************************************* SHA256 POR ARCHIVOS: *******************************************************
ffae0da625d66639871b0409fe1bba790c802e8d55829b8aa953aab2661037d2	.//files_sha256.py
ddfb563037ac7b1a9d6374d4329f6b448042d2f28d4bc1a37833a78d77fe60cd	./folder1/doc1
234235d6a0dc9bc706f03acbd64a74fadc030cec47afb6e37a0f29815a4caa00	./folder1/folder2/doc2
5a1ce05bb764ca46a87bf61d452238d2f92b08a65731d39ea21443cdb0411643	./folder1/folder3/folder4/doc4

******************************************************* SHA256 POR CARPETAS: *******************************************************
dc13c8bab6fb68502341d529a894fd4ba57b28b58b08ab781260c8cbc629cdb5	./
63da083e1987c70b870e2aa9d91906506eb002fa9fc400029a98eda5511af3ae	./folder1
e5e1a3698bbcc2b6d080b752f7d6eb7c6862893d88d55a05c9f80f9e0b70b7f0	./folder1/folder2
0edd8157585c3e97a7d55e8b4575332de14ba08dc1965c02e7662bd316daafc2	./folder1/folder3
0edd8157585c3e97a7d55e8b4575332de14ba08dc1965c02e7662bd316daafc2	./folder1/folder3/folder4
