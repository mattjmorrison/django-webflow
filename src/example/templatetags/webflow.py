from django import template
from django.core.urlresolvers import reverse
register = template.Library()

@register.simple_tag
def webflow_step_url(step_name):
    return reverse('webflow_step', kwargs={'step_name':step_name})

@register.tag(name="webflow_management")
def webflow_management(parser, token):
    return WebflowManagementNode()

class WebflowManagementNode(template.Node):
    def __init__(self):
        self.total_flow_steps = template.Variable('params.webflow.total_flow_steps')

    def render(self, context):
        try:
            return self.total_flow_steps.resolve(context)
        except template.VariableDoesNotExist:
            return ''

@register.tag(name="next_webflow_step")
def next_webflow_step(parser, token):
    return NextWebflowStepNode()

class NextWebflowStepNode(template.Node):
    def __init__(self):
        self.next_step = template.Variable('params.webflow.next_flow_step')

    def render(self, context):
        try:
            return self.next_step.resolve(context)
        except template.VariableDoesNotExist:
            return ''

@register.tag(name="prior_webflow_step")
def prior_webflow_step(parser, token):
    return PriorWebflowStepNode()

class PriorWebflowStepNode(template.Node):
    def __init__(self):
        self.prior_step = template.Variable('params.webflow.prior_flow_step')

    def render(self, context):
        try:
            return self.prior_step.resolve(context)
        except template.VariableDoesNotExist:
            return ''

@register.tag(name="current_webflow_step")
def current_webflow_step(parser, token):
    return CurrentWebflowStepNode()

class CurrentWebflowStepNode(template.Node):
    def __init__(self):
        self.current_step = template.Variable('params.webflow.current_flow_step')

    def render(self, context):
        try:
            return self.current_step.resolve(context)
        except template.VariableDoesNotExist:
            return ''

@register.tag(name="webflow_step_list")
def webflow_step_list(parser, token):
    bits = token.split_contents()
    if len(bits) < 2:
        raise template.TemplateSyntaxError("'%s' takes at least one argument"
                                  " (variable to be created)" % bits[0])

    return WebflowStepListNode(bits[-1])

class WebflowStepListNode(template.Node):
    def __init__(self, asvar):
        self.steps = template.Variable('params.webflow.steps')
        self.asvar = asvar

    def render(self, context):
        try:
            context[self.asvar] = self.steps.resolve(context) 
        except template.VariableDoesNotExist:
            pass

        return ''