#include <stdio.h>

int main(void) {
	int i, num, a, b;

	scanf("%d", &i);

	for (num = 1; num <= i; num++) {
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d\n", num, (a + b));

	}
	return 0;
}