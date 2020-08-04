// Fill out your copyright notice in the Description page of Project Settings.


#include "GenerateTerrain.h"
#include "GenericPlatform/GenericPlatformFile.h"
#include "GenericPlatform/GenericPlatformProcess.h"
#include "Misc/Paths.h"
#include "Misc/FileHelper.h"
#include "HAL/FileManagerGeneric.h"

bool UGenerateTerrain::GenerateTerrain()
{
	// 
	FGenericPlatformProcess::CreateProc(TEXT("python 'D:\\Users\\Lee\\Unreal Projects\\PCM_PIpeline_v2\\pointcloud_to_raster_fast.py' D:\\PointClouds\\Plot237\\P237_2018.las"), 
										nullptr, true, false, false, nullptr, 0, nullptr, nullptr);

	return 0;
}
