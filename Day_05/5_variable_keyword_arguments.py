# **kwargs → Variable Keyword Arguments
# **kwargs lets you pass any number of keyword arguments (key=value format).
# Inside the function, kwargs behaves like a dictionary.
# 👉 Use **kwargs when you don’t know which keyword arguments will be passed.

# def company_info(**kwargs):
#     print("Keyword arguments received:", kwargs)
#     for key in kwargs:
#         print(key, kwargs[key])
# company_info(Ticker="AAPL", CEO="Tim Cook", Revenue="200 Billion", PE=20)

def company_info(**kwargs):
    print("Keyword arguments received:", kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
company_info(Ticker="AAPL", CEO="Tim Cook", Revenue="200 Billion", PE=20, PB=10.20)

