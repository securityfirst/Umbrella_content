TEXTSECURE TOOL GUIDE
=====================

TextSecure Tool Guide\
Secure messaging for Android
----------------------------

**Lesson to read:\
? [Sending a message](umbrella://lesson/sending-a-message)**\
**Download Location:** TextSecure can be downloaded from [Open
WhisperSystems](https://whispersystems.org/); and can also be downloaded
from the [Google Play
store](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms)\
**Computer requirements:** Android 2.3 and up\
**Version used in this guide:**  TextSecure 2.1.7\
**License:** GPLv3\
**Level:** Beginner - Intermediate\
**Other reading: **\
? <https://github.com/WhisperSystems/TextSecure/wiki/Using-TextSecure>\
? <https://securityinabox.org/en/textsecure_main>\
? <http://support.whispersystems.org/>\
**Time required:** 15 minutes

**Using TextSecure will give you:**\
? The ability to send confidential messages with your mobile phone using
end-to-end encryption

### 1.0 Before you start

NOTE: TextSecure works over a Wi-Fi or data connection. While the
current version can also be used to send SMS if such a connection is
unavailable, **this function will shortly be removed due to security
concerns and future versions will work over the internet only.**

Messages in blue are sent over a data connection, while those in green
have been sent over SMS.

TextSecure can also currently be used to send SMS to non-TextSecure
users, however, those messages will not be encrypted in transit.
Encrypted text messages are marked with a small lock.

Both sides have to be using TextSecure for the messages to be secure
while they travel over the Internet.

You can set up a passphrase that will encrypt these conversations when
they are stored on your local phone. This means that they are better
protected against being read if your phone is seized or compromised.

TextSecure is available in more than 30 languages. You can change the
language of the app by selecting ?Settings? then ?Language.?

### 2.0 How to install TextSecure

**Step 1:** Download and install TextSecure

On your Android phone, enter the Google Play store and search for
?TextSecure.? Select the app, ?TextSecure Private Messenger.?

Select ?Install? and accept the Terms of Service by selecting ?Accept.?
The app will download and install automatically.

![](tool_textsecure1.png)

**Step 2:** Create a passphrase to encrypt data locally

Open the app. You will be prompted to create a passphrase in order to
locally encrypt your data. This means that your data will be encrypted
in transit, and that your messages will also be encrypted locally on
your phone. If you choose to skip this step, your messages will still be
encrypted in transit, but will not be protected on your device. For more
information on selecting a strong passphrase, see the **[Passwords
Lesson](umbrella://lesson/passwords)**.

![](tool_textsecure2.png)

**Step 3 (optional):** Import existing text messages

You will then be asked if you would like to import your existing text
messages into TextSecure?s encrypted database. This is up to you: It
simply means that old text messages (SMS) will be imported into the
TextSecure app and encrypted.

**Step 4 (optional):** Register your phone with TextSecure

The next screen will prompt you to ?Connect with TextSecure? by
registering your mobile phone number with TextSecure. This will allow
you to avoid SMS charges in some cases when communicating with other
TextSecure users. This is an optional step. Once you have registered
your phone, TextSecure will automatically verify your number using a
text message.

### 3.0 Verifying Keys

TextSecure uses end-to-end encryption. When you first send a message to
another contact that uses the app, the app will initiate a key exchange
message with the other user.

You will want to verify keys with the other user (for more information,
view the EFF module on [Key
Verification](https://ssd.eff.org/en/node/37/)). To view the keys, click
on the padlock icon in the top right of the screen and select ?Verify
Identity.? You will be shown two sets of keys: one belonging to you and
one belonging to the other user.

TextSecure supports manual verification or verification by scanning the
other user?s barcode. If you are in the same room as the other person,
you can easily scan the barcode on their phone (reachable by clicking on
the lock icon on the menu bar at the top of your conversation, selecting
?verify identity? and then clicking on the barcode icon) or read your
keys aloud to one another.

If you are not in the same room, there are different ways to verify keys
with varying degrees of trustworthiness. For example, you can read your
keys aloud to one another on the phone if you recognize one another?s
voices or send them using another verified method of communication such
as PGP or OTR.

The Problem with Mobile Phones
==============================

Mobile phones are basically insecure:

1.  Information sent from a mobile phone is vulnerable
2.  Information stored on a mobile phone is vulnerable
3.  Mobile phones give out information about their location
4.  Mobile phones can be used to eavesdrop

![](mobile1.png)

Not only can the company that runs your mobile phone network intercept
your calls and text messages (if unencrypted), and monitor your location
? many companies also choose, or are required, to share this information
with governments if asked.

Here, we'll describe some of vulnerabilities you need to be aware of
when using mobile phones of any type, and recommend ways you can stay a
bit safer.

Many checkpoints have a legitimate purpose, for example to prevent
weapons from entering an area. Some checkpoints, however, are designed
to harass people or as a cover for ambush, theft or violence. It is
important to recognise the difference between a legal, sanctioned
checkpoint and one designed for the gain of the checkpoint personnel.

You first need to rapidly assess the nature of the checkpoint.

-   Where it is located?
-   Who is manning it?
-   What does their mood appear to be?
-   Are there any signs of trouble?

Checkpoints at crossroads, bridges, mountain passes and town entrances
and exits are to be expected, and are likely to have been set up for the
general monitoring of all passers-by. Checkpoints in the middle of a
forest or on a mountain road away from habitation may exist for a more
ominous purpose. Checkpoints manned by regular army and police forces
may be less problematic than ones manned by irregulars.

If you suspect that there is a risk of violence or other serious
problems, turn round and drive steadily away, if it is safe to do so.

Before approaching or leaving a checkpoint, inform base by radio. Do so
in a discreet way, far enough from the checkpoint to avoid them seeing
that you are using the radio

K9 & APG TOOL GUIDE
===================

K9 & APG Tool Guide\
 Encrypted email for Android
----------------------------

**Lesson to read: [Email](umbrella://lesson/email)**\
**Download Location: \
? [APG homepage](http://www.thialfihar.org/projects/apg/)\
? [K-9 Mail homepage](https://code.google.com/p/k9mail)**\
**Phone requirements: **\
? Android 1.5 or up\
? APG must be installed before installing K-9 Mail\
**Version used in this guide: **\
? APG 1.1.1\
? K-9 5.001\
**License: **\
? APG: Free and Open Source Software (Gnu GPL v3)\
? K-9: Free and Open Source Software (Apache 2.0)\
**Other reading: **\
? [Passwords](umbrella://lesson/passwords)\
? [Mobile Phones](umbrella://lesson/mobile-phones)\
**Level:** Advanced\
**Time required:** 30-40 minutes

**Using K-9 & APG will give you:**\
? APG can be used to encrypt, decrypt and sign emails and single files
locally on your phone.\
? When APG is used with K-9 it gives you the ability to use encrypted
email easily on your phone.

**Android Privacy Guard (APG) for Android Devices**

![](tool_k91.png)

### 1.0 How To Install APG

**Step 1.** On your Android device, download and install the app from
**[Google Play
here](https://play.google.com/store/apps/details?id=org.thialfihar.android.apg)** by
pressing, ?Install?.

![](tool_k92.png)

**Step 2:** Before the installation process begins, you will be prompted
to review the access that the application will have on your phone.
Review this carefully. Once you are happy with the permissions that will
be granted, press ?Accept? and the installation will complete. If you do
not agree with the permissions that will be granted, press the back
button and the installation will be cancelled.

![](tool_k93.png)

### 1.1 Key Management

In order to encrypt files or messages when you first start APG, you will
be asked to either import existing GPG keys or create a new public and
private key on your phone.

![](tool_k94.png)

**Note:** If you want to send encrypted files or messages to other
people, you will either need to import their public keys or decide on a
shared password.

### 1.1.1 Key Management - Create Your Public And Private Keys

If you do not already have your private and public GPG key or wish to
use a separate GPG keys for your Android device you can use APG to
create them.

**Step 1:** When you open APG for the first time click the ?Creating
your own key? button, as shown above.

**Step 2:** Wait 2 - 3 minutes while your GPG keys are generated. You
will be able to assign your name and email address to the key in the
next step.

**Step 3:** In the following screen, below:

? We strongly recommend that you protect your GPG keys with password. To
do this press ?Set Passphrase? and provide strong password. See the
**[Passwords lesson](umbrella://lesson/passwords)** on how best to do
this;\
? Fill in your *name, email address*;\
? It is important that you set an expiry date on the GPG keys, after
which time the keys can no longer be used to encrypt files.

![](tool_k95.png)

**Step 4:** Once all the information is correct, tap ?Save? at the top
of the screen to be brought back to the main APG screen, as shown above,
where you will see a list of all your keys.

### 1.1.2 Key Management - Import Keys From A File

To use GPG keys that you created on another device or computer, or to
import the public keys of your contact:

**Step 1:** Copy the GPG key(s) to your Android device via USB or save
them from the email that you received on the Android device.

**Step 2:** In APG, click the ?Importing Keys? button.

**Step 3:** On the following screen click the ?Open? button at the top
of your screen to open a file browser.

**Step 4:** From the file browser, select the key(s) you wish to import.

**Step 5:** Review the keys you will import and tap ?Import Selected
Keys? to add the GPG keys to APG. You may decide which keys you do not
wish to import by deselecting appropriate checkbox for the keys.

![](tool_k96.png)

**Step 6:** Once you have imported all the desired GPG keys you will be
brought back to the main screen where you will see a list of all your
keys.

![](tool_k97.png)

### 1.1.3 Key Management - Import Keys From The Clipboard

GPG keys can be sent in the body of an email instead of as an attachment
to import such a key

**Step 1:** Copy the GPG key from your email to the clipboard. The image
below shows a GPG key in the body of an email.

![](tool_k98.png)

**Step 2:** Open APG and expand the side menu on any APG screen by
pressing ?APG? at the top left of your screen.

**Step 3:** Select ?Import Keys? to bring up the import key screen.

**Step 4:** Tap ?Keyserver? at the top of the screen to display the
import options menu and select ?Import form clipboard?.

![](tool_k99.png)

**Step 5:** Tap ?Get key from the clipboard? to copy the key from the
clipboard.

**Step 6:** Tap ?Import selected keys? at the bottom of the screen to
finish importing the key into APG

![](tool_k910.png)

###  1.1.4 Key Management - Share Your Public Key As A File

In order for your contacts to be able to send you encrypted email, you
will first need to send them your *public key*

**Step 1:** From the main **APG** window tap on your key's entry to
bring you to the *info* screen (as above) for your GPG key.

**Step 2:** Tap on the three vertical dots in the top right corner to
display the menu and select ?Export to file?.

![](tool_k911.png)

**Step 3:** Select the location and file name you want to save your
public key to and press ?OK?.

![](tool_k912.png)

** Step 4:** The saved file cannot be given to your contacts, for
example via email or IM.

### 1.1.5 Key Management - Share Your Public Key From The Clipboard

**Step 1:** From the main APG window tap on your key's entry to bring
you to the *info* screen for your GPG key.

**Step 2:** Tap the three connected dots at the top of the screen to
bring up sharing options and select ?Share whole key?.

**Step 3:** In the following menu select ?Copy to clipboard? to copy
your GPG public key to the clipboard.

![](tool_k913.png)

**Step 4:** Paste the public key into an email or IM chat session to
your contact.

### 1.1.6 Key Management - Verify Identities

In order to ensure that you have received the correct GPG public key for
your colleague and not someone trying to impersonate them, it is very
important that you verify the GPG keys fingerprints either in person or
via a medium that you can verify who you are talking to such as a video
call or telephone call.

**Step 1:** From the main **APG** window tap on your key's entry to
bring you to the *info* screen for your GPG key. Your contact should do
the same and tap on the key they have for you.

![](tool_k914.png)

**Step 2:** Locate the **Fingerprint** line under the **MASTER
KEY** heading and read out the 40 character long string one line at a
time.

![](tool_k915.png)

**Step 3:** Your contact should verify that the fingerprint you read
out, is the fingerprint displayed for your key on their phone or
computer.

**Step 4:** Repeat steps 1 to 3 but tap on your contacts key at the
first step.

### 1.2 Message Encryption

APG provides two ways for you to encrypt files on your Android
device. Public key encryption is the desired option to use when sending
files to other people as you will not have to share any passphrase with
them. However you will need to receive public key from each person you
wish to encrypt files to in advance. Passphrase encryption can be useful
to be able to decrypt a file at a later date without the need to have
access to a public key. But this method requires sharing the passphrase
used to encrypt the file in order to decrypt it later.

Message encryption in **APG** can be useful if you want to store
encrypted notes in another application or send encrypted email or
message via a service that you can not use K-9 Mail with (eg. webmail,
social networking message, etc.).

### 1.2.1 Message Encryption - Public Key

**Step 1:** Expand the side menu on any **APG** screen by
pressing ?APG? at the top left of your screen.

**Step 2:** Select ?Encrypt? to bring up the encryption screen.

**Step 3:** To view the list of possible recipients press ?Select?
button with the person icon. **Note:** If you want to be able to decrypt
the message at a later time, you will need to remember to include
yourself in the list of recipients.

**Step 4:** On the Recipient selection screen, tick all the people that
need to be able to decrypt the message and press ?Okay?.

![](tool_k916.png)

**Step 5:** Choose how to encrypt your message. Tapping ?Share
with?? will allow you to send the encrypted message to another
application on your phone such as an email client.
Tapping ?Clipboard? will copy the encrypted message to your clipboard
allowing you to paste the message anywhere that you can paste, such as
an online forum.

### 1.2.2 Message Encryption - PassPhrase

**Step 1:** Expand the side menu on any APG screen by pressing ?APG? at
the top left of your screen.

**Step 2:** Select ?Encrypt? to bring up the encryption screen.

**Step 3:** Press the &lt; or &gt; buttons to either side of **PUBLIC
KEY** to change the encryption type to PASSPHRASE.

**Step 4:** Enter a strong password in the fields provided.

**Step 5:** Enter the message you want to encrypt

![](tool_k917.png)

**Step 6:** Choose how to use your encrypted message. Tapping ?Share
with?? will allow you to send the encrypted message to another
application on your phone such as an email client.
Tapping ?Clipboard? will copy the encrypted message to your clipboard
allowing you to paste the message anywhere that you can paste, such as
an online forum.

**Note:** If you plan to share the encrypted message with a contact you
will need to relay the *passphrase* to them in a secure way, such as in
person. It should never be sent to anyone over email or IM if it is not
encrypted.

### 1.2.3 Message Decryption

**Step 1:** Copy the entire contents of the encrypted message that you
received in the other app to the clipboard by long-taping on the message
and selecting copy button.

**Step 2:** Switch to APG app and expand the side menu on any APG screen
by pressing ?APG? at the top left of your screen.

**Step 3:** Select ?Decrypt? to bring up the encryption screen.

**Step 4:** APG will automatically detect that the clipboard has an
encrypted message in it and ask you for either your GPG password, if the
sender used public key encryption, or for the message password, if you
used the *passphrase* encryption.

![](tool_k918.png)

**Step 5:** The decrypted message will be displayed in a text window
inside APG.

### 1.3 File Encryption

As with message encryption public key is the preferred encryption method
but password encryption will allow you to decrypt on a phone or computer
that does not have a private key installed but does
have APG or GPG software.

### 1.3.1 File Encryption - Public Key

**Step 1:** Expand the side menu on any APG screen by pressing ?APG? at
the top left of your screen.

**Step 2:** Select ?Encrypt? to bring up the encryption screen.

**Step 3:** To view the list of possible recipients press ?Select? by
the person icon. **Note:** If you want to be able to decrypt the file
yourself at a later time, you will need to remember to include yourself
in the list of recipients.

**Step 4:** On the Recipient selection screen, tick all the people you
want to be able to decrypt the file and press ?Okay?.

![](tool_k919.png)

**Step 5:** Press the &lt; or &gt; buttons to either side
of **MESSAGE** to change the encryption type to **FILE**.

**Step 6:** Tap the open file icon to open the file browser and select
the file you want to encrypt.

![](tool_k920.png)

**Step 7:** press ?Encrypt File? to choose a file name and location to
save the file to.

![](tool_k921.png)

**Step 8:** Tap ?OK? to complete the encryption process.

### 1.3.2 File Encryption - PassPhrase

**Step 1:** Expand the side menu on any APG screen by pressing ?APG? at
the top left of your screen.

**Step 2:** Select ?Encrypt? to bring up the encryption screen.

**Step 3:** Press the &lt; or &gt; buttons to either side of **PUBLIC
KEY** to change the encryption type to PASSPHRASE.

**Step 4:** Enter a strong password in the fields provided.

**Step 5:** Press the &lt; or &gt; buttons to either side
of **MESSAGE** to change the encryption type to FILE.

**Step 6:** Tap the open file icon to open the file browser and select
the file you want to encrypt.

![](tool_k922.png)

**Step 7:** press ?Encrypt file? to choose a file name and location to
save the file to.

![](tool_k923.png)

**Step 8:** Tap ?OK? to complete the encryption process.

**Note:** If you plan to share the encrypted file with a contact you
will need to relay the *passphrase* to them in a secure way, such as in
person. It should never be sent to anyone over email or IM if it is not
encrypted.

### 1.3.3 File Decryption

**Step 1:** Expand the side menu on any APG screen by pressing ?APG? at
the top left of your screen.

**Step 2:** Select ?Decrypt? to bring up the encryption screen.

**Step 3:** Tap the &lt; or &gt; buttons to either side
of **MESSAGE** to change the encryption type to **FILE**.

**Step 4:** Tap the open file icon to open the file browser and select
the file you want to decrypt.

![](tool_k924.png)

**Step 7:** press ?Decrypt? after which you will be prompted for your
GPG keys password if public key encryption was used or for the file
password if you used the *passphrase* encryption.

![](tool_k925.png)

**Step 8:** Tap ?OK? to choose a location to save the decrypted
document.

![](tool_k926.png)

**Step 9:** Tap ?OK? to complete the decryption process.

------------------------------------------------------------------------

**K-9 Mail with APG**

![](tool_k927.png)

### 2.0 How to Install *K-9 Mail*

### 

**Note:** Before you start using K-9 Mail you will need to have an email
account, such as Gmail, that supports either secure POP3 or IMAP
connections.

**Step 1.** On your Android device, **download** and **install** the app
from the [Google Play store
here](https://play.google.com/store/apps/details?id=com.fsck.k9) store
by tapping ?Install?.

![](tool_k928.png)

**Step 2.** Before the installation process begins, you will be prompted
to review the access that the application will have on your phone.
Review this carefully. Once you are happy with the permissions that will
be granted, tap ?Accept? and the installation will complete. If you do
not agree with the permissions that will be granted, tap the back button
and the installation will be cancelled.

![](tool_k929.png)

**Step 3.** Tap ?Open? to run the app for the first time

### 2.1 How to configure K-9 Mail

After installing K-9 Mail and running it for the first time you will be
presented with a welcome screen describing the features of the mail
client. Press ?Next? to begin the account setup.

Where possible, K-9 Mail will attempt to automatically configure your
email account for you. If this is not possible or you wish to have more
control over the account setup you can also manually configure your
account.

### 2.1.1 Automatic account setup

**Step 1:** Enter your email address and email password in the fields
provided and tap ?Next?.

![](tool_k930.png)

**Step 2: K-9 Mail** will connect to the internet and attempt to get
your account settings.

**Step 3:** Once the settings have been retrieved you will be asked to
enter your name as you want it to be displayed on all outgoing email and
to give the account a name. The account name will allow you to
distinguish between multiple accounts, should you want to add more.
Tap ?Done? to complete the account setup.

![](tool_k931.png)

**Step 4:** K-9 Mail will display changes to the program since the last
version, tap ?OK? to dismiss this window and be brought to your mail
account.

![](tool_k932.png)

**Step 5:** To make sure the account is working in K-9
Mail, send yourself an email from your computer and download it from the
K-9 Mail client.

### 2.1.2 Manual account setup

**Step 1:** Enter your email address and email password in the fields
provided and tap ?Manual setup?.

**Step 2:** Select the account type your email is (IMAP/POP/Exchange)
and tap the relevant button as in the image below.

**Note:** you will need to refer to your email client settings on your
computer to know what account type your email server uses.

![](tool_k933.png)

**Step 3:** Next are the incoming server settings. If unsure, refer to
the email client on your computer for settings. Always ensure that
the *security type* is set to
either *STARTTLS* or *SSL/TLS*. **Never** use the *none* option.

![](tool_k934.png)

**Step 4. K-9 Mail** will then connect to your mail server to check if
your settings are correct. It might display a warning about the
certificate of your secured connection. *Do not ignore this!* This is
the only time you can verify that the certificate really belongs to your
mail server. If you ignore this, you can not be sure if you are not
subject to a *Man-in-the-Middle attack*, and your communications could
be intercepted. You can see a SHA-1 fingerprint at the very end of the
warning. Either **check** on your computer if the installed certificate
from your mail server has the same fingerprint, or find a way to check
your mail server's certificate directly from your provider.

**Step 5. K-9 Mail** asks you to configure your outgoing server
settings. Again, **ensure** that *Security
Type* is *STARTTLS* or *SSL/TLS*. For all additional
settings, **check** your computer's email client or the settings of your
email provider.

![](tool_k935.png)

**Step 6.** K-9 Mail now asks you how often you want it to automatically
poll for email. Set the option to *never* and uncheck *enable push mail*
for this account, if you only want to receive email when you manually
check, otherwise leave the settings as they are to automatically receive
email as they arrive to your account.

![](tool_k936.png)

**Step 7.** The last pieces of information to provide are a nickname for
the email account which will be displayed in K-9 Mail and to set up the
name you wish to be displayed on all outgoing email.

**Step 8:** To make sure the account is working in K-9
Mail, send yourself an email from your computer and download it from the
K-9 Mail client.

We recommend that you use K-9 Mail only in addition to your computer's
email client. Therefore it is important that when you download email
with your Android phone, it does not delete the email on the server,
since you want to receive the email later with your computer, too. By
default, K-9 Mail is set up this way, but you may want to learn more
about the settings which can be found in *accounts*; this can be reached
by long pressing on the account you have just set up and
selecting *account settings* from the menu. You may also wish to check
the *fetching mail* and *sending mail* account option for settings.

### 2.2 How to Send and Receive Encrypted eMail

One of the main benefits of using K-9 Mail over other email clients is
that it lets you send and receive GPG encrypted email. Before you can
start sending and receiving encrypted email, you need to ensure that you
have all your OpenPGP keys imported into APG, as outlined in the APG
section above. If you followed all the necessary steps in the APG keys
section your keys will be imported.

### 2.2.1 Sending encrypted email

**Step 1:** From any screen in K-9 Mail tap the Send Email icon to start
a new email.

**Step 2:** On the email composition screen add your recipient by either
typing in an email address or pressing the Add Recipient icon and
selecting one from your address book.

**Step 3:** Enable encrypted email by checking the box next
to *encrypt*.

**Step 4:** When finished writing your email, press the Send icon to
send.

![](tool_k937.png)

**Step 5:** The following screen will ask you to select which GPG keys
to encrypt to. Be default the recipient key and your own should already
be selected.

**Note:** You should always ensure that your key is selected so that you
can read the encrypted email that you had send.

![](tool_k938.png)

**Step 6:** Once all recipient keys have been selected, press ?OKAY? to
send the email.

**Note:** Currently K-9 Mail cannot encrypt attachments, so you will
need to encrypt any files with APG that you wish to send, before you
compose the email. This is explained in the APG encryption section
above. To attach the files tap the paperclip attachment icon and select
the encrypted file (ending in *.gpg*).

### 2.2.2 Receiving encrypted email

**Step 1:** Open your *inbox* and tap the email you wish to read.

![](tool_k939.png)

**Step 2:** Tap the ?Decrypt? button.

![](tool_k940.png)

**Step 3:** Enter the passphrase for your GPG key when prompted and
press ?OK? to decrypt the email.

![](tool_k941.png)

**Note:** as **K-9 Mail** is currently not able to decrypt encrypted
attachments, you will need to save the attachments to your phone
and decrypt them with APG, as explained in the APG decryption section
above.

Anonymity Online
================

Accessing information on the Internet, or publishing material online
such as photos or videos, leaves many traces of who and where you are
and what you are doing. This may put you at risk. You can reduce your
risks through the use of anonymising tools such as Tor.

![](interneta1.png)

**Remember, these tools can only protect your anonymity if you do not
log in to sites or post something online that could identify you!**

Grab bags are bags filled with an individual?s survival essentials in
case they need to move rapidly. They should be prepared for high-risk
activists, journalists and humanitarians at times of heightened risk and
kept close to an exit in their residence ? somewhere easy to grab and
run.

You should plan out several potential escape routes in case of
emergency. Remember that the best escape route may vary depending on the
time of day (e.g. across the roof at night-time, via a garden fence in
the day time) so it is important to move the location of the grab bags
as necessary.

Keeping your webmail private ? HTTPS
====================================

There are a few important steps that you can take in order to increase
the security of your email communication. The first is to make sure that
only the person to whom you send a given message is able to read it.

Keeping your webmail private ? HTTPS
------------------------------------

HTTPS, (also referred to as SSL or TLS), encrypts your communications so
that it cannot be read by other people on your network. This can include
the other people using the same Wi-Fi in an airport or at a café, the
other people at your office or school, the administrators at your ISP,
malicious hackers, governments, or law enforcement officials.
Communications sent over your web browser, including the web pages that
you visit and the content of your emails, using HTTP rather than HTTPS
are very easy for an attacker to intercept and read.

Most email providers give you a way of accessing your email using a web
browser, such as Firefox or Chrome. Of these providers, most of them
provide support for HTTPS. You should always make sure that your
connection is secure before logging in, reading your email, or sending a
message. You can tell that your email provider supports HTTPS if you log
in to your webmail and the URL at the top of your browser begins with
the letters HTTPS instead of HTTP (for
example: https://mail.google.com).

If your email provider supports HTTPS, but does not do so by default,
try replacing HTTP with HTTPS in the URL and refresh the page. If you?d
like to make sure that you are always using HTTPS on sites where it is
available, download the [HTTPS
Everywhere](https://www.eff.org/https-everywhere) browser add-on for
Firefox or Chrome.

Webmail providers that use HTTPS by default include Gmail, RiseUp and
Yahoo.

Some webmail providers give you the option of choosing to use HTTPS by
default by selecting it in your settings, such as Hotmail.

HTTPS is the most basic level of encryption for your web browsing that
we recommend for everybody. It is as basic as putting on your seat belt
when you drive.

![](email1.png)

Journalists and humanitarian workers should be fully equipped with gear
appropriate to the situation they are operating in. In extreme
circumstances, this could involve wearing hazmat suits, carrying
detectors, or ingesting oral tablets to block or act against possible
biological, chemical, or nuclear agents. In combat zones, it would
involve wearing body armor rated to withstand shrapnel and high-powered
bullets. In cases of street clashes or violence, it could mean wearing
an inconspicuous anti-stab vest.

### If you are having a physical security emergency, the following are useful resources.

IMMEDIATE SUPPORT
=================

Normally available for support within the first 24 hours\
\
**Where:** Global Embassy Listings

<https://embassy-finder.com>

Front Line
----------

**Where:** Global\
\
**Type of Threat:** Threats of Violence, Physical Assault, Imprisonment,
Lawsuit, Infringement on Rights\
\
**Language:** Arabic, English, French, Russian, Spanish\
\
**Accept Urgent Appeals?** Yes!\
\
**Description:** Front Line protects Human Rights Defenders through a
24hour emergency hotline (phone and encrypted email), international
advocacy, security training and training manuals, grants and fellowships
(including emergency funding), and evacuation support. Front Line?s
Dublin Platform links grassroots human rights defenders with UN
mechanisms, international human rights networks, and each other.\
\
**Web site:** frontlinedefenders.org\
Dublin, Tel: (+353) 1 212 3750\
**Email:** info@frontlinedefenders.org\
Brussels, Tel: (+32) 2 230 93 83\
**Secure Online Communication:** web
https://secure.hyperlink.ie/frontline/\
comment.en.html\
\
24 hour emergency support, Tel: (+353) 1 21 00 489

Rory Peck Trust
---------------

**Where:** Global\
\
**Type of Threat:** Freelance journalists who suffer: Physical Assault,
Imprisonment, Infringement on Rights, Discrimination, Attack on Freedom
of Expression\
\
**Language:** English\
\
**Accept Urgent Appeals?** Yes!\
\
**Description:** The principal objectives of the Trust are to provide
practical assistance and support to freelance newsgatherers and their
families worldwide, to raise their profile, promote their welfare and
safety, and to support their right to report freely and without fear.\
\
**Web site:** [www.rorypecktrust.org](www.rorypecktrust.org)\
London, Tel: (+44) 203 219 7860

U.S. Centers for Disease Control and Prevention
-----------------------------------------------

**Where:** Global\
\
**Type of Threat:** Disease, outbreak, medical health protection\
**Language:** English\
**Accept Urgent Appeals?** No\
\
**Description:** The U.S. government agency is a public source for
information on common diseases, disorders, and treatments. The CDC
website provides information about sickness and disease, healthy living,
safety and emergency care, and disaster preparedness and response.\
\
**Web site:** www.cdc.gov\
Atlanta, Tel: +1-800-232-4636 (24-hour health information hotline,
Monday through Friday)

DELAYED SUPPORT
===============

Normally available for support after first 24 hours

Amnesty International
---------------------

**Where:** Global\
\
**Type of Threat:** Physical Assault, Imprisonment, Infringement on
Rights, Discrimination, Attack on Freedom of Expression\
\
**Language:** Arabic, English, French, Spanish\
\
**Accept Urgent Appeals?** Yes!\
\
**Description:** Amnesty International leads a global movement of
research, solidarity, and action on behalf of victims of human rights
violations. Amnesty International campaigns to end discrimination,
abuse, and infringements on human rights, physical and mental integrity,
and the freedom of thought and expression.\
\
**Web site:** www.amnesty.org\
New York, Tel: (+1) 212 807-8400\
London, Tel: (+44) 20-74135500

Asian Human Rights Commission
-----------------------------

**Where:** East Asia; South & Southeast Asia\
\
**Type of Threat:** Physical Assault, Imprisonment, Infringement on
Rights, Discrimination, Attack on Freedom of Expression\
**Language:** Bahasa, Burmese, Chinese, English, French, German,
Italian, Japanese, Korean, Tagalog\
\
**Accept Urgent Appeals?** Yes!\
\
**Description:** The Asian Human Rights Commission monitors,
investigates, advocates, and takes solidarity action around human rights
violations across Asia. AHRC?s Urgent Appeal Programme mobilizes
thousands of individu- als to speak out around particular cases.
(Directed by Ashoka Fellow Basil Fernando.)\
\
**Web site:** www. ahrchk.net\
Hong Kong, Tel: 852-2698 6339\
**Email:** ahrchk@ahrchk.org

Committee to Protect Journalists
--------------------------------

**Where:** Global\
\
**Type of Threat:** Threats of Violence, Physical Assault, Imprisonment,
Lawsuit, Infringement on Rights, Discrimination, Attack on Freedom of
Expression\
\
**Language:** English\
\
**Accept Urgent Appeals?** Yes\
\
**Description:** The Committee to Protect Journalists promotes press
freedom worldwide by defending the rights of journalists to report the
news without fear of reprisal. CPJ reveals abuses against the press,
acts on behalf of imprisoned or threatened journalists, and warns
journalists of attacks on press freedom. CPJ?s Journalist Assistance
Program offers emergency sup- port around medical attention, relocation,
legal aid, and evacuation.\
\
**Web site:** [www.cpj.org](www.cpj.org)\
New York, Tel: (+1) 212 465-1004\
**Email:** JournAsst@cpj.org

Conectas
--------

**Where:** Brazil; Latin America, Africa, Asia\
\
**Type of Threat:** Threats of Violence, Imprisonment, Lawsuit,
Infringement on Rights, Discrimination\
\
**Eligible:** Human Rights advocates (activists and academics)\
\
**Language:** English, Portuguese, Spanish\
\
**Accept Urgent Appeals?** No\
\
**Description:** Conectas? Justice Program supports strategic litigation
and pro bono legal services to support vulnerable groups and victims of
human rights violations. Conectas? Global South Program links human
rights aca- demics and activists in Africa, Asia, and Latin America to
share knowledge, connect them to the UN, and strengthen the new
generation of human rights defenders. (Directed by Ashoka Senior Member
Oscar Vilhena.)\
\
**Web site:** conectas.org\
Sao Paulo, Tel: (+5511) 3884-7440\
**Email:** conectas@conectas.org

CIVICUS & Civil Society Watch
-----------------------------

**Where:** Global\
**Type of Threat:** Physical Assault, Imprisonment, Lawsuit,
Infringement on\
Rights, Discrimination, Attack on Freedom of Expression\
\
**Language:** English\
**Accept Urgent Appeals?** Yes\
\
**Description:** CIVICUS strengthens civil society and civic action
around the world through an international alliance of more than 1000
members across 100 countries. Civil Society Watch (CSW) mobilizes rapid
responses in situations in which rights and liberties of citizens are
threatened or limited. CSW makes statements of protests, letter-writing
campaigns, press campaigns, public marches, and missions to verify acts
of violations of rights.\
\
**Web sites:** www.civicus.org; www.civilsocietywatch.org\
**Emails:** info@civicus.org; cswatch@civicus.org\
South Africa, Tel: (+27 11) 833-5959

European Interagency Security Forum
-----------------------------------

**Where:** Global\
**Type of Threat:** Humanitarian aid workers facing security threats in
the field\
**Accept Urgent Appeals?** No\
\
**Description:** EISF?s aim is to improve holistic security risk
management (SRM) approaches allowing sustainable access of aid workers
to populations in need. The EISF Secretariat works in collaboration with
its? Members to produce original research, arrange biannual forum
meetings and regular workshops and facilitate information sharing
between members and the wider NGO community.\
\
**Web site:** [www.eisf.eu](www.eisf.eu) London,\
Tel: (+44) 203 195 1360\
**Email:** eisf-coordinator@eisf.eu

Federation for Human Rights
---------------------------

**Where:** Global\
**Type of Threat:** Physical Assault, Imprisonment, Infringement on
Rights, Discrimination, Attack on Freedom of Expression\
\
**Language:** Arabic, English, French, Spanish\
**Accept Urgent Appeals?** No\
\
**Description:** FIDH works with over 141 non-governmental organizations
in over 100 countries towards improvements in victim protection,
prevention of human rights violations, and judicial punishment of
perpetrators. Over the past 25 years they have organized over 1000
missions in 100 countries. FIDH works closely with the World
Organisation Against Torture (OMCT) through its Observatory for the
Protection of Human Rights Defenders.\
\
**Web site:** [www.fidh.org](www.fidh.org)\
Paris, Tel: (+33) 1 43 55 25 18

Fund for Global Human Rights
----------------------------

**Where:** India, Pakistan, Liberia, Sierra Leone, Guinea, Democratic
Republic of Congo, Burundi, Uganda, Mexico, Guatemala, Algeria, Morocco,
Tunisia\
**Type of Threat:** Threats of Violence, Physical Assault, Imprisonment,
Infringement on Rights, Discrimination, Attack on Freedom of Expression\
**Language:** Arabic, English, French, Spanish\
\
**Accept Urgent Appeals?** No\
\
**Description:** The Fund for Global Human Rights channels financial
resources to on-the-ground human rights organizations, strengthening
human rights movements and communities around the world. The Fund for
Global Human Rights pools funding from international donors, funds local
and regional human rights groups, and creates networks to link often
isolated activists.\
\
**Web site:** [www.globalhumanrights.org](www.globalhumanrights.org)\
Washington, DC, Tel: (+1) 202 347-7488\
**Email:** info@globalhumanrights.org

Human Rights First
------------------

**Where:** Global\
**Type of Threat:** Threats of Violence, Physical Assault, Imprisonment,
Infringement on Rights, Discrimination, Attack on Freedom of Expression\
**Language:** English\
\
**Accept Urgent Appeals?** Yes\
\
**Description:** Human Rights First protects people at risk, including
victims of human rights violations and discrimination. Their Human
Rights Defenders program supports human rights defenders targeted for
threats and attack through advocacy and mobilizing their volunteer
network.\
\
**Web site:**[www.humanrightsfirst.org](www.humanrightsfirst.org)\
New York, Tel: (+1) 212 845-5200

Human Rights Watch
------------------

**Where:** Global\
**Type of Threat:** Threats of Violence, Imprisonment, Lawsuit,
Infringement on Rights, Discrimination, Attack on Freedom of Expression\
\
**Language:** Arabic, Chinese, English, French, German, Hebrew, Korean,
Persian, Portuguese, Russian\
**Accept Urgent Appeals?** Yes\
\
**Description:** Human Rights Watch stands with victims and activists to
prevent discrimination, uphold political freedom, protects people from
inhumane conduct in wartime, and brings offenders to justice by exposing
human rights violations and holding abusers accountable. HRW?s principal
advocacy strategy is to shame offenders through press attention, exert
dip- lomatic and economic pressure, and build coalitions around specific
human rights issues.\
\
**Web site:** [www.hrw.org](www.hrw.org)\
New York, Tel: (+1) 212-290-4700\
**Email:** hrwnyc@hrw.org

International Service for Human Rights
--------------------------------------

**Where:** Global\
**Type of Threat:** Threats of Violence, Physical Assault, Imprisonment,
Lawsuit, Infringement on Rights, Discrimination, Attack on Freedom of
Expression\
**Language:** English\
\
**Accept Urgent Appeals?** No\
\
**Description:** ISHR provides information, training, and support to
human rights defenders around the world. Their Human Rights Defenders
Offices strengthens UN procedures to support Human Rights Defenders, and
is promoting similar mechanisms in Africa and the Americas. They do not
take urgent appeals, as they focus on training and aggregating
knowledge.\
\
**Web site:** www.ishr.ch Geneva, Tel: (+41) 22 733 51 23

Observatory for the Protection of Human Rights Defenders
--------------------------------------------------------

**Where:** Global\
**Type of Threat:** Threats of Violence, Physical Assault, Imprisonment,
Lawsuit, Infringement on Rights, Discrimination, Attack on Freedom of
Expression\
**Language:** English, various\
\
**Accept Urgent Appeals?** Yes\
\
**Description:** The Observatory is among the largest coalitions of NGOs
(nearly 300 local, national, and regional organizations) fighting
against arbitrary detention and executions, torture, forced
disappearances, and other forms of violence. The Observatory has
denounced and stopped attacks against human rights defenders through
urgent appeals, fact-finding missions, lobbying, training, and reports.
They do take urgent appeals.\
\
**Web site:** www.omct.org click on ?Human Rights Defenders?\
**Email:** omct@omct.org\
Switzerland, Tel: (+41) 22 809 4939

Peace Brigades International
----------------------------

**Where:** Latin America; South & Southeast Asia; Eastern Europe &
Central Asia; North America\
**Type of Threat:** Threats of Violence, Imprisonment, Infringement on
Rights, Discrimination, Attack on Freedom of Expression\
\
**Accept Urgent Appeals?** No\
\
**Description:** Peace Brigades International offers protective
accompaniment to human rights organizations to deter potential attacks
and provide moral support. While PBI does not work directly for
threatened organizations, they build international support networks and
pressure governments to protect their citizens. PBI also supports Peace
Education Programs.\
\
**Web site:** [www.peacebrigades.org](www.peacebrigades.org)\
London, Tel: +44 20 7065 0775

Urgent Action Fund for Women?s Human Rights and Urgent Action Fund Africa
-------------------------------------------------------------------------

**Where:** Global\
\
**Type of Threat:** Threats of Violence, Physical Assault, Imprisonment,
Lawsuit,Infringement on Rights, Discrimination, Attack on Freedom of
Expression\
**Language:** Arabic, Albanian, Bahasa, English, French, Nepali,
Spanish, Russian,\
\
**Accept Urgent Appeals?** Yes!\
\
**Description:** UAF and UAF-Africa operate Rapid Response Grant-making
programs to support women activists around: a) peace-building in
situations of armed conflict, escalating violence, or politically
volatile environments;b) potentially precedent-setting legal and
legislative actions; and c) protection of women human rights defenders.
Their Research, Publications, and Advocacy program is a resource for
activists, funders, and allies of women?s human rights activism.\
\
**Web site:** www.urgentactionfund.org\
USA, Tel: (+1) 303 442-2388 (all requests outside Africa)\
Kenya, Tel: (+254) 20 2931095 (all requests in Africa)\
**Email:** urgentact@urgentactionfund.org;
proposal@urgentactionfund-africa.or.ke

Witness
-------

**Where:** Global\
**Language:** English\
\
**Accept Urgent Appeals?** No\
\
**Description:** WITNESS uses video and online technologies to open the
eyes of the world to human rights violations. We empower people to
transform personal stories of abuse into powerful tools for justice,
promoting public engagement and policy change. WITNESS regularly
conducts on-site trainings with our Core Partners, teaching them how to
document human rights abuses safely and effectively with video and how
to use video to further their advocacy goals.\
\
**Web Site:** [www.witness.org](www.witness.org)\
New York, Tel: (+1) 718.783.2000

B. LEGAL NETWORKS
=================

Advocates for International Development (A4ID)
----------------------------------------------

**Description:** Advocates for International Development (A4ID)
mobilizes the skills and expertise of the legal profession to combat
poverty and inequality of opportunity worldwide. A4ID promotes awareness
of social, economic, and legal issues while strengthening the capacity
of citizen sector organizations.\
\
**Web site:** [www.a4id.org](www.a4id.org)\
**Email:** info@a4id.org

Cyrus R. Vance Center for International Justice
-----------------------------------------------

**Where:** Latin America, Africa, Global\
\
**Description:** The Cyrus R. Vance Center for International Justice
supports lawyers worldwide who promote access to justice, equitable
judicial systems, socially-oriented public policies, and confidence in
the legal profession. The Vance Center championed the Pro Bono
Declaration for the Americas and manages the Global Network for Justice
Initiatives (GNJI).\
\
**Web site:** www.nycbar.org/VanceCenter/index.htm;
[www.gnji.net](www.gnji.net)\
New York, Tel: (+1) 212 382-4718

Human Rights Law Network
------------------------

**Where:** India, South AsiaDescription: HRLN uses the legal system to
advance human rights. HRLN lawyers collaborate with human rights
organizations and grass-roots develop- ment collectives to defend the
rights of marginalized and vulnerable groups. HRLN provides pro bono
legal services and conducts public interest litigation, engages in
advocacy and campaigns, conducts legal awareness programs, investigates
violations, and publishes ?Know Your Rights? materials.\
\
**Web site:** www.hrln.org\
New Delhi, Tel: +91-11-24374501, 24376922

International Senior Lawyers Project
------------------------------------

**Where:** Global\
\
**Description:** ISLP provides volunteer legal services from skilled and
experienced attorneys to advance democracy and the rule of law, protect
human rights and promote equitable economic development worldwide.
Through the pro bono work of retired and active practitioners, working
independently and in law firms, ISLP helps governments and citizens
develop and implement legal reforms, assists programs that advance the
social and economic well-being of people in developing countries, and
builds the capacity of local organizations and professionals to meet the
needs of their communities.\
\
**Web site:** [www.islp.org](www.islp.org)\
New York, Tel: (+1) 212 895-1359

Lex Mundi Pro Bono Foundation
-----------------------------

**Description:** The Lex Mundi Pro Bono Foundation engages Lex Mundi?s
global network of 160 top-tier business law firms present in over 100
countries to provide pro bono legal assistance to social entrepreneurs.\
\
**Web site:** [www.lexmundiprobono.org](www.lexmundiprobono.org)\
Washington, DC, Tel: (+1) 202 429-8169

Public Interest Law Initiative (PILI)
-------------------------------------

**Where:** Central & Eastern Europe, Russia\
Description: PILI advances human rights around the world by stimulating
public interest advocacy and developing the institutions necessary to
sustain it. PILI is strengthening the use of law as an instrument for
achieving social justice.\
**Web site:** [www.pili.org](www.pili.org)\
Budapest, Tel: (+36) 1 461-5700\
Moscow, Tel: (+7) 795 628 00 20\
New York, Tel: (+1) 212 803-5381

C. INTERNATIONAL MECHANISMS
===========================

In addition to citizen sector organizations, inter-governmental
institutions offer additional support to human rights defenders and
individuals who have suffered human rights violations.

U. N. Special Representative on Human Rights Defenders
------------------------------------------------------

**Where:** Global\
**Accept Urgent Appeals?** Yes\
\
**Description:** The UN Special Representative on Human Rights Defenders
supports and gathers information on behalf of human rights defenders
around the world. The Special Representative operates in complete
independence of any state, is not a UN staff member, and does not
receive a salary.\
**Web site:**
http://[www2.ohchr.org/english/issues/defenders/](www2.ohchr.org/english/issues/defenders/)\
Geneva, Tel: (+41) 22 917 1234\
**Email a complaint:** urgent-action@ohchr.org\
\
**Additional Resources:**

-   Guidelines for submitting complaints\
    http://www2.ohchr.org/english/issues/ defenders/complaints.htm
-   UN Declaration on Human Rights Defenders\
    http://[www2.ohchr.org/english/issues/defenders/](www2.ohchr.org/english/issues/defenders/)declaration.htm

U.N. Office of the High Commissioner for Human Rights
-----------------------------------------------------

**Where:** Global\
**Accept Urgent Appeals?** Yes\
**Description:** The UN Office of the High Commissioner for Human Rights
(OHCHR) promotes and protects the enjoyment and full realization by all
people of all rights established in the Charter of the United Nations,
including the Universal Declaration of Human Rights.\
\
**Web site:**
http://[www2.ohchr.org/english/issues/defenders/](www2.ohchr.org/english/issues/defenders/)\
Geneva, Tel: (+41) 22 917 0656\
**Email a complaint:** civilsocietyunit@ohchr.org\
\
**Additional Resources:**

-   Universal Decl. of Human Rights
    http://[www.unhchr.ch/udhr/index.htm](www.unhchr.ch/udhr/index.htm)
-   International human rights instruments www2.ohchr.org/english/law/

Inter-American Commission of Human Rights (Washington, DC) and Inter-American Court of Human Rights (San Jose)
--------------------------------------------------------------------------------------------------------------

**Where:** the Americas\
**Languages:** English, French, Portuguese, Spanish\
**Accept Urgent Appeals?** Yes\
\
**Description:** The Inter-American Commission a) receives, analyzes,
and investigates petitions alleging human rights violations; b) observes
the general human rights situation in member states; c) carries out
on-site visits to analyze specific situations; and d) submits cases to
the Inter-American Court for litigation. The Inter-American Court issues
and enforces judgments. Both are comprised of representatives from
members of the Organization of American States.\
**Note:** Individuals and citizen sector organizations may directly
petition the Inter-American Commission, only after exhausting all
options within their State to address the situation.\
\
**Web Sites:** Inter-American Commission [www.cidh.org](www.cidh.org)\
Inter-American Court www.corteidh.or.cr

African Commission on Human and People?s Rights
-----------------------------------------------

**Where:** Africa\
**Languages:** English, French\
**Accept Urgent Appeals?** Yes\
\
**Description:** The African Commission promotes and protects human
rights across Africa through investigations of alleged violations,
recommendations to the State(s) involved, and ensuring appropriate
measures are taken. Recommendations are submitted to the Organisation of
African Unity (OAU) to monitor compliance.\
\
**Note:** Individuals, citizen sector organizations, and States party to
the African Charter may directly petition the Inter-American Commission,
only after exhausting all options within their State to address the
situation.\
\
**Web Sites:** African Commission [www.achpr.org](www.achpr.org)\
Banjul, Tel 220 39 29 62 Africa Union (Addis Ababa) www.africa-union.org

European Court of Human Rights
------------------------------

**Where:** Europe\
Languages: English, French\
**Accept Urgent Appeals?** Yes\
\
**Description:** the European Court of Human Rights ensures that States
respect the rights guaranteed by the European Convention on Human
Rights. The European Court examines complaints (known as ?applications?)
lodged by individuals, and issues binding judgments where the State is
found in violation of these rights.\
\
**Note:** Individuals may file complaints directly to the Court, only
after exhausting all options within their State to address the
situation.\
\
**Web Site:** www.echr.coe.int/ECHR

International Criminal Court
----------------------------

**Description:** Founded in part by the United Nations and based in The
Hague, the International Criminal Court tries individuals accused of
inter- national crimes including genocide, crimes against humanity, and
war crimes. Only States and the international communicate can bring
cases to the ICC. The ICC is an independent body and is based on a
treaty, joined by 105 countries.\
\
**Web Site:** www.icc-cpi.int

PSIPHON TOOL GUIDE
==================

Psiphon Tool Guide\
Censorship Circumvention
------------------------

**Lesson to read:\
? [The Internet](umbrella://lesson/the-internet)**\
**Download Location:** <https://psiphon.ca/en/download.html>\
**Computer requirements:** An internet connection, a computer running
Windows or an Android 2.2 phone or up (Psiphon 3 versions for iPhones
and Mac OS X are coming soon)\
**Version used in this guide:** Psiphon 3\
**License:** Free open-source software; GNU GPL Version 3\
**Level:** Beginner\
**Other reading:** <https://psiphon.ca/en/user-guide.html>\
**Time required:** 5 minutes

**Using Psiphon will give you:**\
? The ability to safely get around internet censorship to access blocked
websites and applications on your phone or computer.

### 1 Before you start

? **ALERT:** The Psiphon Team has discovered a specific instance of
malware disguised as a Psiphon 3 Windows executable. The malware is
being distributed as a zip file named "pisphone3.zip" on www.copy.com
and may be available from other sources. The zip file contains a
malicious binary named "pisphone3.exe" with the properties described
at [Virus
Total](https://www.virustotal.com/en/file/54201e181615c7eb18ee5a5ca3a0b7924cf3097ac5214fbee530741b6a6bc3da/analysis/1372262585/).
Note the misspelling of the name. This Windows executable is not
digitally signed by Psiphon Inc. Never run a fresh download of Psiphon
without checking its digital signature, as
described [here](https://psiphon.ca/en.html#is_my_psiphon_3_for_windows_authentic).\
? It should be noted that although Psiphon is does not allow individual
user?s IP addresses to be associated with any individual website
visited, Psiphon is intended primarily as a censorship evasion tool,
rather than one that guarantees anonymity.

### 2 Psiphon for Android

Download the appropriate version of Psiphon from
[here](https://psiphon.ca/en/download.html).

Click on a Psiphon APK link from within your Android email or browser to
begin the installation.

(If you get an error, you may need to [enable
sideloading](https://psiphon.ca/en/faq.html#android-enable-sideloading).)

When you launch the Psiphon app, it will automatically start connecting
to the Psiphon network.

When you see the Psiphon ?P? next to a key in the top left corner it
indicates Psiphon is running in VPN or Whole Device mode and all
applications are tunnelled through Psiphon.

Under the Status Tab, you will see a P in the centre of the screen. The
colour of this P indicates Psiphon?s connection status.\
? Grey: connecting\
? Red: not connected\
? Blue: connected

![](tool_psiphon1.png)

To run Psiphon in Tunnel *Whole Device* mode, you must have Android 4.0+
or a rooted phone. This option is unavailable for non-rooted phones with
an older version of Android.

Once the app has connected to the network, it will launch the built-in
Psiphon browser. Psiphon for Android does not automatically tunnel the
traffic for the default Android browser or other apps. By default, only
the Psiphon browser is tunnelled through the Psiphon network.

![](tool_psiphon2.png)

Once the Psiphon browser is open:\
? The P in the top left will show you Psiphon is running\
? The arrow on the centre left allows you to switch between open tabs\
? The X at the bottom of the page closes the current tab\
? The star at the bottom of the page bookmarks the current page\
? The + at the bottom of the page opens a new tab

### 3 Psiphon for Windows

Download the appropriate version of Psiphon from
[here](https://psiphon.ca/en/download.html), and run the program.

(You should [verify, here, that your copy of Psiphon for Windows is
authentic](https://psiphon.ca/en/faq.html#authentic-windows).)

When you run it, you should see a security prompt showing that this
program is a legitimate product of Psiphon Inc.

![](tool_psiphon3.png)

Psiphon automatically starts connecting when you run it. While it is
connecting, a spinning icon is displayed.

You can select one of the following tunnel modes: **VPN, SSH, or SSH+**

? We recommend that you **select the VPN** option, which means all of
your traffic automatically tunnels through Psiphon.\
? The key difference between SSH/SSH+ and VPN is that SSH is application
specific while a VPN encrypts all traffic on your computer. With VPN,
you turn on the VPN and then all your traffic is encrypted so the web
browser, Skype, and email would all bypass censorship as long as the VPN
is on.\
? In Psiphon?s SSH and SSH+ modes, it automatically sets the proxy
settings and traffic for applications that respect these settings tunnel
through Psiphon. These settings are respected by default by all major
web browsers. SSH plus obfuscation adds a randomized layer on top of SSH
to avoid protocol fingerprinting.\
? In SSH and SSH+ modes, Psiphon offers a split option where
international traffic is tunnelled through the proxy and domestic
traffic is not. Check the ?Don?t proxy...? option to enable split
tunnelling. When this option is on, unproxied domains are reported in
the message area.\
? Use SSH/SSH+ options if you want to access domestic sites quickly and
your threat model allows it. However we recommend **selecting the VPN
option**.

Connection to the Psiphon server is established when the green tick icon
is displayed on the left of the window.

![](tool_psiphon4.png)

When you close the program, Psiphon automatically disconnects. You can
also click on the icon to toggle the connection.

Remember that:\
? Because Psiphon 3 is VPN-based, it is able to proxy all of your
Internet traffic, not just websites\
? Traffic between your PC and the VPN server is encrypted, HOWEVER the
traffic between that server and a non-HTTPS website will not be
encrypted. (The same applies to other Internet services, such as when
connecting with Outlook or Thunderbird to a non-SSL email provider.)\
? If you have not established a connection, you are not using the VPN.
Just because you have Psiphon 3 sitting on your computer somewhere does
not mean your requests go through the proxy.\
? Web pages may load more slowly when using a VPN. This is normal and it
is because the browser is not connecting directly to the website\
? Some paid VPN services may be faster than free ones like Psiphon 3,
but you should be careful before trusting a business with your
information, as it could be shared with other organisations or sold to
other companies

JITSI TOOL GUIDE
================

Jitsi Tool Guide\
Secure Audio, Video and Instant Messaging
-----------------------------------------

**Lesson to read: [Making a Call](umbrella://lesson/making-a-call)**\
**Download Location:** <https://jitsi.org/Main/Download>\
**Computer requirements** All Windows Versions, Mac OS X, Ubuntu, Linux\
**Version used in this guide:** Jitsi 2.4\
**License:** Free and Open-Source Software\
**Level:** Beginner\
**Time required:** 15-20 minutes

### 1.1 Getting started

**Using Jitsi will give you:**\
? A secure alternative to Skype that encrypts calls, messages and video
all the way from your computer to the recipient's computer.\
? The ability to register various accounts that you may already have
(such as Facebook, MSN, Google Talk or Yahoo Messenger), with Jitsi and
use it to communicate in them simultaneously.\
? The ability to communicate securely and simultaneously with other
programs recommended in this app such as Pidgin, Adium and ChatSecure.

### 2.1 How to Install Jitsi

To install Jitsi, perform the following steps:

**Step 1.** Double click ?jisi-2.4-latest-x86.exe?; the *Open File -
Security Warning* dialogue box may appear. If it does, click ?Next? to
activate the *Windows Installer* screen, followed by the *Welcome to the
Jitsi Setup Wizard* window.

**Step 2.** Click ?Next? to activate the *End User License
Agreement* window; check the *I accept the terms in the License
Agreement* option to enable the *Next* button, and then click ?Next? to
activate the *Destination Folder* window.

**Step 3.** Click ?Next? to activate the *Additional Tasks* window and
accept the default settings as presented.

**Note:** Enabling the *Auto-start when computer restarts or
reboots* option may slow down the overall function of your computer,
especially if you already have multiple applications configured to run
when your computer starts up.

**Step 4.** Click ?Next? to activate the *Ready to Install
Jitsi* window, and then click ?Install? to activate the *Installing
Jitsi* window displaying the installation progress bar.

**Step 5.** Click ?Finish? to complete the installation process and
automatically launch the **Jitsi** *Sign in* window as follows:

![](tool_jitsi1.png)

**Note:** In some instances, installing and launching Jitsi for the
first time triggers a *Windows Security Alert* prompt screen, as shown
below.

**Step 6.** Select both **Private** and **Public** networks check-boxes,
and then click *Allow access*\*\*\* to see the *Jitsi Sign in window* or
main user interface window.

![](tool_jitsi2.png)

### 2.2 How to Add Accounts in Jitsi

Please note that even with Jitsi encryption, account providers
like Google or Facebook are monitoring the very fact that you are
communicating (and perhaps with whom you are communicating), and may
share this information with third-parties, such as corporations or
governments. Therefore it is perhaps best to avoid using those accounts
for very sensitive communication even with Jitsi encryption.

### 2.2.1 How to Add a Gmail/Google Account

**Note:** The example which follows is based on a Google Talk account,
the set-up process for the other communication protocols is similar.
Communications or some encryption features may not work between users of
different account providers (like Facebook, Gmail, Yahoo, etc.).
However, they should work when communicating between two accounts from
the same provider.

**Step 1.** Select **Start &gt;
Jitsi** or double-click the Jitsi desktop icon to open Jitsi.

**Step 2.** In the *sign in* window, type in the username and password
of the Gmail account you would like to use for chat purposes, so that it
resembles the following:

![](tool_jitsi3.png)

**Note:** You can add multiple accounts using different protocols at the
same time.

**Step 3.** Click ?Sign in? to activate your account chat window.

**Note:** If you closed *Sign in* window, or you want to add another
account, you can add it by selecting ***File &gt; Add new account...***
menu. In the new window select **Network** as *Google Talk* and type
in the user name and password of the Gmail account as shown on the image
below:

![](tool_jitsi4.png)

To verify that you have registered your Gmail account with Jitsi,
perform the following steps:

**Step 1.** Select **Tools &gt; Options** in the menu to activate the
following window:

![](tool_jitsi5.png)

**Note:** If you are using 2-step verification to protect access to
your Gmail account, when you try to log in from Jitsi with your regular
password you may see a message like the one below. To log in
using Jitsi, you will need to generate an "application-specific
password". See Google's [instructions on how to do
this](https://support.google.com/accounts/answer/185833?hl=en).

### 2.2.2 Registering new Jabber/XMPP or SIP account and adding it to Jitsi

### 

Jabber/XMPP and SIP are open standards of text and voice communication.
There are many servers that offer free accounts which you can use with
Jitsi. Below we are recommending some of the servers that you could use
for sensitive communication.

? **Riseup.net** Jabber/XMPP account

If you have account on the Riseup.net secure email service (located in
the USA) you may use this account also to communicate over Jabber/XMPP
network by adding this account to Jitsi - see below on how to add
existing Jabber/XMPP account.

? **Jabber.ccc.de** and other Jabber/XMPP accounts

You can register an account on Jabber.ccc.de server (located in Germany)
by taking following steps:

**Step 1.** In Jitsi, select ***File &gt; Add new account...*** in the
menu. In the new window, select ***Network:* XMPP** and check the
*Create a new XMPP account\*\*\* option*. In
*\*Server*, type jabber.ccc.de, type in the XMPP username you would like
to create, and fill in the *Password* and *Confirm* password fields so
that it resembles the following:

![](tool_jitsi6.png)

**Step 2.** Click **Add**. After successful registration you will be
presented with a window similar to that above.

If the username which you requested is already taken by somebody else,
the registration process will fail with the message *We failed to create
your account due to the following error: Could not confirm data*. You
can try again by repeating the process and selecting a different
username.

**Note** that if you do not log in to your jabber.ccc.de for longer than
12 months your account will be automatically removed from the server and
the username will become available for registration by other people.

? **ostel.co** SIP account

**SIP** accounts cannot be registered from within the Jitsi program.
The **ostel.co** server (located in USA) offers [registration on their
web page](https://ostel.co/users/sign_up). Select a username, password
and provide your existing email address and click the *Sign up* button
on the web page. After successful registration come back to Jitsi
program. Select ***File &gt; Add new account...*** in the menu, select
**Network: SIP**, type in your username (e.g.
terence.the.tester@ostel.co) and the password you created during the web
registration and click ***Add***. See following image for reference:

![](tool_jitsi7.png)

? **Adding existing Jabber/XMPP or SIP account to Jitsi**

If you already have Jabber/XMPP or SIP account you can add it
to Jitsi by selecting ***File &gt; Add new account...*** in the menu and
selecting the appropriate Network (either XMPP or SIP depending on the
account type).

### 2.2.3 How to Add a Facebook Account

Facebook has two settings that you may need to change before Jitsi can
connect to your Facebook Chat.

? **Facebook Username**

Facebook requires a username for Jitsi to connect to Facebook chat.
Many Facebook users already have a username. To check your username, log
in to your Facebook account: your username is what appear in the
location bar of your browser after *https://www.facebook.com/* when you
view your Timeline or Page. Your username is also in your Facebook email
address for your personal account (ex: username@facebook.com). You can
see or change the username or get one by going to your *Account
Settings &gt; General* section or by
visiting <https://www.facebook.com/username>. To set
username Facebook may ask you for your account verification which may
require sending SMS to a mobile phone number which you will need to
provide to Facebook in the process of verification.

? **App Settings**

Facebook?s ?application platform? must be turned on before **Jitsi** can
connect to Facebook Chat. Visit your Facebook *Account Settings &gt;
Apps* section and check that the setting for Apps you use is turned On.
This turns "application platform" on for your account.

**Note** that that turning Facebook?s "application platform" opens up
much of your Facebook data to third-party application developers. This
data is available not only to the Facebook applications that you use,
but also Facebook applications used by any of your friends. After
turning on Facebook?s "application platform", be sure to check the
settings under "Apps others use". This setting allows you to hide some
personal information from applications used by your friends.
Unfortunately, Facebook does not offer settings to hide all personal
information. Certain categories of information (like your friend list,
gender, or info you have made public) are visible as long as Facebook?s
"application platform" is turned "on". It is up to you to determine
whether this is an acceptable tradeoff of your privacy.

Now you are prepared to add your Facebook account to Jitsi. To do this
follow the steps below:

**Step 1.** From the main menu select ***File &gt; Add New Account...***

**Step 2.** In the Add New Account dialogue, **Network** menu
choose *Facebook*, enter your username and password and Click **"Add"**

![](tool_jitsi8.png)

### 2.3 How to change password for account with Jitsi

It is important element of security to know how to change the password
for each account that one has. Many of the accounts that you can use
with Jitsi offer changing password as a part of their settings, which
are accessible over web interface. However some Jabber/XMPP and SIP
account will not have any web interface to manage them. You can change
password for those account using Jitsi by following steps below:

**Step 1.** Select ***Tools &gt; Options*** in the
menu, select the ***Accounts*** tab

**Step 2.** Click on ***Edit*** button on the bottom to activate a new
window.

**Step 3.** Click on *Change account password* to activate *Change
account password* window.

**Step 4.** Enter new password and Re-enter password and click
on ***OK*** button to close this window.

**Step 5.** Close Account Registration Wizard.

### 2.4 How to configure Jitsi to improve it's security

### 2.4.1 Disable and remove call and chat history

Jitsi by default stores information about the incoming and outgoing
voice/video calls and the history of your text chats -- all messages
that you sent and received. You can access voice/video calls
by clicking on the clock icon on the main Jitsi window:

![](tool_jitsi9.png)

You can see the text chat history by clicking on the egg-timer like icon
in the text chat window while chatting with a contact:

![](tool_jitsi10.png)

Even if you encrypt the text chat with OTR all the text messages you
send and receive are stored on your computer in open text format.

 To prevent Jitsi collecting this information (and remove already
gathered data), you and your contact should take the following steps.

**To disable Jitsi from collecting the information:**

**Step 1.** Select *Tools &gt; Options* in the
menu, select the ***General*** tab and uncheck the ***Log chat
history*** option.

**Step 2.** in the *Options* window, first **select the Advanced** tab,
then **select the *Logging*** section, and then **uncheck the *Enable
packet logging*** option as shown below:

![](tool_jitsi11.png)

Your changes will take effect after you restart Jitsi.

**To remove already collected information about your calls and text
messages:**

**Step 1.** Quit Jitsi.

**Step 2.** Remove the entire log history folder *history\_ver1.0* from
the Jitsi user profile folder. You can remove a sub-folder of
*history\_ver1.0* if you want to dispose of only part of the history.
The location of the *user profile* and *log history* folders depends on
the operating system:

? On Windows XP and earlier, this is located in *C:\\Documents and
Settings\\&lt;Windows login/user name&gt;\\Application
Data\\Jitsi\\history\_ver1.0*\
? On Windows Vista, 7, 8, this is *C:\\Users\\&lt;Windows login/user
name&gt;\\AppData\\Roaming\\Jitsi\\history\_ver1.0*\
? Mac OS X: from your home folder *\~/Library/Application
Support/Jitsi/history\_ver1.0*\
? Linux: from your home folder *\~/.jitsi/history\_ver1.0*

See the [Secure Deleting lesson](umbrealla://lesson/safely-deleting) for
more on how to dispose of information securely.

### 2.4.2 Require private messaging when text chatting

It is recommended that you set Jitsi up to require private and encrypted
text messaging using OTR encryption whenever possible. To do
this, select ***Tools &gt; Options*** in the menu, select
the ***Security*** tab, select the *Chat* sub-tab and check ***Require
private messaging*** at the bottom of the screen.

### 2.4.3 Protect passwords to your accounts with master password

It is best not to let Jitsi remember passwords to your accounts. If you
decide otherwise for ease of use anybody who gets access to your
computer will be able to log in to your accounts by simply starting
Jitsi. It will also be possible to view your passwords in
the Options window. It is therefore **strongly recommended** to protect
passwords to your accounts with good master password. Once you set up
the master password, Jitsi will ask you for it upon starting the
program.

**Step 1.** Open the Options window
by selecting ***Tools &gt; Options*** in the menu, select
the ***Security*** tab and ***Passwords*** sub-tab, and check ***Use a
master password*** to activate the ***Master Password*** window.

**Step 2.** In the new window, type in your password. For more on
creating a strong password, see the **[Password
lesson](umbrella://lesson/passwords)**.

**Step 3. Click *OK*** to confirm the password and activate a new window
which should say ***Master Password successfully set up***. Click
"OK" to close it and come back to the *Options* window which should
resemble below:

![](tool_jitsi12.png)

**Note:** The ***Change Master Password*** button lets you change the
master password and the ***Saved Passwords...*** button lets you access
the list of passwords remembered by Jitsi and remove them if need be.

### Jitsi - Add contacts and communicate text & voice

### 3.1 Add contacts (buddies) to Jitsi

After adding at least one account to Jitsi and logging in, you are ready
to add your contacts and communicate with them.

**Step 0.** Open the Jitsi main window by selecting ***Start &gt;
Jitsi*** or double-clicking the Jitsi desktop icon.

**Step 1.** Select ***File &gt; Add contact...*** which will open the
following window:

![](tool_jitsi13.png)

**Step 2.** Select which of your accounts you would like to add this
contact to (for example *terance.the.tester@jit.si*).

**Optional:** You may also add the contact to a group among your other
contacts. However, first you must create the group. You can do this by
selecting *File &gt; Create group...* from the menu).

Type in your contact's user name or address into the ***ID or
Number*** field (for example, *sally.the.doer@jit.si*).

You can choose the name or nickname for the contact, which will be
visible in your contacts list in the Jitsi main window; type it into
the ***Display name*** field.

**Step 3.** Click on *Add* to close the *Add contact* window and come
back to Jitsi main window. In your contact list you will now see your
new contact added with the note "Waiting for authorisation".

**Step 4.** When your contact (sally.the.doer@jit.si) logs in to her
account, a pop-up window will inform her that you have requested to add
her to your list of contacts:

Your contact has a choice of selecting the *Ignore* option, in which
case your request will continue awaiting authorisation; *Deny*, in which
case you will receive information that your request was rejected;
and *Authorise*, in which case you will receive information that your
contact has accepted your authorisation request, and the entry for your
contact in your contact list will become active.

### 3.2 Text chat (Instant Messaging) with OTR encryption

Now that you added and authorised your contact, you can click on their
name in the contact list and initiate text conversation, voice or video
calls, and desktop sharing, by choosing the relevant icon under their
name:

![](tool_jitsi14.png)

Step 1. We will now explore one of Jitsi's most important features: the
ability to text chat securely, encrypting your messages with OTR. OTR
functions in a similar manner to GPG/PGP described in other chapters in
this toolkit. Just as with PGP, before you and your contact can encrypt
your communications, you both need to configure Jitsi to generate your
encryption keys. You can do this
by selecting ***Tools &gt; Options*** menu and selecting
the ***Security*** tab and ***Chat*** sub-tab. You will then see a
window similar to one shown in the image below:

![](tool_jitsi15.png)

**Step 2.** Next, click the ***Generate*** button. As a result you will
see the fingerprint of the key that has been generated:

![](tool_jitsi16.png)

One key is generated per account. You only need to do this again if you
add a new account or install Jitsi on another device and do not move the
existing keys to it.

Now you are ready to communicate:

**Step 3.** Select a contact from Jitsi main window and click on
the *send message* icon (first from the left under the contact's name)
to open a text chat window:

![](tool_jitsi17.png)

Note the *Encrypt chat with OTR* icon, the open padlock on the right-top
side of the window. This inconspicuous symbol informs you whether the
chat is encrypted or not. Now the lock is open (there is a tiny space
between handle and the body of the lock!).

**Step 4.** Click on the *Encrypt chat with OTR* icon. Note the changes
in the window:

![](tool_jitsi18.png)

Observe that the padlock is now locked. This means that whatever
messages you and your contact send to each other are encrypted. Note the
message that this is an *unverified private* conversation and that you
should *authenticate* sally.the.doer@jit.si.

**Step 5.** Click on the link ***authenticate
sally.the.doer@jit.si*** to open the *Authenticate Buddy* window:

![](tool_jitsi19.png)

Note the message that encourages you to compare the fingerprints of your
keys with your contact over another channel (not this text chat). In
doing this, you can be more certain that you are communicating with your
contact and not somebody else. A good choice for key comparisons is to
do it face to face, or via video or voice communication as these provide
easier means to authenticate the identity of the other person. After you
compare fingerprints, select the option ***I have verified*** the
fingerprint from the pull-down menu and click on ***Authenticate
Buddy***:

![](tool_jitsi20.png)

Closing the *Authenticate Buddy* window returns you to the chat window.

![](tool_jitsi21.png)

Note that padlock no longer includes the orange triangle with the white
exclamation mark. This means that you have authenticated your
contact. **The authentication should be done only once per contact.** If
the triangle with exclamation mark returns, it means that you are
chatting to somebody who you have not yet authenticated. This can happen
when your contact moves to another device with another encryption key
(another installation of Jitsi, or another OTR enabled program, etc.).
In this case you will need to re-authenticate each other again to be
sure of the identity of person with whom you communicate.

Jitsi allows you to text chat with more than one person in the same
time. OTR encryption will only work when chatting to one person.

### 3.3 Voice and video chat with ZRTP encryption

Jitsi offers voice and video chats which can be independently encrypted
with open standard called ZRTP. In order to initiate the chat you need
to

**Step 1.** Click on the contact in Jitsi contact list and click on the
voice (second icon from the left under the contact's name) or video
(third) icon. A new window will appear indicating that Jitsi is
establishing the connection:

![](tool_jitsi22.png)

Your contact will see an incoming call notification.

**Step 2.** If your contact accepts the call you will receive
information that you are connected:

![](tool_jitsi23.png)

**Note** the red open padlock. This means that your call is not yet
encrypted with ZRTP.

**Step 3.** Wait... Your and your contact's programs are establishing an
encrypted connection, which may take a moment. If they succeed you will
see the letters *zrtp* appear against an orange background with a closed
padlock like below. If they don't succeed in establishing a connection,
you still can chat but without encryption. You can disconnect,
restart Jitsi and try again to see if this time the programs will
connect with encryption. ZRTP may not work in calls between accounts
from different providers (such as between Google and Jit.si).

![](tool_jitsi24.png)

**Step 4.** Observe the section under the letters *zrtp* and padlock
with the message "Compare with partner" followed by 4
characters. Read these letters to your contact and ask if she sees the
same characters. If she does, it means that your communication is
encrypted and nobody is interfering with it. You
can click ***Confirm***. The orange *zrtp* field will turn green:

![](tool_jitsi25.png)

**Step 5.** You may close the black confirmation section of the window
by clicking on the white x sign on upper-right part of the black
section:

Jitsi lets you voice and video chat with more than one person. Note that
with this communication, ZRTP encryption can be engaged between
initiator of the call and other parties, but not between parties
themselves.

Why back-up?
============

Backing up is the copying and archiving of computer data so it can
retrieve it if something happens to the original. Years of work can
disappear in an instant as a result of theft, carelessness,
confiscation, or breakage, so it is extremely important to have an
up-to-date backup and a well-tested means of restoring it.

Creating an effective backup policy can be tricky for a few reasons:

-   The need to store original data and backups in different physical
    locations;
-   The importance of keeping backups confidential;
-   The challenge of coordinating among different people who share
    information with one another using their own portable
    storage devices.

In addition to backup and file-recovery tactics, this lesson addresses
two specific tools, Cobian Backup and Recuva.

Surveillance
============

Surveillance is the monitoring of people?s behaviour, activities, or
other patterns for the purpose of harming, influencing, managing,
directing, or protecting them.

![](surveillance1.png)

**Why might people be interested in keeping you under physical
surveillance?**

-   Break-in/ theft of sensitive materials
-   Arrest
-   Monitor who is coming and going from the office
-   Intimidation
-   Physical attack on staff

**Who might be interested in keeping you under surveillance?**

-   Authorities of the country in which the regional office is located
    (police, intelligence, military)
-   External security agencies of other countries in the region
-   Criminals
-   Terrorists
-   Private contractors
-   Embassy officials of ?friendly? countries
-   Individuals (may be disgruntled with the organisation)

### If you are having a digital security emergency, the following are useful resources.

IMMEDIATE SUPPORT
=================

Normally available for support within the first 24 hours

Digital Security First Aid Kit
------------------------------

**Where:** Global\
\
**Type of Threat:** Digital security incidents, website/social media
breaches, seized devices, DDoS mitigation, malware\
Accept Urgent Appeals? No\
\
**Description:** The Digital First Aid Kit aims to provide preliminary
support for people facing the most common types of digital threats. The
Kit offers a set of self-diagnostic tools for human rights defenders,
bloggers, activists and journalists facing attacks themselves, as well
as providing guidelines for digital first responders to assist a person
under threat.\
\
**Web site:** <https://digitaldefenders.org/digitalfirstaid/>

Digital Security Helpline
-------------------------

**Where:** Global\
**Type of Threat:** Digital security incidents, website/social media
breaches\
**Accept Urgent Appeals?** No\
\
**Description:** The Digital Security Helpline is a free of charge
resource for civil society around the world. It is run by the
international human rights organization Access. It provides rapid
response on digital security incidents, tool recommendations and support
for securing technical infrastructure, websites and social media against
attacks.\
\
**Web site:** www. accessnow.org\
**Email:** help@accessnow.org

Tactical Technology Collective
------------------------------

**Where:** Global\
**Type of Threat:** Digital and information security tools and manuals\
**Accept Urgent Appeals?** No\
\
**Description:** We have three focal areas: understanding & shaping
issues; digital security and privacy; and data politics. They work to
raise awareness, build practical skills and offer both critical
reflection and inspiration in all of these areas. Through trainings and
workshops they provide direct support to over 2000 advocates a year,
either through intensive training in small groups, or through 'flash
trainings' or clinics at large-scale gatherings and conferences.\
\
**Web site:** [www.tacticaltech.org](www.tacticaltech.org)\
**Email:** ttc@tacticaltech.org\
Berlin, Tel: (+49) (0) 30 41 71 53 33\
Bangalore, Tel: (+ 91) (0)80 4153 1129

REDPHONE TOOL GUIDE
===================

RedPhone Tool Guide\
Encrypted phone calls for Android
---------------------------------

**Lesson to read:\
? [Making a Call](umbrella://lesson/making-a-call)**\
**Download Location:** [; can also be downloaded from
the ](https://whispersystems.org/)[Google Play
store](https://play.google.com/store/apps/details?id=org.thoughtcrime.redphone)\
**Computer requirements:** Android 2.2 and up\
**Version used in this guide:** RedPhone 0.9.6\
**License:** Free Open-Source Software; GPLv3\
**Level:** Beginner-Intermediate\
**Other reading:** <http://support.whispersystems.org/>\
**Time required:** 15 minutes

**Using RedPhone will give you:**\
? The ability to make encrypted voice calls over a Wi-Fi or data
connection using your normal phone number

NOTE: RedPhone only encrypts calls that are between two RedPhone users,
or between users of RedPhone and Signal, the app for iPhones. (See
[Signal Tool Guide](umbrella://lesson/signal) for instructions for
iPhones)

### 1.0 How to install RedPhone

**Step 1:** Download and install RedPhone

On your Android phone, enter the Google Play store and search for
?RedPhone.? Select the app, ?RedPhone :: Secure Calls.?

Select ?Install? and accept the Terms of Service by selecting ?Accept.?
The app will download and install automatically.

![](tool_redphone1.png)

**Step 2:** Register your mobile

Once you have installed the app, open it; you will automatically be
prompted to register your mobile number.

![](tool_redphone2.png)

Once you have registered your mobile number, RedPhone will send you an
SMS code to verify that the number belongs to you. Type in the code when
prompted by the app. You have now successfully installed RedPhone and
are ready to make encrypted calls!

### 2.0 Using RedPhone

In order to use RedPhone, the person that you are calling must also have
RedPhone (or Signal) installed. If you try to call someone using the
RedPhone app and they do not have it installed, the app will ask if you
would like to invite them to use RedPhone via SMS, but it will not allow
you to complete your call from inside the app.

![](tool_redphone3.png)

When you make a call to another RedPhone or Signal user (from either
your default system dialer or from inside the app), you will be given a
random pair of words. This word pair will allow you to verify your
identity and keys with the other user?also known as key verification.

![](tool_redphone4.png)

The trustworthiest way to verify the identity of a caller is to use
out-of-band authentication to verify the word pair. You can also read
the words aloud if you recognize the caller?s voice, although very
sophisticated attackers might be able to defeat this if they needed to.
The word pair must be identical.

PGP FOR LINUX TOOL GUIDE
========================

PGP for Linux Tool Guide\
Encrypted email for Linux
-------------------------

**Lesson to read:\
? [Email](umbrella://lesson/email)**\
**Computer requirements:** An internet connection, a computer running
Linux, an email account\
**Version used in this guide: **\
? Linux: Debian 7.0 ("Wheezy")\
? Mozilla Thunderbird 24.8.1\
? Enigmail 1.6\
? GPG4Win 1.4.18\
**License:** Free Software; mix of Free Software licenses\
**Level:** Expert\
**Other reading:** <https://www.gnupg.org/documentation/guides.html>\
**Time required:** 30-60 minutes

**Using PGP will give you:**\
? The ability to protect your email communications from being read by
anyone except their intended recipients.\
? The ability to prove that an email came from a particular person,
instead of being a fake message sent by another sender (it is otherwise
very easy for email to be fabricated). Both of these are important
defenses if you're being targeted for surveillance or misinformation.

### 1.0 Before you start

To use Pretty Good Privacy (PGP), you will need to install some extra
software that will work with your current email program. You will also
need to create a private key, which you will keep private. The private
key is what you will use to decrypt emails sent to you, and to digitally
sign emails that you send to show they truly came from you. Finally,
you'll learn how to distribute your public key?a small chunk of
information that others will need to know before they can send you
encrypted mail, and that they can use to verify emails you send.

This guide will show you how to use PGP with a Linux-style operating
system using Mozilla Thunderbird, a popular open source graphical email
client.

You can't currently use PGP directly with a web email service like
Gmail, Hotmail, Yahoo! Mail, or Outlook Live. You can still use your
webmail address; you?ll just have to configure it with the Thunderbird
program on your computer.

**Note that both ends of the email conversation need to be using
PGP-compatible software for it to work.**

People will normally use this only on their own personal devices, not on
shared devices. Fortunately, PGP is available for most desktop computers
and mobile devices, and you can point them to these guides to help them
set up their own version.

### 2.0 Installing Thunderbird, GnuPG and Enigmail

PGP is an open standard, which means that more than one piece of
software can use it. The software we're going to use for PGP is called
GnuPG. We'll also be adding a plug-in to Thunderbird called Enigmail,
which lets you use GnuPGP from within Thunderbird. The following
instructions require some comfort with the command line.

If you're using using a Red Hat-based distribution such as Red Hat or
Fedora Core, open a terminal and run these commands:

*sudo yum install gnupg thunderbird thunderbird-enigmail*

If you are using a Ubuntu-based distribution such as Ubuntu, or Linux
Mint, open a terminal and type these commands to make sure you have the
right software installed:

*sudo apt-get install gnupg thunderbird enigmail*

If you're using the Debian distribution, you'll find that Thunderbird is
called ?Icedove.? Like Debian in general, this is for entirely
reasonable but somewhat obscure reasons. Apart from the name, it's
exactly the same program: we'll not mention Icedove again, but you can
just replace ?Thunderbird? with Icedove in the rest of this guide, and
everything should still work.

Use this command in the Terminal to install it:

*sudo apt-get install gnupg icedove enigmail*

### 2.1 Configuring Thunderbird

Now that you've installed Thunderbird, open it as you would another
application on your machine (you might pick it from a list of
applications on a menu, or type its name into an application search).
You will see the first run wizard appear.

![](tool_pgplin1.png)

To set up your existing email address, click "Skip this and use my
existing email,? and then enter your name, email address, and the
password to your email account.

![](tool_pgplin2.png)

If you use a popular free email service like Gmail, Thunderbird should
be able to automatically detect your email settings when you click
?Continue.?

**If you use two-factor authentication with Google (and depending on
your threat model you probably should!) you cannot use your standard
Gmail password with Thunderbird. Instead, you will need to create a new
application-specific password for Thunderbird to access your Gmail
account. See [Google's own
guide](https://support.google.com/mail/answer/1173270?hl=en) for doing
this.**

![](tool_pgplin3.png)

If it doesn't, you may need to manually configure your IMAP and SMTP
settings. If you don?t know how to do this, talk to your email provider,
or ask someone technical who is familiar with your email provider (so,
an IT person at work, or a technical friend who uses the same ISP as
you; they don't need to know how to use PGP, but you can ask them ?Do
you know the IMAP and SMTP settings for my email address??).

### 2.2 Configuring Enigmail

Enigmail is a plugin for Thunderbird that encrypts and decrypts
PGP-encoded emails, and makes handling private and public keys a little
easier. If you have the latest version of Enigmail, you should be
presented with the Enigmail Setup Wizard.

![](tool_pgplin4.png)

If you don't see it, you can use this menu option from Thunderbird to
make it appear. Click on the three horizontal lines (the ?hamburger
menu?) on the right of the Thunderbird window.

![](tool_pgplin5.png)

Here's the first option that Enigmail offers you: three options for
handling when to encrypt your mail.

![](tool_pgplin6.png)

The default option is to encrypt emails if you have the ?public key? of
another person, Enigmail will encrypt the email you send but leave
emails unencrypted if you don't have the public key of the recipient
yet. You also have the option to encrypt emails all the time to everyone
with PGP keys, which means that you will have to find the public keys
for people for whom you don't have them already, or turn off automatic
encryption completely and only use PGP when directed.

We don't know what the appropriate option is for you, but believe the
?Convenient auto encryption? option to be a good choice. If you are in
doubt, choose ?Don't encrypt my messages by default.?

Click the ?Next? button.

![](tool_pgplin6.png)

Now you have an option to digitally sign all outgoing emails. Signing
your email with PGP allows the recipient to check that you sent the
message, and that the contents of the message were not tampered with.
Click the ?Sign my messages by default? button to turn this feature on.

The downside of doing this, however, is that it can also flag to anyone
you send mail to that you use PGP. [In some parts of the
world](www.cryptolaw.org/) (including China, Iran, Belarus, and some
Middle-East states) using unlicensed encryption, even for personal use,
is illegal, so you might have very good reasons to not let others know
you use PGP.

Click the ?Next? Button.

Now you'll see an option to have Enigmail make some changes to the
configuration of Mozilla Thunderbird.

![](tool_pgplin7.png)

If you click the Details button you can review what those changes are.

The following options can be unchecked (reenabled), for a more seamless
transition, if you use PGP/Mime by default (we'll set that later):\
? Disable flowed text\
? View message body as plain text\
? Do not compose HTML messages

The final option prevents potential problems in the encryption and
decryption of your email. Be aware that selecting this box will remove
the ability to send text that is bolded, underlined or colored. After
reviewing the changes, click the ?OK button.?

Now you will start creating your private key and public key.

### 2.3 Creating a public key and private key

Installation and setup of the Enigmail add-on is complete. Now you'll
have the option of creating your public and private key pair. This
assumes you have not created a private key before.

![](tool_pgplin8.png)

Click the ?Next? button.

Unless you have already configured more than one email account, Enigmail
will choose the email account you've already configured. The first thing
you'll need to do is come up with a strong passphrase for your private
key. See the **[Passwords lesson](umbrella://lesson/passwords)** for
more information on how to do this.

Enigmail will display some information about your private key as well as
the configuration settings. We recommend creating 4096-bit length keys.
Click the ?Next? button.

![](tool_pgplin9.png)

**Your key will expire at a certain time; when that happens, other
people will stop using it entirely for new emails to you, though you
might not get any warning or explanation about why. So, you may want to
mark your calendar and pay attention to this issue a month or so before
the expiration date.**

It's possible to extend the lifetime of an existing key by giving it a
new, later expiration date, or it's possible to replace it with a new
key by creating a fresh one from scratch. Both processes might require
contacting people who email you and making sure that they get the
updated key; current software isn't very good at automating this. So
make a reminder for yourself; if you don't think you'll be able to
manage it, you can consider setting the key so that it never expires,
though in that case other people might try to use it when contacting you
far in the future even if you no longer have the private key or no
longer use PGP.

Enigmail will generate the key and when it is complete, a small window
will open asking you to generate a revocation certificate. This
revocation certificate is important to have as it allows you to make the
private key and public key invalid. It is important to note that merely
deleting the private key does not invalidate the public key and may lead
to people sending you encrypted mail that you can't decrypt.

![](tool_pgplin10.png)

Click the ?Generate Certificate? button.

A window will open to provide you a place to save the
revocation certificate. While you can save the file to your computer, we
recommend saving the file on a USB drive that you are using for nothing
else and storing the drive in a safe spot. We also recommend removing
the revocation certificate from the computer with the keys, just to
avoid unintentional revocation.

Even better, save this file on a separate encrypted disk. Choose the
location where you are saving this file and click the ?Save? button.

Now Enigmail will give you further information about saving the
revocation certificate file again. Click the ?OK? button.

Finally, you are done with generating the private key and public key.
Click the ?Finish? button.

### 2.4 Optional steps

### 2.4.1 Display long key-IDs

The next steps are completely optional but they can be helpful when
using OpenPGP and Enigmail. Briefly, the Key ID is a small part of the
fingerprint. When it comes to verifying that a public key belongs to a
particular person the fingerprint is the best way. Changing the default
display makes it easier to read the fingerprints of the certificates you
know about. Click the configuration button, then the Enigmail option,
then Key Management.

![](tool_pgplin11.png)

A window will open showing two columns: Name and Key ID.

![](tool_pgplin12.png)

On the far right there is a small button. Click that button to configure
the columns. Unclick the Key ID option and click the Fingerprint option.

![](tool_pgplin13.png)

Now change the width of the Fingerprint column by moving the mouse to
the lines between each column heading (that is, just to the left of the
?Key ID? header at the top of the list of keys), and dragging the line
to the left. Keep moving left until you can see all of the Key ID, like
this:

Now the columns will look like this:

![](tool_pgplin14.png)

Now you are set up to send and receive regular and encrypted email. Next
you will go through the steps of actually finding the people to exchange
encrypted mail with.

**Using PGP doesn't completely encrypt your email so that the sender and
receiver information is encrypted. Encrypting the sender and receiver
information would break email. Using Thunderbird with the Enigmail
add-on gives you an easy way to encrypt and decrypt the content of your
email.**

### 3.0 Letting others know you are using PGP

**a) Let people know you are using PGP with an email**

You can easily email your public key to another person by sending them a
copy as an attachment.

Click the ?Write? button in Mozilla Thunderbird.

Fill in an address and a subject, perhaps something like ?my public
key,? click the Enigmail menu and select the ?Attach My Public Key?
option.

![](tool_pgplin15.png)

You can now the email and the recipient will be able to download and use
the public key you sent.

**If this method is used, it's a good idea to have the recipient verify
your public key's fingerprint over some other form of communication, in
case email is already being intercepted and tampered with.**

**b) Let people know you are using PGP on your website**

In addition to letting people know via email, you can post your public
key on your website. The easiest way is to upload the file and link to
it. This guide won't go into how to do those things, but you should know
how to export the certificate as a file to use in the future.

Click the configuration button, then the Enigmail option, then Key
Management.

Highlight your certificate in bold, then right-click to bring up the
menu and select Export keys to file.

![](tool_pgplin16.png)

A small window will pop up with three buttons. Click the ?Export Public
Keys Only? button.

![](tool_pgplin17.png)

**Make sure you don't click the ?Export Secret Keys? button because
exporting the secret key could allow others to impersonate you if they
are able to guess your password.**

Now a window will open so you can save the file. In order to make it
easier to find in the future please save the file to the Documents
folder.

Now you can use this file as you wish.

**c) Uploading to a keyserver**

Keyservers make it easier to search for and download public keys. Most
modern keyservers are synchronizing, meaning that a public key uploaded
to one server will eventually reach all servers.

Although uploading your public key to a keyserver might be a convenient
way of letting people know that you have a public PGP certificate, you
should know that due to the nature of how keyservers work, there is no
way to delete public keys once they are uploaded, you can only mark them
as revoked.

**Before uploading your public key to a keyserver, it is good to take a
moment to consider whether you want the whole world to know that you
have a public key without the ability to remove this information at a
later time.**

If you choose to upload your public key to keyservers, you will go back
to the Enigmail Key Management window.

Click the Keyserver menu item and select the Upload Public Keys option.

![](tool_pgplin18.png)

### 3.1 Finding other people who are using PGP

**a) Getting a public key by email**

You might get a public key sent to you as an email attachment.

![](tool_pgplin19.png)

Notice the attachment at the bottom of the window. Right-click on the
attachment and select ?Import OpenPGP Key.? A small window will open
giving you the results of the import. Click the OK button.

If you open up the Enigmail key management window again, you can check
the result. Your PGP key is in bold because you have both the private
key and the public key. The public key you just imported is not bold
because it doesn't contain the private key.

![](tool_pgplin20.png)

**b) Getting a public key as a file**

It's possible that you get a public key by downloading it from a website
or someone might have sent it through chat software. In a case like
this, you will assume you downloaded the file to the Downloads folder.

Open the Enigmail Key Manager and click on the ?File? menu. Select
?Import Keys from File.?

The public key might have very different file name endings such as .asc,
.pgp, or .gpg. Select the file and click the ?Open? button. A small
window will open, giving you the results of the import. Click the ?OK?
button.

**c) Getting a public key from a key server**

Keyservers can be a very useful way of getting public keys. Try looking
for a public key. Open up the key manager then click the ?Keyserver?
menu and select ?Search for Keys.?

![](tool_pgplin21.png)

A small window will pop up with a search field. You can search by a
complete email address, a partial email address, or a name. In this
case, you will search for certificates containing ?eff.org.?

![](tool_pgplin22.png)

A larger window will pop up with many options. If you scroll down you'll
notice some certificates are italicized and grayed out. These are
certificates that have either been revoked or expired on their own.

![](tool_pgplin23.png)

Let's take the public keys of Danny O'Brien for example, he has one
expired or revoked certificate and one valid certificate. Select the
valid certificate by clicking the box on the left then press the OK
button.

![](tool_pgplin24.png)

In some cases a person may have more than one certificate, all appearing
valid. Note that it's possible for anyone to upload a public certificate
for anyone else, and that one of these keys may not belong to the person
that owns the email address associated with it. In this case, verifying
the fingerprint is extremely important.

A small notification window will pop up letting you know if you
succeeded, and the Enigmail Key Manager will now show you the added
certificates:

![](tool_pgplin25.png)

### 4.0 Sending PGP encrypted mail

Now you will send your first encrypted email to a recipient. In the main
Mozilla Thunderbird window click the ?Write? button. A new window will
open.

Write your message, and enter a recipient. For this test, select a
recipient whose public key you already have. Enigmail will detect this
and automatically encrypt the email (you can tell it will be encrypted
by the golden key at the bottom right of the email).

![](tool_pgplin26.png)

**Note that the subject line won't be encrypted, so choose something
innocuous, like ?hello.?**

When you click the ?Send? button, you'll be given a window to enter the
password to your PGP Key. Remember this is different from your email
password!

Enter your password then click the ?OK? button and your email will be
encrypted and sent.

The body of the email was encrypted and transformed. For example our
text above, was converted to this:

![](tool_pgplin27.png)

### 4.1 Receiving PGP encrypted mail

Let's go through what happens when you receive encrypted email. First,
click on the message.

A small window opens asking you for the password to the PGP key.
Remember: Don't enter your email password. Click the ?OK? button.

![](tool_pgplin28.png)

Now the message will show up decrypted

![](tool_pgplin29.png)

### 5.0 Revoking the PGP Key

**a) Revoking your PGP Key through the Enigmail interface**

The PGP keys generated by Enigmail automatically expire after five
years. So if you lose all your files, you can hope that people will know
to ask you for another key once the key has expired.

You might have a good reason to disable the PGP key before it expires.
Perhaps you want to generate a new, stronger PGP key. The easiest way to
revoke your own PGP key in Enigmail is through the Enigmail Key Manager.
Right-click on your PGP key (it's in bold), and select the ?Revoke Key?
option.

![](tool_pgplin30.png)

A window will pop up letting you know what happens and asking for your
confirmation. Click the ?Revoke Key? button.

![](tool_pgplin31.png)

The password window opens, enter your password for the PGP key and click
the ?OK? button.

Now a new window will open up letting you know you succeeded. Click the
?OK? button.

When you go back to the Enigmail Key Management window you'll notice a
change to your PGP key. It is now grayed out and italicized.

![](tool_pgplin32.png)

**b) Revoking a PGP Key with a revocation certificate**

As mentioned before, the PGP keys generated by Enigmail automatically
expire after five years. So if you lose all your files you can be sure
that people will know to ask you for another key once the key has
expired.

Like we mentioned before, you might have a good reason to disable the
PGP key before it expires.

Similarly, others might have good reasons to revoke an existing key.

You might get sent revocation certificates from friends as a notice that
they want to revoke their key.

In the previous section you might have noticed that Enigmail generates
and imports a revocation certificate internally when you use the
Enigmail Key Manager to revoke a key. Since you already have a
revocation certificate, you will use the one you generated earlier to
revoke your own key.

Start with the Enigmail Key Manager and click the ?File? menu and select
?Import Keys from File.?

![](tool_pgplin33.png)

A window will open up so you can select the revocation certificate.
Click on the file, and click the ?Open? button. You'll get a
notification that the certificate was imported successfully and that a
key was revoked. Click the ?OK? button.

![](tool_pgplin34.png)

Once you click the ?OK? button, you'll be taken back to the Enigmail Key
Manager and you see the certificate you revoked greyed out and
italicized.

![](tool_pgplin35.png)

If the key you revoked is your own, and you previously uploaded your
public key to the key servers, you will want to re-upload the
now-revoked key to the key servers, so that others see not to use it
anymore.

Now that you have all the proper tools, try sending your own
PGP-encrypted email.

ORBOT AND ORWEB TOOL GUIDE
==========================

Orbot & Orweb Tool Guide\
Circumvention and anonymity online for Android
----------------------------------------------

**Lesson to read: [The Internet](umbrella://lesson/the-internet)**

**Download Location: **\
? Orbot: <https://guardianproject.info/apps/> or from [Google
Play](https://play.google.com/store/apps/details?id=org.torproject.android)\
? Orweb: <https://guardianproject.info/apps/> or from [Google
Play](https://market.android.com/details?id=info.guardianproject.browser)\
**Phone requirements:**\
? Android 2.3 and up (Android 1.6 and up for Orweb)\
**Version used in this guide: **\
? Orbot: 14.0.4.3\
? Orweb: 0.6.1\
**License: **\
? Orbot: Freeware ? BSD\
? Orweb: Free and Open Source Software (GPL v3)\
**Level:** Advanced\
**Time required:** 30-40 minutes

**Using Orbot & Orweb combined will give you:**\
? The ability to conceal your digital identity from the websites that
you visit.\
? The ability to conceal the websites you visit from Internet Service
Providers (ISPs) and other surveillance mechanisms.\
? The ability to bypass Internet censorship and filtering rules.

**ORBOT**

![](tool_orbot1.png)

### 1.1 Things you should know about this tool before you start

Orbot provides Android devices with access to the Tor Network. Form more
information see the **[Internet
lesson](umbrella://lesson/the-internet)**

### 2.0 How to Install Orbot

**Step 1:** On your Android device, download and install the app from
the [Google Play store
here](https://play.google.com/store/apps/details?id=org.torproject.android).

 ![](tool_orbot2.png)

**Step 2:** Before the installation process begins, you will be prompted
to review the access the application will have on your phone. Review
this carefully. Once you are happy with the permissions that will be
granted, press ?Accept? and the installation will complete. If you do
not agree with the permissions that will be granted, press the back
button and the installation will be cancelled.

### 2.1 How to Configure Orbot

Using Orbot for the first time

**Step 1:** To open Orbot you tap the application's icon.

![](tool_orbot3.png)

**Step 2:** Tap the language that you want and then tap ?Next?.

**Step 3:** A configuration wizard will appear with a description of
Orbot. Read it and tap ?Next?.

**Step 4:** You will then be presented with a warning screen. Once you
have read this and understand the requirements tap ?Next?.

![](tool_orbot4.png)

**Step 5:** A screen will appear asking you to grant Orbot Superuser
access. Superuser access requires that your device is rooted if you want
to make use of Orbot's Transparent Proxy features - we will not explore
this feature in the Orbot guide. (For information about rooting your
phone, see the **[Mobile Phones, Expert
lesson](umbrella://lesson/mobile-phones)**.)

If your smartphone is not rooted, just tick the option that states *I
understand and would like to continue without Superuser*. The next
screen explains in order for you to benefit from Tor, you will need to
use apps built to work with Orbot, or that support HTTP or SOCKS proxy.

![](tool_orbot5.png)

**Step 6:** A list of applications that work with Orbot will appear.
Take note of them and tap ?Next?.

![](tool_orbot6.png)

**Step 7:** Orbot configuration is now complete. A final screen
describing the typical users of Tor and Orbot will appear, once you have
read this tap ?Finish?.

![](tool_orbot7.png)

**Step 8:** After pressing ?Finish? you will be presented with the
deactivated Orbot screen.

![](tool_orbot8.png)

### 3.0 Basic Usage

### 3.0.1 Starting and Stopping Orbot

**Step 1:** Touch and hold the grey Orbot icon in the centre of the
screen until it turns yellow and says *Orbot is starting*.

![](tool_orbot9.png)

**Step 2:** The first time you start Orbot a notification will appear to
confirm you connected successfully to the Tor network. You will only see
the notification screen the first time you start Orbot after
installation. Tap ?OK? to see the green Orbot indication that Orbot is
running.

![](tool_orbot10.png)

** Step 3:** To disconnect Orbot you touch and hold the
green Orbot until it turns grey. Or if you want to disconnect and quit
Orbot, tap the menu icon (three vertical dots in the top right of the
screen) in the top right of the screen and select ?Exit?.

![](tool_orbot11.png)

### 3.0.2 Browsing the internet anonymously

In order to browse or chat on the internet anonymously, you need to
install an app which can route your browsing through a proxy in
conjunction with Orbot. This is what Orbweb, the tool outlined below
will do for you.

### 3.1 Advanced Usage

### 3.1.1 New Identity

If at any stage you want to appear to come from a new location, you can
get a *new identity* from Orbot by swiping *left* or *right* on the
green Orbot image. The image will briefly spin and then display *You've
switched to a new Tor Identity*.

![](tool_orbot12.png)

### 3.1.2 Using Bridges

If Tor access is restricted or illegal in your country, or you wish to
disguise the fact that you are using Tor, you can configure Orbot to
use bridges.

**Step 1:** Tap the icon with three staggered dots at the top of the
screen to be brought to the settings screen.

**Step 2:** Scroll down to the bridges section and check the box next
to Use Bridges.

![](tool_orbot13.png)

**Step 3:** Tap the Bridges section underneath *Use Bridges* to be
presented with a screen to enter the *IP address* of the *bridge* you
want to use. Once correctly entered, tap ?OK?. Restart Orbot to begin
using the *bridge*.

![](tool_orbot14.png)

### 3.1.3 Auto Starting Orbot

To make sure you never forget to start Orbot it can be configured to
start when you turn on your Android Device.

**Step 1:** Tap the icon with three staggered dots at the top of the
screen to be brought to the settings screen.

**Step 2:** Check the *Start Orbot* on boot option at the top of the
settings screen.

![](tool_orbot15.png)

**ORWEB**

![](tool_orbot16.png)

### 1.1 Things you should know about this tool before you start

Orweb is a free Android-platform mobile phone application, created by
the Guardian Project for browsing the internet anonymously in
conjunction with Orbot.

**Note:** There is a bug in the current version of Orweb (0.6.1 and
older) that may leak information about you, such as your IP address, to
the website owners if you are viewing HTML5 based videos. Orweb will
still allow you to circumvent censorship and prevent you from being
spied on by your Internet Service Provider (ISP) but we do not recommend
itto be used to view sites that may be considered hostile. For more
information on the issue see the developers' response.

Orweb will only work properly after installing and configuring Orbot.

Remember, if you previously created a mail or blog without using Orweb,
the site will still know your real location even if you return
using Orweb.

If you want stronger anonymity while using Orweb other steps need to be
taken including:

? Never access accounts made in your real name\
? Never give your personal data\
? Never do the same things that you do when not trying to be anonymous.

For an alternative that works with iOS on iPhones,
use [OnionBrowser](https://mike.tig.as/onionbrowser/).

### 2.0 How to Install Orweb

**Step 1:** On your Android device, download and install the app from
the [Google Play store
here](https://play.google.com/store/apps/details?id=info.guardianproject.browser)
by tapping ?Install?.

![](tool_orbot17.png)

**Step 2:** Before the installation process begins, you will be prompted
to review the access the application will have on your phone. Review
this carefully. Once you are happy with the permissions that will be
granted, press ?Accept? to start the installation. If you do not agree
with the permissions that will be granted, press the back button and the
installation will be cancelled.

**Step 3:** Once Orweb downloads and installation has completed, you can
press ?Open? to start the application.

### 3.0 Basic Usage

**Using Orweb for the first time**

**Step 1:** To open Orweb you tap the application's icon.

![](tool_orbot18.png)

**Step 2:** Orweb will launch and automatically try to connect
to *https://check.torproject.org*, to ensure that its connection to
the Tor network is working. If it can connect, you will see a message
telling you that your *browser is configured to use Tor*. If
Orweb cannot connect to the website you will see an error message in the
browser. If this happens, it is suggested that you check that Orbot is
installed and running corectly on your android device if this happens.

![](tool_orbot19.png)

** Step 3:** To browse to websites, tap the area at the top of the
screen to the right of the Orweb icon and type in the address you want
to visit. Press ?Go? on the onscreen keypad.

![](tool_orbot20.png)

###  3.1 Advanced Usage

### 3.1.1 Change User Agent

If you want to hide the type of device that you are using from the
websites you visit, Orweb can be configured to pretend to be a number of
different devices.

**Step 1:** Tap on the menu icon (three vertical dots) found in the top
right of the screen and tap ?Settings?.

![](tool_orbot21.png)

**Step 2:** Once in the *settings* section, scroll down to
the Privacy section and tap ?User Agent?.

![](tool_orbot22.png)

**Step 3:** You will be presented with a list of *User Agents*. Tap your
choice (e.g. Tap *iPhone* to set it. Now any time you visit a website,
it will think you are using an *iPhone*).

![](tool_orbot23.png)

### 3.1.2 Clear Browsing History

### 3.1.2.1 Manually

To manually clear your browsing history and cache, and to hide the
websites you have been visiting on your phone, tap on the menu icon
(three vertical dots) and press ?Clear History/Cache?.

### 3.1.2.2 Automatically

To automatically remove your browsing history and cache as you go to a
new page:

**Step 1:** Tap on the menu icon (three vertical dots) followed
by ?Settings?.

**Step 2:** In the settings screen, scroll down and tap *Clear Back
History*.

![](tool_orbot24.png)

**Note:** When you set this, you will not be able to press the back
button to view web pages you have already visited.

### 3.1.3 Clearing Cookies

**Note:** Deleting cookies will sign you out of any websites that you
were logged into.

**Step 1:** Tap on the menu icon (three vertical dots) found in the top
right of the screen and tap ?Settings?.

**Step 2:** Scroll down to the Cookies section and press ?Clear cookie
data?.

**Step 3:** Tap ?OK? to confirm the deleting of cookies.

![](tool_orbot25.png)

What is PGP?
============

If your threat model includes a government or law enforcement, or you
have some other reason for wanting to make sure that your email provider
is not able to turn over the contents of your email communications to a
third party, you may want to consider using end-to-end encryption for
your email communications. End-to-End Encryption is uninterrupted
protection of data traveling between two communicating parties.

![](email3)

PGP is the standard for end-to-end encryption of your email. PGP stands
for Pretty Good Privacy. It's actually very good privacy. If used
correctly, it can protect the contents of your messages, text, and even
files from being understood even by well-funded government surveillance
programs.

If travelling, you should first follow the advice outlined in the
Preparation lesson.

This lesson focuses specifically on how to cross borders if travelling
for sensitive work or with sensitive information. In establishing the
potential risk and risk mitigation measures for crossing borders, it is
important to establish a few basics about the reasons for, and possible
sensitivities of, your trip. It is vital to be aware of the nature of
the information you will be carrying into and out of the country, and
how you will carry it.

Sensitive or revealing information you may carry could include:

-   Data on people at risk/HRDs you are meeting
-   Travel plansPasswords/ access codes
-   Censored/ banned information
-   Organisation sensitive information
-   Personal information
-   Embarrassing/ incriminating information
-   Legal - encryption or data not allowed for export
-   Receipts
-   Reports

This information may be stored in/on notebooks, publications, laptops,
phones, USBs, CDs, or SD cards.

Remember:

-   Only minimal data should be brought with you
-   Bring a ?clean? laptop and phone if possible
-   Carry sensitive information and electronic equipment in hand
    luggage, as at least you know If it has been tampered with
-   Small, encrypted USB sticks or Micro SD cards can be useful for
    security and being able to hide sensitive data if necessary. See the
    Protecting Files lesson for advice on how to encrypt files.
-   Bring a cheap notebook in which you can rip out the pages unnoticed
-   Tamper proof Scotch tape can be useful for enhancing the security of
    your equipment, hotel safe, laptop ports etc.
-   Check pockets, wallet, bags everything before travel
-   Prepare your story (More in next section)

PGP FOR WINDOWS PC TOOL GUIDE
=============================

PGP for Windows PC Tool Guide\
Encrypted email for Windows
------------------------------

**Lesson to read:\
? [Email](umbrella://lesson/email)**\
**Download Location: **\
? GPG4Win\
? Mozilla Thunderbird\
? Enigmail\
**Computer requirements:** An internet connection, a computer running
Mac OS X, an email account\
**Version used in this guide: **\
? Windows: Windows 7 Ultimate\
? Mozilla Thunderbird 24.6.0\
? Enigmail 1.7\
? GPG4Win 2.2.1\
**License:** Free Software; mix of Free Software licenses\
**Level:** Advanced\
**Time required:** 30-60 minutes

**Using PGP will give you:**\
? The ability to protect your email communications from being read by
anyone except their intended recipients.\
? The ability to prove that an email came from a particular person,
instead of being a fake message sent by another sender (it is otherwise
very easy for email to be fabricated). Both of these are important
defenses if you're being targeted for surveillance or misinformation.

### 1.0 Before you start

To use Pretty Good Privacy (PGP), you will need to install some extra
software that will work with your current email program. You will also
need to create a private key, which you will keep private. The private
key is what you will use to decrypt emails sent to you, and to digitally
sign emails that you send to show they truly came from you. Finally,
you'll learn how to distribute your public key?a small chunk of
information that others will need to know before they can send you
encrypted mail, and that they can use to verify emails you send.

**Note that both ends of the email conversation need to be using
PGP-compatible software for it to work.**

People will normally use this only on their own personal devices, not on
shared devices. Fortunately, PGP is available for most desktop computers
and mobile devices, and you can point them to these guides to help them
set up their own version. This guide is for Windows users.

### 1.1 Overview

To use PGP to exchange secure emails you have to bring together three
programs: GPG4Win (GNU Privacy Guard for Windows known as GnuPG),
Mozilla Thunderbird and Enigmail.

? GnuPG is the program that actually encrypts and decrypts the content
of your mail.\
? Mozilla Thunderbird is an email client that allows you to read and
write emails without using a browser.\
? Enigmail is an add-on to Mozilla Thunderbird that ties it all
together.

Note! What this guide teaches is how to use PGP with Mozilla
Thunderbird, an email client program that performs a similar function to
Outlook. You may have your own favorite email software program (or use a
web mail service like Google Mail or Outlook.com). This guide won't tell
you how to use PGP with these programs. You can choose either to install
Thunderbird and experiment with PGP with a new email client, or you can
investigate other solutions to use PGP with your customary software. We
have still not found a satisfactory solution for these other programs.

**Using PGP doesn't completely encrypt your email: the sender and
receiver information is still unencrypted and so is the subject line!**

Encrypting the sender and receiver information isn?t possible in the
existing email system. What using Mozilla Thunderbird with the Enigmail
add-on gives you is an easy way to encrypt the content of your email.
Someone spying on your emails may still see the identities of the people
you communicate with and when you email them.

You will first download all the software needed, install it, and then
end with configuration and usage.

### 2 Downloading the software

### 2.1 Getting GPG4Win

You can get GnuPG (also known as GPG) on Windows by downloading the
small installer from the GPG4Win download page.

![](tool_pgpwin1.png)

Click on the most recent version of GPG4Win with GnuPG component only
(Vanilla or Light) to download the GPG installer.

**Note: This version of GPG is available only on a web site that offers
?http? downloads, not secure ?https? downloads. If you are concerned
that you may be targeted for surveillance by an organization that can
tamper with your Internet connection, you may want to investigate more
drastic solutions, such as downloading and running Tails, a
secure operating system that replaces Windows.**

Many browsers will ask you to confirm whether you want to download this
file. Internet Explorer 11 shows a bar at the bottom of the browser
window with an orange border.

For any browser it is best to first save the file before proceeding,
so *click the ?Save? button*. By default, most browsers save downloaded
files in the Downloads folder.

### 2.2 Getting Mozilla Thunderbird

Go to the Mozilla Thunderbird website.

![](tool_pgpwin2.png)

Click on the green button labelled ?Thunderbird Free Download.?

The Mozilla Thunderbird website will have detected your preferred
language. If you want to use Thunderbird in another language click on
the ?Other Systems & Languages? link and make your selection from there.

Many browsers will ask you to confirm if you want to download this file.
Internet Explorer 11 shows a bar at the bottom of the browser window
with an orange border.

![](tool_pgpwin3.png)

For any browser, it is best to first save the file before proceeding, so
click the ?Save? button. By default, most browsers save downloaded files
in the Downloads folder.

### 2.3 Getting Enigmail

You can get Enigmail from the Enigmail website.

![](tool_pgpwin4.png)

Many browsers will ask you to confirm if you want to download this file.
Internet Explorer 11 shows a bar at the bottom of the browser window
with an orange border.

![](tool_pgpwin5.png)

For any browser it is best to first save the file before proceeding, so
click the ?Save? button. By default, most browsers save downloaded files
in the Downloads folder.

After downloading Enigmail, GPG4Win, and Mozilla Thunderbird you should
have three new files in your Downloads folder:

![](tool_pgpwin6.png)

### 3 Installing the software

### 3.1 Installing GPG4Win

Keep the Windows Explorer window open and double-click on
gpg4win-xxx-x.x.x.exe. You'll be asked if you want to allow the
installation of this program. Click the ?Yes? button.

![](tool_pgpwin7.png)

A window will open, giving you an overview of what will be installed.
Click the ?Next? button.

![](tool_pgpwin8.png)

A window with the license agreement will open up. Click the ?Next?
button.

![](tool_pgpwin9.png)

The GPG4Win Vanilla package doesn't have components to select, so click
the ?Next ?button again. For the GPG4Win-Light package, unselect all
optional components to install GnuPG only.

![](tool_pgpwin10.png)

Next, you'll have the ability to choose where GPG is installed. Don't
change the default setting. Click the ?Next? button.

![](tool_pgpwin11.png)

The next two windows will have some installation options. Click the
?Next? button and then click the "Install" button:

![](tool_pgpwin12.png)![](tool_pgpwin13.png)

You will see a window with a progress bar?when it's done it will say
?Installation Complete.? Click the ?Next? button again.

![](tool_pgpwin14.png)

Finally, you are at the last installation step. Remove the check mark
next to ?Show the README file? and click the ?Finish? button.

![](tool_pgpwin15.png)

That's it. Now let's move on to installing Mozilla Thunderbird.

### 3.2 Installing Mozilla Thunderbird

Similar to GPG4Win, you install Mozilla Thunderbird by double-clicking
the Thunderbird Setup 24.6.0.exe file. As usual, you will be asked if
you want to run this file. Click the ?Run? button.

![](tool_pgpwin16.png)

You will be asked if you want to allow Mozilla Thunderbird to make a
change to your computer by installing software. Click the ?Yes? button.

![](tool_pgpwin17.png)

You will see the Mozilla Thunderbird Setup window. Click the ?Next?
button.

![](tool_pgpwin18.png)

Next, you will get a choice between a Standard setup and a Custom setup.
Keep the Standard setup selection and click the ?Next? button.

![](tool_pgpwin18.png)

You will be given a summary of where Mozilla Thunderbird's files will be
installed. Click the ?Install? button.

![](tool_pgpwin19.png)

When the installation process is complete, you will see a final window
that enables you to launch Mozilla Thunderbird. Click the ?Finish?
button.

![](tool_pgpwin20.png)

### 3.3. Enigmail installation

**Step 1. Preparation**

When Mozilla Thunderbird launches for the first time, you will see this
small confirmation window asking about some default settings. We
recommend clicking the ?Set as Default? button.

![](tool_pgpwin21.png)

Next, you will be asked whether you would like a new email address.
Click the ?Skip this and use my existing email? button. Now you will
configure Mozilla Thunderbird to send and receive email. If you are used
to only reading and sending email through gmail.com, outlook.com, or
yahoo.com, Mozilla Thunderbird will be a new experience, but it isn't
that different overall.

![](tool_pgpwin22.png)

**Step 2. Adding a mail account to Mozilla Thunderbird**

A new window will open.

![](tool_pgpwin23.png)

Enter your name, email address, and the password to your email account.
Mozilla doesn't have access to your password or your email account.
Click the ?Continue? button.

![](tool_pgpwin24.png)

In many cases Mozilla Thunderbird will automatically detect the
necessary settings. In some cases Mozilla Thunderbird doesn't have
complete information and you'll need to enter it yourself. Here is an
example of the instructions Google provides for Gmail:

Incoming Mail (IMAP) Server - Requires SSL\
? imap.gmail.com\
? Port: 993\
? Requires SSL:Yes

Outgoing Mail (SMTP) Server - Requires TLS\
? smtp.gmail.com\
? Port: 465 or 587\
? Requires SSL: Yes\
? Requires authentication: Yes\
? Use same settings as incoming mail server

**Full Name or Display Name:** \[your name or pseudonym\]

**Account Name or User Name:** your full Gmail address
(username@gmail.com). Google Apps users, please
enter username@your\_domain.com

**Email address:** your full Gmail address (username@gmail.com) Google
Apps users, please enter username@your\_domain.com

**Password:** your Gmail password

**If you use two-factor authentication with Google (and depending on
your threat model you probably should!) you cannot use your standard
Gmail password with Thunderbird. Instead, you will need to create a new
application-specific password for Thunderbird to access your Gmail
account. See [Google's own
guide](https://support.google.com/mail/answer/1173270?hl=en) for doing
this.**

When all the information is entered correctly, click the ?Done? button.

![](tool_pgpwin25.png)

Mozilla Thunderbird will start downloading copies of your email to your
computer. Try sending a test email to your friends.

**Step 3. Installing Enigmail**

Enigmail is installed in a different way from Mozilla Thunderbird and
GPG4Win. As mentioned before, Enigmail is an Add-on for Mozilla
Thunderbird. Click the ?Menu button,? also called the Hamburger button,
and select ?Add Ons.?

![](tool_pgpwin26.png)

You'll be taken to the Add-ons Manager tab.

![](tool_pgpwin27.png)

Click the cog to bring up a small menu and select ?Install add-on from
file? which will bring up a file-selection window.

![](tool_pgpwin28.png)

The file selection window will very likely open to the Downloads folder.
If it doesn't, go to the Downloads folder (where Enigmail was saved to)
click on enigmail-1.7-tb+sm.xpi then click the ?Open? button.

![](tool_pgpwin29.png)

Now you will see a small window asking you to confirm whether you want
to install Enigmail. Click the ?Install Now? button.

![](tool_pgpwin30.png)

After the Enigmail add-on is installed, Mozilla Thunderbird will ask to
restart the browser to activate Enigmail. Click the ?Restart Now? button
and Mozilla Thunderbird will restart.

![](tool_pgpwin31.png)

When Mozilla Thunderbird restarts, an additional window will open up
that will start the process of setting up the Enigmail add-on. Keep the
?Yes, I would like the wizard to get me started? button selected and
click the ?Next? button.

![](tool_pgpwin32.png)

Enigmail provides you with three options for handling mail. The default
option is to encrypt emails if you have the ?public key? of another
person, Enigmail will encrypt the email you send but leave emails
unencrypted if you don't have the public key of the recipient yet. You
also have the option to encrypt emails all the time to everyone with PGP
keys, which means that you will have to find the public keys for people
for whom you don't have them already, or turn off automatic encryption
completely and only use PGP when directed.

![](tool_pgpwin33.png)

We don't know what the appropriate option is for you, but believe the
?Convenient auto encryption? option to be a good choice. If you are in
doubt, choose ?Don't encrypt my messages by default.? Click the ?Next?
button.

Now you have an option to digitally sign all outgoing emails. Signing
your email with PGP allows the recipient to check that you sent the
message, and that the contents of the message were not tampered with.
Click the ?Sign my messages by default? button to turn this feature on.
The downside of doing this, however, is that it can also flag to anyone
you send mail to that you use PGP. [In some parts of the
world](www.cryptolaw.org/) (including China, Iran, Belarus, and some
Middle-East states) using unlicensed encryption, even for personal use,
is illegal, so you might have very good reasons to not let others know
you use PGP.

Click the ?Next? Button.

![](tool_pgpwin34.png)

Now you'll see an option to have Enigmail make some changes to the
configuration of Mozilla Thunderbird.

![](tool_pgpwin35.png)

If you click the Details button you can review what those changes are.

![](tool_pgpwin36.png)

The following options can be unchecked (reenabled), for a more seamless
transition, if you use PGP/Mime by default (we'll set that later):

? Disable flowed text\
? View message body as plain text\
? Do not compose HTML messages

The final option prevents potential problems in the encryption and
decryption of your email. Be aware that selecting this box will remove
the ability to send text that is bolded, underlined or colored. After
reviewing the changes, click the ?OK button.?

The small window will close. Click the ?Next? button.

Now you will start creating your private key and public key.

### 4 Creating a public key and private key

Installation and setup of the Enigmail add-on is complete. Now you'll
have the option of creating your public and private key pair. This
assumes you have not created a private key before.

Click the ?Next? button.

![](tool_pgpwin37.png)

Unless you have already configured more than one email account, Enigmail
will choose the email account you've already configured. The first thing
you'll need to do is come up with a strong passphrase for your private
key. See the **[Passwords lesson](umbrella://lesson/passwords)** for
more information on how to do this.

Make sure that you've written down this passphrase on paper until you
have memorized it. Keep it somewhere where you can tell if it has been
taken or viewed (like your wallet or purse). Just make sure you don't
leave this paper lying around.

Click the ?Next? button.

Enigmail will display some information about your private key as well as
the configuration settings. We recommend creating 4096-bit length keys.
Click the ?Next? button.

![](tool_pgpwin38.png)

**Your key will expire at a certain time; when that happens, other
people will stop using it entirely for new emails to you, though you
might not get any warning or explanation about why. So, you may want to
mark your calendar and pay attention to this issue a month or so before
the expiration date.**

It's possible to extend the lifetime of an existing key by giving it a
new, later expiration date, or it's possible to replace it with a new
key by creating a fresh one from scratch. Both processes might require
contacting people who email you and making sure that they get the
updated key; current software isn't very good at automating this. So
make a reminder for yourself; if you don't think you'll be able to
manage it, you can consider setting the key so that it never expires,
though in that case other people might try to use it when contacting you
far in the future even if you no longer have the private key or no
longer use PGP.

Enigmail will generate the key and when it is complete, a small window
will open asking you to generate a revocation certificate. This
revocation certificate is important to have as it allows you to make the
private key and public key invalid. It is important to note that merely
deleting the private key does not invalidate the public key and may lead
to people sending you encrypted mail that you can't decrypt.

Click the ?Generate Certificate? button.

![](tool_pgpwin39.png)

A window will open to provide you a place to save the revocation
certificate. While you can save the file to your computer, we recommend
saving the file on a USB drive that you are using for nothing else and
storing the drive in a safe spot. We also recommend removing the
revocation certificate from the computer with the keys, just to avoid
unintentional revocation.

Even better, save this file on a separate encrypted disk. Choose the
location where you are saving this file and click the ?Save? button.

![](tool_pgpwin40.png)

Now Enigmail will give you further information about saving the
revocation certificate file again. Click the ?OK? button.

![](tool_pgpwin41.png)

Finally, you are done with generating the private key and public key.
Click the ?Finish? button.

![](tool_pgpwin42.png)

### 5 Optional steps

### 5.1 Display long key-IDs

The next steps are completely optional but they can be helpful when
using OpenPGP and Enigmail. Briefly, the Key ID is a small part of the
fingerprint. When it comes to verifying that a public key belongs to a
particular person the fingerprint is the best way. Changing the default
display makes it easier to read the fingerprints of the certificates you
know about. Click the configuration button, then the Enigmail option,
then Key Management.

![](tool_pgpwin43.png)

A window will open showing two columns: Name and Key ID.

![](tool_pgpwin43.png)

On the far right there is a small button. Click that button to configure
the columns. Unclick the Key ID option and click the Fingerprint option.

![](tool_pgpwin44.png)

Now the columns will look like this:

![](tool_pgpwin45.png)

Now you are set up to send and receive regular and encrypted email. Next
you will go through the steps of actually finding the people to exchange
encrypted mail with.

### 5.2 Using PGP/MIME

There is a final optional configuration step is to enable PGP/MIME which
makes sending encrypted and signed attachments easier.

You can find this setting by clicking on the Menu Button, hovering over
Options, then clicking Account Settings. The Account Settings window
will open.

![](tool_pgpwin46.png)

When the Account Settings window opens click the OpenPGP Security tab
then click the checkbox next to Use PGP/MIME by default. Next click the
OK button. Now Enigmail will use PGP/MIME by default.

![](tool_pgpwin47.png)

**Using PGP doesn't completely encrypt your email so that the sender and
received information is encrypted. Encrypting the sender and receiver
information would break email. Using Thunderbird with the Enigmail
add-on gives you an easy way to encrypt and decrypt the content of your
email.**

### 6.1 Letting others know you are using PGP

Now that you have PGP, you want to let others know that you are using it
so they can also send you encrypted messages using PGP.

Let's look at three different ways you can let people know you are using
PGP.

**a) Let people know you are using PGP with an email**

You can easily email your public key to another person by sending them a
copy as an attachment.

Click the ?Write? button in Mozilla Thunderbird.

![](tool_pgpwin48.png)

Fill in an address and a subject, perhaps something like ?my public
key,? click the Enigmail menu and select the ?Attach My Public Key?
option.

![](tool_pgpwin49.png)

You can send the email and the recipient will be able to download and
use the public key you sent.

If this method is used, it's a good idea to have the recipient verify
your public key's fingerprint over some other form of communication, in
case email is already being intercepted and tampered with.

**b) Let people know you are using PGP on your website**

In addition to letting people know via email, you can post your public
key on your website. The easiest way is to upload the file and link to
it. This guide won't go into how to do those things, but you should know
how to export the certificate as a file to use in the future.

Click the configuration button, then the Enigmail option, then Key
Management.

Highlight the certificate in bold, then right-click to bring up the menu
and select Export keys to file.

![](tool_pgpwin50.png)

A small window will pop up with three buttons. Click the ?Export Public
Keys Only? button.

![](tooL_pgpwin51.png)

Make sure you don't click the ?Export Secret Keys? button because
exporting the secret key could allow others to impersonate you if they
are able to guess your password.

Now a window will open so you can save the file. In order to make it
easier to find in the future please save the file to the Documents
folder.

![](tool_pgpwin52.png)

Now you can use this file as you wish.

**c) Uploading to a keyserver**

Keyservers make it easier to search for and download public keys. Most
modern keyservers are synchronizing, meaning that a public key uploaded
to one server will eventually reach all servers.

Although uploading your public key to a keyserver might be a convenient
way of letting people know that you have a public PGP certificate, you
should know that due to the nature of how keyservers work, there is no
way to delete public keys once they are uploaded, you can only mark them
as revoked.

**Before uploading your public key to a keyserver, it is good to take a
moment to consider whether you want the whole world to know that you
have a public key without the ability to remove this information at a
later time.**

If you choose to upload your public key to keyservers, you will go back
to the Enigmail Key Management window.

Click the Keyserver menu item and select the Upload Public Keys option.

![](tool_pgpwin53.png)

### 6.2 Finding other people who are using PGP

**a) Getting a public key by email**

You might get a public key sent to you as en email attachment.

![](tool_pgpwin54.png)

Double-click on the new message, and it'll open a new tab. Notice the
attachment at the bottom of the window. Right-click on the attachment
and select ?Import OpenPGP Key.? A small window will open giving you the
results of the import. Click the OK button.

![](tool_pgpwin55.png)

If you open up the Enigmail key management window again, you can check
the result. Your PGP key is in bold because you have both the private
key and the public key. The public key you just imported is not bold
because it doesn't contain the private key.

![](tool_pgpwin56.png)

**b) Getting a public key as a file**

It's possible that you get a public key by downloading it from a website
or someone might have sent it through chat software. In a case like
this, you will assume you downloaded the file to the Downloads folder.

Open the Enigmail Key Manager and click on the ?File? menu. Select
?Import Keys from File.?

![](tool_pgpwin57.png)

The public key might have very different file name endings such as .asc,
.pgp, or .gpg. Select the file and click the ?Open? button.

![](tool_pgpwin58.png)

A small window will open, giving you the results of the import. Click
the ?OK? button.

![](tool_pgpwin59.png)

**c) Getting a public key from a key server**

Keyservers can be a very useful way of getting public keys. Try looking
for a public key. Open up the key manager then click the ?Keyserver?
menu and select ?Search for Keys.?

![](tool_pgpwin60.png)

A small window will pop up with a search field. You can search by a
complete email address, a partial email address, or a name. In this
case, you will search for certificates containing ?eff.org.?

![](tool_pgpwin61.png)

A larger window will pop up with many options. If you scroll down you'll
notice some certificates are italicized and grayed out. These are
certificates that have either been revoked or expired on their own.

![](tool_pgpwin62.png)

Let's take the public keys of Danny O'Brien for example, he has one
expired or revoked certificate and one valid certificate. Select the
valid certificate by clicking the box on the left then press the OK
button.

![](tool_pgpwin63.png)

In some cases a person may have more than one certificate, all appearing
valid. Note that it's possible for anyone to upload a public certificate
for anyone else, and that one of these keys may not belong to the person
that owns the email address associated with it. In this case, verifying
the fingerprint is extremely important.

A small notification window will pop up letting you know if you
succeeded:

![](tool_pgpwin64.png)

The Enigmail Key Manager will now show you the added certificates:

![](tool_pgpwin65.png)

### 7.1 Sending PGP encrypted mail

Now you will send your first encrypted email to a recipient. In the main
Mozilla Thunderbird window click the ?Write? button. A new window will
open.

![](tool_pgpwin66.png)

Write your message, and enter a recipient. For this test, select a
recipient whose public key you already have. Enigmail will detect this
and automatically encrypt the email.

![](tool_pgpwin67.png)

*Note that the subject line won't be encrypted, so choose something
innocuous, like ?hello.?*

When you click the ?Send? button, you'll be given a window to enter the
password to your PGP Key. Remember this is different from your email
password!

Enter your password then click the ?OK? button and your email will be
encrypted and sent.

![](tool_pgpwin68.png)

The body of the email was encrypted and transformed. For example this
text:

![](tool_pgpwin69.png)

Will be transformed into:

![](tool_pgpwin70.png)

### 7.2 Receiving PGP encrypted mail

Let's go through what happens when you receive encrypted email. Notice
that that Mozilla Thunderbird is letting you know you have new mail.
Click on the message.

![](too.png;_pgpwin71)

A small window opens asking you for the password to the PGP key.
Remember: Don't enter your email password. Click the ?OK? button.

![](tool_pgpwin72.png)

Now the message will show up decrypted

![](tool_pgpwin73.png)

### 8 Revoking the PGP Key

**a) Revoking your PGP Key through the Enigmail interface**

The PGP keys generated by Enigmail automatically expire after five
years. So if you lose all your files, you can hope that people will know
to ask you for another key once the key has expired.

You might have a good reason to disable the PGP key before it expires.
Perhaps you want to generate a new, stronger PGP key. The easiest way to
revoke your own PGP key in Enigmail is through the Enigmail Key Manager.

![](tool_pgpwin74.png)

Right-click on your PGP key (it's in bold), and select the ?Revoke Key?
option.

![](tool_pgpwin75.png)

A window will pop up letting you know what happens and asking for your
confirmation. Click the ?Revoke Key? button.

![](tool_pgpwin76.png)

The password window opens, enter your password for the PGP key and click
the ?OK? button.

![](tool_pgpwin77.png)

Now a new window will open up letting you know you succeeded. Click the
?OK? button.

![](tool_pgpwin78.png)

When you go back to the Enigmail Key Management window you'll notice a
change to your PGP key. It is now grayed out and italicized.

![](tool_pgpwin79.png)

**b) Revoking a PGP Key with a revocation certificate**

As mentioned before, the PGP keys generated by Enigmail automatically
expire after five years. So if you lose all your files you can be sure
that people will know to ask you for another key once the key has
expired.

Like we mentioned before, you might have a good reason to disable the
PGP key before it expires.

Similarly, others might have good reasons to revoke an existing key.

You might get sent revocation certificates from friends as a notice that
they want to revoke their key.

In the previous section you might have noticed that Enigmail generates
and imports a revocation certificate internally when you use the
Enigmail Key Manager to revoke a key. Since you already have a
revocation certificate, you will use the one you generated earlier to
revoke your own key.

Start with the Enigmail Key Manager and click the ?File? menu and select
?Import Keys from File.?

![](tool_pgpwin80.png)

A window will open up so you can select the revocation certificate.
Click on the file, and click the ?Open? button.

![](tool_pgpwin81.png)

You'll get a notification that the certificate was imported successfully
and that a key was revoked. Click the ?OK? button.

![](tool_pgpwin82.png)

Once you click the ?OK? button, you'll be taken back to the Enigmail Key
Manager and you see the certificate you revoked greyed out and
italicized.

![](tool_pgpwin83.png)

If the key you revoked is your own, and you previously uploaded your
public key to the key servers, you will want to re-upload the
now-revoked key to the key servers, so that others see not to use it
anymore.

Now that you have all the proper tools, try sending your own
PGP-encrypted email.

The best defence against kidnapping is having and practising a
high-quality, well-managed security management plan, which is based on a
thorough understanding of the general context and risks, and on the
context and threat of kidnapping specific to your location.
Understanding who carries out kidnappings, and why, will help shape your
avoidance and survival strategies.

The main reasons for kidnappings are:

-   To hold for ransom
-   To cause a political effect
-   To achieve publicity
-   To be used as human shields

The main actors that carry out kidnappings are:

-   Criminals
-   Political extremists
-   Terrorists
-   Militia groups
-   Regimes that use terror

Factors which may encourage kidnapping:

-   The state?s ability to provide protection from the crime, and
    prosecute those who engage in such activity
-   A lack of political, legal or military response will encourage more
    actors to become involved
-   Media coverage of successful kidnap attempts
-   High financial rewards from kidnapping

CHATSECURE TOOL GUIDE
=====================

ChatSecure Tool Guide\
Secure texting for iPhone and Android
-------------------------------------

**Lesson to read: [Sending a
Message](umbrella://lesson/sending-a-message)**\
**Download location:** <https://chatsecure.org> ; can also be downloaded
from the [Apple App
store](https://itunes.apple.com/us/app/chatsecure/id464200063) or
the [Google Play
store](https://play.google.com/store/apps/details?id=info.guardianproject.otr.app.im).\
**System requirements:** iOS 6.0, Android (varies)\
**Version used in this guide:** 2.2.4 (iPhone), 13.1.2 (Android)\
**License:** Apple, GPLv3; Android, Apache 2.0\
**Other reading:** <https://guardianproject.info/apps/chatsecure/>\
**Level:** Beginner-Intermediate\
**Time required:** 5-10 minutes

![](tool_chatsecure.png)

ChatSecure is a free mobile phone application for iPhone and Android
devices that allows users to communicate with off the record instant
messaging. ChatSecure allows users to send instant messages and chats
using a cell phone, instead of with a traditional desktop or laptop
computer. It's compatible with iPhone and Android phones.

ChatSecure supports OTR encryption over XMPP. All messages sent via
ChatSecure are completely private, so long as the person you are
chatting with is also using an OTR compatible instant messaging client
like ChatSecure, Adium, Pidgin, or Jitsi. The app?s capabilities allow
it to deliver audio messages, photos, files, or text.

When you send messages using ChatSecure, they are not stored on the
phone system's memory. ChatSecure used with the privacy plugin Orbot
should be able to bypass most firewalls, network restrictions, and
blacklists. The app can manage multiple accounts, so you can chat with
your Facebook friends, Google contacts, or other privacy conscious users
that use an instant messaging program that supports OTR encryption.

### How to install and configure ChatSecure

1\. Download and install ChatSecure

Visit the Apple App Store or Google Play store and search for ChatSecure
by The Guardian Project. Select ?Install? and accept the Terms of
Service by clicking ?Accept.? The app will download and install
automatically.

2\. Open the app and set your password

When you open the app you will be promoted to set a password. You will
be prompted to create a passphrase in order to locally encrypt your
data. If you choose to do this, your data will be encrypted in transit,
as well as encrypted locally on your phone.\
If you choose to skip this step, your messages will still be encrypted
in transit, but will not be protected on your device. For more
information on selecting a strong passphrase, see the [Passwords
lesson](umbrella://lesson/passwords).

3\. Configure your accounts

You can add a variety of different accounts your ChatSecure app. To add
GoogleTalk or Google Hangouts, choose ?Google.? To add any XMPP or
Jabber messaging service, choose ?Jabber (XMPP).? To add your Facebook
account, also choose ?Jabber (XMPP).?\
Once you?ve added your account, type in your username (or email address)
and your password to sign in. Your contacts should load automatically.

To add a second or third account, click on the ?accounts? tab in the
menu. In the upper right hand corner, click on the ?+? sign. You can
either choose to add an existing account or create a new account.

### How to use ChatSecure

1\. Sign in to your accounts

To sign in to your account, click on the ?accounts? tab in the menu and
turn on the accounts you wish to use. Once you sign in, anyone can
connect with you from a mobile or desktop instant messaging application.

2\. Start end-to-end encryption

Once you?ve started a chat with someone, click on the unlocked lock icon
on the top menu bar of the display. Choose ?Start Encryption.? If the
person you are chatting with has an OTR compatible instant messaging
system, then you will have the option to verify your (and their)
fingerprint.

ChatSecure offers three ways to verify OTR fingerprints, but if you're
chatting with someone over a desktop instant messenger and not with
ChatSecure, the best way to verify an OTR fingerprint is by
communicating through another channel. You can resend your fingerprint
over an SMS (TextSecure), say it over the phone if you recognize one
another's voices, use PGP email, or verify in person. Click on ?manual
verification? and ChatSecure will display your and your friend's
fingerprints. If you can confirm that you both have the same
information, you can click ?verify.?

ChatSecure supports manual verification or verification by scanning the
other user?s barcode (QR). If you are in the same room as the other
person, you can easily scan the barcode on their phone or read your keys
aloud to one another.

3\. Understand your options

? Just like a desktop instant messaging service, ChatSecure gives you
the option to appear offline, busy, idle, or away. To change this
setting click on your name at the top of your friends list.\
? ChatSecure also allows you to initiate group chats and add new
contacts, both of which can be done from the main menu. (Note that group
chats cannot be secured like one-on-one chats due to limitations of the
OTR protocol.)\
? The app supports multimedia messaging, can take pictures, and can send
photos and files securely if your friend is also using end-to-end
encryption and you are able to verify her identity.\
? ChatSecure gives you the option to create a new XMPP or Jabber
messaging account that supports OTR encryption. If you don't already use
XMPP messaging, this is a great opportunity to create one and experiment
with non-proprietary messaging.

PIDGIN TOOL GUIDE
=================

Pidgin Tool Guide\
Encrypted instant messaging for Windows
---------------------------------------

**Lesson to read:\
? [Sending a message](umbrella://lesson/sending-a-message)**\
**Download Location: **\
? <https://pidgin.im/download/> \
? <https://otr.cypherpunks.ca/>\
**Computer requirements:** An internet connection, a computer running
Windows XP or higher, and an XMPP (Jabber) account.\
*(Pidgin is able to work with many chat systems, such as AIM, Facebook,
Google Talk, MSN, MXit and Yahoo, but here we'll focus on XMPP, formerly
known as Jabber)*\
**Version used in this guide: **\
? Windows 7 Ultimate\
? Pidgin 2.10.9, pidgin-otr 4.0.0-1\
**License:** Free Software; mix of Free Software licenses\
**Level:** Beginner\
**Other reading:** <https://pidgin.im/cgi-bin/mailman/listinfo/support>\
**Time required:** 20 minutes

**Using OTR with Pidgin will give you:**\
? The ability to organise and manage some of the most popular instant
messaging services through a single program.\
? The ability to have encrypted chats on instant messenger, without the
server logging those chats.\
? The ability to make sure that the person you are chatting with really
is that person.

### 1.0 Before you start

Pidgin is an easy-to-use, instant messaging client for Windows that uses
a protocol called OTR (Off-the-record), which allows users to have
confidential conversations.

? Note: OTR should not be confused with Google's ?Off the record,? which
just disables chat logging, and does not have encryption or verification
capabilities.\
? Pidgin supports the following IM services: AIM, Bonjour, Gadu-Gadu,
Google Talk, Groupwise, ICQ, IRC, MSN, MXit,MySpaceIM, SILC, SIMPLE,
Sametime, Yahoo!, Zephyr and any IM clients running the XMPP messaging
protocol.\
? Pidgin does not permit communication between different IM services.
For instance, if you are using Pidgin to access your Google
Talk account, you will not be able to chat with a friend using
an ICQ account.\
? However, Pidgin can be configured to manage multiple accounts based on
any of the supported messaging protocols. That is, you may
simultaneously use both Gmail and ICQ accounts, and chat with
correspondents using either of those specific services (which are
supported by Pidgin).\
? Pidgin, automatically logs conversations by default, however you do
have the ability to disable this feature. That said, you do not have
control over the person with whom you are chatting?she could be logging
or taking screenshots of your conversation, even if you yourself have
disabled logging.

**Why should I use Pidgin + OTR?**

When you have a chat conversation using Google Hangouts or Facebook chat
on the Google or Facebook websites, that chat is encrypted using HTTPS,
which means the content of your chat is protected from hackers and other
third parties while it?s in transit. It is not, however, protected from
Google or Facebook, which have the keys to your conversations and can
hand them over to authorities.

After you have installed Pidgin, you can sign in to it using multiple
accounts at the same time. For example, you could use Google Hangouts,
Facebook, and XMPP simultaneously. Pidgin also allows you to chat using
these tools without OTR. Since OTR only works if both people are using
it, this means that even if the other person does not have it installed,
you can still chat with them using Pidgin.

Pidgin also allows you to do out-of-band verification to make sure that
you?re talking to the person you think you?re talking to. For every
conversation, there is an option that will show you the key fingerprints
it has for you and the person with whom you are chatting. A "key
fingerprint " is a string of characters like "342e 2309 bd20 0912 ff10
6c63 2192 1928,? that?s used to verify a longer public key. Exchange
your fingerprints through another communications channel, such as
Twitter DM or email, to make sure that no one is interfering with your
conversation.

**Limitations: When should I not use Pidgin + OTR?**

Pidgin is a complex program, which has not been written with security as
a top priority. It almost certainly has bugs, some of which might be
used by governments or even big companies to break into computers that
are using it. Using Pidgin to encrypt your conversations is a great
defence against the kind of untargeted surveillance that is used to spy
on everyone's Internet conversations, but if you think you will be
personally targeted by a well-resourced attacker (like a nation-state),
you should consider stronger precautions, such as PGP -encrypted email.

### 2 Downloading and installing

### 2.1 Getting Pidgin

You can get Pidgin on Windows by downloading the installer from the
Pidgin download page.

![](tool_pidgin1.png)

Click on the *purple* DOWNLOAD tab. ***Don't** click the green Download
Now button because you?ll want to choose a different installer file.* 

You'll be taken to the download page.

![](tool_pidgin2.png)

*Again, **don't** click the green Download Now button because we want to
choose a different installer file. *

The default installer for Pidgin is small because it doesn't contain all
the information and downloads the files for you. This sometimes fails so
you will have a better experience with the ?offline installer? which
contains all the necessary installation material.

Click the ?**offline installer**? link. You will be taken to a new page
titled ?Sourceforge? and after a few seconds, a small popup will ask
whether you want to save a file.

? Note: While Pidgin's download page uses "HTTPS" and is therefore
relatively safe from tampering, the website it directs you to to
download the Windows version of Pidgin is currently Sourceforge, which
uses unencrypted "HTTP," and therefore offers no protection. That means
that the software you download could be tampered with before you
download it. This risk would mostly come from either someone with access
to the local Internet infrastructure attempting to conduct targeted
surveillance against you personally (for instance a malicious hot-spot
provider), or a state or government planning to distribute compromised
software to many users. The [HTTPS
Everywhere](https://www.eff.org/https-everywhere) extension can rewrite
Sourceforge download URLs to HTTPS, so it's recommended you install
HTTPS Everywhere before downloading any other software. Additionally, in
our experience, Sourceforge often has confusing full-page ads on its
download pages that can trick people into installing something they may
not want to.  You can install an ad blocker before any other software to
avoid these confusing ads.

Many browsers will ask you to confirm whether you want to download this
file. Internet Explorer 11 shows a bar at the bottom of the browser
window with an orange border.

![](tool_pidgin3.png)

For any browser, it is best to first save the file before proceeding, so
click the ?Save? button. By default, most browsers save downloaded files
in the Downloads folder.

### 2.2 Getting OTR

You can get pidgin-otr, the OTR plugin for Pidgin, by downloading the
installer from the [OTR download page](https://otr.cypherpunks.ca/).

![](tool_pidgin4.png)

Click the ?Downloads? tab to be taken to the ?Downloads? section of the
page. Click the ?Win32 installer for pidgin? link.

![](tool_pidgin5.png)

Many browsers will ask you to confirm whether you want to download this
file. Internet Explorer 11 shows a bar at the bottom of the browser
window with an orange border.

![](tool_pidgin6.png)

For any browser, it is best to first save the file before proceeding, so
click the ?Save? button. By default, most browsers save downloaded files
in the Downloads folder.

After downloading Pidgin and pidgin-otr you should have two new files in
your

Downloads folder:

![](tool_pidgin7.png)

### 2.3 Installing Pidgin

Keep the Windows Explorer window open and double-click on
pidgin-2.10.9-offline.exe. You'll be asked if you want to allow the
installation of this program. Click the ?Yes? button.

![](tool_pidgin8.png)

A small window opens asking you to select a language. Click the ?OK?
button.

![](tool_pidgin9.png)

A window opens up giving you a quick overview of the installation
process. Click the ?Next? button.

![](tool_pidgin10.png)

Now you get a license overview. Click the ?Next? button.

![](tool_pidgin11.png)

Now you can see what different components are installed. Don't change
the settings. Click the ?Next? button.

![](tool_pidgin12.png)

Now you can see where Pidgin will be installed. Don't change this
information. Click the ?Next? button.

![](tool_pidgin13.png)

Now you'll see a window with scrolling text until it says ?Installation
Complete.? Click the ?Next? button.

![](tool_pidgin14.png)

Finally, you?ll see the last window of the Pidgin installer. Click the
?Finish? button.

![](tool_pidgin15.png)

### 2.4 Installing pidgin-otr

Go back to the Windows Explorer window and open and double-click on
pidgin-otr-4.0.0-1.exe. You'll be asked if you want to allow the
installation of this program. Click the ?Yes? button.

![](tool_pidgin16.png)

A window opens up giving you a quick overview of the installation
process. Click the ?Next? button.

![](tool_pidgin17.png)

Now you get a license overview. Click the ?I Agree? button.

![](tool_pidgin18.png)

You will see where pidgin-otr will be installed. Don't change this
information. Click the ?Install? button.

![](tool_pidgin19.png)

Finally, you?ll see the last window of the pidgin-otr installer. Click
the ?Finish? button.

![](tool_pidgin20.png)

### 3 Configuration

### 3.1 Configuring Pidgin

Go to the Start menu, click the Windows icon, and select Pidgin from the
menu.

![](tool_pidgin21.png)

### 3.2 Adding an account

When Pidgin launches for the first time, you will see this welcome
window giving you an option to add an account. Since you don't have an
account configured yet, click the ?Add? button.

![](tool_pidgin22.png)

Now you'll see the ?Add Account? window.

***Pidgin is able to work with many chat systems, such as AIM, Facebook,
GoogleTalk, MSN, MXit and Yahoo, but here we'll focus on XMPP, formerly
known as Jabber.***

At the Protocol entry, select the ?XMPP? option.

At the Username entry, enter your XMPP username.

At the Domain entry, enter the domain of your XMPP account.

At the Password entry, enter your XMPP password.

Checking the box by the ?Remember password? entry will make accessing
your account easier. Be aware that by clicking ?Remember password,? your
password will be saved on the computer, making it accessible to anyone
who may happen to access your computer. If this is a concern, do not
check this box. You will then be required to enter your XMPP account
password every time you start Pidgin.

![](tool_pidgin23.png)

### 3.3 Adding a Buddy

Now you will want to add someone to chat with. Click the ?Buddies? menu
and select ?Add Buddy.? An ?Add Buddy? window will open.

![](tool_pidgin24.png)

At the ?Add Window,? you can enter the username of the person you want
to chat with. This other user does not have to be from the same server,
but does have to use the same protocol, such as XMPP.

At the ?Buddy's username? entry, enter your buddy?s username with the
domain name. This will look like an email address.

At the ?(Optional) Alias? entry, you can enter a name of your choice for
your buddy. This is entirely optional, but can help if the XMPP account
of the person you are chatting with is hard to remember.

Click the ?Add? button.

![](tool_pidgin25.png)

Once you have clicked the ?Add? button, Boris will get a message asking
if he gives authorization for you to add him. Once Boris does, he adds
your account and you will get the same request.

Click the ?Authorize? button.

![](tool_pidgin26.png)

### 3.4 Configuring the OTR plugin

Now you will configure the OTR plugin so you can chat securely. Click
the ?Tools? menu and select the ?Plugins? option.

![](tool_pidgin27.png)

Scroll down to the ?Off-the-Record Messaging? option, and check the box.

Click on the ?Off-the-Record Messaging? entry and click the ?Configure
Plugin? button.

![](tool_pidgin28.png)

Now you will see the ?Off-the-Record Messaging? configuration window.
Notice that is says ?No key present.?

Click the ?Generate? button.

![](tool_pidgin29.png)

Now a small window will open and generate a key. When it is done, click
the ?OK? button.

![](tool_pidgin30.png)

You'll see new information: a 40 character string of text, broken up
into 5 groups of eight characters. This is your OTR fingerprint. Click
the ?Close? button.

![](tool_pidgin31.png)

Now click the ?Close? button on the Plugins window.

### 4.0 Chatting securely

You are now able to chat with Boris. The two of you can send messages
back and forth. However, we're still not chatting securely. Even if you
are connecting to the XMPP server, it is possible that the connection
between you and Boris is not secure from snooping.

If you look at the chat window, notice that it says ?Not private? in red
on the bottom right. Click the ?Not private? button.

![](tool_pidgin32.png)

A menu will open up, select ?Authenticate buddy.?

![](tool_pidgin33.png)

A window will open up. You are asked: ?How would you like to
authenticate your buddy??

The drop-down has three options:

**Option 1: Shared secret**

A shared secret is a line of text you and the person you want to chat
have agreed to use ahead of time. You should have shared this in person
and never have exchanged it over insecure channels such as email or
Skype.

You and your buddy need to enter this text together. Click the
?Authenticate? button.

![](tool_pidgin34.png)

The shared secret verification is useful if you and your buddy have
already made arrangements to chat in the future but haven't yet created
OTR fingerprints on the computer you are using.

**Option 2: Manual fingerprint verification**

Manual fingerprint verification is useful if you were already given your
buddy's fingerprint and are now connecting with Pidgin. This will not be
useful if your buddy changed computers or had to create new
fingerprints.

If the fingerprint you were given and the fingerprint on the screen
match, select ?I have? and click the ?Authenticate? button.

![](tool_pidgin35.png)

**Option 3: Question and answer**

Question and answer verification is useful if you know your buddy but
have not established a shared secret nor had a chance to share
fingerprints. This method is useful to establish verification based on
something both of you know, like a shared event or memory.

Enter the question you want to ask. Don't make it so simple that someone
can guess it easily, but don't make it impossible. An example of a good
question would be ?Where did we go for dinner in Minneapolis?? And
example of a bad question would be ?Can you buy apples in Tokyo??

**The answers must match exactly; so keep that in mind when choosing an
answer to your question. Capitalization matters, so you might consider
including a note like (for example: use capitals, lower case).**

Enter the question and answer then click the ?Authenticate? button.

![](tool_pidgin36.png)

Your buddy will have a window open with the question displayed asking
for the answer. They will have to answer and click the ?Authenticate?
button. Then they will receive a message letting them know if the
authentication was successful.

![](tool_pidgin37.png)![](tool_pidgin38.png)

Once your buddy had completed the authentication procedure, you will get
a window letting you know the authentication succeeded.

![](tool_pidgin39.png)

Your buddy should also verify your account so that both of you can be
sure that the communication is secure. Here is what it would like for
Akiko and Boris. Notice the green ?Private? icons in the lower right of
the chat window.

![](tool_pidgin40.png)

### 5 Working with other software

The mechanisms to verify the authenticity should work between different
chat software such as Jitsi, Pidgin, Adium, and Kopete. You are not
required to use the same chat software to use chat over XMPP and OTR,
but sometimes there are errors in the software. Adium, a chat software
for OS X, has an error receiving the Question and Answer verification.
If you find that verifying others is failing for you when you are using
Question and Answer verification, check whether they are using Adium and
see if you can use another verification method.

Prevention
==========

Human rights workers, journalists and humanitarian staff are sometimes
arrested or detained. The risk of this happening can be significantly
reduced by:

-   Good relations with local authorities and groups where possible
-   Appropriate behaviour, on and off duty
-   Obeying local laws and customs
-   Ensuring that all legal documentation is correct, and carried by all
    staff and vehicles as required
-   Training and briefing staff before they begin their assignments

Be aware of which areas and groups benefit from aid and which do not,
and therefore might feel discriminated against, and make sure that as
many people as possible in the area of operations understand your
organisation and the role it is playing. Transparency, good
communications, integrity, even-handedness and respectful attitudes help
as well.

Evacuation planning and rehearsals should be carried out regularly.
Security situations can deteriorate rapidly, often without warning. The
evacuation plan should be prepared and all staff should understand an
outline of it. The following issues should be considered when preparing
your evacuation plan.

-   **Under what circumstances will you evacuate?** Outline the
    situations and indicators under which you will put this evacuation
    plan into action. Identify the situations under which you will:
    -   **Suspend** work activities in response to security concerns;
    -   **Hibernate** by staff remaining where they are but keeping a
        low profile;
    -   **Relocate** with staff moving internally within the country or
        to a safe-house to escape security concerns, or;
    -   **Evacuate** with staff stopping work and leaving the country
        due to severe security concerns.
-   **Who will be evacuated** - It is essential that all staff members
    clearly understand their and their families? eligibility for
    evacuation or relocation assistance.
    -   **Priority 1** ? International staff family members
    -   **Priority 2** ? Staff members who are in immediate personal
        danger due to the conditions of the crisis
    -   **Priority 3** ? Individuals other than essential staff
    -   **Priority 4** ? Essential staff
-   **Where will staff be evacuated to?**Identify a first-choice
    destination and an alternate destination for evacuation
    or relocation. Organise an emergency safe-house or safe-haven
    if needed. Determine visa requirements, and the logistics that will
    be needed upon arrival.
-   **How will staff be evacuated?**Establish a notification system and
    an assembly point. Detail the route and method of evacuation. Check
    to ensure that these routes can be travelled under
    emergency conditions. Coordinate plans with embassies, UN agencies,
    and other NGOs as appropriate.
-   **What goes and what stays?**Identify which documents, such as
    contracts, payroll records, etc. will be needed to re-establish
    operations once relocated or upon re-entry. Other documents should
    be marked for destruction, or left behind, as appropriate. Consider
    how evacuated documents will be perceived if seized by a particular
    person or group. They may contain information that could put those
    evacuating at risk, and would be better destroyed.
-   **Who is responsible for the various tasks during an evacuation?**
    During crises key staff will be fully occupied so responsibilities
    for evacuation should be clearly defined during the planning stage.
-   **What will be the expected impact of evacuation on the
    operation?**Will the office be closed and, if so, how? What are the
    policies and plans for continuing operations through national staff
    members acting on their own? Or through contractors, if feasible and
    appropriate?

Radios are an insecure method of communication and should not be used
for senstive communication if at all possible. If possible, use
alternative options as outlined in the [Making a Call
lesson](umbrella://lesson/making-a-call). However many in the
humanitarian field still need to use them sometimes. If necessary,
develop a system of code words between those communicating so that your
message will not be so easily understood.

![](radios.png)

Protest marches, rallies or unplanned gatherings may be small and
self-limiting or may become riots and civil disturbance.

It is important to prepare adequately (in proportion to the expected
event) before going to cover it. This can have many different meanings
depending on the size of the team you work with, but should include the
following if possible and appropriate:

-   Prepare emergency and fall back plans ? agree at what stage you
    should pull out and emergency meeting points;
-   Source and pack protective equipment ? see the Protective Equipment
    lesson for more advice on this;
-   Pack a first aid pack ? you should also remind yourself of how to
    administer basic first aid;
-   Select broadcast equipment carefully ? you may want to use discreet
    cameras if filming becomes dangerous;
-   Contact your Safety Adviser or the person responsible for security
    in the organisation you are contracted to ? they should consider the
    size of team needed and whether or not it should include security
    personnel;
-   Teams covering disorder, riots etc should have training and briefing
    on safety in civil unrest situations. Experience is also a
    great help.
-   For large protests a specific risk assessment should be carried out.

Types of Stress
===============

Stress is a natural reaction, and it can be positive and stimulating.
Not all stress is bad. There are different types of stress, both healthy
and unhealthy. Healthy stress helps people focus on the task at hand,
mobilises energy and prepares them for action. When stress occurs too
often, however, or is too intense or lasts too long, it turns from
positive to negative.

![](stress1.png)

There are 3 different types of unhealthy stress: chronic, traumatic, and
also post-traumatic.\
\
1. Chronic stress is a combination of stress factors that builds up over
time, eroding our resilience and ability to work or function
effectively. This type of stress is dealt with below in the beginner?s
lesson.\
\
Traumatic stress results from directly experiencing, or being otherwise
closely exposed to, traumatic events or incidents that are life-
threatening or involve physical and emotional loss. It is dealt with in
the Advanced lesson\
\
Post-traumatic stress is prolonged stress which can occur months or even
years after an event. It is dealt with in the Expert lesson.\
\
People who have been trained about stress responses often react better
under stress because they understand what is happening to them.

Each person will experience stress differently and therefore must manage
their stress in their own way. Stress management varies by culture,
gender, personality, identity and many other factors.

Regular phone calls
===================

When you make a call from a landline or a mobile phone, your call is not
end-to-end encrypted. If you're using a mobile phone, your call may be
weakly encrypted between your handset and the cell phone towers. However
as your conversation travels through the phone network, it's vulnerable
to interception by your phone company and, by extension, any governments
or organizations that have power over your phone company. There are also
inexpensive techniques which other people can use to listen to your
calls if they are close to your phone.

![](call1.png)

*Regular phone calls to or from your mobile phone are not secure.*

![](msg1.png)

Keep what you need
==================

The most basic rule for managing information securely is that any
information that could put people at risk should always be
compartmentalised and kept ?need to know?. This means that only those
people who really need that piece of information to operate should be
given it. For example, if a team is working with a high-risk source,
only the source?s direct contact within the team should have his or her
real name and details ? the rest of the team can operate using a code
name. This reduces the risk for both the source and those other members
of the team.

![](managing_information1.png)

If there is not a good reason to keep a piece of sensitive information
then you should simply delete it (see the [Safely Deleting
lesson](umbrella://lesson/safely-deleting)).

How To Circumvent Online Censorship
===================================

Many governments, companies, schools, and public access points use
software to prevent Internet users from accessing certain websites and
Internet services. This is called Internet filtering or blocking and is
a form of censorship. Content filtering comes in different forms.
Sometimes entire websites are blocked and sometimes content is blocked
based on keywords contained in it. One country might block Facebook
entirely, or only block particular Facebook group pages?or it might
block any page or web search with certain words in it.

![](internetb1.png)

Regardless of how content is filtered or blocked, you can almost always
get the information you need by using a circumvention tool.
Circumvention tools usually work by diverting your web or other traffic
through another computer, so that it bypasses the machines conducting
the censorship.

There are different ways of circumventing Internet censorship, some of
which provide additional layers of security that you may need. The tool
that is most appropriate for you depends on your threat model. If you?re
not sure what your threat model is, you should work it out using the
[Managing Information lesson](umbrella://lesson/managing-information).
Users with a high threat model who need to ensure total anonymity online
should use tools outlined in the Advanced section of this lesson.

Post-Traumatic Stress Disorder - Causes
=======================================

What happens if people don?t heal within the weeks following the trauma?

Post-Traumatic Stress Disorder (PTSD) develops in about 1 in 3 people
who experience severe trauma. Certain factors such as if you or your
family have had depression or anxiety in the past, or you don't receive
much support from family or friends, can make you more susceptible to
developing PTSD after a traumatic event.

In most cases, PTSD develops during the first month after a traumatic
event. However, in a minority of cases, there may be a delay of months
or even years before symptoms start to appear.

![](stress4.png)

Threats of Physical Harm
========================

Finally, understand that there is always one way that attackers can
obtain your password: They can directly threaten you with physical harm
or detention. If you fear this may be a possibility, such as if you are
going to be travelling across hostile borders with sensitive
information, consider ways in which you can hide the existence of the
data or device you are password-protecting, rather than trust that you
will never hand over the password. One possibility is to maintain at
least one computer/email/keepass account that contains largely
unimportant information, whose password you can reveal quickly.

If you have good reason to believe that someone may threaten you for
your passwords, it's good to make sure your devices are configured so
that it won't be obvious that the account you are revealing is not the
?real? one. Is your real account shown in your computer's login screen,
or automatically displayed when you open a browser? If so, you may need
to reconfigure things to make your account less obvious.

In such circumstances, you should also treat your password manager as a
sensitive file, and hide/protect it as we describe in the [Protecting
Files lesson](umbrella://lesson/protecting-files).

Get full access to your smartphone
==================================

Firmware is the permanent software that a manufacturer programmes into a
device?s read-only memory. They run in cooperation with the device's
operating system and are responsible for basic operations of the
hardware of your smartphone, such as the speaker, microphone, cameras,
touchscreen, memory, keys, antennas, etc. Most functionalities are
'locked in' so the user is not capable of controlling or altering these
functions. There are however, some applications and functionalities that
can enhance the security of data and communications on a smartphone.
Also there are some other existing functionalities that can be removed
to avoid security risks.

For this, and other reasons, some smartphone users choose to alter the
programs running the smartphone. The process of overcoming these
manufacturer imposed limits on a smartphone is called rooting (in case
of Android devices), or jailbreaking (in case of iOS devices, like
iPhone or iPad). Successful rooting or jailbreaking will enable you to
install additional applications, make modifications, and give you total
control over data storage and memory of the smartphone in order to make
it more secure.

*WARNING:* Rooting or jailbreaking may not be a reversible process, and
it requires experience with software installation and configuration.
Consider the following:

-   There is a risk of making your smartphone permanently inoperable, or
    'bricking' it (i.e. turning it into a 'brick').
-   The manufacturer or mobile carrier warranty may be voided.
-   In some places, this process maybe illegal.

![](mobileexp1.png)

But if you are careful, a rooted device is a straightforward way to gain
more control over your smartphone to make it much more secure.

Rooting or jailbreaking is a complex process and different for every
device. Search the internet for instructions on the best way to root
your own device.

Countering Physical Surveillance
================================

Physical surveillance continues to be a significant danger to those
working on human rights. Other than a human source, it is the only way
to build detail on what is occurring at meetings. It is obviously
important to know how to identify if you, your colleagues, or partners
are under surveillance.

Counter-surveillance is the process of detecting and mitigating hostile
surveillance. This lesson lets you know how to practice
counter-surveillance at one of the most important times ? when you are
out and about on foot, such as going to a sensitive meeting.

For advice on how to practice counter-surveillance when in a vehicle, go
to the Expert lesson.

![](surveillance2.png)

TOR FOR MAC TOOL GUIDE
======================

Tor for Mac Tool Guide
----------------------

**Lesson to read: [The Internet](umbrella://lesson/the-internet)**\
**This guide outlines how to use the [Tor Browser
Bundle](https://www.torproject.org/projects/torbrowser.html.en) on
Mac.Computer requirements:** An internet connection, a computer running
Mac OS X\
**Version used in this guide:** Tor Browser Bundle: 3.6.2\
**License:** Free Software; mix of Free Software licenses\
**Level:** Intermediate\
**Other reading:** <https://tor.stackexchange.com/>\
Time required: 15-30 minutes

**Using Tor will give you:**\
? The ability to get around internet censorship\
? The ability to get online anonymously

### 1.0 Before you start

Tor is a volunteer-run service that provides both privacy and anonymity
online by masking who you are and where you are connecting. The service
also protects you from the Tor network itself.

For people who might need occasional anonymity and privacy when
accessing websites, Tor Browser provides a quick and easy way to use the
Tor network.

The easiest way to use the Tor network is to use the Tor Browser Bundle,
which combines a web browser, the Tor software, and other helpful
software that will give you a way of more securely accessing the web.

**The Tor Browser works just like other web browsers, except that it
sends your communications through Tor, making it harder for people who
are monitoring you to know exactly what you're doing online, and harder
for people monitoring the sites you use to know where you're connecting
from. Keep in mind that only activities you do inside of Tor Browser
itself will be anonymised. Having Tor Browser installed on your computer
does not make things you do on the same computer using other software
(such as your regular web browser) anonymous.**

2.0 Getting Tor Browser Bundle
==============================

Open a browser like Mozilla Firefox or Internet Explorer and type:
<https://www.torproject.org/projects/torbrowser.html.en> in the URL bar.
If you are using a search engine to look for the Tor Browser Bundle,
make sure that the URL is correct.

![](tool_torosx1.png)

Click the big purple download button to get the installation program for
Tor Browser Bundle.

![](tool_torosx2.png)

The website will have detected your operating system and you'll get the
correct file for Windows. If, for any reason, you want a different
installer file you can scroll down to the Tor Browser Downloads section.

![](tool_torosx3.png)

Many browsers will ask you to confirm whether you want to download this
file.

For any browser, it is best to save the file first before proceeding. So
click the Save button.

### 2.1 Installing Tor Browser Bundle

After the download is complete, you might get an option to open the
folder where the file was downloaded to. The default location is the
Downloads folder.

Double-click on the Tor Browser installer. This opens the .dmg file.

(On recent versions of OS X, you might get a warning that it's from an
"unidentified developer" ? you can get around this complaint
by control-clicking and selecting "open".)

Drag the included file into your Applications folder and you will have a
Tor Browser application in your chosen language that you can pin on your
Dock.

![](tool_torosx4.png)

**Starting Tor Browser for the first time**

Open the Tor Browser folder from your Applications folder and double
click on the file called Tor Browser.

The first time Tor Browser starts, you may get a window that allows you
to modify some settings if necessary. You might have to come back and
change some configuration settings, but go ahead and try to connect to
the Tor network by clicking the Connect button.

After clicking the connect button, a new window will open with a green
bar that will get longer as the Tor software starts up.

![](tool_torosx5.png)

The first time Tor Browser starts it might take a bit longer than usual,
but be patient, within a few minutes Tor Browser will be done and a web
browser opens up congratulating you.

![](tool_torosx6.png)

Countering Physical Surveillance
================================

Physical surveillance continues to be a significant danger to those
working on human rights. Other than a human source, it is the only way
to build detail on what is occurring at meetings. It is obviously
important to know how to identify if you, your colleagues, or partners
are under surveillance.

Counter-surveillance is the process of detecting and mitigating hostile
surveillance. This lesson lets you know how to practice
counter-surveillance at one of the most important times ? when you are
in a vehicle, such as going to a sensitive meeting.

For advice on how to practice counter-surveillance when on foot, go to
the Advanced lesson.

![](surveillance4.png)

KEEPASSX TOOL GUIDE
===================

KeePassX Tool Guide\
Secure password management
--------------------------

**Lesson to read: [Passwords](umbrella://lesson/passwords)**\
**Download Location:** <https://www.keepassx.org/downloads>\
**Computer requirements:** Windows 2000 or higher, Mac OS X 10.4-10.9\
**Version used in this guide:** KeePassX 0.4.3 (KeePassX is a
cross-platform version of the Windows-only KeePass program.)\
**License:** Free and Open-Source Software (primarily GPLv2)\
**Other Reading:** <https://www.keepassx.org/forum/>\
**Level:** Beginner\
**Time required:** 5 minutes

**Using KeePassX will give you:**

? The ability to save all your passwords in one convenient and secure
database\
? The ability to create and store many strong passwords without having
to remember them

### 1.0 Things to consider with KeePassX

KeePassX is a password safe?a program you can use to store all your
passwords for various websites and services. A password safe is a great
tool because it allows you to use different difficult-to-guess passwords
for all your services, without needing to remember them. Instead, you
only need to remember one master password that allows you to decrypt a
database of all your passwords. Password safes are convenient and allow
you to organize all of your passwords in one location.

**It should be noted that using a password safe creates a single point
of failure and establishes an obvious target for bad actors or
adversaries. Research has suggested that many commonly used passwords
safes have vulnerabilities, so use caution when determining whether or
not this is the right tool for you.**

### 1.1 How KeePassX works

KeePassX works with files called password databases, which are exactly
what they sound like?files that store a database of all your passwords.
These databases are encrypted when they?re stored on your computer?s
hard disk, so if your computer is off and someone steals it they won?t
be able to read your passwords.

Password databases can be encrypted via three methods: using a master
password, using a keyfile, or both. Let?s look at the pros and cons of
each.

### 1.2 Using a master password

A master password acts like a key?in order to open the password
database, you need the correct master password. Without it, nobody can
see what?s inside the password database. There are a few things to keep
in mind when using a master password to secure your password database.

? *This password will decrypt all of your passwords, so it needs to be
strong!* That means it shouldn?t be something easy to guess, and it
should also be long?the longer the better! Also, the longer it is, the
less you need to worry about having special characters or capitals or
numbers. A password that is only made up of six random words (in all
lower case, with spaces in between) can be harder to break than a
12-character password made up of upper and lower case letters, numbers,
and symbols.\
? *You need to be able to remember this password!* Since this one
password will allow access to all your other passwords, you need to be
able to make sure you can remember it without writing it down. This is
another reason to use something
like [Diceware](http://world.std.com/~reinhold/diceware.html)?you can
use regular words that are easy to remember, instead of trying to
remember unnatural combinations of symbols and capital letters.

### 1.3 Using a keyfile

Alternatively, you can use a keyfile to encrypt your password database.
A keyfile acts the same way a password would?every time you want to
decrypt your password database you will need to provide that keyfile to
KeePassX. A keyfile should be stored on a USB drive or some other
portable media, and only inserted into your computer when you want to
open your password database. The benefit of this is that even if
somebody gets access to your computer?s hard disk (and thus your
password database) they still won?t be able to decrypt it without the
keyfile stored in the external media. (Additionally, a keyfile can be
much harder for an adversary to guess than a normal password.) The
downside is that any time you want to access your password database,
you?ll need to have that external media handy (and if you lose it or it
gets damaged, then you won?t be able to open your password database).

Using a keyfile instead of a password is the closest thing to having an
actual physical key to open your password database?all you need to do is
insert your USB drive, select the keyfile, and presto! If you do choose
to use a keyfile instead of a master password, though, make sure your
USB drive is stored somewhere safe?*anyone who finds it will be able to
open your password database*.

### 1.4 Using both

The most secure method for encrypting your password database is to use
both a master password and a keyfile. This way, your ability to decrypt
your password database depends on what you know (your master password)
and what you have (your keyfile)?and any malicious entity who wants to
get access to your passwords will need both. (With that said, keep in
mind your threat model?for most home users who just want to store their
passwords, a strong master password should be sufficient. But if you?re
worried about protecting against state-level actors with access to huge
computational resources, then the more security the better.)

Now that you understand how KeePassX works, let?s get started with
actually using it!

### 2.0 Getting started with KeePassX

Once you?ve installed KeePassX from
[here](https://www.keepassx.org/downloads), go ahead and launch it.

Once it?s started, select ?New Database? from the File menu.

A dialog will pop up which will ask you to enter a master password
and/or use a keyfile. Select the appropriate checkbox(es) based on your
choice.

Note that if you want to see the password you?re typing in (instead of
obscuring it with dots) you can click the button with the ?eye? to the
right.

Also note that you can use any existing file as a keyfile?an image of
your cat for example, could be used as a keyfile. You?ll just need to
make sure the file you choose never gets modified, because if its
contents are changed then it will no longer work for decrypting your
password database.

Also be aware that sometimes opening a file in another program can be
enough to modify it; the best practice is to not open the file except to
unlock KeePassX. (It is safe to move or rename the keyfile, though.)

Once you?ve successfully initialized your password database, you should
save it by choosing ?Save Database? from the File menu. (Note that if
you want, you can move the password database file later to wherever you
like on your hard disk, or move it to other computers?you?ll still be
able to open it using KeePassX and the password/keyfile you specified
before.)

### 2.1 Organizing passwords

KeePassX allows you to organize passwords into ?Groups,? which are
basically just folders. You can create, delete, or edit Groups or
Subgroups by going to the ?Groups? menu in the menubar, or by
right-clicking on a Group in the left-hand pane of the KeePassX window.
Grouping passwords doesn?t affect any of the functionality of
KeePassX?it?s just a handy organizational tool.

### 2.2 Storing/generating/editing passwords

To create a new password or store a password you already have,
right-click on the Group in which you want to store the password, and
choose ?Add New Entry? (you can also choose ?Entries &gt; Add New Entry?
from the menubar). For basic password usage, do the following:

? Enter a descriptive title you can use to recognize this password entry
in the ?Title? field.\
? Enter the username associated with this password entry in the
?Username? field. (This can be blank if there is no username.)\
? Enter your password in the ?Password? field. If you?re creating a new
password (i.e. if you?re signing up for a new website and you want to
create a new, unique, random password) click the ?Gen? button to the
right. This will pop up a password generator dialog, which you can use
to generate a random password. There are several options in this dialog,
including what sorts of characters to include and how long to make the
password.\
 \* Note that if you generate a random password, it?s not necessary that
you remember (or even know!) what that password is! KeePassX stores it
for you, and any time you need it you?ll be able to copy/paste it into
the appropriate program. This is the whole point of a password safe?you
can use different long random passwords for *each* website/service,
without even knowing what the passwords are!\
 \* Because of this, you should make the password as long as the service
will allow and use as many different types of characters as possible.\
 \* Once you?re satisfied with the options, click ?Generate? in the
lower right to generate the password, and then click ?OK.? The generated
random password will automatically be entered in the ?Password? and
?Repeat? fields for you. (If you?re not generating a random password,
then you?ll need to enter your chosen password again in the ?Repeat?
field.)\
? Finally, click ?OK?. Your password is now stored in your password
database. To make sure the changes are saved, be sure to save the edited
password database by going to ?File &gt; Save Database.? (Alternatively,
if you made a mistake, you can close and then re-open the database file
and all changes will be lost.)

If you ever need to change/edit the stored password, you can just choose
the Group it?s in and then double-click on its title in the right-hand
pane, and the ?New Entry? dialog will pop up again.

### 2.3 Normal use

In order to use an entry in your password database, simply right-click
on the entry and choose ?Copy Username to Clipboard? or ?Copy Password
to Clipboard,? and then go to the window/website where you want to enter
your username/password, and simply paste in the appropriate field.
(Instead of right-clicking on the entry, you can also double-click on
the username or password of the entry you want, and the username or
password will be automatically copied to your clipboard.)

### 2.4 Advanced use

One of the most useful features of KeePassX is that it can automatically
type in usernames and passwords for you into other programs when you
press a special combination of keys on your keyboard. Note that although
this feature is only available under Linux, other password safes like
KeePass (on which KeePassX was based) support this feature on other
operating systems, and it works similarly.

To enable this feature, do the following.

*1. Choose your global hotkey.* Choose ?Settings? from the ?Extras?
menu, and then choose ?Advanced? in the pane on the left. Click inside
the ?Global Auto-Type Shortcut? field, and then press the shortcut-key
combination you wish to use. (For example, press and hold Ctrl, Alt, and
Shift, and then hit ?p.? You can use any key combination you like, but
you?ll want to make sure that it doesn?t conflict with hotkeys other
applications use, so try to stay away from things like Ctrl+X or
Alt+F4.) Once you?re satisfied, click ?OK.?

*2. Setup auto-type for a specific password.* Make sure that you have
the window open where you?ll want to enter the password. Then go to
KeePassX, find the entry for which you want to enable auto-type, and
double-click on the entry?s title to open up the ?New Entry? dialog.

*3.* Click the ?Tools? button in the bottom left, and select ?Auto-Type:
Select target window.? In the dialog that pops up, expand the drop-down
box and choose the title of the window in which you want the username
and password to be entered. Click OK, and then click OK again.

*Test it out!* Now in order to autotype your username and password, go
to the window/website where you want KeePassX to autotype your
username/password for you. Make sure your cursor is in the text box for
your username, and then hit the combination of keys you chose above for
the global hotkey. As long as KeePassX is open (even if it?s minimized
or not focused) your username and password should automatically be
entered.

Note that depending on how the website/window is set up, this feature
may not work 100% correctly right off the bat. (It might enter the
username but not the password, for example.) You can troubleshoot and
customize this feature, though?for more information we recommend looking
at the KeePass
documentation [here](http://keepass.info/help/base/autotype.html).
(Although there are some differences between KeePass and KeePassX, that
page should be enough to guide you in the right direction.)

It is recommended that you use a key combination that is difficult to
hit accidentally. You don't want to accidentally paste your bank account
password into a Facebook post!

### 2.5 Other features

You can search your database by typing something in the search box (the
text box in the toolbar of the main KeePassX window) and hitting enter.

You can also sort your entries by clicking on the column header in the
main window.

You can also ?lock? KeePassX by choosing ?File &gt; Lock Workspace,? so
that you can leave KeePassX open, but have it ask for your master
password (and/or keyfile) before you can access your password database
again. You can also have KeePassX automatically lock itself after a
certain period of inactivity. This can prevent someone from accessing
your passwords if you step away from your computer. To enable this
feature, choose ?Extras &gt; Settings? from the menu and click on the
security options. Then check the box that says ?Lock database after
inactivity of {number} seconds.?

KeePassX can also store more than just usernames and passwords. For
example, you can create entries to store important things like account
numbers, or product keys, or serial numbers, or anything else. There?s
no requirement that the data you put in the ?Password? field actually
has to be a password. It can be anything you want?just input what you
want to store in the ?Password? field instead of an actual password (and
leave the ?Username? field blank if there?s no username) and KeePassX
will safely and securely remember it for you.

Passwords are often the first and only barrier between your information
and anyone who might want to read, use or destroy it without your
permission.

In general, when you want to protect something - whether a house or an
email account - you lock it up with a key. All keys, physical and
electronic, have one thing in common: they open their locks just as
effectively in the hands of somebody else. You can use the most advanced
security tools, but if your password is weak, or if you allow it to fall
into the wrong hands, they will not do you any good.

![](password1.png)

Vehicle-related accidents are the major cause of injuries and fatalities
among aid personnel. Driving in unfamiliar and sometimes difficult
conditions can increase the likelihood of an accident. Other dangers
include ambush, robbery and aggressive behaviour of armed personnel at
checkpoints. If available and practical, all staff members should
receive driver safety training.

The most important piece of security advice an aid worker or human
rights defender can be given is ALWAYS WEAR A SEATBELT.

Driving Guidelines

-   Park in well-lit, heavily populated areas. Close all windows and
    lock doors before leaving the vehicle. Have keys ready in hand when
    returning to vehicle. Check the back seat before entering.
-   Immediately lock doors upon entry. Open windows no more than 5 cm
    and only those windows near occupied seats.
-   Do not speed or drive too fast for conditions. Observe local driving
    laws and regulations.
-   Avoid night driving or driving alone where possible.
-   Avoid letting the fuel tank fall below half full.
-   Keep a spare vehicle key in the office.
-   Never voluntarily carry unauthorized passengers,
    especially soldiers. However, if threatened, provide
    the transportation. In the event of an attempted carjacking, you
    should not risk your life to save a vehicle.

Protecting Yourself on Social Networks
======================================

Social networking sites are some of the most popular websites and tools
we use on the Internet. Facebook, Google+, and Twitter have hundreds of
millions of users each. With social networking platforms come many
benefits, such as the unprecedented opportunity to communicate, publish,
coordinate, and persuade. Many people use it for their professional as
well personal lives. But, this also means that we're sharing a lot about
ourselves online, usually more than we realise. In some cases, this can
put our operations, our contacts, or us at risk.

![](socialb1.png)

When using social networks it is important to consider:

-   -   What information do I want keep private and who do I want to
    keep it private from?

Depending on your circumstances, you may need to protect yourself
against the social media site itself, against other users of the site,
or both.

Your main goal if you have been kidnapped is to survive and regain
freedom.

How you behave during a kidnapping can increase or reduce the likelihood
of survival and regaining freedom. You therefore have some control over
the outcome of a kidnapping.

There are five key phases of a kidnap/hostage situation:

1.  Surveillance
2.  Capture
3.  Transport (This could happen several times)
4.  Confinement
5.  Release/ Termination

Prevention measures for stages one and two are dealt with in the
Beginner lesson. This lesson will outline survival strategies for
capture, transport, confinement and release.

What is malware?
================

Malware, short for "malicious software," is software that is used to
harm computer users. It can do things like gather information,
impersonate a user, gain access to other computers, or stop a computer
from working. It could do this by allowing an attacker to record from a
webcam and microphone, disabling anti-virus programs, recording
keystrokes, copying emails and other documents, stealing passwords, and
more. Most malware is criminal and is often used to obtain banking
information or other valuable information. However, it is also used by
governments, law enforcement agencies, and even private citizens to spy
on users.

![](malware1.png)

TOR FOR WINDOWS TOOL GUIDE
==========================

Tor for Windows Tool Guide\
Online Anonymity and Circumvention
----------------------------------

**Lesson to read: [The Internet](umbrella://lesson/the-internet)**\
**This guide outlines how to use the [Tor Browser
Bundle](https://www.torproject.org/projects/torbrowser.html.en) on
Windows.Computer requirements:** An internet connection, a computer
running Windows\
**Version used in this guide:** Windows: Windows 7 Ultimate; Tor Browser
Bundle: 3.6.2\
**License:** Free Software; mix of Free Software licenses\
**Level:** Intermediate\
**Other reading:** <https://tor.stackexchange.com/>\
Time required: 15-30 minutes

**Using Tor will give you:**\
? The ability to get around internet censorship\
? The ability to get online anonymously

### 1.0 Before you start

Tor is a volunteer-run service that provides both privacy and anonymity
online by masking who you are and where you are connecting. The service
also protects you from the Tor network itself.

For people who might need occasional anonymity and privacy when
accessing websites, Tor Browser provides a quick and easy way to use the
Tor network.

The easiest way to use the Tor network is to use the Tor Browser Bundle,
which combines a web browser, the Tor software, and other helpful
software that will give you a way of more securely accessing the web.

**The Tor Browser works just like other web browsers, except that it
sends your communications through Tor, making it harder for people who
are monitoring you to know exactly what you're doing online, and harder
for people monitoring the sites you use to know where you're connecting
from. Keep in mind that only activities you do inside of Tor Browser
itself will be anonymised. Having Tor Browser installed on your computer
does not make things you do on the same computer using other software
(such as your regular web browser) anonymous.**

### 2.0 Getting Tor Browser Bundle

Open a browser like Mozilla Firefox or Internet Explorer and type:
<https://www.torproject.org/projects/torbrowser.html.en> in the URL bar.
If you are using a search engine to look for the Tor Browser Bundle,
make sure that the URL is correct.

![](tool_torwin1.png)

Click the big purple download button to get the installation program for
Tor Browser Bundle.

![](tool_torwin2.png)

The website will have detected your operating system and you'll get the
correct file for Windows. If, for any reason, you want a different
installer file you can scroll down to the Tor Browser Downloads section.

![](tool_torwin3.png)

Many browsers will ask you to confirm whether you want to download this
file. Internet Explorer 11 shows a bar at the bottom of the browser
window with an orange border.

![](tool_torwin4.png)

For any browser, it is best to save the file first before proceeding. So
click the Save button. This example shows Tor Browser Bundle version
3.6.2, which was the current version at the time we wrote this. There
will probably be a more recent version available for download by the
time you read this.

### 2.1 Installing Tor Browser Bundle

After the download is complete, you might get an option to open the
folder where the file was downloaded to. The default location is the
Downloads folder. Double-click on the
file *torbrowser-install-3.6.2\_en-US.exe*

![](tool_torwin5.png)

After double-clicking on the Tor Browser installer, a window will open
with a warning about the origin of the software. You should always take
these warnings seriously and make sure you trust the software you want
to install and that you got an authentic copy from the official site
over a secure connection. Since you know what you want, and you know
where to get the software, and the download was from the Tor Project's
secure HTTPS site, go ahead and click Run.

![](tool_torwin6.png)

A small window will open asking what language you want to use for the
Tor Browser Bundle. There are several to choose from. Pick the language
you want and click the OK button.

![](tool_torwin7.png)

You'll find a new window that will tell you where the Tor Browser Bundle
will be installed. The default location is your desktop. You can change
this to be a different location if you want, but for now keep the
default.

![](tool_torwin8.png)

The installation process is complete when you see a window that says you
have completed the installation process. If you click the Finish button,
the Tor Browser will start immediately. For now, uncheck the box by ?Run
Tor Browser Bundle.? We'll come back to using Tor Browser Bundle in a
bit. If you missed unchecking the checkbox and Tor Browser starts, just
close the window for now.

![](tool_torwin9.png)

Tor Browser Bundle will not be installed with other programs and will
not show up in your start menu.

![](tool_torwin10.png)

### 3.0 Using Tor Browser Bundle

**Starting Tor Browser for the first time**

You chose not to start Tor Browser when you finished with the installer,
so now go ahead and start Tor Browser for the first time. If you
followed all the default settings from the installation you'll see a
folder on your desktop called Tor Browser.

![](tool_torwin11.png)

Open the Tor Browser folder and double click on the file called Start
Tor Browser.

![](tool_torwin12.png)

The first time Tor Browser starts, you'll get a window that allows you
to modify some settings if necessary. You might have to come back and
change some configuration settings, but go ahead and try to connect to
the Tor network by clicking the Connect button.

![](tool_torwin13.png)

After clicking the connect button, a new window will open with a green
bar that will get longer as the Tor software starts up.

![](tool_torwin14.png)

The first time Tor Browser starts it might take a bit longer than usual,
but be patient, within a few minutes Tor Browser will be done and a web
browser opens up congratulating you.

![](tool_torwin14.png)

Dealing with the kidnapping of a member of staff is a very sensitive and
complex task. This lesson provides only the basic outline for
recommended actions.

**If one of your staff is kidnapped we highly recommend reading the
detailed advice given in the ?Further Reading? links at the end of this
lesson.**

Recording passwords securely
============================

Our Basic section showed you how to create a strong, memorable password.
However, because you need a different password for every account or
service and also need to change them every few months, it can soon
become difficult to remember them all. Fortunately, there are software
tools to help with this ? a password manager is a software application
that can generate random, secure passwords for each of your accounts and
record them in a portable, encrypted password database, such as KeePass.

![](password_adv1.png)

The password manager protects all of your passwords with a single master
password so you only have to remember one thing. Of course, if you use
this method, it becomes especially important that you create and
remember a very secure password for KeePass, or whatever tool you
choose. Whenever you need to enter a password for a specific account,
you can look it up using only your master password, which makes it much
easier to follow all of the suggestions above.

KeePass sits on your desktop, and it also portable, which means that you
can put the database on a USB memory stick in case you need to look up a
password while you are away from your primary computer.

You can learn how to set up and use this tool in the [Keepass tool
guide](umbrella://lesson/keepassx).

RECUVA TOOL GUIDE
=================

Recuva Tool Guide\
Data recovery and secure deletion
---------------------------------

**Lesson to read:\
? [Backing Up](umbrella://lesson/backing-up)**\
**Download Location:** <http://www.piriform.com/recuva/builds>  \
**Computer requirements:** Any version of Windows\
**Version used in this guide:** Recuva 1.3\
**License:** Freeware\
**Level:** Intermediate\
**Time required:** 20 minutes

**Using Recuva will give you:**\
? The ability to perform different scanning techniques\
? The ability to recover previously deleted files on your computer,
including emails, images and videos\
? The ability to securely delete private or sensitive information

Mac OS users could use [TestDisk and PhotoRec](www.cgsecurity.org/), as
an alternative, which are also compatible with Microsoft Windows and GNU
Linux.

### 1.1 Before you start

In situations where private or sensitive files may have been mistakenly
deleted, Recuva can help you to scan for and restore some of them. As
discussed in the **[Deleting
lesson](umbrella://lesson/safely-deleting)**, a file deleted using the
standard Windows operating system Delete function, even after the
Recycle Bin has been emptied, might still exist on the computer.

However, there are circumstances under which Recuva cannot retrieve
information. If you have permanently deleted or wiped any temporary
files by running CCleaner with the Secure file deletion (Slower) option
enabled, those files are virtually unrecoverable. Recuva cannot recover
files after programs like CCleaner or Eraser have been used to wipe free
disk space or if Windows itself has already overwritten any previously
occupied space. Recuva also cannot recover damaged documents and files.

Recuva can also be used to securely overwrite your private or sensitive
data.

### How to Install Recuva

### 2.0 How to Install Recuva

**Step 1.** Double click ?rcsetup138.exe?; the *Open File - Security
Warning* dialog box may appear. If it does, click ?Run? to activate the
language box.

**Step 2.** Click ?OK? to activate the Welcome to the *Recuva Setup
Wizard* screen.

**Step 3.** Click ?Next? to activate the *License Agreement* screen.
Please read the *License Agreement* before proceeding with the rest of
the installation process.

**Step 4.** Click ?I Agree? to activate the *Choose Install*
Location screen.

**Step 5.** Click ?Next? to activate the *Install Options* screen.

**Note:** The *Install Options* screen appears with the *Install
optional Yahoo! toolbar* option enabled. Do *not* install the Yahoo!
toolbar, which may compromise your Internet privacy and security.

**Step 6.** Check the *Install optional Yahoo! toolbar* check box to
disable it as shown below:

![](tool_recuva1.png)

**Step 7.** Click ?Install? to begin installing Recuva. This will
activate the installation progress bar that will disappear after the
installation has completed itself in a few minutes.

**Step 8.** Click ?Finish? to complete installing Recuva.

Now that you have successfully installed Recuva, you are ready to begin
recovering and/or overwriting private and sensitive information.

### How to Perform Different Scans Using Recuva

### 3.0 Before You Begin

In this section, you will learn how to perform different types of scans,
and be introduced to the *General* and *Actions* tabs in the
*Options* screen. **Note:** A scan will simply retrieve and display the
files which are potentially recoverable. The actual recovery procedures
are discussed in the next section.

### 3.1 How to Perform a Scan Using the Recuva Wizard

The Recuva *Wizard* is recommended in situations where neither the full
nor partial name of the file you would like to recover is known. It is
also recommended if this is the first time you are using Recuva.
The Recuva *Wizard* lets you set the scan parameters by letting you
specify the file type and/or from where the file was deleted.

To begin scanning for deleted files, perform the following steps:

**Step 1.** Click the Recuva icon or select Start &gt; Programs &gt;
Recuva &gt; Recuva to launch the program, and activate the following
screen:

![](tool_recuva2.png)

**Tip:** If you know the exact or even partial name of a file you would
like to recover, click ?Cancel? to go to the *Piriform Recuva* main user
interface, and then follow the steps in section 3.2 How to Perform a
Scan without Using the Recuva Wizard.

**Step 2.** Click ?Next? to activate the following screen:

![](tool_recuva3.png)

The *Recuva Wizard File type* displays a list of different file types,
and describes what files might be recovered when each option is enabled.

**Step 3.** Check the *Other* option, and then click ?Next? to activate
the following screen:

![](tool_recuva4.png)

**Note:** The default setting for the *Recuva Wizard File
Location* screen is the *I'm not sure option*. This option will extend
the scan to all drives as well as removable media, except CDs, DVDs and
optical media. It may, therefore, require a longer time to generate
results.

Files are most frequently deleted from Recycle Bin in
the Windows operating systems, to minimize the chance of your
accidentally deleting private or sensitive information.

**Step 4.** Check the *In the Recycle Bin* option as shown above, and
then click ?Next? to activate the following screen:

![](tool_recuva5.png)

**Note:** For this exercise, do not enable the *Deep Scan* option. This
scanning technique will be discussed in section 3.3 How to Perform a
Deep Scan.

**Step 5.** Click ?Start? to begin recovering your deleted files.

During the file recovery process, two progress status bars appear in
quick succession. The *Scanning the drive for deleted files* progress
bar lists the deleted files. The *Analyzing the file contents* progress
bar groups and sorts the deleted files into file types and degree of
recoverability. They also display the duration of the scanning and
analysis processes. Your *Piriform Recuva* main user interface may then
resemble the following screen:

![](tool_revua6.png)

The *Piriform Recuva* main user interface lists information about each
deleted file, arranged in six columns. Each column is described as
follows:

**Filename** This displays the name and file extension of the deleted
file. Click the *Filename* title to arrange the deleted files in
alphabetical order.

**Path:** This displays where the deleted file was found. Given that
the *In the Recycle Bin* option was enabled in this example, the file
path is *C:RECYCLER* for all the deleted files. Click the *Path* title
to view all the files listed under a particular directory or file path.

**Last modified:** This displays the last time the file was modified
before it was deleted, and can be useful in helping to identify the file
you would like to recover. Click *Last modified* to list the deleted
files according to the oldest or most recent.

**Size:** This displays the size of the file. Click *Size* to list the
deleted files beginning with the largest or smallest deleted file.

**Status:** This displays the extent to which the file is recoverable,
and corresponds to the file status icons discussed
below. Click *Status* to sort the deleted files into the three basic
categories, and list them from *Excellent* to *Unrecoverable*.

**Comment:** This displays why a given file may or may not be
recoverable, and the extent to which a deleted file has been overwritten
in the Windows Master File Table. Click *Comment* to view the extent to
which a file or group of files have been overwritten.

Each file is associated with a coloured status icon which indicates the
extent to which each file can be successfully recovered:

The following list describes each status icon:

? Green: The chances for a full recovery are excellent.\
? Orange: The chances for recovery are acceptable.\
? Red: The chances for recovery are unlikely.

### 3.2 How to Perform a Scan without Using the Recuva Wizard

To access the Recuva main user interface directly, (that is, not use
the *Recuva Wizard*), perform the following steps:

**Step 1.** Click the Recuva icon or select Start &gt; Programs &gt;
Recuva &gt; Recuva.

**Step 2.** Check the *Do not show this Wizard on startup* option,
then click ?Cancel? to activate the following screen:

![](tool_recuva7.png)

The *Piriform Recuva* main user interface is divided into the results
pane on the left and the *Preview*, *Info* and *Header* tabs in which to
sort and view information about a specific deleted file. It lets you set
certain scan options, similar to those in the *Recuva Wizard*.

**Step 3.** Click to activate the drop-down list and select the drive to
be scanned; the *Local Disk (C:)* is the default and used in this
example as follows:

![](tool_recuva8.png)

The *Filename* or *path* drop-down list lets you specify the kind of
file you are looking for, and loosely corresponds to the *Recuva Wizard
File type* screen.

![](tool_recuva9.png)

The *Filename* or *path* feature is a combination of a text box and
drop-down list. It has two main uses: To let you directly search for a
specific file, and/or to sort through a list of deleted files, according
to file type.

Alternatively, the *Filename* or *path* feature can be used to search
for files of a specific type, or to sort through a general list of
deleted files in the results pane.

To begin scanning for a file of which all or part of the name is known,
perform the following steps:

**Step 1.** Type in the name or partial name of a file you would like to
recover as follows (in this example, the file *triangle.png* is being
scanned):

![](tool_recuva10.png)

Tip: Click X to reset the *File name and path* (which appear greyed
out).

**Step 2.** Click ?Scan? to begin scanning for your deleted file(s);
shortly thereafter, a screen will appear resembling the following:

![](tool_recuva11.png)

### 3.3 How to Perform a Deep Scan Using Recuva

The *Enable Deep Scan* option lets you conduct a more thorough scan;
naturally, a deep scan takes a longer time, depending on your computer
speed and the number of files you have. This option might prove useful
if your initial scan does not display the files you would have liked to
recover. Although a deep scan may even take hours depending on the
amount of data stored on your computer, it may improve your chances of
recovering the files you require.

The Recuva *Deep Scan* option can be enabled either
through checking the *Enable Deep Scan* option in the *Recuva Wizard*.

**Step 1.** Click ?Options? to activate the *Options* screen,
then click the *Actions* tab as follows:

![](tool_recuva12.png)

**Step 2.** Check the *Deep Scan (increases scan time)* option,
then click ?OK?.

**Step 3.** Click ?Scan? to begin scanning for deleted files using
the *Deep Scan* option. As mentioned earlier, a deep scan can
potentially take a few hours, depending on the size of your hard disk
and computer speed:

![](tool_recuva13.png)

### 3.4 An Introduction to the Options Screen

In this section, you will learn how to use the different settings to
successfully recover and overwrite your private or sensitive information
in the *Options* screen. To configure these settings, perform the
following steps:

**Step 1:** Click ?Options? to activate the following screen:

![](tool_recuva14.png)

The *Options* screen is divided into
the *General*, *Actions* and *About* tabs.

The *General* tab lets you define a number of important settings,
including *Language* (Recuva supports 37 languages), *View mode* and
disabling or enabling the *Recuva Wizard*.

![](tool_recuva15.png)

The View Mode lets you select how you would like to view the deleted
files, and can also be enabled whenever you right click a file in
the *Piriform Recuva*.

? **List:** This option lets you view the deleted files in a list\
? **Tree:** This option lets you view the directory path of deleted
files in the form of an expandable tree.\
? **Thumbnails:** This option lets you view the deleted files as
graphics or images where possible.

Most importantly perhaps, the *Advanced* section of the *General* tab
lets you set the number of times your data can be overwritten by random
data to protect it from recovery by hostile or malicious parties.

The *Secure overwriting* drop-down list displays four options for
overwriting your private information. Its default mode is *Simple
Overwrite (1 pass)*. A pass refers to the number of times your document,
file or folder will be overwritten with random data to render it
completely unreadable.

**Step 2: Select** the *DOD 5220.22-M (3 passes)* option as follows:

![](tool_recuva16.png)

A single pass may prove quite effective in overwriting a given document,
file or folder; however, there are parties with the resources and skills
to recover a relatively light secure overwrite. Three passes is a solid
balance between the time required to perform a secure overwrite, and the
ability to recover that document, file or folder.

**Step 3.** Click ?OK? to save your *General* tab configuration options.

![](tool_recuva17.png)

? **Show files found in hidden system directories:** This option lets
you display files in hidden system directories.

? **Show zero-byte files:** This option lets you show you files that
have little to no content, and which are basically irrecoverable.Show
securely deleted files: This option lets you display files that have
been securely deleted in the results pane.

**Note:** If you have already used CCleaner or a similar program, it
changes the filename to ZZZZZZZ.ZZZ when it securely deletes a file, for
security reasons.

? **Deep Scan:** This option lets you scan the entire drive for the
deleted document or file; if previous scans have proven ineffective in
locating your file, the Deep Scan may prove useful. However, it does
require more time. Please refer to section 3.3 How to Perform a Deep
Scan Using Recuva.

? **Scan for non-deleted files (for recovery from damaged or reformatted
disks):** This option lets you attempt to recover files from disks that
may have sustained physical damage or software-related corruption.

The *About* tab displays version information, as well as links to the
Piriform web site.

Now that you are more confident about performing different scans and
familiar with the settings in the *General* and *Actions* tabs in
the Options screen, you are ready to learn how to actually recover
and/or securely overwrite your private or sensitive information.

### How to Recover and Securely Overwrite Files Using Recuva

### 4.0 Before You Begin

In this section, you will learn how to recover a previously deleted
file, as well as how to securely overwrite any private or sensitive
information.

Recuva lets you create a new folder for storing your recovered files.
Although Recuva does let you use existing folders, for reasons of safety
and security, we recommend that you copy your recovered files to a
removable device like a backup drive or USB memory stick.

**Important:** Although Recuva does an excellent job of securely
overwriting information, it may leave a file marker indicating the
existence of such a file. To protect your privacy and security, it makes
sense to save any important, private or sensitive information to a
removable device, and not to the original location or path.

### 4.1 How to Recover a Deleted File

To begin recovering a deleted file, perform the following steps:

**Step 1.** Connect your removable disk or a USB memory stick to your
computer.

**Step 2.** Check the check box next to a file you want to recover to
enable the Recover... button or double click that file to both
check and highlight that file.

**Step 3.** Click ?Recover?? to activate the *Browse For Folder* screen.

**Step 4.** Select a destination and then click ?Make New Folder? to
create your recovery folder as shown below.

![](tool_recuva18.png)

**Note:** In this example, the folder for storing your recovered
documents and files has been given an obvious label. However, keeping
your digital privacy and security in mind, we encourage you to be more
careful in labelling your own folder.

**Step 5.** Click ?Yes? to begin the file recovery process; a progress
status screen appears as follows:

![](tool_recuva19.png)

After the files have been recovered, a confirmation will appear
resembling the following screen:

![](tool_recuva20.png)

**Note:** Recuva supports multiple file recovery. Simply check the check
boxes of the files you would like to recover and perform steps
**3** to **5**.

Now that you are comfortable with recovering a previously deleted file,
you are ready to learn how to use the pop-up menu to perform multiple
file recoveries and secure overwriting of files.

### 4.2 How to Use the Pop-up Menu

Recuva offers different options for selecting the documents, files or
folders you would like to delete or securely overwrite.

? **Checking** is generally used to quickly select several
non-contiguous or separate files for recovery or secure overwriting.\
? **Highlighting** is generally used to quickly select contiguous
multiple files in a block or group for recovery or secure overwriting.

Right click on a deleted file displayed in the Recuva main to activate
the following pop-up menu:

![](tool_recuva21.png)

**Recover Highlighted:** This item lets you recover all or any
highlighted deleted file(s).

**Recover Checked:** This item lets you recover a checked deleted file.

**Check Highlighted:** This item lets you check a highlighted deleted
file.

**Uncheck Highlighted:** This item lets you uncheck a highlighted
deleted file.

As you recall, the View Mode can also be set in the *General* tab in
the *Options* screen. This item lets you select how you would like to
view the deleted files.

? **List:** This option lets you view the deleted files in a list as
in Figure 5\
? **Tree:** This option lets you view the directory path of deleted
files in the form of an expandable tree.\
? **Thumbnails:** This option lets you view the deleted files as
graphics or images where possible.

**Highlight Folder:** This option lets you select multiple deleted files
according to their directory path, and lets you perform the actions
listed in the pop-up menu on them.

**Secure Overwrite Highlighted:** This option lets you securely
overwrite a highlighted deleted file.

**Secure Overwrite Checked:** This option lets you securely overwrite a
checked deleted file, changing its status icon to red.

### 4.3 How to Securely Overwrite a Deleted File

To securely overwrite a deleted file, perform the following steps:

**Step 1.** Check the individual file you would like to have securely
overwritten, and then right click the check box it to activate the
pop-up menu.

**Step 2.** Select ?Secure Overwrite Checked? to activate the following
confirmation dialog box:

![](tool_recuva22.png)

**Step 3.** Click ?Yes? to begin the overwriting process; depending on
the size and status of the file as well as the *Secure
overwriting* option you selected in the *General* tab in
the *Options* screen, this could take some time. After the overwriting
process has been completed, a screen resembling the following appears:

![](tool_recuva23.png)

You have successfully completed recovering and securely overwriting
files using Recuva previously deleted files.

### 5 PORTABLE RECUVA

### 5.1 Differences between the Installed and Portable Versions of Recuva

Given that portable tools are not installed on a local computer, their
existence and use may remain undetected. However, keep in mind that your
external device or USB memory stick, and portable tools are only as safe
as the computer you are using, and may risk being exposed to adware,
malware, spyware and viruses.

There are no other differences between Portable Recuva and the version
designed to be installed.

### 5.2 How to Download and Extract Recuva Portable

To begin downloading and extracting Recuva Portable, perform the
following steps:

**Step 1.** Click <http://www.piriform.com/recuva/download/portable> to
be directed to the appropriate download site, and automatically activate
the following screen:

**Step 2.** Click ?OK? to save the *rcsetup140.zip* installation file to
your computer; and then navigate to it.

**Step 3.** Right click to activate the Windows pop-up menu, and
then select the Extract files... item as shown below:

![](tool_recuva24.png)

**Step 4.** Navigate to the removable drive or USB memory stick as shown
below, and then click ?New Folder? to create a new folder in which to
extract the installation file.

![](tool_recuva25.png)

**Step 5.** Enter a name for the new folder in the document tree as
shown below:

![](tool_recuva26.png)

Alternatively, you may type in a folder name in the accompanying
drop-down list: 

![](tool_recuva27.png)

**Note:** Although for the purposes of this example, the new folder is
entitled Recuva Portable, users may choose different name.

**Step 6.** Click ?OK? to begin extracting its contents to newly created
folder.

**Step 7.** Navigate to your destination external drive or USB memory
stick, as shown below, then open it to confirm that the Portable
Recuva program was successfully extracted.

![](tool_recuva28.png)

**Step 8.** Double click *Recuva.exe* to activate the Portable
Recuva wizard.

Please refer to the rest of the Recuva tool guide above to begin
configuring and using it.

HOW TO CHANGE YOUR FACEBOOK PRIVACY SETTINGS
============================================

How to change your Facebook privacy settings
--------------------------------------------

**Lesson to read: [Social Media](umbrella://lesson/social-media)**\
**Level:** Beginner\
**Time required:** 10 minutes

### How to Protect Your Privacy from Facebook's Graph Search

Facebook now has a feature?Graph Search?that has been the subject of
many privacy concerns. Graph Search allows users to make structured
searches to filter through friends, friends of friends, and strangers.
This feature relies on your profile information being made widely or
publicly available, yet there are some Likes, photos, or other pieces of
information that you might not want out there.

Since Facebook removed the ability to remove yourself from search
results altogether, the Electronic Frontier Foundation put together a
quick how-to guide to help you take control over what is featured on
your Facebook profile and on Graph Search results ? we have outlined it
below. (Facebook also has a
new [video](https://www.youtube.com/watch?v=bSji6Y66aKo) explaining how
to control what shows up in Graph Search.)

### What's public on my profile?

Click on the lock in the top menu bar, and under "Who can see my stuff?"
click "View As." This will take you to the public view of your profile.
Here you can see exactly what information, photos, and posts are
available to the public. If there's anything you don't want the whole
Facebook universe to be able to see, you can change individual settings
to hide particular items.

![](tool_facebook1.png)

### How do I hide my general information?

Go to your profile page and click "Update Info." You can control who is
able to see what personal information you've listed?and if they're able
to see it, they're able to search it.

![](tool_facebook2.png)

### Who can see my posts, both past and future?

You can access your [privacy
settings](https://www.facebook.com/settings?tab=privacy) by clicking on
the lock in the top menu bar, then clicking "See More Settings." From
here, you can choose your audience for future posts (including photos),
and you can also limit who has access to previous posts that were more
widely accessible.

![](tool_facebook3.png)

### How do I hide my photo albums?

Go to your profile page and click on "Photos," then "Albums." You can
configure who has access to each album.

![](tool_facebook4.png)

Note that tagging others in a photo by default gives their friends the
ability to see that photo. Also note that removing a photo from your
Timeline does not remove it from being searched, especially if it is
someone else's photo.

In order to make sure that photo is not searchable, you must detag
yourself or report the photo. Facebook has another [great
video](https://www.youtube.com/watch?v=CaJYQXiu3PY) about how to do just
this.

To detag yourself, click on a photo, and on the bottom of the picture
click on "Options." Next, click "Report/Remove Tag." This gives you the
option to remove your tag, as well as to notify the poster that you'd
like the photo to be taken down.

![](tool_facebook6.png)![](tool_facebook5.png)

### How do I hide my "Likes"?

Go to your profile page and click on "Likes." Click "Edit" on the top
right. From there, you can edit who can see your liked pages in each
individual category.

![](tool_facebook7.png)

### Do I actually "Like" these things?

While you are configuring your "Likes," we encourage you to take a
moment to reassess the pages you have listed. A few years later, you may
not like "Free Booze Fridays" anymore. Unliking is as simple as going to
a particular page, hovering your mouse over "Liked," and clicking
"Unlike."

![](tool_facebook8.png)

### How do I hide my friends and relationships?

Besides locking down your own personal information, it turns out that
your friends and relationships can appear in searches associated with
you. Because [they have no
control](https://www.eff.org/deeplinks/2013/01/facebook-graph-search-privacy-control-you-still-dont-have) over
how they appear in such searches, we strongly encourage you to do the
altruistic thing and lock down your friendship settings. Here's how to
set your privacy settings to keep your friendships and relationships?and
therefore related search results?limited in visibility to only whom you
want.

First, go to your profile and click on "Friends." On the top right of
the page, click on the "Edit" button. This allows you to select who can
see your friend list.

![](tool_facebook9.png)

Next, you should adjust the settings of your relationships and family
associations. Go to your profile and click "Update Info," then scroll
down to "Family" on the bottom left. When you click "Edit," you can
choose the specific privacy settings for each relationship.

![](tool_facebook10.png)

### Keep it up!

The most important think you can do is to check your privacy settings
often?especially after new features are released. Facebook has done a
better job of making new privacy settings more accessible while also
notifying users of any changes. Their explanations, however, can lose
sight of bigger picture concerns.

HOW TO HOW TO OPT-OUT OF FACEBOOK'S DATA BROKER RELATIONSHIPS
=============================================================

How to opt-out of Facebook's data broker relationships
------------------------------------------------------

**Lesson to read: [Social Media](umbrella://lesson/social-media)**\
**Other reading:**
<https://www.eff.org/deeplinks/2012/04/4-simple-changes-protect-your-privacy-online>\
**Level:** Beginner\
**Time required:** 30 minutes

Facebook is teaming up with four of the world?s largest corporate data
brokers to ?enhance? the ad experience for users. Datalogix, Epsilon,
Acxiom, and BlueKai obtain information gathered about users through
online means (such as through cookies when users surf the web) as well
as through offline means (such as through loyalty cards at supermarkets
and product warranty cards).  Facebook will use this information to
tailor its ads. The Electronic Frontier Foundation describes what this
means and how you can avoid it.

In practical terms, this means that limiting how much information you
put on Facebook is not enough to limit how ads are targeted to you on
Facebook. Your interests, age, shopping history (including offline), web
browsing, location, and much more could be stored by these data brokers
and utilized to market to you ? even if you?ve been careful not to share
this type of information with Facebook.

So, what can users do? If you?re concerned about this practice, you can
opt out of the targeted advertisements by individually visiting each of
the data broker partners currently working with Facebook. We've got
directions below for opting out of each site.

We also have two general tips:

**1.  Install an add-on to protect your privacy online.** Facebook is
using "blind cookie-matching" to match up users of online marketer
BlueKai with specific Facebook accounts. Blocking trackers is a good
general practice for stopping this type of tracking. We recommend you
use a tool such as [Ghostery](http://www.ghostery.com/) (now available
on Firefox, Safari, Chrome, Opera and Internet Explorer).

**2. Avoid giving your phone number and email address to companies when
possible.** Facebook and these companies are primarily using hashed
email addresses to match users between databases, though they may also
use hashed phone numbers. If you?re filling out a survey or signing up
to receive email updates from a website, consider creating and using a
different email address than the one you associate with your Facebook
account. Similarly, consider setting up an alternate phone number you
can give to companies apart from the phone number you connect with your
social media accounts.

### Opt Out Instructions:

Note that in general, opting out of data brokers will not necessarily
result in your data being removed from their lists. Instead, these
companies will generally 'suppress' your information from certain uses
-- including, hopefully, in the batches of data sent to Facebook. The
process below takes a bit of effort, but you really do need to opt out
of all four data brokers separately to get out of this program.

**Acxiom**

1\. To get started, visit Acxiom's [Opt Out
Form](https://isapps.acxiom.com/optout/optout.aspx). Then scroll down
until you see your "opt-out choices." Here there will be a list of the
types of media you would like to opt out of (mail, telemarketing, email,
and online advertising).  You can check all four, though note that their
online advertising opt-out is cookie-based, meaning it will disappear
every time you clear your cookies. 

![](tool_facebook11.png)

2\. Certify that you are just a single person.

![](tool_facebook12.png)

3\. Fill out the form with your personal information. In order to be sure
that Acxiom doesn't target advertisements at you through Facebook,
you'll want to provide Acxiom with the phone number and email address
associated with your Facebook profile. Use the green + signs on the form
to add information.

![](tool_facebook13.png)

4\. Click submit. After you hit submit (and get through a CAPTCHA),
you'll be offered a chance to install Acxiom's opt out cookie. You can
choose to do this or not, but remember that this is not a persistent
method of protecting your privacy: the opt out cookie will disappear as
soon as you clear your cookies. See instructions below for opting out of
BlueKai for advice on dealing with web tracking.

![](tool_facebook14.png)

5.  You will then receive an email with a link in it from Acxiom. You
can click on this link or else copy and paste it into a new
browser window. Visiting this page will take you to another CAPTCHA.
Fill this out.

Congratulations - you've opted out of Acxiom!

**Datalogix**

1. To opt out of this program, visit the Datalogix.com [privacy
page](https://www.datalogix.com/privacy/). Scroll down to the word
?Choice? and the last sentence in the first paragraph says:

*?If you wish to opt out of all Datalogix-enabled advertising across
channels including direct mail, online, mobile and analytic products,
click here.?*

2\. Click there and a form will pop up that asks for your name, address,
and email address. Fill this out and click submit.

![](tool_facebook15.png)

Datalogix promises that the opt-out will take effect within 30 days.
Once you?ve been opted out, Datalogix will no longer include your
information in the hashed data they provide to Facebook. 

**Epsilon**

As Epsilon explains on their [Consumer Preference
Center](www.epsilon.com/consumer-preference-center) page, there are
several ways to opt out of the Epsilon marketing database: 

**EMAIL:** Email <optout@epsilon.com> and include the following
information:\
? full name (including middle initial)\
? current address\
? previous address if you have been at your current address fewer than
six months

**PHONE:** Phone 1.888.780.3869 and leave the above information.

**MAIL:** Mail the above information to the below addresses:\
**U.S. Consumers:** Epsilon\
?P.O. Box 1478\
?Broomfield, CO 80036\
**Canadian Consumers:** Epsilon?\
41 Metropolitan Rd.?\
Toronto, Ontario\
?M1R 2T5

We note that not all of these methods require you to provide an email
address.  Epsilon may have methods to match your name with your email,
but you can also provide your email address to be sure.

Note that opting out doesn't actually remove the data from Epsilon's
database but rather just marks it as "suppressed" to they will stop
sharing it for marketing purposes. This means that if the information is
ever re-submitted, you won't be added back to the list.

**BlueKai**

Unlike the other data brokers Facebook is working with on this new
project, BlueKai does not directly collect data from your offline
activities. Instead, they use tracking cookies that collect data about
your online browsing habits and then use that information to infer what
types of products you might like to buy.

**The best way to opt out of this is to use a browser add-on to block
third-party tracking.**\
Rather than try to block only BlueKai, we recommend you block all
third-party trackers. You can use a tool such
as [Ghostery](http://www.ghostery.com/) (now available on Firefox,
Safari, Chrome, Opera and Internet Explorer) as noted earlier.

**CONGRATULATIONS** -- you've managed to get out of Facebook's new data
broker-driven targeted marketing, and helped protect yourself from
several important data brokers.  

Regular SMS Text messages
=========================

SMS messages are not well encrypted so you should not rely on them to
transmit sensitive information securely. Sent SMS messages can be
intercepted and kept by your service operator or by third parties with
inexpensive equipment. Those messages will carry the phone numbers of
the sender and recipient as well as the content of the message. What's
more, SMS messages can easily be altered or forged by third parties.

If you do need to use SMS for something, consider establishing a code
system between you and your recipients. Codes may make your
communication more secure and may provide an additional way of
confirming the identity of the person you're communicating with. Code
systems need to be secure and change frequently.

Saved messages on your phone can easily be accessed by anybody who gets
hold of your phone so consider deleting all received and sent messages
straightaway.

*Regular SMS text messages to or from your mobile phone are not secure.*

Traumatic Stress - Causes
=========================

Human rights activists do difficult and challenging work, and see a good
deal of human misery. We may even be fearful for our lives at times. It
is therefore important to know how to react following a traumatic event,
and how to recognise the symptoms of traumatic stress. (Post-traumatic
stress is dealt with in the Expert Lesson.)

Any event which is very distressing and outside of the realm of normal
human experience can result in traumatic stress. Traumatic stress
usually produces a very intense response, including fear and/or
helplessness, which may overwhelm the individual?s coping mechanisms.
Such a response is a **normal reaction to an abnormal situation.**

![](stress3.png)

For many people activists, journalists or aid workers, meetings can be
high-risk encounters. Meetings can expose the identity or work of either
you or the person you meet with, and have often been the scene of
arrests. For this reason, it is vital to put the highest level of
planning and preparation into meetings involving vulnerable human rights
defenders or whistleblowers.

-   Ask some strategic questions before your trip
    -   What is the objective of the trip? (ensure clear Terms
        of Reference)
    -   What profile are you/your org org taking? High profile/ low
        profile? Why?
    -   What is the threshold of acceptable risk your organisation is
        willing to take?
    -   What about the risk to partners who you are meeting with?
    -   What damage could this trip cause potential adversaries? How
        interested will potential adversaries be in this trip?
-   Complete a risk assessment
-   Discuss trip with regional security focal point to confirm whether
    trip falls within threshold of acceptable risk
-   Where possible, organise post-arrival context/ security briefings
    from partners

Satellite phones, which provide high-quality, direct-dial voice, fax,
and e-mail, are often used to supplement a radio network, especially in
moderate- to high-risk areas. Today?s satellite terminals are rugged,
portable, and may be cheaper to operate than cellular phones in some
areas. Modern satellite phone networks encrypt voice traffic to prevent
eavesdropping and so are usually thought of as safer than radios.
However, anyone with cheap computer equipment and radio could eavesdrop
on calls by breaking this encryption quite easily.

PGP FOR MAC O SX TOOL GUIDE
===========================

PGP for Mac O SX Tool Guide\
Encrypted email for Mac
----------------------------

**Lesson to read:\
? [Email](umbrella://lesson/email)**\
**Download Location:**\
 ? [GPG Suite](https://gpgtools.org/) \
? [Mozilla Thunderbird](https://www.mozilla.org/thunderbird/) \
? [Enigmail](https://www.enigmail.net/home/index.php)\
**Computer requirements:** An internet connection, a computer running
Mac OS X, an email account\
**Version used in this guide: **? GPG Suite Beta 4\
? Mozilla Thunderbird 31.2.0\
? Enigmail 1.7.2\
**License:** Free Software; mix of Free Software licenses\
**Level:** Advanced\
**Other reading:** <http://support.gpgtools.org/>\
**Time required:** 30-60 minutes

**Using PGP will give you:**\
? The ability to protect your email communications from being read by
anyone except their intended recipients.\
? The ability to prove that an email came from a particular person,
instead of being a fake message sent by another sender (it is otherwise
very easy for email to be fabricated). Both of these are important
defenses if you're being targeted for surveillance or misinformation.

### 1.0 Before you start

To use Pretty Good Privacy (PGP), you will need to install some extra
software that will work with your current email program. You will also
need to create a private key, which you will keep private. The private
key is what you will use to decrypt emails sent to you, and to digitally
sign emails that you send to show they truly came from you. Finally,
you'll learn how to distribute your public key?a small chunk of
information that others will need to know before they can send you
encrypted mail, and that they can use to verify emails you send.

This guide will show you how to use PGP with an Apple Mac (but not iPad
or iPhone), with either the Mac's built-in Mail program, or with Mozilla
Thunderbird, a popular alternative email program.

You can't currently use PGP directly with a web email service like
Gmail, Hotmail, Yahoo! Mail, or Outlook Live. You can still use your
webmail address; you?ll just have to configure it with the Thunderbird
program on your computer.

**Note that both ends of the email conversation need to be using
PGP-compatible software for it to work.**

People will normally use this only on their own personal devices, not on
shared devices. Fortunately, PGP is available for most desktop computers
and mobile devices, and you can point them to these guides to help them
set up their own version. This guide is for Mac users.

### 2.0 Installing GPGTools on your Mac

PGP is an open standard, which means that more than one piece of
software can use it. The software we're going to use for PGP is called
the GPG Suite, from GPG Tools, because it works on Macs, is free for
anyone to use, and it's open source: the underlying source code is
available for anyone to check for bugs and backdoors.

Once the GPG Suite is installed, you can set up your keys for the first
time, and then enable PGP on Apple Mail and, optionally, Thunderbird.

**Step 1: Install the program.**

First, go to <https://www.gpgtools.org/> in your browser and choose
?Download GPG Suite.

![](tool_pgposx1.png)

You'll end up with a disk image that you can click on to install the
software. If you're not accustomed to installing third-party software on
your computer, ask a nearby Mac expert ? this is a step most techies can
help you with, even if they don't know PGP or encryption.

![](tool_pgposx2.png)

Clicking on install will give you a list of tools that will be added to
your computer.

![](tool_pgposx3.png)

***What exactly am I installing here?***

These are tools will mostly work behind the scenes so that more than one
program on your Mac can use PGP. Think of them as programs that other
programs can use, rather than applications that you will use directly.
GPGMail lets Apple Mail send and read PGP emails, GPG Keychain Access
lets you keep your private and public keys in the same manner as you can
save other passwords on your Mac.

GPGServices optionally adds a feature to OS X to let you use PGP
directly in programs other than email (for instance, in a word
processor). GPGPreferences is for changing PGP settings in Apple's
preferences. Finally, MacGPG2 is the basic tool that any program needs
to use to do encryption or signing.

In October 2014, the GPG Tools team announced that they would soon be
charging for GPGMail, the part of their package that lets you use GPG
with Apple's Mail application. This tutorial is about using GPG with
Thunderbird, so it doesn't use that component. You can just use the
zero-cost part of the GPG Suite, as outlined here, if you like. This
option has the added benefit that all of these tools are "free software"
meaning you are still allowed to freely examine, edit and redistribute
GPG Mail's underlying source code, so they are even more secure. For
more information, see GPG Tools' [own
FAQ](https://gpgtools.org/news.html) on their decision.

Click "Continue" to install GPG Suite.

![](tool_pgposx4.png)

When the installation is complete, open GPG Keychain (found in your
applications folder) if it doesn't automatically open and prompt you to
generate your PGP keys after installation.  Click "New" to generate your
PGP keys.

![](tool_pgposx5.png)

**Step 2: Create your PGP key**

Sometimes when you install new software, your computer will pester you
with questions that have no obvious answer, without actually giving you
any advice on how to reply. This is one of those times.

It's important to spend a little time thinking about the answers you'll
give here, because changing your PGP key details can be difficult later,
and if you?ve chosen to publish your key somewhere, you won?t be able to
unpublish it. (There are still thousands of old public keys from the
1990?s floating around, with the names and old email addresses of the
people who made them back then.)

PGP keys contain a name and an email address that link the key to you.
The email address will be one of the ways others can discover which key
to use when they are encrypting a message to you.

***When should I not put my real name or email address on my PGP key?
When shouldn't I upload my key?***

For most people, it makes sense to add a real email address to your key,
and upload it to the public keyservers ? it's how people will match the
right key to you. They can send you an email directly, and know it will
be encrypted with the right key, and when they receive a signed email
from you, the digital signature will be marked with your name.

For some people, though, it will not make sense to add your real name to
your key, for instance if your threat model means that having your
identity publicly attached to your key (and the linked email address) is
not a good idea. Edward Snowden communicated with journalists using PGP
and an anonymous email address before he revealed his identity; his PGP
key certainly wasn't marked with his name.

**Uploading your key is normal practice, but it can reveal that you're
using encryption, even if you don't use your own name. Also, as we'll
see, others might upload your key and associate their own key with it,
implying that you and they have a connection. That can be harmful if you
are communicating and don't want people to know it. It can also be
troublesome if you're not communicating, but your attacker wants people
to think that you are associated.**

Here's a rough guideline: if you're thinking about using a pseudonym
generally, use that pseudonym (and alternative email) when labeling your
key. If you are in a more dangerous environment, when you don't want
people to know you're using PGP at all, or know who you are
communicating with, don't upload your key to the public keyservers ? and
make sure the small group of people you're communicating with know not
to upload your key either. There are other ways of verifying keys that
don't rely on them being available on the public key server ? see EFF?s
guide to [Key
Verification](https://ssd.eff.org/en/module/key-verification#overlay=en/node/37/)
for more information.

Click the "Upload public key after generation" box if you'd like to let
others find your key quickly so that they can send you encrypted
messages. It's like adding your phone number to a public phone
directory: you don't need it, but it's convenient for others.

Before generating the key, expand "Advanced options." You can leave the
comment blank, and leave the key type "RSA and RSA (default)." But make
sure to change the Length field to 4096.

![](tool_pgposx6.png)

**Your key will expire at a certain time; when that happens, other
people will stop using it entirely for new emails to you, though you
might not get any warning or explanation about why. So, you may want to
mark your calendar and pay attention to this issue a month or so before
the expiration date.**

It's possible to extend the lifetime of an existing key by giving it a
new, later expiration date, or it's possible to replace it with a new
key by creating a fresh one from scratch. Both processes might require
contacting people who email you and making sure that they get the
updated key; current software isn't very good at automating this. So
make a reminder for yourself; if you don't think you'll be able to
manage it, you can consider setting the key so that it never expires,
though in that case other people might try to use it when contacting you
far in the future even if you no longer have the private key or no
longer use PGP.

When you're ready, click the "Generate key" button.

You computer will start generating both your public and private key. It
shouldn't take any more than a couple of minutes to finish (it takes a
while because to create your keys, your computer needs to gather random
numbers. Think of it as your computer throwing a pair of dice many,
many, many times.)

![](tool_pgposx7.png)

When you're done generating your key, you'll see it key listed in GPG
Keychain Access. You can double-click on your key to see information
about it, including its "fingerprint ??a unique way to identify your PGP
key.

Now is a good time to generate a revocation certificate. (A revocation
certificate is a file that you can generate that announces that you no
longer trust that key. You generate it when you still have the secret
key, and keep it for any future disaster.) In the future, if you ever
worry that your private key has been copied by someone, you accidentally
delete or lose your private key, or you forget your passphrase, you can
tell everyone it has been revoked, or cancelled, by using a revocation
certificate.

It's better to create one now, because you need the private key and
passphrase to create a revocation certificate. If you leave it until
later, you might lose one or the other, and then it will be too late. So
create a certificate by clicking on your key, choosing the ?Key? menu
entry, and then ?Create Revocation Certificate.? You'll be prompted for
somewhere to save the file. You might want to keep it with a backup copy
of the key (see next step).

**Step 3: Back up your PGP key**

If you lose access to your private key, you won't be able to decrypt any
incoming PGP mail, or your old mail. On the other hand, you want to keep
your private key as securely as you can.

You might want to save a backup copy to a USB key, which you keep safely
hidden. You will only need it if you lose your original key, but for
safety you will want to keep it out of the hands of your potential
attackers.

***Is everything lost if my attackers get hold of my PGP private key?***

What if you get your Mac stolen, or your backup key is taken from you?
Does that mean your PGP messages are vulnerable? No: if you've chosen a
good passphrase and nobody has been able to learn what it is, you should
still be mostly protected. To be safe, you may want to revoke your old
key, and create a new PGP key. This won?t stop your old key from being
able to decrypt your old email, but it will discourage other people from
using the old key for their new emails to you.

To backup your key, open GPG Keychain Access. Select your key, and click
?Export? in the toolbar. Put your USB drive into the machine, and choose
it in the ?Where? part of the ?Save As...? dialog. Check the ?Allow
secret key export? checkbox.

**OPTION A) Configuring Apple Mail**

When you first open Apple Mail, you'll see a first run wizard that helps
you set up your email address. Fill out your name, email address, and
your email password and click "Create."

![](tool_pgposx8.png)

**Mail account setup wizard**

If you use popular free email services like Gmail, Mail should be able
to automatically detect your email settings when you click Continue. If
it doesn't, you may need to manually configure your IMAP and SMTP
settings. Talk to the company you use for email, or ask someone
technical who is familiar with your email provider (so, an IT person at
work, or a technical friend who uses the same ISP as you. They don't
need to know about PGP, but you can ask them ?Can you set up Apple Mail
for me??).

![](tool_pgposx9.png)

Mail account setup auto-detect

When you're composing a new message, there are two icons just beneath
the Subject field. There's a padlock (encrypt email) and a star
(digitally sign email). If the padlock is closed it means this email
will be encrypted, and if the star has a check in it, it means this
email will be digitally signed.

**Sending PGP Signed or Encrypted Email**

![](tool_pgposx10.png)

You can always sign your email, even if the recipient doesn?t use PGP.
Because digitally signing emails requires your secret key, Mail will pop
up a window asking for your passphrase when you first sign an email.

You can only encrypt emails if the person you?re emailing uses PGP and
you have that person?s public key. If the encryption padlock icon is
unlocked and greyed out so you can't click on it, this means you first
need to import the recipient's public key. Either ask them to send it to
you, or use the GPG Keychain Access app to find the key to from a public
keyserver.

To be absolutely safe, you'll need to verify the keys you get from the
keyserver or your colleague. See EFF?s guide to [Key
Verification](https://ssd.eff.org/en/module/key-verification#overlay=en/node/37/)
for more information.

**OPTION B) Using PGP with Mozilla Thunderbird**

This walkthrough shows how to use GPG with the free, open source,
Thunderbird mail client from Mozilla, together with the Enigmail plugin
for email encryption.

First, download Thunderbird from <https://www.mozilla.org/thunderbird>,
mount the disk image as you did with GPG Tools, and drag the Thunderbird
into Applications. When you open it for the first time it will ask if
you want to set it as your default email client. Go ahead and click "Set
as Default.?

![](tool_pxposx11.png)

Then you will see the first run wizard. To set up your existing email
address, click "Skip this and use my existing email." Then enter your
name, email address, and the password to your email account.

![](tool_pgposx12.png)

If you use popular free email services like Gmail, Thunderbird should be
able to automatically detect your email settings when you click
Continue. If it doesn't, you may need to manually configure your IMAP
and SMTP settings?ask your ISP, or a technical friend who knows about
setting up email, to help. Sometimes, Thunderbird can just guess the
correct settings.

**If you use two-factor authentication with Google (and depending on
your threat model you probably should!) you cannot use your standard
Gmail password with Thunderbird. Instead, you will need to create a new
application-specific password for Thunderbird to access your Gmail
account. See [Google's own
guide](https://support.google.com/mail/answer/1173270?hl=en) for doing
this. **

![](tool_pgposx13.png)

After you're done configuring Thunderbird to check your email, click
"Done." Then click on "Inbox" in the top left to load your emails.

Now that you've installed and configured Thunderbird to work with your
email, you need to
install [Enigmail](https://www.enigmail.net/home/index.php), the GPG
add-on for Thunderbird. In Thunderbird, click the menu icon in the
top-right, and choose Add-ons.

![](tool_pgposx14.png)

Search for "enigmail" in the search box in the top right.

![](tooL_pgposx15.png)

Click the Install button next to the Enigmail extension to download and
install Enigmail. When it's done, click "Restart Now" to restart
Thunderbird.

The first time you run Thunderbird with Enigmail enabled it opens the
OpenPGP Setup Wizard. Click "Cancel." We will manually configure
Enigmail instead.

Click the menu button, hover over Preferences, and choose Account
Settings.

![](tool_pgposx16.png)

Go to the OpenPGP Security tab. Make sure "Enable OpenPGP support
(Enigmail) for this identity" is checked. "Use specific OpenPGP key ID"
should be selected, and if your key isn't already selected you can click
"Select Key" to select it.

You should also check "Sign non-encrypted message by default," "Sign
encrypted messages by default," and "Use PGP/MIME by default," but not
(for most people) "Encrypt messages by default."

If most of the people that you email use PGP (or you would like to
encourage them to do so), you may wish to encrypt by default. It would
be ideal to encrypt all the emails you send, but that is not always
possible. Remember that you can only send encrypted email to other
people who use PGP, and you need to have their public keys in your
keychain. For most people, manually choosing to encrypt each email you
send will probably work best.

![](tool_pgposx17.png)

Then click "OK" to save all of the settings.

Congratulations, you now have Thunderbird and Enigmail set up! Here are
a couple of quick pointers:

? You can click the menu button, hover over OpenPGP, and open Key
Management to see the PGP key manager that's build-in to Enigmail. It's
very similar to GPG Keychain Access, and it's your choice which you
use.\
? When you're composing a new message, there are two icons in the bottom
right corner of the window: a pen (digitally sign email) and a key
(encrypt email). If the icons are gold it means they are selected, and
if they're silver it means they're not selected. Click on them to toggle
signing and encrypting the email you're writing.

![](tool_pgposx18.png)

COBIAN BACKUP TOOL GUIDE
========================

Cobian Backup\
Backing up your computer files
------------------------------

**Lesson to read: [Backing Up](umbrella://lesson/backing-up)**\
**Download Location:** <http://www.cobiansoft.com/cobianbackup.htm>\
**Computer requirements:** \
? XP, 2003, Vista, 2008, Windows 7\
? Windows 95, 98 and ME are compatible with Cobian version 7.\
**Version used in this guide:** Cobian 10\
**License:** Freeware\
**Level:**  Intermediate\
**Time required:** 30 minutes

### 1. Things you should know about this tool before you start

Cobian Backup is used to archive, (or to make a backup copy) of your
files and directories. Backups can be stored in other directories or
drives on your computer, other computers on the office network, or on
removable devices (CDs, DVDs and USB memory sticks). Cobian Backup lets
you archive your directories and files on a regular basis. It works
silently in the background on your system (that is, in the system tray),
checking your schedule and executing the backup process when
necessary. Cobian Backup can also compress and encrypt files as it
generates the backup file.

? Using Cobian will give you:\
? The ability to back up all documents, files and folders\
? The ability to compress and decompress your backup files\
? The ability to encrypt and decrypt your archived files

**Installing Cobian ? in brief**\
? Open www.cobiansoft.com/cobianbackup.htm\
? Click on the link "Download Cobian Backup" on the page.\
? Save the installer, then find it and doubleclick it\
? Read the 'Installation Note' below before you continue\
? After you have successfully installed Cobian you may delete the
installation program from your computer.

### 2.0 How to Install Cobian Backup

**Installation Note:** Before you begin the installation process, verify
that you have both the latest versions of the **Microsoft Windows
Installer** and the **Microsoft.NET Framework**.

Installing Cobian Backup is a relatively easy and quick procedure.

**Step 1.** Double click ?cbsetup.exe?; the *Open File - Security
Warning* dialog box may appear. If it does, click ?Run? to activate the
light blue *Extracting the resource* progress status bar, followed a few
moments later by the following screen:

![](tool_cobian1.png)

**Step 2.** Click ?Next? to activate the *Please read and accept the
license agreement screen* check the *I accept* option, and then click
?Next? again to activate the following screen:

![](tool_cobian2.png)

**Step 3.** Click ?Next? to activate the following screen:

![](tool_cobian3.png)

**Step 4.** Check the *Use Local System account* option in the *Service
options* pane, so that your own resembles Figure 3 above. This option
ensures that Cobian Backup will be running silently in the background
all the time, so that your backups will occur as scheduled.

**Step 5.** Click ?Next? to activate the following message prompt:

![](tool_cobian4.png)

**Step 6.** Click ?Yes? to activate the next installation screen, and
then click ?Next? to continue with the installation process.

**Step 7.** Click ?Done? to complete the installation process. After the
installation process has been completed, the Cobian Backup icon will
appear in the **Windows System Tray**.

### 2.1 How to Backup Your Directories and Files

In this section you will learn how to perform a simple backup or archive
of a specified files and/or folders. Cobian Backup uses a *backup
task* which can be configured to include a specified group of files
and/or folders. A backup task can be set to run on a specified day and
time.

To create a new backup task, perform the following step:

**Step 1.** Click ?Schedule? to create a new backup task, and activate
the *New task* window as follows:

![](tool_cobian5.png)

The left sidebar lists a number of tabs and their associated screens -
used to set different backup options and parameters - are displayed in
the pane at right. All the options in the *General* tab are described
below:

### 2.1.1 Option Descriptions

*Task Name:* This *Task Name* text field lets you enter a name for the
backup task. Use a name that identifies the nature of the backup. For
example, if the backup is going to contain video files, you could name
it *Video Backup*.

*Disabled:* This option *must* be left unchecked.\
Warning: Enabling the *Disabled* option will override the rest of the
options, and prevent the backup task from running.

*Include Subdirectories:* This option lets you include all the
subdirectories/folders within a selected directory/folder for the backup
task. This is an efficient method for backing up a large number of
folders and/or files. As an example, if you select the *My
Documents* folder and check this option, then all files and folders
in *My Documents* will be included in the backup task.

*Create separated backups using timestamps:* This option lets you
specify that the date and time of the backup task will be automatically
included in the folder name containing your backup file. This is a good
idea because it means that you will easily be able to identify when the
backup was performed.\
*Use file attribute logic:* This option is only relevant when you choose
to perform an incremental or differential backup (see below). File
attributes contain information about the file.

**Note:** The following option is only available for Windows OS versions
more recent than *and* including Windows XP.

*Use Volume Shadow Copy:* This option lets you backup files which are
locked.\
Cobian Backup verifies this information to determine whether there has
been a change in the source file from the last time a backup was
performed. If you then run an *Differential* or *Incremental* backup,
the file will be updated.

**Note:** You will only be able to run a full or 'dummy backup' if
you *disable this option* (the dummy backup option is explained below).

### 2.1.2 Backup type Descriptions

*Full:* This option means that every single file in the source location
will be copied to your backup directory. If you have enabled the *Create
separated backups using timestamp* option, you will have several copies
of the same source (identified by the time and date of the backup in the
folder title). Otherwise, Cobian Backup will overwrite the previous
version (if any).

*Incremental:* This option means the program will verify if the files
selected for backup have been changed since the last backup was
performed. If there has been no change, it will be skipped over during
the backup process, saving backup time. The *Use file attribute
logic* option needs to be checked in order to perform this backup.

*Differential:* The program will check if the source has been changed
from the last **full** backup. If there is no need to copy that file, it
will be skipped, saving backup time. If you have run a full backup
before on the same set of files, then you can continue backing it up,
using the Differential method.

*Dummy task:* You can use this option to get your computer to run or
shut down programs at certain times. This is a more advanced option
which is not really relevant to our basic backup procedure.

**Step 2.** Click ?OK? to confirm your search options and parameters for
your backup task.

### 2.2 How to Create a Backup File

To begin creating a backup file, perform the following steps:

**Step 1.** Click ?Files? in the left sidebar of the *New task* window
to display a *blank* version of the following screen:

![](tool_cobian6.png)

**Step 2.** Select the files you want to back up. (In *Figure 3* above,
the *My Documents* folder is selected.)

**Step 3.** Click ?Add? in the *Source* pane to activate the *Directory*
menu.

**Step 4.** Select *Directory* if you want to back up an entire
directory, and *Files* to back up individual files. To specify
individual files or directories to be backed up, select *Manually*, and
type in the file path or directory for your backup.

**Note:** You can add as many files or directories as you like. If you
wish to back up files currently on your FTP server, choose the FTP
site option (you will need to have the appropriate server login
details).

When you have selected the files and/or folders, they will appear in
the *Source* area. As you can see in *Figure 3* above, the *My
Documents* folder is displayed there, meaning this folder will now be
included in the backup task.

The *Destination* pane specifies where the backup will be stored.

**Step 5.** Click ?Add? in the *Destination* pane to activate the
Directory menu.

**Step 6.** Select *Directory* to open a browser window where you select
the destination folder for your backup file.

**Note:** If you want to create several versions of the backup file, you
may specify several folders here. If you selected the *Manually* option,
you must type in the full path to the folder where you want to keep the
backup. To use a remote Internet server to store your
archive, select the FTP site option (you will need to have the
appropriate server login details).

The screen should now resemble the example above example with file(s)
and/or folder(s) in the source area and folder(s) in the destination
area. However, don't click *OK* just yet! You still need to set a
schedule for your backup.

### 2.3 How to Schedule Your Backup Task

For your automatic backup to work, you need to fill in
the *Schedule* section. This section lets you specify when you want the
backup to be performed.\
To set the schedule options, perform the following steps:

**Step 1.** Select ?Schedule? from the left sidebar, to activate the
following pane:

![](tool_cobian7.png)

The *Schedule type* options are listed in the drop-down menu, and
described below:

*Once:* The backup will be done once only at the date and time specified
in the *Date/Time* area.

*Daily:* The backup will be done every day at the time specified in
the *Date/Time* area.

*Weekly:* The backup will be done on the days of the week selected. In
the example above, the backup will be done on Fridays. You may select
other days also. The backup will be done on all days selected at the
time specified in the *Date/Time* area.

*Monthly:* The backup will be done on the days typed into the days of
the month box at the time specified in the *Date/Time* area.

*Yearly:* The backup will be done on the days typed into the days of the
month box, during the month specified, and at the time specified in
the *Date/Time* area.

*Timer:* The backup will be done repeatedly at intervals specified in
the Timer text box in the *Date/Time* area.

*Manually:* You will have to run the backup yourself from the main
program window.

**Step 2.** Click ?OK? to confirm the options and settings for the
backup schedule as follows:

![](tool_cobian8.png)

Once you have decided on a backup schedule, you have completed the final
step. The backup will now run on the folders specified according to the
schedule you have chosen.

### 3.0 How to Compress Your Backup File

**Step 1.** Create a backup task as documented in section 2.3,
containing the backup files you want to archive.

**Step 2.** Select ?Archive? from the left sidebar to activate the *New
task* screen as follows:

![](tool_cobian9.png)

The **Compression** pane is used to specify the method for compressing
your backup.

**Note:** Compression is used to reduce the amount of space for file
storage. If you have a bunch of old files that you use only
occasionally, but you still want to keep, it would make sense to store
them in a format where they take up as little space as possible.
Compression works by removing a lot of unnecessary coding out of your
documents, while leaving important information intact. Compression does
not damage your original data. The files are not viewable when
compressed. The process must be reversed and your files 'decompressed'
when you want to view the files again.

The three sub-options in the *Compression type* drop-down list are:

*No Compression:* This option does not perform any compression, as you
would expect.

*Zip Compression:* This option is the standard compression technique
for **Windows** systems, and the most convenient. Archives once created
can be opened with standard Windows tools (or you can download
the [ZipGenius](http://www.zipgenius.it/) program to access them).

Selecting a compression type listed automatically enables the *Split
options* section, and its corresponding drop-down list.

The *Split options* apply to storage on removable media, for example
CDs, DVDs, floppy disks and USB memory sticks. The various split options
will subdivide the archive into sizes that will fit onto your storage
device of choice.

Example: Let's say that you are archiving a large number of files, and
you want to burn them to a CD. However, your archive size turns out to
be larger than 700MB (the size of a CD). The splitting function will
split the archive into pieces smaller than or equal to 700MB, which you
can then burn onto your CDs. If you are planning to back up onto your
computer's hard disk, or the files that you want to back up are smaller
than the device you plan to store them on, you can skip this section.

The following options are available to you when you click on the *Split
options* drop-down list. Your choice will depend on the type of
removable storage device available to you.

![](tool_cobian10.png)

? 3,5" - Floppy disk. This option is big enough to perform backup of a
small number of documents\
? Zip - Zip Disk (check the capacity of the one you are using). You will
need a special Zip Drive in your computer and the custom-made disks\
? CD-R - CD disk (check the capacity of the one you are using). You will
need a CD Writer in your computer and a CD writing program
(see [DeepBurner Free](http://www.deepburner.com/) version or
other [disk burning
tools](http://www.thefreecountry.com/utilities/dvdcdburning.shtml)).\
? DVD - DVD disk (check the capacity of the one you are using). You will
need a DVD Writer in your computer and a DVD writing program
(see [DeepBurner Free](http://www.deepburner.com/) version or
other [disk burning
tools](http://www.thefreecountry.com/utilities/dvdcdburning.shtml)).

If you are backing up onto several USB memory sticks you may want to set
a custom size.

To do this, perform the following steps:

**Step 1. Select** the *Custom size* (bytes) option, then type the size
of the archive in bytes into the text field.

To give you an idea of sizes\
? 1KB (kilobyte) = 1024 bytes - a one-page text document made in Open
Office is approximately 20kb\
? 1MB (megabyte) = 1024 KB - a photo taken on a digital camera is
usually between 1 - 3 MB\
? 1GB (gigabyte) = 1024 MB - approximately half hour of a DVD quality
movie

**Note:** When choosing a custom size to split your backup for a CD or
DVD disk, Cobian Backup will not copy the backup to your removable
device automatically. Rather, it will create your archive in those files
on the computer and you will need to burn them to the CD or DVD disk
yourself.

*Password Protect:* This option lets you enter a password to protect the
archive. Simply type, then re-type a password into the two boxes
provided. When you try to decompress the archive, you will be asked for
the password before the task commences.

**Note:** If you want to secure your archive, you should think about
using another method than a password. Cobian Backup lets you encrypt
your archive. This is covered below.

*Comment:* This option lets you write something descriptive about the
archive, but it is not a requirement.

### 3.1 How to Decompress Your Backup File

To decompress your backup, perform the following steps:

**Step 1. Select &gt; Tools &gt; Decompressor.**

The Decompressor window appears as follows:

![](tool_cobian11.png)

**Step 2.** Click on the open file icon to open a browse window to
enable you to select the archive you want to decompress.

**Step 3.** Select the archive (*.zip* or *.7x* file) and
then click ?OK?.

**Step 4.** Select a directory into which you will unpack (output) the
archived file.

**Step 5.** Click on the compression icon to open another window that
lets you choose the folder in which to unpack the archive.

**Step 6.** Select a folder, and then click ?OK?.

Use Windows Explorer to view the files that go to that folder.

### 4.0 About Encryption

Encryption may be a necessity for those wishing to keep their backup
secure from unauthorised access. Encryption is the process of encoding,
or scrambling, data in such a way that it appears unintelligible to
anyone who does not have the specific key needed to decode the message.
For more information on encryption, read the [Protecting Files
lesson](umbrella://lesson/protecting-files).

### 4.1 How to Encrypt Your Backup File

The *Strong encryption* pane is used to specify the encryption method to
be used.

**Step 1.** Click the *Encryption* type drop-down box to activate its
list of different encryption methods.

To keep things simple, we recommend that you choose from either
the *Blowfish* or the *Rijndael* (128 bits) methods. These will provide
excellent security for your archive, and let you access the encrypted
data with a chosen password.

**Step 2.** Select the *Encryption* type you want to use.

**Note:** *Rijndael* and *Blowfish* both offer approximately the same
level of security. *DES* is weaker but the encryption process is faster.

**Step 3.** Type and re-type the password into the two boxes provided.

The strength of the password is indicated by the bar marked 'Passphrase
quality'. The further the bar moves to the right, the stronger the
passphrase. Refer to the **[Passwords
lesson](umbrella://lesson/passwords)** for information on creating and
storing strong passwords.

**Step 4.** Click ?OK?.

### 4.2 How to Decrypt Your Backup File

Decrypting your backup file is easy and quick. To decrypt your backup
file, perform the following steps:

**Step 1. Select &gt; Tools &gt; Decrypter and Keys:**

*This will activate the Decrypter and Keys window as follows:*

![](tool_cobian12.png)

**Step 2.** Click ?Select? to select the archive you want to decrypt.

**Step 3.** Click ?Destination? to select the folder in which to store
the decrypted archive.

**Step 4.** Select the same encryption type you selected earlier, in
section 4.1 How to Encrypt Your Backup File, in the *Methods* drop-down
list.

**Step 4. Select** the appropriate encryption method (the one you used
to encrypt your backup file).

**Step 5.** Type your passphrase into the *Passphrase* text fields.

**Step 6.** Click ?Decrypt!?

The file(s) will be decrypted to the location that you specified. If the
files were also compressed, you will need to decompress them as outlined
in section 3.1 How to Decompress Your Backup.

How to protect sensitive files
==============================

Many human rights activists have sensitive information that could have
serious consequences if seen by the wrong people. The [Managing
Information lesson](umbrella://lesson/managing-information) can help you
determine your threat model. Following the steps laid out in the
Home/Office section and the [Malware](umbrella://lesson/malware) lesson
will help you to protect your computer physically and digitally. However
there may be situations where these precautions fail or you need to show
your computer to someone whom you don?t want to see the files. This is
why you should also protect the files themselves. You can do this by
encrypting them so that only you can read them.

![](protecting1.png)

Encryption is a way to enhance the security of a message or file by
scrambling the contents so that it can only be read by someone who has
the right encryption key to unscramble it.Many activists use TrueCrypt,
but serious vulnerabilities have recently been found in it.
[VeraCrypt](https://veracrypt.codeplex.com/wikipage?title=Downloads) is
a good, free, open-source, alternative that we recommend instead. Much
like a safe, VeraCrypt creates an encrypted container on your computer
or hard drive, that you can put as many files as you like into.

We will shortly be creating a tool guide for VeraCrypt. For now, users
can get a step-by-step guide of how to use and install it
[here](https://veracrypt.codeplex.com/wikipage?title=Beginner%27s%20Tutorial).

ADIUM TOOL GUIDE
================

Adium & OTR\
Secure instant messaging for Mac
--------------------------------

**Lesson to read: [Sending a
Message](umbrella://lesson/sending-a-message)**\
**Download Location:** <https://adium.im/>\
**Computer requirements** (Adium 1.5 or later): Mac OS X 10.6.8 or
newer, an Apple-branded Macintosh computer.\
**Version used in this guide:** Adium 1.5.9\
**License:** GNU GPL\
**Other
reading:** <https://pressfreedomfoundation.org/encryption-works>;<https://adium.im/help/>\
**Level:** Beginner-Intermediate\
**Time required:** 15-20 minutes

Adium is a free and open source instant messaging client for OS X that
allows you to chat with individuals across multiple chat protocols,
including Google Hangouts, Yahoo! Messenger, Facebook chat, Windows Live
Messenger, AIM, ICQ, and XMPP.

OTR (Off-the-record) is a protocol that allows people to have
confidential conversations using the messaging tools they?re already
familiar with. This should not be confused with Google's ?Off the
record,? which merely disables chat logging, and does not have
encryption or verification capabilities. For Mac users, OTR comes
built-in with the Adium client.

OTR employs end-to-end encryption. This means that you can use it to
have conversations over services like Google Hangouts or Facebook
without those companies ever having access to the contents of the
conversations. This is different from the way in which Google and AOL
use the term ?off the record? to mean that a conversation is not being
logged; that option does not encrypt your conversation.

### Why should I use Adium + OTR?

When you have a chat conversation using Google Hangouts or Facebook chat
on the Google or Facebook websites, that chat is encrypted using HTTPS ,
which means the content of your chat is protected from hackers and other
third parties while it?s in transit. It is not, however, protected from
Google or Facebook, which have the keys to your conversations and can
hand them over to authorities.

After you have installed Adium, you can sign in to it using multiple
accounts at the same time. For example, you could use Google Hangouts,
Facebook, and XMPP simultaneously. Adium also allows you to chat using
these tools without OTR. Since OTR only works if both people are using
it, this means that even if the other person does not have it installed,
you can still chat with them using Adium.

Adium also allows you to do out-of-band verification to make sure that
you?re talking to the person you think you?re talking to and you are not
being subject to a MITM attack. For every conversation, there is an
option that will show you the key fingerprints it has for you and the
person with whom you are chatting. A "key fingerprint" is a string of
characters like "342e 2309 bd20 0912 ff10 6c63 2192 1928,? that?s used
to verify a longer public key. Exchange your fingerprints through
another communications channel, such as Twitter DM or email, to make
sure that no one is interfering with your conversation.

### Limitations: When should I not use Adium + OTR?

Technologists have a term to describe when a program or technology might
be vulnerable to external attack: they say it has a large ?attack
surface.? Adium has a large attack surface. It is a complex program,
which has not been written with security as a top priority. It almost
certainly has bugs, some of which might be used by governments or even
big companies to break into computers that are using it. Using Adium to
encrypt your conversations is a great defense against the kind of
untargeted dragnet surveillance that is used to spy on everyone's
Internet conversations, but if you think you will be personally targeted
by a well-resourced attacker (like a nation-state), you should consider
stronger precautions, such as PGP -encrypted email.

### Installing Adium + OTR On Your Mac

Step 1: Install the program

First, go to <https://adium.im/> in your browser. Choose ?Download Adium
1.5.9.? The file will download as a .dmg, or disk image, and will
probably be saved to your ?downloads? folder.

Double-click on the file; that will open up a window that looks like
this:

![](tool_adium1.png)

Move the Adium icon into the ?Applications? folder to install the
program. Once the program is installed, look for it in your Applications
folder and double-click to open it.

Step 2: Set up your account(s)

First, you will need to decide what chat tools or protocols you want to
use with Adium. The setup process is similar, but not identical, for
each type of tool. You will need to know your account name for each tool
or protocol, as well as your password for each account.

To set up an account, go to the Adium menu at the top of your screen and
click ?Adium? and then ?Preferences.? This will open a window with
another menu at the top. Select ?Accounts,? then click the ?+? sign at
the bottom of the window. You will see a menu that looks like this:

![](tool_adium2.png)

Select the program that you wish to sign in to. From here, you will be
prompted either to enter your username and password, or to use Adium?s
authorization tool to sign in to your account. Follow Adium?s
instructions carefully.

### How to Initiate an OTR Chat

Once you have signed in to one or more of your accounts, you can start
using OTR.

**Remember: In order to have a conversation using OTR, both people need
to be using a chat program that supports OTR.**

Step 1: Initiate an OTR chat

First, identify someone who is using OTR, and initiate a conversation
with them in Adium by double-clicking on their name. Once you have
opened the chat window, you will see a small, open lock in the upper
left-hand corner of the chat window. Click on the lock and select
?Initiate Encrypted OTR Chat.?

Step 2: Verify your connection

Once you have initiated the chat and the other person has accepted the
invitation, you will see the lock icon close; this is how you know that
your chat is now encrypted (congratulations!) ? But wait, there?s still
another step!

At this time, you have initiated an unverified, encrypted chat. This
means that while your communications are encrypted, you have not yet
determined and verified the identity of the person you are chatting
with. Unless you are in the same room and can see each other?s screens,
it is important that you verify each other?s identities. (For more
information, read the EFF module on [Key
Verification](https://ssd.eff.org/en/module/key-verification#overlay=en/node/37/).)

To verify another user?s identity using Adium, click again on the lock,
and select ?Verify.? You will be shown a window that displays both your
key and the key of the other user. Some versions of Adium only support
manual fingerprint verification. This means that, using some method, you
and the person with whom you?re chatting will need to check to make sure
that the keys that you are being shown by Adium match precisely.

The easiest way to do this is to read them aloud to one another in
person, but that?s not always possible. There are different ways to
accomplish this with varying degrees of trustworthiness. For example,
you can read your keys aloud to one another on the phone if you
recognize each other?s voices or send them using another verified method
of communication such as PGP. Some people publicise their key on their
website, Twitter account, or business card.

**The most important thing is that you verify that every single letter
and digit matches perfectly.**

Now that you have initiated an encrypted chat and verified your chat
partner?s identity, there?s one more thing you need to do.
Unfortunately, Adium logs your OTR-encrypted chats by default, saving
them to your hard drive. This means that, despite the fact that they?re
encrypted, they are being saved in plain text on your hard drive.

To disable logging, click ?Adium? in the menu at the top of your screen,
then ?Preferences.? In the new window, select ?General? and then disable
?Log messages? and ?Log OTR-secured chats.? Your settings should now
look like this:

![](tool_adium3.png)

Also, when Adium displays notifications of new messages, the contents of
those messages may be logged by the OS X Notification Center. This means
that while Adium leaves no trace of your communications on your own
computer or your correspondent's, either your or their computer's
version of OS X may preserve a record. To prevent this, you may want to
disable notifications.

To do this, select "Events" in the Preferences window, and look for any
entries that say "Display a notification." For each entry, expand it by
clicking the gray triangle, and then click the newly-exposed line that
say "Display a notification," then click the minus icon ("-") at the
lower left to remove that line." If you are worried about records left
on your computer, you should also turn on full-disk encryption, which
will help protect this data from being obtained by a third party without
your password.

![](tool_adium4.png)

OBSCURACAM TOOL GUIDE
=====================

ObscuraCam Tool Guide
---------------------

**Lesson to read:**\
? [Mobile Phones](umbrella://lesson/mobile-phones)\
? [Social Media](umbrella://lesson/social-media)\
**Download Location:** [ObscuraCam
homepage](https://guardianproject.info/apps/obscuracam/)\
**Phone requirements:** Android 2.3.3 and up\
**Version used in this guide:** 2.0-RC2b\
**License:** Free and Open Source Software (GPL v3)\
**Level:** Basic\
**Time required:** 5 minutes

**Using ObscuraCam will give you:**\
? The ability to obscure identities by hiding faces in photos taken with
your Android device\
? An easy way to share or save these "obscured" photos

### 1.1 Things you should know about this tool before you start

? ObscuraCam's automatic face-recognition does not *always* work, but
you can easily select and obscure faces manually.\
? On some versions of the Android operating system, the option to delete
the original media file does not work. If you rely on this option,
please check to make sure that you do not have ObscuraCam photos (with
visible faces!) somewhere on your device.\
? If you use ObscuraCam to send photos to yourself or to someone else,
the tool does not provide additional protection (such as end-to-end
encryption) for the photo in transit.\
? A tag is an area in the photo which has been obscured by one of
several methods ObscuraCam can use.

### 2.0 How to Install ObscuraCam

**Step 1.** On your Android device, download and install the app from
the [Google Play store
here](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms) by
tapping ?Install?.

![](tool_obscura1.png)

**Step 2:** Before the installation process begins, you will be prompted
to review the access that the application will have on your phone.
Review this carefully. Once you are happy with the permissions that will
be granted, press ?Accept? and the installation will complete. If you do
not agree with the permissions that will be granted, press the back
button and the installation will be cancelled.

**Step 3. Tap** Open to run the app for the first time

**Step 4:** Review the Terms of use and if you are happy with them
press ?Accept? to be brought to the main screen of ObscuraCam.

### 2.1 Using ObscuraCam to obscure photos

You can use ObscuraCam to hide some or all of the faces that appear in
your photos. It works on pictures that you take with the ObscuraCam app
itself, but you can also blur faces in other photos, as long as you have
a way to copy or move the image files onto your Android device.

### 2.1 Taking And Obscuring New Photos

To take a photo on your Android device without showing your subjects'
faces, perform the following steps:

**Step 1:** From the main screen of ObscuraCam tap ?New Picture?.

![](tool_obscura2.png)

**Step 2:** Your phone's camera app will open, take a photo as you
normally would.

**Step 3:** A screen with a preview of the photo you took will be
displayed. Tap the tick to proceed with obscuring the photo,
otherwise tap the x to discard the current photo and take another.

**Step 4:** ObscuraCam\*\* will attempt to identify faces automatically.

**Step 5:** If ObscuraCam can detect faces in the photo it will add an
image "tag" (a rectangle used to select content that should be hidden)
over the face and pixelate it. If ObscuraCam did not detect any faces or
you need to obscure additional areas on the photo, tap on the area to
add additional tags.

![](tool_obscura3.png)

**Step 6:** To see a preview of the photo you can tap the eye icon, to
return to the edit screen tap anywhere on the preview image.

**Step 7:** To share the obscured photo via an existing application on
your phone such as K-9 Mail or TextSecure tap the icon made up of a dot
with arrows.

**Step 8:** To save the blurred photo to your phone tap the save icon.
You will be asked whether you want to delete the original, unblurred,
image from your phone, if you no longer need the original photo
tap ?Yes? otherwise tap ?No? to save a copy of both the obscured and
unobscured photo.

### 2.1.2 Obscuring Existing Photos

As well as obscuring photos as you take them, ObscuraCam can also
obscure any old photos on your phone or that you copy to your phone.

**Step 1:** From the main screen of ObscuraCam tap ?Obscure Photo?.

**Step 2:** Browse to the file on your phone that you want to obscure.

**Step 3:** ObscuraCam will attempt to detect any faces in the image and
pixelate them.

**Step 4:** If ObscuraCam did not detect any faces or you want to
obscure additional faces or items in the photo tap the relevant area to
add additional pixelation.

**Step 5:** To see a preview of the photo you can tap the eye icon, to
return to the edit screen tap anywhere on the preview image.

**Step 6:** To share the obscured photo via an existing application on
your phone such as K-9 Mail or TextSecure tap the icon made up of a dot
with arrows.

**Step 7:** To save the blurred photo to your phone tap the save icon.
You will be asked whether you want to delete the original, unblurred,
image from your phone, if you no longer need the original photo
tap ?Yes? otherwise tap ?No? to save a copy of both the obscured and
unobscured photo.

### 2.3 Modifying the "blur" mode

### 2.3.1 Resize or move the tag

While editing a photo in ObscuraCam, if you need to resize the tag,
touch one of the four corners of the white outline box so that it turns
green and drag it to make it larger or smaller.

If you need to move the tag so that it is in a better position on the
photo, touch the centre of the pixelated area so that the surrounding
white box turns green, then drag the box to the location you want.

![](tool_obscura4.png)

### 2.3.2 Change the obscure type

ObscuraCam gives you a few options on how to obscure a photo. From the
edit screen tap on an existing obscured area to bring up the obscuring
options:

![](tool_obscura5.png)

**Pixelate** will obscure any part of the photo inside the tag by
pixelating it

![](tool_obscura6.png)

**Redact** will obscure any part of the photo inside the tag by placing
a black box over it

![](tool_obscura7.png)

**Mask** will obscure any part of the photo inside the tag by placing a
funny mask over the person

![](tool_obscura8.png)

**Crowd Pixel** will obscure any part of the photo *outside* the tag by
pixelating the rest of it.

![](tool_obscura9.png)

**Clear Tag** will remove the selected tag from the photo.

### 2.3 Obscuring Videos

Obscuracam can also obscure faces or objects in videos, however unlike
with photos it can only obscure existing photos that you took with your
phone or copied to your phone

### 2.3.1 Automatic Obscuring of Videos

**Step 1:** From the main screen of Obscuracam tap ?Obscure Video?.

**Step 2:** Select the video you with to obscure from your phones
storage

**Step 3:** Tap ?Yes? when asked *Would you like to detect faces in this
video*.

**Step 3:** The video will begin to play and ObscuraCam will attempt to
detect faces. The process for detecting faces takes approximately *4
seconds* for every *1 second* of the video.

**Step 4:** Once the face detection has completed, you can tap Play to
review the video. This will show you the pixelated tags over the faces
as well as a green trail showing the path the tag takes through the
video as the face moves.

![](tool_obscura10.png)

**Step 5:** After reviewing the video and you are happy that all faces
are obscured, tap the save icon at the top of the screen to save the
video to your phones storage.

![](tool_obscura11.png)

**Note:** If ObscuraCam did not properly obscure faces or failed to
detect some, you can see how to manually obscure them in section below.

### 2.3.2 Manual Obscuring of Videos

If ObscuraCam was not able to detect faces properly during the automatic
process or you would like more process over the obscuring process you
can manually obscure video.

**Step 1:** From the main screen of Obscuracam tap ?Obscure Video?.

**Step 2:** Select the video you with to obscure from your phones
storage.

**Step 3:** Tap ?No? when asked *Would you like to detect faces in this
video*.

**Step 4:** Tap the play icon to start playing the video

**Step 5:** While the video plays, touch and hold your finger on a face
in the video to add a tag over it, drag the tag around the screen with
your finger following the movement of the face. Lift your finger off the
screen to stop obscuring the video.

**Note:** As you follow the face on the screen you will see a green
trail being left behind, this is the path the pixelated tag will take
once the video is saved.

**Step 6:** If there are additional faces in the video that you wish to
obscure, touch and hold the blue circle and move the slider back to the
time point where the next face appears on video and repeat *step
5* above.

**Step 7:** Once you have finished manually obscuring faces, you can
tap the play icon to review the video. This will show you the pixelated
tags over the faces as well as a green trail showing the path the tag
takes through the video as the face moves.

**Step 8:** After reviewing the video and you are happy that all faces
are obscured, tap the save icon at the top of the screen to save the
video to your phones storage.

### 2.3.3 Changing Output Video Quality

ObscuraCam chooses a default video quality when saving that make the
video small enough to easily share via email or other methods but does
reduce resolution and quality of the video.

To keep the obscured video in a higher resolution:

**Step 1:** After either automatically or manually detecting faces and
before saving the video, tap the three vertical dots icon to bring up
the menu and select ?Preferences?.

**Step 2:** Review and change the settings you want, where
possibly ObscuraCam will give you the range by which each setting can be
changed.

![](tool_obscura12.png)

**Step 3:** Once you have made the desired output changes, tap the back
button on your phone and save the video.

BASIC SECURITY SETUP FOR ANDROID GUIDE
======================================

Basic Security Setup for Android guide
--------------------------------------

**Lesson to read: [Mobile Phones](umbrella://lesson/mobile-phones)**\
**Phone requirements:** Android 4.4\
**Level:** Beginner\
**Time required:** 5 minutes

### 1.0 Basic Setup

### 1.1 Access to your phone

**Enable** *Lock SIM card*, found under *Settings -&gt; Personal -&gt;
Security -&gt; Set up SIM card lock*. This will mean that you must enter
a PIN number in order to unlock your SIM card each time your phone is
switched on, with out the PIN no phone calls can be made.

**Set up** a *Screen Lock*, found under *Settings -&gt; Personal -&gt;
Security -&gt; Screen Lock*, which will ensure that a code, pattern or
password needs to be entered in order to unlock the screen once it has
been locked. We recommended using the PIN or Password option, as these
are not restricted by length. You can find more information on creating
strong passwords in the [Passwords lesson](umbrella://lesson/passwords).

**Set** the *security lock timer*, which will automatically lock your
phone after a specified time. You can specify a value which suits you,
depending on how regularly you are willing to have to unlock your phone.

### 1.2 Device Encryption

If your device uses Android version 4.0 or newer, you should **turn
on** *device encryption*. This can be done in *Settings -&gt; Personal
-&gt; Security -&gt; Encryption*. Before you can utilise device
encryption, however, you will be required to set a screen lock password
(described above).

**Note:** Before starting the encryption process, ensure the phone is
fully charged and plugged into a power source.

### 1.3 Network settings

**Turn off** Wi-Fi and Bluetooth by default. Ensure
that *Tethering* and *Portable Hotspots*, under Wireless and Network
Settings, are switched off when not in use. *Settings -&gt; Wireless &
Networks -&gt; More -&gt; Tethering & Mobile hotspot*

If your device supports *Near Field Communication (NFC)*, this will be
switched on by default, and so must be switched off manually.

### 1.4 Location settings

**Switch off** *Wireless* and *GPS* location (under *Location Services*)
and mobile data (this can be found under *Settings -&gt; Personal -&gt;
Location*).

**Note:** Only turn on location settings as you need them. It is
important not have these services running by default in the background
as it reduces the risk of location tracking, saves battery power and
reduces unwanted data streams initiated by applications running in the
background or remotely by your mobile carrier.

### 1.5 Caller Identity

If you want to hide your caller-ID, go to *Phone Dialler -&gt; settings
-&gt; Additional Settings -&gt; Caller ID -&gt; hide number*.

### 1.6 Software Updates

To ensure that you phone remains secure it is strongly recommended to
keep your software updated. There are two types of updates that need to
be checked

The phone operating system: go to: *settings -&gt; About phone -&gt;
updates -&gt; check for updates*

Apps you have installed: Open the **Play store** app, from the *side
menu* select **My Apps**.

**Note:** When updating your phones software it is important to do it
from a trusted location such as your internet connection at home instead
of somewhere like an internet cafe or coffee shop.

Tips on using anti-virus software effectively
=============================================

The beginner section gave a run through of useful anti-virus software
such as [Avast](https://www.avast.com) or [Clam
Win](http://www.clamwin.com/) and anti-malware software such as
[Spybot](https://www.safer-networking.org/) or
[Malwarebytes](https://www.malwarebytes.org/). There are a few ways in
which you can make sure you get the most out of your software.

![](malware_adv1.png)

-   Do not run two anti-virus programs at the same time, as this might
    cause your computer to run extremely slowly or to crash. Uninstall
    one before installing another. However anti-malware software is
    designed to work alongside anti-virus software.
-   Make sure that your anti-virus program updates itself regularly.
    Without updates it can quickly become ineffective. All of the
    software recommended here supports free updating.
-   Enable your anti-virus software's 'always on' virus-detection
    feature if it has one. It may also be called 'Realtime Protection,'
    'Resident Protection,' or something similar.
-   Scan all of the files on your computer regularly. You don't have to
    do this every day but you should do it from time to time. How often
    may depend on the circumstances. Have you connected your computer to
    unknown networks recently? With whom have you been sharing USB
    memory sticks? Do you frequently receive strange attachments by
    email? Has someone else in your home or office recently had virus
    problems? Tools such as Avast can do this for you.

Activists and human rights defenders are increasingly documenting their
protests using cameras and mobile phones ? often to powerful effect. The
following are useful tips for you to remember if you are going to a
protest and are concerned about protecting your electronic devices if
you?re detained by police.

Think carefully about what?s on your phone before bringing it to a
protest. Your phone contains a wealth of private data, which can include
your list of contacts, the people you have recently called, your text
messages and email, photos and video, GPS location data, your web
browsing history and passwords, and the contents of your social media
accounts. Through stored passwords or active logins, access to the
device can allow someone to obtain yet even more information on remote
servers. (You can log out of these services).

In many countries, people are required to register their SIM cards when
they purchase a mobile phone. If you take your mobile phone with you to
a protest, it makes it easy for the government to figure out that you
are there. If you need to keep your participation in a protest secret
from governments or law enforcement, cover your face so that it is
harder to identify you from photos. However, do note that masks may get
you into trouble in some locations due to anti-mask laws.

**If it is important to keep your presence at the protest concealed, do
not take your mobile phone with you.**

**If you absolutely must bring a mobile phone with you, try to bring one
that is not registered in your name.**

How to delete information securely
==================================

Most of us think that a file on our computer is deleted once we put the
file in our computer's trash folder and empty the trash; in reality,
this does not actually delete files ? it just makes them invisible to
the user until the space they took up on your computer is overwritten
with something else. This means that, with the right tools, your
?deleted? files can often be retrieved.

![](deleting1.png)

The best way to delete a file forever, then, is to make sure it gets
overwritten immediately.\
This can be done easily using Eraser (for Windows) or Secure Delete (for
Mac OS X), both of which are described below. Users of Linux and other
open-source operating systems can use GNU shred, but this requires a
more advanced technical proficiency.

![](deleting2.png)

Note that securely deleting data from solid state drives (SSDs), USB
flash drives, and SD cards is very hard! The instructions below
apply only to traditional disk drives. If you?re using an SSD or a USB
flash drive, you can skip to the section about it below.

SIGNAL TOOL GUIDE
=================

Signal Tool Guide\
Encrypted phone calls for iPhones
---------------------------------

**Lesson to read:\
? [Making a Call](umbrella://lesson/making-a-call)**\
**Download Location:** The app can be downloaded from the [Apple App
Store](https://itunes.apple.com/us/app/signal-private-messenger/id874139669?mt=8)\
**Computer requirements:** Requires iOS 7.0 or later. Compatible with
iPhone, iPad, and iPod touch.\
**Version used in this guide:** Signal ? Private Messenger 1.0.5\
**License:** GPLv3\
**Level:** Beginner-Intermediate\
**Other reading:**\
? <https://whispersystems.org/blog/signal/>\
? <http://support.whispersystems.org/>\
**Time required:** 15-20 minutes

**Using Signal will give you:**\
? The ability to make encrypted voice calls over a Wi-Fi or data
connection using your normal phone number

NOTE:\
? Although it uses telephone numbers as contacts, calls actually use
your data connection; therefore both parties to the conversation must
have Internet access on their mobile devices.\
? Signal only encrypts calls that are between two Signal users, or
between users of Signal and RedPhone, the app for Androids. (See
**[RedPhone Tool Guide](umbrella://lesson/redphone)** for instructions
for Androids)

### 1.0 How to install Signal

**Step 1:** Download and Install Signal ? Private Messenger

On your iOS device, enter the App Store and search for ?Signal.? Select
the app ?Signal ? Private Messenger? by Open Whisper Systems.

Click to download the app and accept the iTunes Store Terms & Conditions
by selecting ?Accept.? The app will download and install automatically.
Click ?Open? to launch the app.

**Step 2:** Register and Verify your Phone Number

You will see a screen that looks like this:

![](tool_signal1.png)

Enter your mobile phone number and click ?Register.? In order to verify
your phone number, you will be sent an SMS text with a six-digit code;
enter the code in the space provided. If you are unable to receive SMS
texts, you have the option of receiving a phone call to verify your
phone number. Click ?Verify.?

### 2.0 Using Signal

In order to use Signal, the person that you are calling must have either
Signal or RedPhone (for Android devices) installed. If you try to call
someone using the Signal app and they do not have Signal or RedPhone
installed, the app will ask if you would like to invite them via SMS,
but it will not allow you to complete your call from inside the app.

![](tool_signal2.png)

### 2.1 How to Initiate an encrypted call

To initiate an encrypted call to a contact, you must use the dialer
within the Signal app. (This differs from RedPhone for Android, which
also allows you to use the default system dialer.)

Once a call is established, both parties to the call will be shown a
random pair of words. This word pair will allow you to verify your
identity and keys with the other user?also known as key verification.

![](tool_signal3.png)

The most trustworthy way to verify the identity of a caller is to use
out-of-band authentication to verify the word pair. You can also read
the words aloud if you recognize the caller?s voice, although very
sophisticated attackers might be able to defeat this if they needed to.
The word pair must be identical.
