import pdb


class CustomHtmxMixin:
    def dispatch(self, request, *args, **kwargs):
        # pdb.set_trace()
        self.template_htmx = self.template_name
        if not request.htmx:
            self.template_name = 'common/base_dashboard.html'
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['template_htmx'] = self.template_htmx
        return super().get_context_data(**kwargs)
