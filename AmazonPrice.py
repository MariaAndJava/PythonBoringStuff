import bs4, logging
import requests

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
res = requests.get('https://www.amazon.de/Hoden-Fahrrad-Indikatoren-hinten-Silikon/dp/B071F4ZW7M', headers=headers)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('html.a-js.a-audio.a-video.a-canvas.a-svg.a-drag-drop.a-geolocation.a-history.a-webworker.a-autofocus.a-input-placeholder.a-textarea-placeholder.a-local-storage.a-gradients.a-transform3d.-scrolling.a-text-shadow.a-text-stroke.a-box-shadow.a-border-radius.a-border-image.a-opacity.a-transform.a-transition.a-ember.a-ws body.a-m-de.a-aui_152852-c.a-aui_157141-c.a-aui_158613-t1.a-aui_72554-c.a-aui_dropdown_187959-c.a-aui_pci_risk_banner_210084-c.a-aui_perf_130093-c.a-aui_tnr_v2_180836-c.a-aui_ux_145937-c.a-meter-animate div#a-page header.nav-opt-sprite.nav-locale-de.nav-lang-de.nav-ssl.nav-rec div#navbar.nav-sprite-v1.celwidget.nav-bluebeacon.nav-a11y-t1.nav-packard-glow.hamburger.layout2.split-bg.using-mouse div#nav-belt div.nav-right div#nav-tools.layoutToolbarPadding a#nav-cart.nav-a.nav-a-2 span.nav-cart-icon.nav-sprite')
#elems[0].text.strip()
logging.debug(elems)