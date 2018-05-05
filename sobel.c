
int main(void){
	static int image[1000][1000];
	static int av;
	static int conv_x;
	static int conv_y;

	for (int i = 0; i < M; i++)
	{
		for(int j=0;j<N;j++){
			readPixel(&image[i][j]);
		}
	}

	for(int i = 1;i < M - 1; i++){
		for(int j=1;j < N - 1; j++){
			conv_x = convolution_x(image[i-1][j-1], image[i][j-1],image[i+1][j-1], 
								   image[i-1][j],image[i][j], image[i+1][j],
								   image[i-1][j+1], image[i][j+1],image[i+1][j+1]);
			conx_y = convolutionx_y(image[i-1][j-1], image[i][j-1],image[i+1][j-1], 
								   image[i-1][j],image[i][j], image[i+1][j],
								   image[i-1][j+1], image[i][j+1],image[i+1][j+1]);
			av = division(conv_x, conx_y);
			writePixel(&av);
			
		}
	}
}