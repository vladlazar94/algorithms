#ifdef DEBUG
    #include <iostream>
#endif
#include <vector>

namespace vl{

template<typename T>
class Matrix{

public:
    Matrix(std::vector<std::vector<T>> input):
        rows{input.size()},
        columns{input.front.size()}
    {
        //TODO: verify that all vectors have the same length.

        elements = new T [ rows * columns ];
        //TODO: catch std::bad_alloc exception.

        for(size_t j = 0; j < rows; j++){
            for(size_t i = 0; i < columns; i++){
                elements[columns * i + j] = input[i][j];
            }
        }
    }

    Matrix(size_t n, size_t m):
        rows{n},
        columns{m}
    {
        elements = new T [ rows * columns ];
        //TODO: catch std::bad_alloc exception.
    }
    ~Matrix(){
        delete [] elements;
    }
        

    T& operator()(size_t i, size_t j){

        #ifdef DEBUG
        if(i > collumns - 1 or j > rows - 1 ori < 0 or j < 0 ){
            std::cout << "Segfault!: indexed outside of matrix memory area!" << std::endl;
        }
        #endif

        return elements[columns * i + j];
    }

private:

    const size_t rows;
    const size_t columns;
    T* elements = nullptr;

};

} // End of namespace vl.

