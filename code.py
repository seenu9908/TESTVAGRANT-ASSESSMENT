class Planet:

  def  _init_(self,name, surface_gasses, no_of_moons, has_ring):
    self.name = name
    self.surface_gasses= surface_gasses
    self.no_of_moons = no_of_moons
    self.has_ring = has_ring
  

def count_of_moons(collection):
    count = 0
    for planet in collection:
      if planet.has_ring == "Yes":
        count += planet.no_of_moons
    return count

def gas_retrival(collection):
  gas_count = {}
  for planet in collection:
    if planet.surface_gasses:
      for gas in planet.surface_gasses:
        if gas in gas_count.keys():
          gas_count[gas] += 1
        else:
          gas_count[gas] = 1
  
  maxi = max(list(gas_count.values()))
  for k,v in gas_count.items():
    if v == maxi:
      return k

size = int(input())

collection = []

for i in range(size):
  name = input()
  surface_gasses = input().split(",")
  no_of_moons = int(input())
  rings = input()
  collection.append(Planet(name, surface_gasses, no_of_moons, rings))

print(count_of_moons(collection))

print(gas_retrival(collection))
