"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


def on_start(container):
    phantom.debug('on_start() called')

    # call 'custom_list_enumerate_1' block
    custom_list_enumerate_1(container=container)

    return

def custom_list_enumerate_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("custom_list_enumerate_1() called")

    playbook_input_list_name = phantom.collect2(container=container, datapath=["playbook_input:list_name"])

    parameters = []

    # build parameters list for 'custom_list_enumerate_1' call
    for playbook_input_list_name_item in playbook_input_list_name:
        parameters.append({
            "custom_list": playbook_input_list_name_item[0],
        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="community/custom_list_enumerate", parameters=parameters, name="custom_list_enumerate_1")

    return


def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # This function is called after all actions are completed.
    # summary of all the action and/or all details of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    ################################################################################
    ## Custom Code End
    ################################################################################

    return