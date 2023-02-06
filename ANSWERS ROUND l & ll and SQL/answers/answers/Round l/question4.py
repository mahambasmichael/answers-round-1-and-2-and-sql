def main():
    qty = None
    cost = None
    try:
        qty= fetch_quantity()
    except Exception as e:
        print(e)
        return
    
    try:
        cost = fetch_cost()
    except Exception as e:
        print("Exception in fetch_cost():",e )
        try:
         cost_per_quantity = cost/qty 
    except Exception as e
        print("Exception in cost/qty calculation:", e)