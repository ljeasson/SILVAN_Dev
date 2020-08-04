// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "SegmentInPoints.generated.h"

/**
 * 
 */
UCLASS()
class PCM_PIPELINE_V2_API USegmentInPoints : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
	
		UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "Points"))
		static void SegmentInPoints(ULidarPointCloud* Target, FVector BoxCenter, FVector BoxSize, int32& NumPoints, TArray<FVector>& PointVectors, ULidarPointCloud*& NewPointCloud);
};
