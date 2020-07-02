"""
Scrape car data and recreate a custom HTML page with it.

URL: https://www.autoblog.com/classifieds/
"""
import re
import requests

template_start = "<html><body><div><ul>"
template_end = "</ul></div></body></html>"


def main():
    url = 'https://www.autoblog.com/sell-your-own/listings/'
    html = requests.get(url).text
    pattern = r'src="(//s.aolcdn.com/\S+)" alt="(\d{4}) (\w+) (\w+)"'
    car_matches = re.findall(pattern, html)
    cars = {}
    with open('cars.html', 'w') as f:
        f.write(template_start)
        if car_matches:
            # sort cars by year
            car_matches.sort(key=lambda t: t[1])
            # group car photos under their respective car title
            for car_match in car_matches:
                img_src, year, make, model = car_match
                title = f"{year} {make} {model}"
                cars.setdefault(title, [])
                cars[title].append(img_src)

            for title, img_srcs in cars.items():
                f.write(f"<li><h3>{title}</h3>")
                for img_src in img_srcs:
                    f.write(f"""
                    <img src="https:{img_src}" alt="{title}"
                    width="200" height="140"/>
                    """)
                f.write("</li>")
        else:
            f.write("<li>No cars found</li>")
        f.write(template_end)


if __name__ == '__main__':
    main()
