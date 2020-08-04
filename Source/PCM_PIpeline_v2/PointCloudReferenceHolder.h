// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Containers/Array.h"
#include "LidarPointCloud.h"
#include "LidarPointCloudComponent.h"
#include "PointCloudReferenceHolder.generated.h"

UCLASS()
class PCM_PIPELINE_V2_API APointCloudReferenceHolder : public AActor
{
	GENERATED_BODY()

	UPROPERTY(Category = Collision, VisibleDefaultsOnly)
		class UBoxComponent* ColComp;

	UPROPERTY(Category = Mesh, VisibleDefaultsOnly)
		class UStaticMeshComponent* ObjectComponent;

	UPROPERTY(Category = PointClouds, EditAnywhere)
		TArray<ULidarPointCloud*> pointCloudArray;


	
public:
	// Sets default values for this actor's properties
	APointCloudReferenceHolder();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

	// Add new point cloud to array
	virtual void AddPointCloud(ULidarPointCloud* newPointCloud);

	// Get origin coordinates of point cloud at index
	virtual void GetOrigin(int index);

};
