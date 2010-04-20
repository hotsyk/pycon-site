from django.template import RequestContext
from django.shortcuts import render_to_response

__all__ = ('render_to')


def render_to(template_path):
    """
    Expect the dict from view. Render returned dict with
    RequestContext.
    """

    def decorator(func):

        def wrapper(request, *args, **kwargs):
            output = func(request, *args, **kwargs)
            if not isinstance(output, dict):
                return output
            kwargs = {'context_instance': RequestContext(request)}
            output['request'] = request
            if 'MIME_TYPE' in output:
                kwargs['mimetype'] = output.pop('MIME_TYPE')
            if 'TEMPLATE' in output:
                template = output.pop('TEMPLATE')
            else:
                template = template_path
            return render_to_response(template, output, **kwargs)
        return wrapper

    return decorator

