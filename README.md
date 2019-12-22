# Kijiji Auto Poster

### Description
KijijiAutoPoster is an automation tool using `selenium` with `Python` to make posting on Kijiji easer. As of now, it is only able to repost Laptop Ads.

### Index
1. [How to Install KijijiAutoPoster](#installing-kijijiautoposter)
2. [License](#license)
3. [How to Use KijijiAutoPoster](#using-kijijiautoposter)


### Installing KijijiAutoPoster
To install KijijiAutoPoster you will need to download [selenium](https://pypi.org/project/selenium/) and [Mozilla Firefox](https://www.mozilla.org/en-CA/firefox/new/) along with its [Gecko Driver](https://github.com/mozilla/geckodriver/releases).

### Using KijijiAutoPoster
To use KijijiAutoPoster you will have to modify the following variables in `KijijiAutoPoster.py`:
- `driver_path`: The Gecko Driver location.
- `email`: The Kijiji Email or Username.
- `password`: The Kijiji Password.
- `postal_code`: Ther Postal Code you want used for the ad.
- `title`: The Ad Title.
- `brand`: The laptop brand.
- `screen_size`: The laptop screen size.
- `description`: The bio of the ad.
- `tags`: The tags of the ad.
- `price`: The price of the laptop.

Then, run `KijijiAutoPoster.py`.

### License
See the [LICENSE.txt](LICENSE.txt) file for license rights and limitations (MIT).
