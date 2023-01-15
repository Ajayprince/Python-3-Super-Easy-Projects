import pyshorteners as ps
link = input("Enter the link: ")
shortener = ps.Shortener()
final_link = shortener.tinyurl.short(link)
print(final_link)