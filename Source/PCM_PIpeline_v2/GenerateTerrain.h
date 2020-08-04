// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "GenerateTerrain.generated.h"

/**
 * 
 */
UCLASS()
class PCM_PIPELINE_V2_API UGenerateTerrain : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()

		UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "Terrain"))
		static bool GenerateTerrain();
	
};
