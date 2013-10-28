# Create your views here.

from django.http import HttpResponse
import datetime
import mechanize
import re
from bs4 import BeautifulSoup

def home (request):
	
	# html = "<html><body>Hi there.</body></html>"

	br = mechanize.Browser()

	# Browser options
	br.set_handle_equiv(True)
	br.set_handle_gzip(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)

	# Follows refresh 0 but not hangs on refresh > 0
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

	# Want debugging messages?
	#br.set_debug_http(True)
	#br.set_debug_redirects(True)
	#br.set_debug_responses(True)

	


	r = br.open('https://google.com')
	html = r.read

	#  Ignore robots.txt 
	br.set_handle_robots(False)

	# User-Agent (this is cheating, ok?)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

	br.select_form ('f')
	br.form ['q'] = 'foo'

	br.submit()

	# Find the link to foofighters.com; why did we run a search?
	resp = None
	for link in br.links():
	    siteMatch = re.compile( 'www.foofighters.com' ).search( link.url )
	    if siteMatch:
	        resp = br.follow_link( link )
	        break

	content = r.get_data()






	return HttpResponse(content)

def destacado(request):
	# html = "<html><body>Hi there.</body></html>"

	br = mechanize.Browser()

	# Browser options
	br.set_handle_equiv(True)
	br.set_handle_gzip(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)

	# Follows refresh 0 but not hangs on refresh > 0
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

	# Want debugging messages?
	#br.set_debug_http(True)
	#br.set_debug_redirects(True)
	#br.set_debug_responses(True)

	


	r = br.open('https://www.compraspublicas.gob.ec/ProcesoContratacion/compras/CPC/index.cpe').get_data()

	

	#  Ignore robots.txt 
	br.set_handle_robots(False)

	# User-Agent (this is cheating, ok?)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

	soup = BeautifulSoup(r)
	try:
		all_divs  = soup.find_all('iframe',  attrs={"id": "frmFormaBuscar"})
	except IndexError:
		table = "unknown"

	return HttpResponse(all_divs)

	
# 	<div class="destacadoHomeThumb">
#         <img src="http://static.plusvalia.com//fotos/propiedades/b/_221_895740_9783218.jpg?v=2" alt="" />
#     </div>
#                                         <h2>Departamento en Venta en Norte, Quito</h2>
#                                         <h3><div class="overflow-shadow"></div>ANTONIO GRANDA CENTENO</h3>
#                                         <span class="destacadoHomeInfo">
#                                             <span class="destacadoHomePrecio">$ 164.500</span>
#                                         </span>
#                                     </a>
# <!--
#                                     <a href="/propiedades/departamento_venta/elegante-departamento-con-acabados-de-lujo_895740.html" class="destacadoHome" title="Departamento en Venta en Norte, Quito">
#                                         <h2>ELEGANTE DEPARTAMENTO CON ACABADOS DE LUJO</h2>
#                                         <h3>Venta en Norte, Quito, Pichincha</h3>
#                                         <span class="destacadoHomeThumbInfo">
#                                             <img src="http://static.plusvalia.com//fotos/propiedades/l/_221_895740_9783218.jpg?v=2" alt="" />
#                                             <span class="destacadoHomeInfo">
#                                                 <ul>
#                                                     <li>148 m&sup2; totales</li>
#                                                     <li>119 m&sup2; cubiertos</li>
#                                                     <li>3  Habitaciones</li>
#                                                 </ul>
#                                                 <span class="destacadoHomePrecio">$ 164.500</span>
#                                                 <h3 class="destacadoHomeAnunciante">INMOPLUS</h3>
#                                             </span>
#                                         </span>
#                                     </a>



