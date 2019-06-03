#include <stdio.h>
#include "zipf_generator.h"
#include <iostream>
#include <fstream>

using namespace std;

int main () {
  ZipfGenerator z = ZipfGenerator(0.01, 40359450);
  ofstream f;
  f.open ("zipf.txt");
  for (int i = 0; i < 10000; i++) {
    f << z.Next() << "\n";
  }
  f.close();
  return 0;
}