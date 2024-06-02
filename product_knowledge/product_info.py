import requests

product_id = str(input("Enter product id")).strip()
api_url = f"https://dev.shopalyst.com/shopalyst-service/v1/products/{product_id}"
response = requests.get(api_url)
data = response.json()
sku_attributes = {sku["attributes"]["1"]: {"offerPrice": sku["offerPrice"], "skuId": sku["skuId"]} for sku in data["skuSet"]}
matching_attribute_values = [
    {
        **attribute,
        "offerPrice": sku_attributes[attribute["id"]]["offerPrice"],
        "skuId": sku_attributes[attribute["id"]]["skuId"]
    }
    for attribute in data["attributeValues"] if attribute["id"] in sku_attributes
]
output = []
for i, attribute in enumerate(matching_attribute_values, 1):
    product_info = (
        f"Product {i}\n"
        f"skuId : {attribute['skuId']}\n"
        f"shade : {attribute['value']}\n"
        f"offerPrice : {attribute['offerPrice']}\n"
        f"title : {attribute['title']}\n"
        "--------------------------"
    )
    output.append(product_info)
print("\n\n".join(output))


