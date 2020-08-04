// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "LidarPointCloudShared.h"
#include "LidarPointCloud.h"
#include "PointColor.generated.h"

/**
 * 
 */
UCLASS()
class PCM_PIPELINE_V2_API UPointColor : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
	UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "Color"))
		static void SetPointColor(FLidarPointCloudPoint target, FColor newColor);

	UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "Color"))
		static void SetPointCloudColor(ULidarPointCloud *target, FColor newColor);
};
