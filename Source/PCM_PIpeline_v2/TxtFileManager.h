// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "TxtFileManager.generated.h"

/**
 * 
 */
UCLASS()
class PCM_PIPELINE_V2_API UTxtFileManager : public UBlueprintFunctionLibrary
{
    GENERATED_BODY()

    UFUNCTION(BlueprintCallable, Category = "Custom", meta = (Keywords = "Read"))
        static void ReadTxtFile(FString directory, TArray<FString>& lines);

};
