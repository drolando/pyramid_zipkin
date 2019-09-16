# -*- coding: utf-8 -*-
from py_zipkin.testing import MockTransportHandler

from .app import main


def generate_app_main(settings, firehose=False):
    normal_transport = MockTransportHandler()
    firehose_transport = MockTransportHandler()
    app_main = main({}, **settings)
    app_main.registry.settings['zipkin.transport_handler'] = normal_transport
    if firehose:
        app_main.registry.settings['zipkin.firehose_handler'] = firehose_transport
    return app_main, normal_transport, firehose_transport
