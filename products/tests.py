from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Product, ProductCategory


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store')
        self.assertTemplateUsed(response, 'products/index.html')


class ProductsListViewTestCase(TestCase):

    def test_view(self):
        path = reverse('products:index')
        response = self.client.get(path)

        products = Product.objects.all()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Catalog')
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertEqual(list(response.context_data['object_list']), list(products[:3]))

    # def test_view_with_category(self):
    #     print(Product.objects.all())
    #     print(ProductCategory.objects.all())
    #     category = ProductCategory.objects.first()
    #     path = reverse('products:category', kwargs={'category_id': category.id})
    #     response = self.client.get(path)
    #
    #     products = Product.objects.all()
    #     self.assertEqual(response.status_code, HTTPStatus.OK)
    #     self.assertEqual(response.context_data['title'], 'Store - Catalog')
    #     self.assertTemplateUsed(response, 'products/products.html')
    #     self.assertEqual(
    #         list(response.context_data['object_list']),
    #         list(products.filter(category_id=category.id))
    #     )


