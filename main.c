#include <stdio.h>


struct Material {
    int material_index;
    char material_name[30];
    float alpha_250;
};


struct Room {
    float room_length;
    float room_width;
    float room_height;
    float room_volume;
};


void calculate_room_volume(struct Room *room) {
    room->room_volume = room->room_length * room->room_width * room->room_height;
}


void update_material(struct Material *mat) {
    mat->alpha_250 = 0.5;
}


void print_material(struct Material *mat) {
    printf("Alpha = %f\n", mat->alpha_250);
    printf("Name of the material is %s", mat->material_name);
}

int main() {
    struct Material material[2];
    for (int i = 0; i < 2; i++) {
        printf("Enter the name of the material number %d\n", i+1);
        scanf("%s", material[i].material_name);
        printf("Enter the alpha coefficient at 250 Hz.\n");
        scanf("%f", &material[i].alpha_250);
    }
    return 0;
}

