def change(amount):
  assert(amount > 23)
  if amount == 24:
    return [5, 5, 7, 7]
  if amount == 25:
    return [5, 5, 5, 5, 5]
  if amount == 26:
    return [7, 7, 7, 5]
  if amount == 27:
    return [5, 5, 5, 5, 7]
  if amount == 28:
    return [7, 7, 7, 7]
  coins = change(amount - 7)
  coins.append(7)
  return coins

print(change(49))