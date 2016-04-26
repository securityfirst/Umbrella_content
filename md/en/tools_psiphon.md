PSIPHON TOOL GUIDE
==================

Psiphon Tool Guide\
Censorship Circumvention
------------------------

**Lesson to read:\
? [The Internet](umbrella://lesson/the-internet)**\
**Download Location:** <https://psiphon.ca/en/download.html>\
**Computer requirements:** An internet connection, a computer running
Windows or an Android 2.2 phone or up (Psiphon 3 versions for iPhones
and Mac OS X are coming soon)\
**Version used in this guide:** Psiphon 3\
**License:** Free open-source software; GNU GPL Version 3\
**Level:** Beginner\
**Other reading:** <https://psiphon.ca/en/user-guide.html>\
**Time required:** 5 minutes

**Using Psiphon will give you:**\
? The ability to safely get around internet censorship to access blocked
websites and applications on your phone or computer.

### 1 Before you start

? **ALERT:** The Psiphon Team has discovered a specific instance of
malware disguised as a Psiphon 3 Windows executable. The malware is
being distributed as a zip file named "pisphone3.zip" on www.copy.com
and may be available from other sources. The zip file contains a
malicious binary named "pisphone3.exe" with the properties described
at [Virus
Total](https://www.virustotal.com/en/file/54201e181615c7eb18ee5a5ca3a0b7924cf3097ac5214fbee530741b6a6bc3da/analysis/1372262585/).
Note the misspelling of the name. This Windows executable is not
digitally signed by Psiphon Inc. Never run a fresh download of Psiphon
without checking its digital signature, as
described [here](https://psiphon.ca/en.html#is_my_psiphon_3_for_windows_authentic).\
? It should be noted that although Psiphon is does not allow individual
user?s IP addresses to be associated with any individual website
visited, Psiphon is intended primarily as a censorship evasion tool,
rather than one that guarantees anonymity.

### 2 Psiphon for Android

Download the appropriate version of Psiphon from
[here](https://psiphon.ca/en/download.html).

Click on a Psiphon APK link from within your Android email or browser to
begin the installation.

(If you get an error, you may need to [enable
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
? Because Psiphon 3 is VPN-based, it is able to proxy all of your
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
