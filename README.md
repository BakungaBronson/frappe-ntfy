## Frappe Ntfy

A package to send simple notifications via the [Ntfy](ntfy.sh) app.

This app is designed to send notifications through ```ntfy.sh```, a versatile service that allows for sending real-time notifications to various devices. The configuration of this function involves several parameters, each with a specific purpose and expected value types. Below, we provide a comprehensive guide to these parameters and their roles in sending notifications.


## Gettings Started
### 1. Download the Ntfy app:
   Ntfy has an application for iOS and Android, the links can be found on the homepage of the Ntfy website [https://ntfy.sh/](https://ntfy.sh/). Ntfy also is accessible from the web at [https://ntfy.sh/app](https://ntfy.sh/app).

### 2. Subscribe to a topic at Ntfy:
   A topic is a combination of unique characters you can use to send notifications between your devices. The topic functions like a password and should therefore be kept secret.
   To get a topic, go to [https://ntfy.sh/app](https://ntfy.sh/app) and type in a topic.

![Step 1 screenshot](https://images.tango.us/workflows/18cb2897-0c16-4c23-81cc-6a45db0154f1/steps/624272ab-f4a3-448b-9556-3d253d5f1d6c/16eee185-4dd9-4ed3-b6b0-b6a0c8f933f8.png?crop=focalpoint&fit=crop&fp-x=0.9211&fp-y=0.0724&fp-z=2.7941&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=784&mark-y=113&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0zMDQmaD0xNTAmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)

  ![Step 2 screenshot](https://images.tango.us/workflows/18cb2897-0c16-4c23-81cc-6a45db0154f1/steps/dc502ab9-3608-41e0-b452-3649b4974856/27425165-e293-45c7-ba52-890c3491d2d0.png?crop=focalpoint&fit=crop&fp-x=0.1377&fp-y=0.5489&fp-z=1.7606&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=8&mark-y=409&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz01NjYmaD0xMTAmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)
  
  ![Step 3 screenshot](https://images.tango.us/workflows/18cb2897-0c16-4c23-81cc-6a45db0154f1/steps/f1c7ab15-6f42-4e47-8646-7307bd989005/ffde5c41-eee7-48e0-8a4f-0e2754a1acb0.png?crop=focalpoint&fit=crop&fp-x=0.4384&fp-y=0.4704&fp-z=1.4312&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=258&mark-y=432&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz02ODUmaD02NCZmaXQ9Y3JvcCZjb3JuZXItcmFkaXVzPTEw)
  
  ![Step 4 screenshot](https://images.tango.us/workflows/18cb2897-0c16-4c23-81cc-6a45db0154f1/steps/a5d4d409-7d7b-4b66-9b6d-dc1c06c06bd9/f2bd3cef-84be-472e-8421-eea1511c74c8.png?crop=focalpoint&fit=crop&fp-x=0.7213&fp-y=0.6520&fp-z=2.8226&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=440&mark-y=393&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0zMTkmaD0xNDImZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)
   
   From now on when sending notifications to your other decives this is the same topic you must use.
   
### 3. Use topic in making a call:
   One we have our topic, we can send a notification via Frappe Ntfy and it will appear on any device that is subscribed to the topic.
### 4. Sending notifications from the web:
   You do not always need to send notifications via the Frappe Ntfy app only, and you can simply use the app or web interface to send notifications to subscribed devices as well.

![Step 5 screenshot](https://images.tango.us/workflows/18cb2897-0c16-4c23-81cc-6a45db0154f1/steps/0c49557a-6cbc-490a-a1f2-2ed860ab2807/52091eec-c736-4573-8da7-e4a2194df9e0.png?crop=focalpoint&fit=crop&fp-x=0.6307&fp-y=0.9517&fp-z=1.4415&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=39&mark-y=832&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTIyJmg9NjUmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)

![Step 6 screenshot](https://images.tango.us/workflows/18cb2897-0c16-4c23-81cc-6a45db0154f1/steps/83d0111e-a830-4eb6-973e-39782c46708a/38090317-a735-42a7-9ed0-338f4800edad.png?crop=focalpoint&fit=crop&fp-x=0.9720&fp-y=0.9517&fp-z=4.0000&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=949&mark-y=624&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0yMzMmaD0yNTEmZml0PWNyb3AmY29ybmVyLXJhZGl1cz0xMA%3D%3D)

![Step 7 screenshot](https://images.tango.us/workflows/18cb2897-0c16-4c23-81cc-6a45db0154f1/steps/8d5584a0-6924-4ca2-ac7c-67f31ca7a408/44ad19cf-2a81-427d-bae6-04350aab08c5.png?crop=focalpoint&fit=crop&fp-x=0.6307&fp-y=0.2370&fp-z=1.3891&w=1200&border=2%2CF4F2F7&border-radius=8%2C8%2C8%2C8&border-radius-inner=8%2C8%2C8%2C8&blend-align=bottom&blend-mode=normal&blend-x=0&blend-w=1200&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmstdjIucG5n&mark-x=16&mark-y=131&m64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL2JsYW5rLnBuZz9tYXNrPWNvcm5lcnMmYm9yZGVyPTYlMkNGRjc0NDImdz0xMTY5Jmg9MzUwJmZpdD1jcm9wJmNvcm5lci1yYWRpdXM9MTA%3D)

Created with [Tango.us](https://tango.us?utm_source=markdown&utm_medium=markdown&utm_campaign=workflow%20export%20links)

## Use cases
Frappe Ntfy can be used for a number of situations in Frappe including notifications upon:
1. Document creation
2. System error
3. File share
4. Worflow step change
5. Event scheduler changes

The list goes on, and the possibilities are endless since Frappe Ntfy can plug directly into server scripts.


## `ntfy` Function Parameters

- **site** (Optional, string): The base URL for the `ntfy.sh` service. This parameter allows specifying a different endpoint if needed, for instance, when using a self-hosted version of `ntfy` or an alternative server. The default is set to the public `ntfy.sh` service.

  - Default: `https://ntfy.sh/`
  - Example: To use a self-hosted version of `ntfy`, you might set this to `https://ntfy.mydomain.com/`.

- **topic** (Required, string): Specifies the target topic name under which the message will be published. It is essential for directing the notification to the intended recipients.
  - Example: `topic1`

- **message** (Optional, string): The main content of the notification. If left empty or not passed, defaults to "triggered".
  - Example: `Some message`

- **title** (Optional, string): A brief title for the notification, providing a quick overview or context.
  - Example: `Some title`

- **tags** (Optional, string array): A list of tags for additional categorization or identification, which can also map to emojis.
  - Example: `["tag1", "tag2"]`

- **priority** (Optional, int): Indicates the urgency on a scale from 1 (minimum) to 5 (maximum), with 3 as the default.
  - Example: `4`

- **actions** (Optional, JSON array): Custom user action buttons included in the notification for interactive responses.
  - Documentation on the specific JSON structure for actions can be found in the `ntfy.sh` documentation.

- **click** (Optional, URL): A URL that the recipient can visit by clicking on the notification. Useful for directing users to more information or a specific action.
  - Example: `https://example.com`

- **attach** (Optional, URL): URL of an attachment that can be accessed through the notification, for sharing additional resources.
  - Example: `https://example.com/file.jpg`

- **markdown** (Optional, bool): Set to `true` if the message content is formatted using Markdown, allowing for rich text formatting.
  - Example: `true`

- **icon** (Optional, string): URL to an image to use as the notification icon, enhancing visual identification.
  - Example: `https://example.com/icon.png`

- **filename** (Optional, string): The filename for the attachment when downloaded or saved, relevant when `attach` is used.
  - Example: `file.jpg`

- **delay** (Optional, string): Specifies a delay before sending the notification, either as a duration (e.g., "30min") or a specific timestamp (e.g., "9am").
  - Example: `30min`

- **email** (Optional, e-mail address): An email address where the notification can also be sent, expanding delivery options.
  - Example: `phil@example.com`

- **call** (Optional, phone number or 'yes'): A phone number to call upon notification receipt, or 'yes' to initiate a default call, useful for urgent alerts.
  - Example: `+1222334444` or `yes`


### Example Usage (In Frappe Bench):
<img width="653" alt="image" src="https://github.com/BakungaBronson/frappe-ntfy/assets/51344005/fcfd95ef-4ed6-4250-ad4a-fbbd53fa9976">


### Result:
<img width="1002" alt="image" src="https://github.com/BakungaBronson/frappe-ntfy/assets/51344005/954245c7-3f49-4e0d-b772-528f7d7c5322">


To fully understand the capabilities and limitations of the Ntfy function parameters, especially for actions, delay, and formatting options like Markdown, it's advisable to consult the official ntfy.sh documentation available at [docs.ntfy.sh](doc.ntfy.sh) documentation. This resource provides detailed explanations and examples on how to structure JSON payloads for various notification features, ensuring that users can leverage the full potential of the ntfy.sh service within their Frappe applications.

#### License

MIT
