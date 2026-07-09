Spreadsheet Injection, also known as CSV Injection or Formula Injection, is a security vulnerability that occurs when a web application exports untrusted user input into a CSV file without proper sanitization.
This can lead to the execution of malicious formulas within the spreadsheet, allowing attackers to exfiltrate sensitive data, launch phishing attacks, or execute commands on the user's machine. The vulnerability is triggered when a cell in the CSV file starts with specific characters that are interpreted as formulas by spreadsheet applications like **Microsoft Excel, Google Sheets, or LibreOffice Calc**. 

You can use the below characters to injection malicious content in spreadsheets- 

- Equals to (=)
- Plus (+)
- Minus (-)
- At (@)
- Tab (0x09)
- Carriage return (0x0D)
- Line feed (0x0A)
- Full-width (double-byte) variants of formula-initiating characters such as ＝, ＋, －, and ＠, which may be interpreted as formulas in some locales (e.g., Japanese environments).

You can also use the field separator (e.g., ,, ;) and quotes (e.g., ", '), to start a new cell and then have the dangerous character in the middle of the user input, but at the beginning of a cell.

> [!IMPORTANT]
> Microsoft Excel may remove quotes or escape characters from CSV cells when a file is saved and re-opened. As a result, commonly suggested CSV injection mitigations may fail and previously escaped formulas may become active again.

> [!NOTE]
> Modern versions of spreadsheet processing software such as Microsoft Excel, typically prompt uses before allowing the execution of such functionality. Therefore, a certain amount of social engineering is required for successful execution.
> This vulnerability can only be exploited if the participant's Excel environment has Dynamic Data Exchange (DDE) enabled.

## Recommendation
apply the following sanitization to each field of the CSV, so that their content will be read as text by the spreadsheet editor:

- Wrap each cell field in double quotes
- Prepend each cell field with a single quote
- Escape every double quote using an additional double quote

> [!IMPORTANT]
> The above techniques are not reliable in Microsoft Excel after saving and re-opening the CSV file.

To reliably prevent formula execution in Microsoft Excel, prefix any cell starting with =, +, -, or @ with a tab character (0x09) inside the quoted field.
The tab character remains part of the underlying data and may affect downstream processing if the CSV is later imported programmatically. This mitigation is best suited for CSV files intended for human viewing in spreadsheet applications.
