# WhatsappPulitor
A python tool to clean and remove old media files from WhatsApp

This tool provides a quick solution to delete WhatsApp's multimedia files older than a certain date. To overcome the problem that you cannot rely on the date of the last modification (because if you change your phone the backup downloaded from google drive falsifies this date by setting it to the day of recovery) the date is extracted from the file name.
The tool will remove all types of multimedia files, except documents. Since the only type of multimedia that doesn't have the date written in the file's name are documents, this tool cannot remove them. But still he tries.

## How to use
Open the file `whatsapp_pulitor.py`, copy to notepad and set the `date_before_which_to_delete` variable to the desired date (files before this date will be deleted). The value must be in the form YYmmdd (year in complete form, month and day; all joint).

Transfer the code to the android device and run it with a Python3 interpreter app, [for example this](https://www.qpython.com/) - [download from Google Play Store](https://play.google.com/store/apps/details?id=org.qpython.qpy3).

## Tag
WhatsApp Pulitor Cleaner WhatsAppCleaner full memory remove media files
