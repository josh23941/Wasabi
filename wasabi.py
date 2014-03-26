'''
Created on Mar 20, 2014

@author: josh23941
'''
from cement.core import foundation
from cement.utils.misc import init_defaults
from wasabi_core.util import load_input
import json
from wasabi_core.request import request_url
from wasabi_core.crawler import get_child_links

def test():
    pass
# set default config options
defaults = init_defaults('myapp')
defaults['myapp']['debug'] = True

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
    
    #load wasabi config json
    app.log.info("Loading Config JSON")
    wasabi_config = json.loads(load_input(app.pargs.config))
    
    # add application logic
    app.log.info("Getting target's child links")
    get_child_links(request_url((wasabi_config['target'].encode('utf-8'))))
   
    ''' KEPT FOR LOGGING REFERENCE
    if app.pargs.foo:
        app.log.info("Received the 'foo' option with value '%s'." % app.pargs.foo)
    else:
        app.log.warn("Did not receive a value for 'foo' option.")
    '''
    
finally:
    # close the application
    app.close()
        