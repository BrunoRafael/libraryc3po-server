# coding: utf-8
import database
import json
import logging

def generateDatabase():
	database.removeAll('Book')
	#bookId, title, authors, description, imgUrl
	database.saveBook('456588', 'Nárnia', {'auth1', 'auth2'}, 22.90, 'Entrando no guarda roupas', 'http://www.hdwallpapers.in/walls/the_chronicles_of_narnia-HD.jpg')
	database.saveBook('456998', 'As raposas do sul', {'Roberto augusto'}, 65.90, 'As raposas mais temidas do universo', 'http://www.fundosanimais.com/1920x1080/raposa-neve.jpg')
	database.saveBook('785699', 'Um sol de manhã', {'Gilliard Pereira'}, 35, 'História de amor entre dois estudantes de engenharia', 'http://falagilson.hp6.com.br/wp-content/uploads/2014/04/sol-manha-800x533.jpg')
	database.saveBook('786555', 'Vencendo as dificuldades da vida', {'Silvio Santos'}, 26.89,'Como vencer e ganhar dinheiro em meio a dificuldade', 'http://nanoincub.com.br/media/k2/items/cache/948378d6a67ac0d7c7c6728581b072ab_XL.jpg')
	database.saveBook('783455', 'O senhor dos anéis - a sociedade do anel', {'J. R. R. Tolkien'}, 26.89, 'O anel que pode destuir tudo', 'http://s30.postimg.org/3vzm2j5w1/o_senhor_dos_aneis_a_sociedade_do_anel_poster_co.png')
	database.saveBook('778555', 'O menino maluquinho', {'Ziraldo'}, 39.89,'Menino maluco que sonha pelos cotovelos', 'http://www.revistagarimpocultural.com.br/wp-content/uploads/2013/06/Menino_Maluquinho_1.jpg')
	database.saveBook('986555', 'Um dia depois de amanhã', {'Carlos Fonseca', 'Elisa smith'}, 58.89, 'A situação do planeta é grave', 'https://upload.wikimedia.org/wikipedia/pt/b/bb/The_day_after_tomorrow_poster_promocional.jpg')
	database.saveBook('786557', 'Anjos e demônios', {'Dan Brown'}, 15.89, 'Uma história oculta nos bastidores do mandato papal', 'https://jovemnerd.com.br/wp-content/uploads/img_anjos_demonios_0310_gde.jpg')
	database.saveBook('786500', 'Picapau - Cataratas do Niágra', {'José das Neves', 'Julio Niagra', 'Carlos Leitão'}, 10,'A descida do picapau nas cataratas do niágra', 'http://img.ibxk.com.br/2014/08/21/21143024923534.jpg?w=1040')
	database.saveBook('786520', 'A pantera cor de rosa', {'Hawley Pratt', 'Friz Freleng'}, 8.99,'As divertidas histórias da pantera em gibi', 'http://publicador.tvcultura.com.br/upload/tvcultura/programas/programa-pantera.jpg')

def dataToJsonString(data):
	return json.dumps(
	        data,
	        default=__date_handler,
	        separators=(',', ': ')
    	);

def __date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()

    return obj