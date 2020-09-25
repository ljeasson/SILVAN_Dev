// Fill out your copyright notice in the Description page of Project Settings.

#include "ExtractPointCloudInfo.h"
#include "LidarPointCloud.h"

void UExtractPointCloudInfo::ExtractPointCloudInfo(ULidarPointCloud* PointCloud, FVector& Origin)
{
	// Get origin at original coordinates
	FDoubleVector OriginalCoords = PointCloud->OriginalCoordinates;
	Origin.X = OriginalCoords.X;
	Origin.Y = OriginalCoords.Y;
	Origin.Z = OriginalCoords.Z;


}