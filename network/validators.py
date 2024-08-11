from rest_framework.exceptions import ValidationError


class SupplierValidator:
    def __call__(self, obj):
        if obj['supplier'] and obj['status'] == 'factory':
            raise ValidationError('Завод не закупает готовую продукцию.')
