// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "SetPointShape.generated.h"

/**
 * 
 */
UCLASS()
class PCM_PIPELINE_V2_API USetPointShape : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
	UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "Point Shape"))
		static void SetPointShape(ULidarPointCloudComponent* PointCloud);

	UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "Point Shape"))
		static void GetPointShape(ULidarPointCloudComponent* PointCloud);
};
