#include <stdio.h>

int main(void) {
	int num, j, z;
	j = 0, z = 0;
	scanf("%d", &num);
	while (j < num) {
		z = 0;
		while (z <= j) {
			printf("*");
			z++;
		}
		printf("\n");
		j++;
	}
	return 0;
}