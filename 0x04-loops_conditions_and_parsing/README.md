# READ ME

## [0-RSA_public_key.pub](./0-RSA_public_key.pub)

   ### how to generate SSH-RSA key pair

   - enter your terminal(git bash)
   - run this code, replace your@email.com with your actual email
   <pre><code>ssh-keygen -o -t rsa -C "your@email.com"</pre></code>

   - it will bring up a prompt to write the filepath you wish your code to be saved
        - open a new terminal window
        - navigate to where you will like it to be stored
        - run pwd to get the path e.g c/user/download
    - paste the file path and add an extra name to it as file_name e.g c/user/download/file_name
    - after that, input passphrase(like a password for accessing)
    - go to the file path you stored the code, two files will be created one with a .pub is the public key, the other is the private key.


