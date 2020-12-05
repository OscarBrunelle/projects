#include <algorithm>
#include <string>
#include <iostream>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    std::string str;
    std::cout << "String: ";
    getline(std::cin, str);

    while (str != "") {
        for(int i(0); i < str.size(); i++) {
            if(rand() % 2 == 1) str[i] = toupper(str[i]);
        }

        std::cout << str << std::endl;
        std::cout << "String: ";
        getline(std::cin, str);
    }

    return 0;
}
