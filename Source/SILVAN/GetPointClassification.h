// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "LidarPointCloudShared.h"
#include "GetPointClassification.generated.h"

/**
 * 
 */
UCLASS()
class SILVAN_API UGetPointClassification : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
		
		UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "Classification"))
		static void GetPointClassification(FLidarPointCloudPoint point, uint8& classification);
};
