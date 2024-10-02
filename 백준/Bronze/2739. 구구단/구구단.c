#include <stdio.h>

int main(void) {
	int i = 1, j;
	scanf("%d", &j);
	while (i < 10) {
		printf("%d * %d = %d\n",j, i, j * i);
		i++;
	}
	return 0;
}