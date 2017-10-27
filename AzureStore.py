from azure.storage.queue import QueueService

def sendToQueue(eventData, queueNm):
    queue_service = QueueService(account_name='earthquakehazard', account_key='oZOch+B0LdsPRXCc2AW9u+tcELXfp6TD69Yw2jL4v3ulIbsKHRkS2kNBAl3ASeXR358oC9NAxOgUXXbMUDs2Lg==')
    if queue_service.exists(queueNm.lower()):
        queue_service.put_message(queueNm, unicode(eventData))
    
        
        
            
            

    