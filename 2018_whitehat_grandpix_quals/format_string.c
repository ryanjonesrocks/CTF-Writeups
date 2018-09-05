#include <sys/types.h>
#include <sys/uio.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int add_log(FILE* f) {
  char line[65536];
  int i = 0, res;
  while (1) {
    res = read(0, &line[i], 1);
    if (res == 0) exit(1);
    i++;
    if (i == 65536) exit(1);
    if (line[i - 1] == '\n') {
      line[i] = '\0';
      break;
    }
  }
  fprintf(f, line);
  return 0;
}


int main(int argc, char const *argv[])
{
  FILE* f;
  f = fopen("/tmp/log", "a+");
  add_log(f);
  fclose(f);
  return 0;
}
