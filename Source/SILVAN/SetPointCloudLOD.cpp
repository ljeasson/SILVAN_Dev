// Fill out your copyright notice in the Description page of Project Settings.

#include "SetPointCloudLOD.h"
#include "LidarPointCloud.h"
#include "LidarPointCloudComponent.h"

void USetPointCloudLOD::SetPointCloudLOD(ULidarPointCloudComponent* PointCloudComponent, ULidarPointCloud* PointCloud, int32& numLODs)
{
	// Set Point Cloud LOD
	numLODs = PointCloud->GetNumLODs();

}