#include <iostream>
#include <list>
#include <algorithm>
#include <chrono>
#include <random>

// Создаем шаблонную функцию customFind для поиска элемента в списке
template <typename T>
typename std::list<T>::iterator customFind(std::list<T>& list, const T& value) {
    for (auto it = list.begin(); it != list.end(); ++it) {
        if (*it == value) {
            return it;
        }
    }
    return list.end();
}

// Создаем шаблонную функцию customFindUserInput для вызова функции customFind с пользовательским вводом
template <typename T>
typename std::list<T>::iterator customFindUserInput(std::list<T>& list, const T& value) {
    return customFind(list, value);
}

int main()
{
    // Создаем список myList и заполняем его числами от 0 до 999999
    std::list<int> myList;
    const int size = 1000000;
    for (int i = 0; i < size; ++i)
    {
        myList.push_back(i);
    }

    // Пользовательский ввод числа для поиска
    int userInput;
    std::cout << "Enter a number to search for: ";
    std::cin >> userInput;

    // Измеряем время выполнения функции customFindUserInput
    {
        auto start = std::chrono::high_resolution_clock::now();
        customFindUserInput(myList, userInput);
        auto end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double, std::micro> time1 = end - start;
        std::cout << "Custom find time: " << time1.count() << " microseconds" << std::endl;
    }

    // Измеряем время выполнения стандартной функции поиска std::find
    {
        auto start2 = std::chrono::high_resolution_clock::now();
        std::find(myList.begin(), myList.end(), userInput);
        auto end2 = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double, std::micro> time2 = end2 - start2;
        std::cout << "find time: " << time2.count() << " microseconds" << std::endl;
    }

    return 0;
}