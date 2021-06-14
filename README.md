# Scrap Python Script
Basic scraping script

# Install

## Requirements

* pip
* pandas
* requests
* BeautifulSoup

## Linux

          sudo apt install git
          sudo apt-get update
          
          mkdir script
          cd script
          git clone https://github.com/Bescri/scrap-script
          cd scrapt-script/
         

## Others S.O

* http://git-scm.com/download/win
* http://git-scm.com/download/mac


## Usage

Change the URL to scrapt.

          url = "{insertURLhere}"
          
Change the TAG items name and his classes

          eq = soup.find_all('{insertTAGhere}', class_='{insertCLASShere}')
          
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)


