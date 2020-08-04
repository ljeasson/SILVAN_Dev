// Fill out your copyright notice in the Description page of Project Settings.


#include "TxtFileManager.h"

void UTxtFileManager::ReadTxtFile(FString directory, TArray<FString>& lines)
{
	FString result;
	IPlatformFile& file = FPlatformFileManager::Get().GetPlatformFile();
	if (file.CreateDirectory(*directory)) {
		FFileHelper::LoadFileToString(result, *directory);
	}

	result.ParseIntoArrayLines(lines);
}