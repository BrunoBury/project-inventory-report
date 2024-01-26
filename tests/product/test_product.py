from inventory_report.product import Product


def test_create_product() -> None:
    product_id = "123"
    product_name = "test product"
    company_name = "test company"
    manufacturing_date = "01/01/2000"
    expiration_date = "01/01/2001"
    serial_number = "123456"
    storage_instructions = "test instructions"

    product = Product(
        id=product_id,
        product_name=product_name,
        company_name=company_name,
        manufacturing_date=manufacturing_date,
        expiration_date=expiration_date,
        serial_number=serial_number,
        storage_instructions=storage_instructions,
    )

    assert product.id == product_id
    assert product.product_name == product_name
    assert product.company_name == company_name
    assert product.manufacturing_date == manufacturing_date
    assert product.expiration_date == expiration_date
    assert product.serial_number == serial_number
    assert product.storage_instructions == storage_instructions


if __name__ == "__main__":
    test_create_product()
