directory_ground = 'D:\PointClouds\USCAYF20180722f1a1_180722_181152_1_dem_filter_reproject\USCAYF20180722f1a1_180722_181152_1_dem_filter_reproject_segmented_ground.txt';
a = importdata(directory_ground);
close all;

% Set precision levels
 precision1 = .0625;
% precision2 = 10;

% Set height values
heights = a(:,3) ; %a.data(:,3);
minH = min(heights);
heights = heights-minH;
maxH = max(heights);
Intensity = a(:,4);  % a.data(:,5);
maxInt = max(Intensity);
minInt = min(Intensity);

range = maxH-minH;
sizeH=size(heights);

% Set x, y coordinates with two precision levels
minx = min(a(:,1));%min(a.data(:,1));
miny = min(a(:,2));%min(a.data(:,2));
xInd1 = round((a(:,1)-minx)*precision1);
yInd1 = round((a(:,2)-miny)*precision1);
% xInd2 = round((a(:,1)-minx)*precision2);
% yInd2 = round((a(:,2)-miny)*precision2);

% Initialize images
img1 = zeros(max(xInd1)+1,max(yInd1)+1);
imgm = zeros(max(xInd1)+1,max(yInd1)+1);
texture = zeros(max(xInd1)+1,max(yInd1)+1);
%imgnums = zeros(max(xInd1)+1,max(yInd1)+1);
% img2 = zeros(max(xInd2)+1,max(yInd2)+1);
img1 = img1+ 2*maxH; 
% img2 = img2+ 2*maxH; 

imgnorm = zeros(max(xInd1)+1,max(yInd1)+1);

%Produce images
for i=1:size(heights)
    
    x1= xInd1(i)+1;
    y1= yInd1(i)+1;
    texture(x1,y1)=Intensity(i)/maxInt;
    if (img1(x1,y1) > heights(i))
        img1(x1,y1) = heights(i);
    end
    if (imgm(x1,y1) < heights(i))
        imgm(x1,y1) = heights(i);
    end
    
    %imgnorm(x1,y1) = hnorm(i);
%     if (img2(x2,y2) > heights(i))
%         img2(x2,y2) = heights(i)
%     end
end

% Max correction
img1(img1>maxH) = 0;
%img1 = medfilt2(img1,[3,3]);
img1norm = img1./maxH;
% img2(img2>maxH) = 0;

imgdiff = imgm-img1; 
imgdnorm = imgdiff./maxH;
texture2 = imfill(texture,'holes');
texturemed = medfilt2(texture2,[3,3]);


figure('Name','Normalized Bottommap');imshow(img1norm);title('Normalized Bottommap');
figure('Name','Normalized Topmap');imshow(imgdnorm);title(['Normalized Diffmap, max=',num2str(max(max(imgdiff)))]);
%figure;imshow(texture);title('texture');
%figure;imshow(texture2);title('texture filled');
%figure;imshow(texturemed);title('texture median');
%%figure('Name','Normalized Topmap');imshow(imgnums);title('Normalized No. of Returns');
