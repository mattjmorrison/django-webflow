from django.views.generic.base import View, classonlymethod, update_wrapper
from django.template.loader import add_to_builtins
from django.http import Http404

from sample.views import *

add_to_builtins('sample.templatetags.webflow')

class FlowView(View):

    @classonlymethod
    def as_view(cls, steps, **initkwargs):

        #copied this stuff from Django's View
        for key in initkwargs:
            if key in cls.http_method_names:
                raise TypeError(u"You tried to pass in the %s method name as a "
                                u"keyword argument to %s(). Don't do that."
                                % (key, cls.__name__))
            if not hasattr(cls, key):
                raise TypeError(u"%s() received an invalid keyword %r" % (
                    cls.__name__, key))

        def view(request, step_name=None, *args, **kwargs):
            step_dict = dict(steps)

            #total steps
            total_steps = len(steps)

            #current step
            if not step_name:
                current_step = steps[0][0]
            elif step_name in step_dict:
                current_step = step_name
            else:
                raise Http404

            #find current step's position in flow
            current_position = 0
            for position, (step, _) in enumerate(steps):
                if current_step == step:
                    current_position = position
                    break

            #find prior step in flow or None
            if current_position - 1 >= 0:
                prior_step = steps[current_position - 1][0]
            else:
                prior_step = None

            #find next step in flow or None
            if current_position + 1 < total_steps:
                next_step = steps[current_position + 1][0]
            else:
                next_step = None

            kwargs.update({
                'webflow':{
                    'total_flow_steps': total_steps,
                    'current_flow_step': current_step,
                    'next_flow_step': next_step,
                    'prior_flow_step': prior_step,
                    'steps':[step[0] for step in steps]
                }
            })

            step_class = step_dict[current_step]
            self = step_class(**initkwargs)
            return self.dispatch(request, *args, **kwargs)

        #copied this stuff from Django's View
        update_wrapper(view, cls, updated=())
        update_wrapper(view, cls.dispatch, assigned=())
        return view

class SampleFlow(object):
    steps = (
        ("one", One),
        ("two", Two),
        ("three", Three),
    )

    @property
    def urls(self):
        from django.conf.urls.defaults import patterns, url

        urlpatterns = patterns('',
            url(r'^(?P<step_name>.+)?$', FlowView.as_view(self.steps)),
        )

        return urlpatterns
