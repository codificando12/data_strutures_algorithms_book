"""Had we implemented the scale function (page 25) as follows, does it work
properly?
def scale(data, factor):
for val in data:
val = factor"""
"""It doesn't work properly because at the end gives you None, so we should use for val in range(len(data))"""

def scale(data, factor):
    for val in range(len(data)):
        data[val] *= factor
    return data

print(scale([1, 5, 2], 10))