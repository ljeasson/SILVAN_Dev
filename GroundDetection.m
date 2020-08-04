directory_ground = 'D:\PointClouds\Plot254\P254_2018_segmented_ground.txt';
output_directory = 'D:\PointClouds\Plot254\';
name = 'segmented_ground_heightmap.png';

limit = 2.5;     % Slope limit
T=zeros(max(xInd1)+1,max(yInd1)+1);
T(Imag>limit)=255;
figure;imshow(T);title(['Gradient Threshold=',num2str(limit)]);
figure;imshow(img1norm);title('normalized image');
imgtnorm=img1norm;
imgtnorm(T==255)=0;
medsize = 3;
imgtmed=medfilt2(imgtnorm,[medsize,medsize]);
figure;imshow(imgtmed);title(['Steep Slope Removed Image Median ',num2str(medsize),'x',num2str(medsize)]);



sigma1 = 3;
imgcompg = imgaussfilt(img1norm,sigma1);

medwindow = [5 5];
imgcompmed = medfilt2(imgcompg,medwindow);   % replaced orignial img1norm


imgtnorm(imgtnorm==0)=imgcompmed(imgtnorm==0);
figure;imshow(imgtnorm);title('Steep Subed with median 7x7');
imgtnorm2=medfilt2(imgtnorm,[3,3]);
figure;imshow(imgtnorm2);title('Heighmap Median 3x3');imwrite(imgtnorm2, [output_directory name '_Heighmap_Median_3x3.png'],'png');
