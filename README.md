# Download iOS app bundle from Crashlytics
Sometimes it’s useful to have original .ipa file on your computer. You may want to download it to quickly install on several devices or see what there are inside. Crashlytics only let you to install app on your iPhone and doesn’t provide way to download. This  iOS extension fixes that. 

## How it works
1. Install [Pythonista](http://omz-software.com/pythonista/).
2. Import get_ipa.py to your iCloud folder.
3. Configure Share extension in Pythonista settings.
4. Open Crashlytics install page.
5. Use long tap on “Install” button.
6. Select “Share” in action menu.
7. Choose “Run Pythonista Script”
8. And finally choose your configuration with the script.

ipa-file will be downloaded to your iCloud Pythonista folder. If you have sync, app will appear on your computer automatically.

## Problems
Currently Pythonista have a [issue](https://github.com/omz/Pythonista-Issues/issues/504) that prevents some user from running iCloud script in extension.