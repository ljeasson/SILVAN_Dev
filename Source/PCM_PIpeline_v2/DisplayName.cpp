// Fill out your copyright notice in the Description page of Project Settings.


#include "DisplayName.h"
#include "LidarPointCloud.h"

void UDisplayName::GetPointCloudName(ULidarPointCloud* Target, FString& name)
{
	name = Target->GetName();
}

void UDisplayName::SetPointCloudName(ULidarPointCloud* Target, FString newName, FString& name)
{
	const TCHAR* newNameChar = *newName;
	Target->Rename(newNameChar);
}