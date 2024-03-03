#pragma once

template <class T>
class DArray
{
  private:
    T** arr;
    unsigned nrOfItems;
    unsigned capacity;

  public:
    DArray<T>()
    {
      this->arr = nullptr;
      this->nrOfItems = 0;
      this->capacity = 0;
    }

    unsigned getNrOfItems() { return this->nrOfItems; }
};

