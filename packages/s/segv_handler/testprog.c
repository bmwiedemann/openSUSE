void another_function(int *yy)
{
	/* add some local variables for "bt full" to see */
	int y = 7;
	double foo = 1.2;
	*yy = 2;
}

void foo(int *x)
{
	/* add some local variables for "bt full" to see */
	int foovar = 7;
	double myval = 1.2;
	another_function(x);
}

int main(void)
{
	foo((int *)3);
	return 0;
}
