// Fill out your copyright notice in the Description page of Project Settings.


#include "SetPointCloudMaterial.h"

void USetPointCloudMaterial::SetPointCloudMaterial(ULidarPointCloudComponent* PointCloud, UMaterialInterface* Material)
{
	PointCloud->SetMaterial(0, Material);
}

void USetPointCloudMaterial::GetPointCloudMaterial(ULidarPointCloudComponent* PointCloud, UMaterialInterface*& Material)
{
	Material = PointCloud->GetMaterial(0);
}