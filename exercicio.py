def calculate_discount(price, discount_percentage):

    valor_com_desconto = price * discount_percentage / 100
    preco_final_com_desconto = price - valor_com_desconto
    

    return round(preco_final_com_desconto, 2)

