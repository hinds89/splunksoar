def lab5(current_container_id=None, peer_list_results=None, **kwargs):
    """
    Custom function to parse search results from the server_peer search and store them in a new custom list.
    
    Args:
        current_container_id (CEF type: phantom container id)
        peer_list_results (CEF type: splunk query)
    
    Returns a JSON-serializable object that implements the configured data paths:
        
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    # Write your custom code here...
    phantom.debug(f'current_container_id = {current_container_id}')
    phantom.debug(f'type is = {type(current_container_id)}')
    list_name = f'temp_{current_container_id}'
    
    # clear list if already exists
    # phantom.remove_list(list_name=list_name)
    phantom.debug(peer_list_results[0][0])
    
    # add items to list
    #for item in peer_list_results[0][0]:
    #    value_to_add = [ item['peer'], item['priority'], item['count'] ]
    #    phantom.add_list(list_name=list_name, values=value_to_add)
    #phantom.debug(value_to_add)
    value_to_add = [ peer_list_results[0][0][0]['peer'], peer_list_results[0][0][0]['priority'], peer_list_results[0][0][0]['count'] ]
    phantom.add_list(list_name=list_name, values=value_to_add)
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
