import requests

ibm_rss_feed = requests.get("https://research.ibm.com/rss?fid=rss")

print(type(ibm_rss_feed))