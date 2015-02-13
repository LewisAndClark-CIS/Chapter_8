// ch8_4.cpp 
// Jason Nguyen
// 2/13/15

#include "stdafx.h"
#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <vector>

using namespace std;

class Critter{

	// private
private:
	string name;
	int hunger = (rand() % 10) + 1;;
	int boredom = (rand() % 10) + 1;

	void pass_time(){
		++hunger;
		++boredom;
	}
	// public
public:
	// constructor
	Critter(string crit_name){
		name = crit_name;
	}

	string mood(){
		int unhappiness = hunger + boredom;
		string m = "";
		if (unhappiness < 5){
			m = "happy";
		}
		else if (5 <= unhappiness && unhappiness <= 10){
			m = "okay";
		}
		else if (11 <= unhappiness && unhappiness <= 15){
			m = "frustrated";
		}
		else{
			m = "mad";
		}
		return m;
	}

	void talk(){
		cout << "I'm " << name << " and I feel " << mood() << " now." << endl;
		pass_time();
	}

	void eat(int food = 4){
		cout << "Brruppp. Thank you." << endl;
		hunger -= food;
		if (hunger < 0){
			hunger = 0;
		}
		pass_time();
	}

	void play(int fun = 4){
		cout << "Wheee!" << endl;
		boredom -= fun;
		if (boredom < 0){
			boredom = 0;
		}
		pass_time();
	}

	void back_door(){
		cout << endl << "Name: " << name << endl;
		cout << "Hunger: " << hunger << endl;
		cout << "Boredom: " << boredom << endl << endl;
	}

};

int _tmain(int argc, _TCHAR* argv[])
{
	int num_crit;
	srand((unsigned)time(0));

	cout << "How many critters do you want?: ";
	cin >> num_crit;
	cin.ignore();


	vector<Critter> crit_vec;
	string crit_name = "";
	int choice = -1;

	for (int i = 1; i <= num_crit; i++)
	{
		cout << "What is #" << i << " critter name?: ";
		getline(cin, crit_name);
		crit_vec.push_back(Critter(crit_name));

	}

	while (choice != 0){
		cout << "\tCritters Caretaker" << endl << endl;
		cout << "\t0 - Quit" << endl;
		cout << "\t1 - Listen to your critters" << endl;
		cout << "\t2 - Feed your critters" << endl;
		cout << "\t3 - Play with your critters" << endl << endl;

		cout << "Choice: ";
		cin >> choice;

		if (choice == 0){
			cout << "Good-bye." << endl;
		}

		else if (choice == 1){
			for (int i = 0; i < num_crit; i++)
			{
				crit_vec[i].talk();
			}
			cin.ignore();
		}

		else if (choice == 2){
			for (int i = 0; i < num_crit; i++)
			{
				crit_vec[i].eat();
			}
			cin.ignore();
		}

		else if (choice == 3){
			for (int i = 0; i < num_crit; i++)
			{
				crit_vec[i].play();
			}
			cin.ignore();
		}

		else if (choice == 21){
			for (int i = 0; i < num_crit; i++)
			{
				crit_vec[i].back_door();
			}
		}

		else{
			cout << endl << "Sorry, but " << choice << " isn't a valid choice..." << endl;
			cin.ignore();
		}

	}

	return 0;
}

