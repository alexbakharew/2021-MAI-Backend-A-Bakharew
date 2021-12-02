from collections import OrderedDict

class LRUCache:
  def __init__(self, capacity: int=10) -> None:
    self.capacity_ = capacity
    self.size_ = 0
    self.dict_ = OrderedDict()

    return

  def get(self, key: str) -> str:
    if key in self.dict_:
      return self.dict_[key]
    else:
      return ""

  def set(self, key: str, value: str) -> None:
    if self.size_ == self.capacity_:
      self.dict_.popitem(last=False)
      self.size_ -= 1
    
    self.dict_[key] = value
    self.size_ +=1

    return

  def rem(self, key: str) -> None:
    if key in self.dict_:
      self.dict_.pop(key)
      self.size_ -= 1

    return

def main():
  cache = LRUCache(100)
  cache.set('Jesse', 'Pinkman')
  cache.set('Walter', 'White')
  cache.set('Jesse', 'James')
  print(cache.get('Jesse')) # вернёт 'James'
  cache.rem('Walter')
  print(cache.get('Walter')) # вернёт ''

if __name__ == "__main__":
  main()