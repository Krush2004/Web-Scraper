import threading
from request_executor import request_executor
from input_data_cleaners import clean_input_elements_list, clean_input_payloads_list

class CustomThread(threading.Thread):
    
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return


# the main function that performs all the checks, calls other functions and executes them. Basically the core.
def run(url_list:list,
        element_list:list,
        payload_list:list,
        **kwargs
        ):


    if url_list == []:
        return error_handler('no urls')
    elif element_list == [] and 'nullify_elem_error' not in kwargs.keys():
        return error_handler('no elements')
    elif payload_list == []:
        return error_handler('no payloads')
    else:
        pass


    # clean the inputted data
    url_param_list = clean_input_payloads_list(payload_list=payload_list)
    element_with_url_list = clean_input_elements_list(element_list=element_list, url_list=url_list)

    # iterate through the amount of urls
    for n in range(len(url_param_list)):
        url = url_list[n]['url']
        req_type = url_list[n]['request type']

        # check if the two url names match
        if url_param_list[n]['for site'] == url:
            # set element list as empty if no elements are found
            element_with_url_list = element_with_url_list[n] if element_with_url_list != [] else []
            if url_param_list[n]['no parameter']['value'] == 'false':
                # start the thread without any request parameters
                r = CustomThread(target=request_executor, args=(url, url_param_list[n], element_with_url_list, req_type))
                r.start()

            elif url_param_list[n]['no parameter']['value'] == 'true':
                if req_type == 'GET':
                    # start the thread and pass parameters as args
                    r = CustomThread(target=request_executor, args=(url, url_param_list[n], element_with_url_list, req_type))
                    r.start()

                elif req_type == 'POST':
                    return error_handler('no payloads for post')


# takes an error as parameter and returns appropriate error message
def error_handler(type_of_error:str):
    if type_of_error == 'no urls':
        return 'show nan_url error'
    
    elif type_of_error == 'no elements':
        return 'show nan_elems error'
    
    elif type_of_error == 'no payloads':
        return 'show nan_payls error'
    
    elif type_of_error == 'no payloads for post':
        return 'show post_without_payload error'