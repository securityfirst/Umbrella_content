TEXTSECURE TOOL GUIDE
=====================

TextSecure Tool Guide\
Secure messaging for Android
----------------------------

**Lesson to read:\
? [Sending a message](umbrella://lesson/sending-a-message)**\
**Download Location:** TextSecure can be downloaded from [Open
WhisperSystems](https://whispersystems.org/); and can also be downloaded
from the [Google Play
store](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms)\
**Computer requirements:** Android 2.3 and up\
**Version used in this guide:**  TextSecure 2.1.7\
**License:** GPLv3\
**Level:** Beginner - Intermediate\
**Other reading: **\
? <https://github.com/WhisperSystems/TextSecure/wiki/Using-TextSecure>\
? <https://securityinabox.org/en/textsecure_main>\
? <http://support.whispersystems.org/>\
**Time required:** 15 minutes

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
