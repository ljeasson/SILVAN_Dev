// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "SetKillZ.generated.h"

/**
 * 
 */
UCLASS()
class PCM_PIPELINE_V2_API USetKillZ : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
	
		UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "Kill"))
		static void SetKillZ(float newKillZ);
};
