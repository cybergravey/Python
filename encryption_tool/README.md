<h1>Encryption Tool</h1>

<h2>Description</h2>
This script encrypts and decrypts a message using simple character substitution. 
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>Random</b>
- <b>String</b>

<h2>Environments Used </h2>

- <b>macOS Sequoia Version 15.3.2</b> 

<h2>Program walk-through:</h2>

<p align="center">
Creates a character set. Includes spaces, puncuation, digits, and letters (uppercase & lowercase). Converts them into a list (chars). Creates a shuffled version of the list (key). <br/>
<img src="https://i.imgur.com/SiHwgkr.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
The encryption process takes a message from the user and replaces each character with its corresponding character in the shuffled key. It outputs the enrypted message.:  <br/>
<img src="https://i.imgur.com/mOwijaI.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
While in terminal, run the script then enter a message: <br/>
<img src="https://i.imgur.com/AJTb96e.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
The message is encrypted as shown: <br/>
<img src="https://i.imgur.com/whD9DzC.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
The decryption process takes the encrypted message from the user, finds the original character by reversing the mapping then outputs the original (decrypted) message.  <br/>
<img src="https://i.imgur.com/vRs6EeQ.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Copy the encrypted message.  <br/>
<img src="https://i.imgur.com/510vJTr.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Paste the encrypted message into the command line and press enter to decrypt:  <br/>
<img src="https://i.imgur.com/NAXtWQz.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
The message is decrypted to its original text:  <br/>
<img src="https://i.imgur.com/if5402s.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
