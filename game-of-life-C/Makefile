

CC		:= gcc

CFLAGS	:= -Wall -Wextra -g -I.

LDFLAGS	:= -lcjson

SRC		:= main.c game_of_life.c
OBJ		:= $(SRC:.c=.o)
TARGET 	:= test_life

all: $(TARGET)


$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(OBJ) $(TARGET)

