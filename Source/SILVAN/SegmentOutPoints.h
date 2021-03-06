// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "LidarPointCloud.h"
#include "SegmentOutPoints.generated.h"

/**
 * 
 */
UCLASS()
class SILVAN_API USegmentOutPoints : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
	
		UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "Points"))
		static void SegmentOutPoints(ULidarPointCloud* Target, FVector BoxCenter, FVector BoxSize, int32& NumPoints, TArray<FVector>& PointVectors, ULidarPointCloud*& NewPointCloud);
};
