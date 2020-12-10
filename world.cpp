#include <iostream>
#include <string>


int main()
{
	int a = 0;
	int b = 1;
    std::string guess = "0";
	std::string number = "5";
	std::string user_answer = "Y";

	while (number != guess)
	{
		a++;

		if (b == 1)
		{
			std::cout << "Guess a number" << std::endl;
		}

		guess = std::to_string(std::cin.get());

		std::cout << number << std::endl;
		std::cout << guess << std::endl;

		if (number == guess)
		{
			std::cout << "Congrats! you guessed right!" << std::endl;
			std::cout << "do you wanna play again? (Y/N)" << std::endl;
			std::string user_input = std::to_string(std::cin.get());

			if (user_input == user_answer) 
			{
				std::string guess = "0";
				b = 1;
				a = 0;
			}
			else
			{
				break;
			}

			
		}

		if (number != guess && a == 3)
		{
			std::cout << "Better luck next time!" << std::endl;
			std::cout << "do you wanna play again? (Y/N)" << std::endl;
			std::string user_input = std::to_string(std::cin.get());

			if (user_input == user_answer)
			{
				std::string guess = "0";
				b = 1;
				a = 0;
			}
			else 
			{
				break;
			}
		}
		b = 3;
	}
}

