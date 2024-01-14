# 0x01 - Craw web

This project is to download all files from a web!

## How to use?

1. Make sure to use python version **3.12** or above.
2. Using virtual environment and install packages from `requirements.txt`

    ```sh
    pip install -r requirements.txt
    ```

3. Get all URLs by `getUrls.py` script

   ```sh
   python3 getUrls.py
   ```

### Use `Python` to download the files

If you want to use python to download the files, please run script `getMedia.py`.

```sh
python3 getMedia.py
```

All files will be stored in folder `/out`

### User `aria2c` to download the files

If you have `aria2c` installed and you want to use it, please run script `genAria2c.py`.

There will be a file named `aria2c.txt` which will be an input for aria2c.

Then run aria2c with an input file and your options.

```sh
aria2c [...your_options] -i aria2c.txt
```
