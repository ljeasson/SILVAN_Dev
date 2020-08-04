// Fill out your copyright notice in the Description page of Project Settings.


#include "PointColor.h"
#include "LidarPointCloudShared.h"

void UPointColor::SetPointColor(FLidarPointCloudPoint target, FColor newColor)
{
	target.Color = newColor;
}

void UPointColor::SetPointCloudColor(ULidarPointCloud *target, FColor newColor)
{
	target->ApplyColorToAllPoints(newColor, true);
}