// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "LidarPointCloud.h"

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "ExtractPointCloudInfo.generated.h"

/**
 * 
 */
UCLASS()
class SILVAN_API UExtractPointCloudInfo : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
		UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "Point Cloud"))
		static void ExtractPointCloudInfo(ULidarPointCloud* PointCloud, FVector& Origin);

};
