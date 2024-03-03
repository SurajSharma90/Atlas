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

      for (int i = 0; i < this->capacity; ++i)
      {
        this->arr[i] = nullptr;
      }
    }

  public:
    DArray<T>()
    {
      this->arr = nullptr;
      this->nrOfItems = 0;
      this->capacity = 5;

      this->initialize();
    }

    ~DArray<T>()
    {
      for (int i = 0; i < this->nrOfItems; ++i)
      {
        delete this->arr[i];
      }
      delete [] this->arr;
    }

    //Operators


    //G&S
    inline const unsigned& getNrOfItems() { return this->nrOfItems; }
    inline const unsigned& getCapacity() { return this->capacity; }
    inline T& at(const unsigned& index) 
    {
      if (index >= 0 && index < this->nrOfItems)
      {
        return *this->arr[index];
      }
    }

    //Functions
    inline void add(const T& obj)
    {
      if (this->nrOfItems < this->capacity)
      {
        this->arr[this->nrOfItems] = new T(obj);
        ++this->nrOfItems;
      }
    }
};
