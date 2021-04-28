// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "LidarPointCloud.h"
#include "LidarPointCloudComponent.h"

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "SetPointCloudLOD.generated.h"

/**
 * 
 */
UCLASS()
class SILVAN_API USetPointCloudLOD : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
		UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "LOD"))
		static void SetPointCloudLOD(ULidarPointCloudComponent* PointCloudComponent, ULidarPointCloud* PointCloud, int32& numLODs);
};
