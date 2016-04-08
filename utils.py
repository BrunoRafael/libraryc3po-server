# coding: utf-8
import database

def generateDatabase():
	#bookId, title, authors, description, imgUrl
	database.saveMessage('456588', )
	database.saveMessage('456998', )
	database.saveMessage('785699',)
	database.saveMessage('786555')
	database.saveMessage('783455')
	database.saveMessage('778555')
	database.saveMessage('986555')
	database.saveMessage('786557')
	database.saveMessage('786500')
	database.saveMessage('786520')

def dataToJson():
	return json.dumps(
        data,
        default=date_handler,
        indent=2,
        separators=(',', ': '),
        ensure_ascii=False
    )