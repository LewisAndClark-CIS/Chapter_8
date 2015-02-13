// ch8_2.cpp 
// Jason Nguyen
// 2/12/15

#include "stdafx.h"
#include <iostream>

using namespace std;

class Television
{
	private:
		int channel = 1;
		int volume = 1;

	public:
		void volume_change(int volume_num)
		{
			volume += volume_num;
		}

		void channel_change(int channel_num)
		{
			channel += channel_num;
		}
		int get_volume(){
			return volume;
		}
		int get_channel(){
			return channel;
		}
		int check_volume(int number)
		{
			if (volume + number > 100 || volume + number < 1)
			{
				return 1;
			}
			else
			{
				return 0;
			}
		}
		int check_channel(int number)
		{
			if (channel + number > 100 || channel + number < 1)
			{
				return 1;
			}
			else
			{
				return 0;
			}
		}
};

int _tmain(int argc, _TCHAR* argv[])
{
	Television tv;
	bool off = 0;
	int choice = 0;
	int number = 0;
	
	while (off != 1)
	{
		cout << "\tMenu" << endl;
		cout << "\t0 - Quit" << endl;
		cout << "\t1 - Change volume" << endl;
		cout << "\t2 - Change channel" << endl << endl;

		cout << "Your choice: ";
		cin >> choice;

		if (choice == 0)
		{
			off = 1;
		}

		else if (choice == 1)
		{
			cout << "Your current volume level is: " << tv.get_volume() << endl;
			cout << "How many volume levels would you like to advance(or de-advance using a negative number): ";
			cin >> number;
			if (tv.check_volume(number) == 1)
			{
				cout << "Can't add " << number << " to volume level " << tv.get_volume() << endl;
			}
			else
			{
				tv.volume_change(number);
			}

		}
		else if (choice == 2)
		{
			cout << "Your current channel level is: " << tv.get_channel() << endl;
			cout << "How many volume levels would you like to advance(or de-advance using a negative number): ";
			cin >> number;
			if (tv.check_volume(number) == 1)
			{
				cout << "Can't add " << number << " to channel level " << tv.get_channel() << endl;
			}
			else
			{
				tv.channel_change(number);
			}

		}
	}
	return 0;
}
