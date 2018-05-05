
int convolutionx_y(int n0, int n1, int n2, int n3, int n4, int n5, int n6, int n7, int n8){
//#ifdef __MICROBLAZE__
    int sumx = 0;
    int mask_x[3][3] = { { -1, 0, 1 }, { -2, 0, 2 }, { -1, 0, 1 } };
    int neighborhood[3][3] = {  { n6, n3, n0 }, { n7, n4, n1 }, { n8, n5, n2 } };

    for (int l = 0; l < 3; l++) {
            for (int k = 0; k < 3; k++) {
                    sumx = sumx + neighborhood[k][l] * mask_x[k][l];
            }
    }
    return sumx;
//#endif
}

int convolution_y(int n0,int n1,int n2,int n3,int n4,int n5,int n6, int n7, int n8) {
//#ifdef __MICROBLAZE__
    int sumy = 0;
    int mask_y[3][3] = { { 1, 2, 1 }, { 0, 0, 0 }, { -1, -2, -1 } };
    int neighborhood[3][3] = {  { n6, n3, n0 }, { n7, n4, n1 }, { n8, n5, n2 } };

    for (int l = 0; l < 3; l++) {
            for (int k = 0; k < 3; k++) {
                    sumy = sumy + neighborhood[k][l] * mask_y[k][l];
            }
    }
    return sumy;
//#endif
}

int division(int x,int y)
{
    return (abs(x) + abs(y)) / 4;
}
