


Mx=[-1,-1,-1;0,0,0;1,1,1];
My=Mx';
%Mx2=[-2,-2,-2,-2,-2;-1,-1,-1,-1,-1;0,0,0,0,0;1,1,1,1,1;2,2,2,2,2];
Mx2=[-1,-1,-1,-1,-1;0,0,0,0,0;0,0,0,0,0;0,0,0,0,0;1,1,1,1,1];
My2=Mx2';


Ix=conv2(img1,Mx,'same');
Iy=conv2(img1,My,'same');

%Ix2=conv2(img1,Mx2,'same');
%Iy2=conv2(img1,My2,'same');


% figure;imshow(Ix);
% figure;imshow(Iy);
Imag=sqrt(Ix.*Ix+Iy.*Iy);
%Imag2=sqrt(Ix2.*Ix2+Iy2.*Iy2);
figure;imshow(Imag./max(max(Imag)));title(['Heightmap Gradient, max= ',num2str(max(max(Imag)))]);
%figure;imshow(Imag2./max(max(Imag2)));title('LOG Heightmap Gradient');

