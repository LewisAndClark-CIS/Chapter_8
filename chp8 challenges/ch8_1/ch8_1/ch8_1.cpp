// ch8_1.cpp
// Jason Nguyen
// 2/12/15
// Critter caretaker

#include "stdafx.h"
#include <iostream>
#include <string>

using namespace std;

class Critter{

	// private
	private:
		string name;
		int hunger = 0;
		int boredom = 0;
		
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

		void eat(){
			int food = 0;
			cout << "How much food would you like to feed the critter(integer num): ";
			cin >> food;
			cout << "Brruppp. Thank you." << endl;
			hunger -= food;
			if (hunger < 0){
				hunger = 0;
			}
			pass_time();
		}

		void play(){
			int fun = 0;
			cout << "How long would you like to play with the critter?(integer num): ";
			cin >> fun;
			cout << "Wheee!" << endl;
			boredom -= fun;
			if (boredom < 0){
				boredom = 0;
			}
			pass_time();
		}

};

int _tmain(int argc, _TCHAR* argv[])
{

	string crit_name = "";

	cout << "What do you want to name your critter?: ";
	getline(cin, crit_name);

	Critter crit(crit_name);

	int choice = 5;

	while (choice != 0){
		cout << "\tCritter Caretaker" << endl << endl;
		cout << "\t0 - Quit" << endl;
		cout << "\t1 - Listen to your critter" << endl;
		cout << "\t2 - Feed your critter" << endl;
		cout << "\t3 - Play with your critter" << endl << endl;

		cout << "Choice: ";
		cin >> choice;

		if (choice == 0){
			cout << "Good-bye." << endl;
		}

		else if (choice == 1){
			crit.talk();
			cin.ignore();
		}

		else if (choice == 2){
			crit.eat();
			cin.ignore();
		}

		else if (choice == 3){
			crit.play();
			cin.ignore();
		}

		else{
			cout << endl << "Sorry, but " << choice << " isn't a valid choice..." << endl;
			cin.ignore();
		}

	}

	cout << endl << endl << "Press the enter key twice to exit...";
	cin.ignore();

	return 0;
}

