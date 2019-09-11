void foo(int *x)
{
	/* add some local variables for "bt full" to see */
	int y = 7;
	double foo = 1.2;
	*x = 2;
}

int main(void)
{
	foo((int *)3);
	return 0;
}
