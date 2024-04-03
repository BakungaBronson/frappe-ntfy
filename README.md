## Frappe Ntfy

A package to send simple notifications via the [Ntfy](ntfy.sh) app.

This app is designed to send notifications through ```ntfy.sh```, a versatile service that allows for sending real-time notifications to various devices. The configuration of this function involves several parameters, each with a specific purpose and expected value types. Below, we provide a comprehensive guide to these parameters and their roles in sending notifications.


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



### Example Usage:

### Result:


To fully understand the capabilities and limitations of the Ntfy function parameters, especially for actions, delay, and formatting options like Markdown, it's advisable to consult the official ntfy.sh documentation available at [docs.ntfy.sh](doc.ntfy.sh) documentation. This resource provides detailed explanations and examples on how to structure JSON payloads for various notification features, ensuring that users can leverage the full potential of the ntfy.sh service within their Frappe applications.

#### License

MIT