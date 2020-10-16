// Fill out your copyright notice in the Description page of Project Settings.

#include "GetPointClassification.h"
#include "LidarPointCloudShared.h"


void UGetPointClassification::GetPointClassification(FLidarPointCloudPoint point, uint8& classification)
{
	// Get all points in the box
	classification = point.ClassificationID;
}