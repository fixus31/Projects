//Georgii Moiseev
#include<iostream>
#include<cmath>
#include<ctime>
#include<cstdlib>
using namespace std;

bool MRT(int, int );
void Input1();

int main()
{
	Input1();
	
	cout<<"\n\n";
	return 0;
}

void Input1()
{
	int p, s;
	cout<<"\n What's your p? ";			//p with ~
	cin>>p;
	cout<<"\n What's your s(prime number with 512 bits)?";
	cin>>s;
	cout<<"\n"<<MRT( p, s);							
}

bool MRT(int p, int s)						//Miller-Rabin Primality-Test
{
	bool check = false;
	int reminder, r, z, a;
	int u = 1;			//exponent
	p--;
	z = p / 2; 
	while(z % 2 == 0)			//finding the divisors (u & r)
	{		 
				z = z / 2;
				u++;
	}
	
	r = p / pow(2, u);			// exponent of a
	srand(time(0));
	
	p++;
	for(int i = 0; i < s; i++)
	{	
		a = rand()%(p-4) + 2;					// Finding a by randomizing s times
		reminder = fmod(pow(a, r), p);
		if(reminder+1 == p ) check = true;		// if reminder + 1 = p, then p is likely prime
		else check = false;						// else p is composite
	}
	
	return check;
	
}
