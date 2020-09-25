// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "LidarPointCloudComponent.h"

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "SetPointCloudMaterial.generated.h"

/**
 * 
 */
UCLASS()
class SILVAN_API USetPointCloudMaterial : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
	
		UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "Material"))
		static void SetPointCloudMaterial(ULidarPointCloudComponent* PointCloud, UMaterialInterface* Material);

		UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "Material"))
		static void GetPointCloudMaterial(ULidarPointCloudComponent* PointCloud, UMaterialInterface*& Material);
};
