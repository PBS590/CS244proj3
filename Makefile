# *****************************************************
# Variables to control Makefile operation

CXX=g++
RM=rm -f
CPPFLAGS = -g -Wall -pedantic -O0 -std=c++11 -D_GLIBCXX_USE_NANOSLEEP -D_GLIBCXX_USE_SCHED_YIELD -I/usr/local/include/ -pthread
LDFLAGS = -L/usr/local/lib

# *****************************************************
# Targets and files

PROGRAMS = main.cc
HEADERS = zipf_generator.h
SOURCES = $(PROGRAMS)
OBJECTS = $(SOURCES:.cc=.o)
TARGETS = $(PROGRAMS:.cc=)

default: $(TARGETS)

main: main.o
	$(CXX) $(CPPFLAGS) -o $@ $^ $(LDFLAGS) $(LDLIBS)

all: main

# Makefile.dependencies:: $(SOURCES) $(HEADERS)
#   $(CXX) $(CPPFLAGS) -MM $(SOURCES) > Makefile.dependencies

# -include Makefile.dependencies

# ****************************************************
# Clean

.PHONY: clean

clean:
	$(RM) *.pb.*  *.o $(TARGETS) $(OBJECTS)