# KijijiAutoPoster

### Description
KijijiAutoPoster is an automation tool using `selenium` with `Python` to make posting on Kijiji easer. As of now, it is only able to repost laptop ads in the Greater Toronto Area.

### Index
1. [How to Install KijijiAutoPoster](#installing-kijijiautoposter)
2. [How to Use KijijiAutoPoster](#using-kijijiautoposter)
3. [License](#license)



### Installing KijijiAutoPoster
To install KijijiAutoPoster you will need to download [selenium](https://pypi.org/project/selenium/) and [Mozilla Firefox](https://www.mozilla.org/en-CA/firefox/new/) along with its [Gecko Driver](https://github.com/mozilla/geckodriver/releases).

### Using KijijiAutoPoster
To use KijijiAutoPoster you will have to modify the following variables in `KijijiAutoPoster.py`:
- `driver_path`: The Gecko Driver location.
- `email`: The Kijiji Email or Username.
- `password`: The Kijiji Password.
- `postal_code`: The Postal Code you want used for the ad.
- `location`: The location of the ad.
- `title`: The ad Title.
- `brand`: The laptop brand.
- `screen_size`: The laptop screen size.
- `description`: The bio of the ad.
- `tags`: The tags of the ad.
- `price`: The price of the laptop.

Then, run `KijijiAutoPoster.py`.

### License
See the [LICENSE.txt](LICENSE.txt) file for license rights and limitations (MIT).
