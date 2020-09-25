// Fill out your copyright notice in the Description page of Project Settings.


#include "SegmentOutPoints.h"
#include "LidarPointCloud.h"

void USegmentOutPoints::SegmentOutPoints(ULidarPointCloud* Target, FVector BoxCenter, FVector BoxExtent, int32& NumPoints, TArray<FVector>& PointVectors, ULidarPointCloud*& NewPointCloud)
{
	// Get all points in the box
	TArray<FLidarPointCloudPoint> boxPoints;
	boxPoints = Target->GetPointsInBoxAsCopies(BoxCenter, BoxExtent, true, false);
	NumPoints = boxPoints.Num();

	// Construct new point cloud from original point cloud
	TArray<FLidarPointCloudPoint> origPoints;
	origPoints = Target->GetPointsAsCopies(false, 0, Target->GetNumPoints());
	NewPointCloud = ULidarPointCloud::CreateFromData(origPoints, false);

	// Remove points in box
	if (NumPoints > 0)
	{
		for (int32 i = 0; i < boxPoints.Num(); i++)
		{
			PointVectors.Add(boxPoints[i].Location);
		}
	}
	FBox box = FBox(PointVectors);
	NewPointCloud->RemovePointsInBox(box, true);
}