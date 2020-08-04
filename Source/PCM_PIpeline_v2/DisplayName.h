// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "LidarPointCloud.h"
#include "DisplayName.generated.h"

/**
 * 
 */
UCLASS()
class PCM_PIPELINE_V2_API UDisplayName : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
	UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "Name"))
		static void GetPointCloudName(ULidarPointCloud* Target, FString& name);

	UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "Name"))
		static void SetPointCloudName(ULidarPointCloud* Target, FString newName, FString& name);
};
