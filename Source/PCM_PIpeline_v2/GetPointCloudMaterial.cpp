// Fill out your copyright notice in the Description page of Project Settings.

#include "GetPointCloudMaterial.h"
#include "LidarPointCloudComponent.h"

void UGetPointCloudMaterial::SetPointCloudMaterial(ULidarPointCloudComponent* PointCloud, UMaterialInterface* Material)
{
	PointCloud->SetMaterial(0, Material);
}

void UGetPointCloudMaterial::GetPointCloudMaterial(ULidarPointCloudComponent* PointCloud, UMaterialInterface*& Material)
{
	Material = PointCloud->GetMaterial(0);
}