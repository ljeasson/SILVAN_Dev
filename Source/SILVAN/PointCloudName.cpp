// Fill out your copyright notice in the Description page of Project Settings.


#include "PointCloudName.h"
#include "LidarPointCloud.h"

void UPointCloudName::GetPointCloudName(ULidarPointCloud* Target, FString& name)
{
	name = Target->GetName();
}

void UPointCloudName::SetPointCloudName(ULidarPointCloud* Target, FString newName, FString& name)
{
	const TCHAR* newNameChar = *newName;
	Target->Rename(newNameChar);
}