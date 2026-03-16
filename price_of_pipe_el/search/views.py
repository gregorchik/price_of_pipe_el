from django.views.generic import TemplateView
from product.models import Product
from django.core.paginator import Paginator


class SearchPageView(TemplateView):
    template_name = 'search/search.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_query = self.request.GET.get('category', '').strip()
        diameter_query = self.request.GET.get('diameter_dn', '').strip()
        pressure_query = self.request.GET.get('pressure_pn', '').strip()
        material_query = self.request.GET.get('material', '').strip()
        product_list = Product.objects.all()

        if category_query:
            product_list = product_list.filter(
                category__startswith=category_query.capitalize()
            )
        if diameter_query:
            product_list = product_list.filter(
                diameter_dn=diameter_query
            )
        if pressure_query:
            product_list = product_list.filter(
                pressure_pn=pressure_query
            )
        if material_query:
            product_list = product_list.filter(
                material__startswith=material_query.capitalize()
            )
        paginator = Paginator(product_list, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context
