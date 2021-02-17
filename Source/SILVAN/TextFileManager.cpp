// Fill out your copyright notice in the Description page of Project Settings.


#include "TextFileManager.h"
#include "Misc/FileHelper.h"
#include "HAL/PlatformFilemanager.h"

bool UTextFileManager::LoadTextFromFile(FString FileName, TArray<FString>& TextArray, FString& TextString)
{
	
	if (!FPlatformFileManager::Get().GetPlatformFile().FileExists(*FileName))
	{
		GEngine->AddOnScreenDebugMessage(-1, 5.f, FColor::Blue, TEXT("Could not Find File"));
		return false;
	}
	else
	{
		// Convert filepath to character array and save to array
		const TCHAR* FILEPATH = *FileName;
		return FFileHelper::LoadFileToStringArray(TextArray, *FileName);
		//return FFileHelper::LoadFileToString(SaveString, *FileName);
	}
}

bool UTextFileManager::SaveArrayText(FString SaveDirectory, FString FileName, TArray<FString> SaveText, bool AllowOverwriting = false)
{
	// Set complete file path
	SaveDirectory += "\\";
	SaveDirectory += FileName;

	if (!AllowOverwriting)
	{
		if (FPlatformFileManager::Get().GetPlatformFile().FileExists(*SaveDirectory))
		{
			return false;
		}
	}
	
	FPlatformFileManager::Get().GetPlatformFile().DeleteFile(*SaveDirectory);
	FString FinalString = "";
	for (FString& Each : SaveText)
	{
		FinalString += Each;
		FinalString += LINE_TERMINATOR;
	}

	return FFileHelper::SaveStringToFile(FinalString, *SaveDirectory);
	
}

bool UTextFileManager::DeleteTextFile(FString SaveDirectory, FString FileName)
{
	// Set complete file path
	SaveDirectory += "\\";
	SaveDirectory += FileName;

	return FPlatformFileManager::Get().GetPlatformFile().DeleteFile(*SaveDirectory);
}