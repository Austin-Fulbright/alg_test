

CC		:= gcc

CFLAGS	:= -Wall -Wextra -g -I.

LDFLAGS	:= -ltinycbor

SRC		:= main.c min_sum_path.c
OBJ		:= $(SRC:.c=.o)
TARGET 	:= test_sum_path

all: $(TARGET)


$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(OBJ) $(TARGET)

