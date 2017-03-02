import os
import json
import logging

import trollius as asyncio
from trollius import From

logger = logging.getLogger(__name__)

frequency = 60
hostname = os.uname()[1].split('.')[0]

@asyncio.coroutine
def get_stats(agent):
    yield From(agent.run_event.wait())

    """
    Configuration file in sentinella-pluging-template/conf/
    when you install yuour plugin this file must be in 
    /etc/sentinella/conf.d/
    """
    config = agent.config['test']
    
    """
    Plugin key is unique in Sentinella if not is valid plugin key
    your metrics never are register.
    """

    plugin_key = config['plugin_key']

    logger.info('starting "get_stats" task for plugin_key "%s"  and host "%s"'.format(plugin_key,hostname))

    while agent.run_event.is_set():
        yield From(asyncio.sleep(frequency))
        try:
            data = {'server_name': hostname,
                    'plugins': {}}
            logger.debug('connecting to data source')
            
            # [START] To be completed with plugin code
            # Here goes your logic
            
            """
            Add dict into list plugins:
            value : Metric value
            type : Metric type (integer,percent,binary)

            Replace metric_1, metric_2, metric_3 to your metrics or add more :)
            """
            data['plugins'].update({"{}".format(plugin_key):{}})

            data['plugins'][plugin_key].update({"metric_1": { "value":100, "type":"integer" }})

            data['plugins'][plugin_key].update({"metric_2": { "value":3.5, "type":"percent" }})

            data['plugins'][plugin_key].update({"metric_3": { "value":1, "type":"binary" }})
                                               

            logger.debug('{}: myplugin={}%'.format(hostname, data))

            yield From(agent.async_push(data))

        except:

            logger.exception('cannot get data source information')

    logger.info('get_stats terminated')
