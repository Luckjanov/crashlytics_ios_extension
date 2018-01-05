import appex
import requests
import re
from urllib.parse import unquote
import plistlib


def main():
  url = appex.get_text()
  if url:
    url_info_plist = (re.search('(.+url=)(.+)', url))[2]
    url_info_plist = unquote(url_info_plist)
    info_plist_str = requests.get(url_info_plist).text

    with open("info.plist", "w") as handle:
      handle.write(info_plist_str)

    with open("info.plist", 'rb') as fp:
      info_plist = plistlib.load(fp)

    ipa_url = info_plist['items'][0]['assets'][0]['url']
    ipa_version = info_plist['items'][0]['metadata']['bundle-version']
    ipa_revision = info_plist['items'][0]['metadata']['subtitle']
    ipa_title = info_plist['items'][0]['metadata']['title']
    ipa_full_name = ipa_title + ' ' + ipa_version + '-' + ipa_revision + '.ipa'

    response = requests.get(ipa_url, stream=True)

    with open(ipa_full_name, "wb") as handle:
      handle.write(response.content)

  else:
    print(appex)
    print('No input URL found.')

if __name__ == '__main__':
  main()
