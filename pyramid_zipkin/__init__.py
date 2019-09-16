# -*- coding: utf-8 -*-
import pyramid.config
from pyramid.tweens import EXCVIEW


def includeme(config):  # pragma: no cover
    # type: (pyramid.config.Configurator) -> None
    config.add_tween('pyramid_zipkin.tween.zipkin_tween', over=EXCVIEW)
