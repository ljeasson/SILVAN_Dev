// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "LidarPointCloudComponent.h"

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "GetPointCloudMaterial.generated.h"

/**
 * 
 */
UCLASS()
class PCM_PIPELINE_V2_API UGetPointCloudMaterial : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
	UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "Material"))
		static void SetPointCloudMaterial(ULidarPointCloudComponent* PointCloud, UMaterialInterface* Material);

	UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "Material"))
		static void GetPointCloudMaterial(ULidarPointCloudComponent* PointCloud, UMaterialInterface*& Material);
};
