CC = gcc
CFLAGS = -Wall -Werror

SRCS = main.c addition.c subtraction.c multiplication.c division.c
OBJS = $(SRCS:.c=.o)
TARGET = calculator

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c operations.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS)