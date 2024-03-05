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

    inline void expand(const unsigned& factor = 2) 
    {
      T** temp_arr = this->arr;

      this->capacity *= factor;
      this->initialize();

      for (size_t i = 0; i < this->nrOfItems; i++)
      {
        this->arr[i] = temp_arr[i];
      }

      printf("Expanded (%i)\n", this->capacity);
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
      if (index < 0 || index >= this->nrOfItems)
        throw std::out_of_range("Index out of range");

      return *this->arr[index];   
    }

    //Functions
    inline void add(const T& obj)
    {
      if (this->nrOfItems >= this->capacity)
        this->expand();

      this->arr[this->nrOfItems++] = new T(obj);
    }

    inline void remove(const unsigned& index)
    {
      if (index < 0 || index >= this->nrOfItems)
        throw std::out_of_range("Index out of range");
      
      delete this->arr[index];
        
      for (int i = index; i < this->nrOfItems-1; ++i)
      {
        this->arr[i] = this->arr[i+1];
      }

      this->arr[--this->nrOfItems] = nullptr;    
    }
};
