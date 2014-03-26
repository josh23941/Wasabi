'''
Created on Mar 20, 2014

@author: josh23941
'''
from cement.core import foundation, hook
from cement.utils.misc import init_defaults
from util import load_input
import json
from request import request_url

# set default config options
defaults = init_defaults('myapp')
defaults['myapp']['debug'] = False
#defaults['myapp']['foo'] = 'bar'

# create an application
app = foundation.CementApp('wasabi', config_defaults=defaults)

# register any framework hook functions after app creation, and before
# app.setup()
'''
def my_hook(app):
    assert app.config.has_key('wasabi', 'foo')

hook.register('post_setup', my_hook)
'''

try:
    # setup the application
    app.setup()

    # add arguments
    app.args.add_argument('-c', '--config', action='store', metavar='STR',
                          help='the configuration file path')
    
    # "run" the app
    #app.log.debug("Config Loaded")
    app.run()
    
    #load wasabi config
    wasabi_config = load_input(app.pargs.config)
    wasabi_config_json = json.loads(wasabi_config)
    
    # add application logic
    request_url(wasabi_config_json['target'])
    
    ''' KEPT FOR LOGGING REFERENCE
    if app.pargs.foo:
        app.log.info("Received the 'foo' option with value '%s'." % app.pargs.foo)
    else:
        app.log.warn("Did not receive a value for 'foo' option.")
    '''
    
finally:
    # close the application
    app.close()
        