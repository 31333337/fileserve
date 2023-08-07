# Python Simple File Server

This is a simple Python script that can be used to serve a single file over HTTP. It's a quick and easy way to make a file available for download to other machines.
It will later be used to serve files over 0kn mixnet for example :P 
## Usage
If no arguments are supplied, then following will ask user for input for filename path, port and verbose mode. 

```bash
python fileserve.py
```

You can also provide the information as command-line arguments:

```bash
python fileserve.py <filename> <port> <verbose>
```

- `<filename>`: The name of the file you want to serve. This is a required argument.
- `<port>`: The port you want to serve the file on. This is optional; if not provided, the default is `1337`.
- `<verbose>`: Whether to print information about incoming connections. This is optional; if not provided, the default is `False`.

## Example

Here's an example of how to use the server:

```bash
python serve.py myfile.txt 8080 True
```

This will serve `myfile.txt` on port `8080`, and it will print information about incoming connections.

## Dependencies

This script requires Python 3. It uses the built-in `http.server` and `socketserver` modules, so no additional Python packages are needed. However, it does import a function from the `get_ip.py` script, which is included in this repository.

## Note

This server is intended for quick, temporary file serving in trusted networks. It should not be used as a production server or for serving sensitive data. Please use a proper web server like Nginx or Apache for that purpose.
