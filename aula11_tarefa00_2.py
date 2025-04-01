d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = {"a": 1, "b": 2}

print(f"Dicionários originais:")
print(f" D1: {d1}")
print(f" D2: {d2}")

d1.update(d2)
d2.update(d3)

print(f"Dicionários atualizados:")
print(f" D1: {d1}")
print(f" D2: {d2}")