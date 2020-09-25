// Fill out your copyright notice in the Description page of Project Settings.


#include "SegmentInPoints.h"
#include "LidarPointCloud.h"

void USegmentInPoints::SegmentInPoints(ULidarPointCloud* Target, FVector BoxCenter, FVector BoxExtent, int32& NumPoints, TArray<FVector>& PointVectors, ULidarPointCloud* &NewPointCloud)
{
	// Get all points in the box
	TArray<FLidarPointCloudPoint> boxPoints;
	boxPoints = Target->GetPointsInBoxAsCopies(BoxCenter, BoxExtent, true, false);
	NumPoints = boxPoints.Num();

	// Construct new point cloud with isolated points
	NewPointCloud = ULidarPointCloud::CreateFromData(boxPoints, false);
	//NewPointCloud->OriginalCoordinates = Target->OriginalCoordinates;
}

