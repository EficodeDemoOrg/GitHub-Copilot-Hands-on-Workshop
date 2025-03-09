Example from https://github.blog/developer-skills/github/how-i-used-github-copilot-to-build-a-browser-extension/

# GitHub Copilot Prompts for Chrome Extension

Here are the prompts used with GitHub Copilot, extracted from the Chrome extension tutorial:

## Prompting for Initial Setup and File Structure in the Copilot Chat

* How do I create a Chrome extension? What should the file structure look like?

![image](https://github.com/user-attachments/assets/14dfae42-e12e-4222-9693-be91df1d35ce)

## Generating code inside the manifest.json file using comments that are prompts for Copilot in-line

* Manifest for Chrome extension that clears browser cache.
* manifest_version: 3
* Permissions for the extension are: storage, tabs, browsingData

Once the comments are added in the file, pressing the Enter key will invoke the Copilot agent.

## Prompting code generation inside background.js using Copilot in-line

* Service Worker for Google Chrome Extension Handles when extension is installedHandles when message is received
* console.log when extension is installed
* send response when message is received and console.log when message is received

## popup.html

*  HTML for Chrome extension that clears browser cache.
   Connect to javascript file called popup.js and CSS file called style.css
   Will render the following buttons with id's:
   - "All History"
   - "Past Month"
   - "Past Week"
   - "Past Day"
   - "Past Hour"
   - "Past Minute"

   Will render an empty paragraph with id "lastCleared"

## Code generation inside popup.js using comments

* This program is a Chrome Extension that clears browser cache.
* Handle on button click:
  - button with id "allHistory" that clears all cache history
  - button with id "pastMonth" that clears cache history from the past month
  - button with id "pastWeek" that clears cache history from the past week
  - button with id "pastDay" that clears cache history from the past day
  - button with id "pastHour" that clears cache history from the past hour
  - button with id "pastMinute" that clears cache history from the past minute Create function that
  - converts dates and times into human-readable format
  - adds "Successfully cleared cache" with date and time in a paragraph with id "lastCleared" 
* convert date and time into human-readable format
* add successfully cleared cache into paragraph with id "lastCleared
* clear all cache history
* clear cache history from the past month
* clear cache history from the past week
* clear cache history from the past day
* clear cache history from the past hour
* clear cache history from the past minute

## style.css

Write a comment that describes the style you want for your extension. Then, type “body” and continue tabbing until GitHub Copilot suggests all the styles.

* Style the Chrome extension's popup to be wider and taller
* Use accessible friendly colors and fonts
* Make h1 elements legible
* Highlight when buttons are hovered over
* Highlight when buttons are clicked
* Align buttons in a column and center them but space them out evenly
* Make paragraph bold and legible
