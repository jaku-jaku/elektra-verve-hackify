files = [
		{"id":"ic6", "src":"./images/v1/IC6.svg.png"},
		{"id":"uc43", "src":"./images/v1/UC43.svg.png"},
		{"id":"uc46", "src":"./images/v1/UC46.svg.png"},
		{"id":"uc72", "src":"./images/v1/UC72.svg.png"},
		{"id":"uc118", "src":"./images/v1/UC118.svg.png"},
		{"id":"uc119", "src":"./images/v1/UC119.svg.png"},
		{"id":"ug4", "src":"./images/v1/UG4.svg.png"},
		{"id":"ug8", "src":"./images/v1/UG8.svg.png"},
		{"id":"ug10", "src":"./images/v1/UG10.svg.png"},
        {"id":"ug38", "src":"./images/v1/UG38.svg.png"},
        {"id":"uc123", "src":"./images/v1/UC123.svg.png"},
        {"id":"ug21", "src":"./images/v1/UG21.svg.png"},
        {"id":"uc119", "src":"./images/v1/UC119.svg.png"},
        {"id":"uc73", "src":"./images/vp1/UC73.svg.png"},
        {"id":"ic19", "src":"./images/vp1/IC19.svg.png"},
        {"id":"ic20", "src":"./images/vp1/IC20.svg.png"},
        {"id":"ig2", "src":"./images/vp1/IG2.svg.png"},
        {"id":"ig2w", "src":"./images/vp1/IG2w.svg.png"},
        {"id":"ig31", "src":"./images/vp1/IG31.svg.png"},
        {"id":"ig17", "src":"./images/vp2/IG17.svg.png"},
        {"id":"ig17-rollover", "src":"./images/vp2/UG17ROLLOVERB.svg.png"},
		{"id":"ug33", "src":"./images/vp2/UG33.svg.png"},
		{"id":"ug34", "src":"./images/vp2/UG34.svg.png"},
		{"id":"ic19", "src":"./images/vp1/IC19.svg.png"},
		{"id":"ic20", "src":"./images/vp1/IC20.svg.png"},
		{"id":"ig2", "src":"./images/vp1/IG2.svg.png"},
		{"id":"ig2w", "src":"./images/vp1/IG2w.svg.png"},
		{"id":"ig31", "src":"./images/vp1/IG31.svg.png"},
		{"id":"ug52", "src":"./images/vp3/UG52.svg.png"},
		{"id":"ug52-rollover", "src":"./images/vp3/UG52-rollover.svg.png"},
		{"id":"ug53", "src":"./images/vp3/UG53.svg.png"},
		{"id":"ug53-rollover", "src":"./images/vp3/UG53-rollover.svg.png"},
		{"id":"ig2", "src":"./images/vp1/IG2.svg.png"},
		{"id":"ig2w", "src":"./images/vp1/IG2w.svg.png"},
		{"id":"ig31", "src":"./images/vp1/IG31.svg.png"},
		{"id":"ic52", "src":"./images/vp4/IC52.svg.png"},
		{"id":"ic52-rollover", "src":"./images/vp4/IC52-rollover.svg.png"},
		{"id":"ug54", "src":"./images/vp4/UG54.svg.png"},
		{"id":"ug54-rollover", "src":"./images/vp4/UG54-rollover.svg.png"},
        {"id":"ug55", "src":"./images/vp4/UG55.svg.png"},
        {"id":"uc64", "src":"./images/vp4/UC64.svg.png"},
        {"id":"uc64-rollover", "src":"./images/vp4/UC64-rollover.svg.png"},
		{"id":"ig2", "src":"./images/vp1/IG2.svg.png"},
		{"id":"ig2w", "src":"./images/vp1/IG2w.svg.png"},
		{"id":"ig31", "src":"./images/vp1/IG31.svg.png"},
        {"id":"logo", "src":"./images/logo.png"},
]


import requests

URL = "http://elektra.com/"

for item in files:
    image_url = URL + item["src"]
    out_file = 'icon_{}.png'.format(item["id"])
    img_data = requests.get(image_url).content
    with open(out_file, 'wb') as handler:
        print("Fetching from {} ==> save @ {}".format(image_url, out_file))
        handler.write(img_data)

