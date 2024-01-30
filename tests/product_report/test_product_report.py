from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        id="123",
        product_name="test product",
        company_name="test company",
        manufacturing_date="01/01/2000",
        expiration_date="01/01/2001",
        serial_number="123456",
        storage_instructions="test instructions",
    )

    expected_report = (
        "The product 123 - test product with serial number 123456 "
        "manufactured on 01/01/2000 by the company test company "
        "valid until 01/01/2001 must be stored according to the "
        "following instructions: test instructions."
    )

    assert str(product) == expected_report
