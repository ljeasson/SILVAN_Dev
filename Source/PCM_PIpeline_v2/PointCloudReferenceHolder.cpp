// Fill out your copyright notice in the Description page of Project Settings.

#include "PointCloudReferenceHolder.h"
#include "Containers/Array.h"

// Sets default values
APointCloudReferenceHolder::APointCloudReferenceHolder()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
	
}

// Called when the game starts or when spawned
void APointCloudReferenceHolder::BeginPlay()
{
	Super::BeginPlay();


}

// Called every frame
void APointCloudReferenceHolder::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}

// Add new point cloud to array
void APointCloudReferenceHolder::AddPointCloud(ULidarPointCloud* newPointCloud)
{
	pointCloudArray.Add(newPointCloud);
	GEngine->AddOnScreenDebugMessage(-1, 5.f, FColor::Cyan, TEXT("New Point Cloud Added"));
}

// Get origin coordinates of point cloud at index
void APointCloudReferenceHolder::GetOrigin(int index)
{
	//ULidarPointCloud* pointCloud = pointCloudArray.GetData(index);
}

