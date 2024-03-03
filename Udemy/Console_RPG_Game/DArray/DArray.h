#pragma once

template <class T>
class DArray
{
  private:
    T** arr;
    unsigned nrOfItems;
    unsigned capacity;

    inline void initialize()
    {
      this->arr = new T*[this->capacity];

      for (T val : this->arr) {
        val = nullptr;
      }
    }

  public:
    DArray<T>()
    {
      this->arr = nullptr;
      this->nrOfItems = 0;
      this->capacity = 0;
    }

    ~DArray<T>()
    {
      for (T val : this->arr)
      {
        delete val;
      }
      delete [] this->arr;
    }

    inline const unsigned& getNrOfItems() { return this->nrOfItems; } const
    inline const unsigned& getCapacity() { return this->capacity; } const

};

