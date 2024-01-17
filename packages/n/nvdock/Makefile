CC = gcc
CFLAGS = $(shell pkg-config --cflags gtk+-2.0) ${RPM_OPT_FLAGS}
LDLIBS = $(shell pkg-config --libs gtk+-2.0)

all: nvdock

nvdock: nvdock.o icon.o util.o
