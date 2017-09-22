# UPV-Redirect
A selenium python script to automate the transfer of all new messages from Université Paul Valéry's website as they don't allow POP3 or IMAP access.

## Use
In the "Credentials" part of the script, fill in username, password, and the email address you wish to have the messages redirected to.

I created a separate folder that filters out the mass-market email that didn't interest me by having this script only redirect emails from said folder that I named "InboxReel". In the code, simply replace the string "InboxReel" with "INBOX" on line 44 if you wish to redirect all email.

Finally, enjoy the sweet sweet satisfaction at getting around their rediculous "security" precaution of banning all access to email that isn't through their website by web browser.
