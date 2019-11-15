#
# spec file for package aws-sdk-java
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%global githash 9883b981ab5103cc6944fbf8f3b973994777350f
Name:           aws-sdk-java
Version:        1.11.3
Release:        0
Summary:        AWS SDK for Java
License:        Apache-2.0 AND SUSE-Public-Domain
Group:          Development/Libraries/Java
URL:            http://aws.amazon.com/sdk-for-java/
Source0:        https://github.com/aws/aws-sdk-java/archive/%{githash}/%{name}-%{githash}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-cbor)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(javax.mail:javax.mail-api)
BuildRequires:  mvn(joda-time:joda-time)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildArch:      noarch

%description
The AWS SDK for Java enables Java developers to easily work with
Amazon Web Services and build scalable solutions with Amazon S3,
Amazon DynamoDB, Amazon Glacier, and more.

%package acm
Summary:        AWS Java SDK for AWS Certificate Manager
Group:          Development/Libraries/Java

%description acm
The AWS Java SDK for AWS Certificate Manager module
holds the client classes that are used for communicating
with AWS Certificate Manager service.

%package api-gateway
Summary:        AWS Java SDK for Amazon API Gateway
Group:          Development/Libraries/Java

%description api-gateway
The AWS Java SDK for Amazon API Gateway module
holds the client classes that are used for
communicating with Amazon API Gateway.

%package applicationautoscaling
Summary:        AWS Java SDK for AWS Application Auto Scaling
Group:          Development/Libraries/Java

%description applicationautoscaling
The AWS Java SDK for AWS Application Auto Scaling module
holds the client classes that are used for communicating
with AWS Application Auto Scaling service.

%package autoscaling
Summary:        AWS Java SDK for Auto Scaling
Group:          Development/Libraries/Java

%description autoscaling
The AWS Java SDK for Auto Scaling module holds the
client classes that are used for communicating with
Auto Scaling Service.

%package bom
Summary:        AWS SDK for Java - BOM
Group:          Development/Libraries/Java

%description bom
The AWS SDK for Java - BOM module holds the
dependency managements for individual Java clients.

%package cloudformation
Summary:        AWS Java SDK for AWS CloudFormation
Group:          Development/Libraries/Java

%description cloudformation
The AWS Java SDK for AWS CloudFormation module holds the
client classes that are used for communicating with
AWS CloudFormation Service.

%package cloudfront
Summary:        AWS Java SDK for Amazon CloudFront
Group:          Development/Libraries/Java

%description cloudfront
The AWS Java SDK for Amazon CloudFront module holds the
client classes that are used for communicating with
Amazon CloudFront Service.

%package cloudhsm
Summary:        AWS Java SDK for the AWS CloudHSM
Group:          Development/Libraries/Java

%description cloudhsm
The AWS Java SDK for AWS CloudHSM holds the client
classes that are used for communicating with the
AWS CloudHSM Service.

%package cloudsearch
Summary:        AWS Java SDK for Amazon CloudSearch
Group:          Development/Libraries/Java

%description cloudsearch
The AWS Java SDK for Amazon CloudSearch module holds the
client classes that are used for communicating with
Amazon CloudSearch Service.

%package cloudtrail
Summary:        AWS Java SDK for AWS CloudTrail
Group:          Development/Libraries/Java

%description cloudtrail
The AWS Java SDK for AWS CloudTrail module holds the
client classes that are used for communicating with
AWS CloudTrail Service.

%package cloudwatch
Summary:        AWS Java SDK for Amazon CloudWatch
Group:          Development/Libraries/Java

%description cloudwatch
The AWS Java SDK for Amazon CloudWatch module holds the
client classes that are used for communicating with
Amazon CloudWatch Service.

%package cloudwatchmetrics
Summary:        CloudWatch Metrics for AWS Java SDK
Group:          Development/Libraries/Java

%description cloudwatchmetrics
This package holds the classes for uploading the
client side metrics collected from AWS Java SDK to
Amazon CloudWatch.

#%% package code-generator

%package codecommit
Summary:        AWS Java SDK for AWS CodeCommit
Group:          Development/Libraries/Java

%description codecommit
The AWS Java SDK for AWS CodeCommit module
holds the client classes that are used for
communicating with AWS CodeCommit.

%package codedeploy
Summary:        AWS Java SDK for AWS CodeDeploy
Group:          Development/Libraries/Java

%description codedeploy
The AWS Java SDK for AWS CodeDeploy module holds the
client classes that are used for communicating with
AWS CodeDeploy Service.

#%% package codegen-maven-plugin

%package codepipeline
Summary:        AWS Java SDK for AWS CodePipeline
Group:          Development/Libraries/Java

%description codepipeline
The AWS Java SDK for AWS CodePipeline module
holds the client classes that are used for
communicating with AWS CodePipeline.

%package cognitoidentity
Summary:        AWS Java SDK for Amazon Cognito Identity
Group:          Development/Libraries/Java

%description cognitoidentity
The AWS Java SDK for Amazon Cognito Identity module holds the
client classes that are used for communicating with
Amazon Cognito Identity Service.

%package cognitoidp
Summary:        AWS Java SDK for Amazon Cognito Identity Provider Service
Group:          Development/Libraries/Java

%description cognitoidp
The AWS Java SDK for Amazon Cognito Identity Provider Service module
holds the client classes that are used for communicating with
Amazon Cognito Identity Provider Service.

%package cognitosync
Summary:        AWS Java SDK for Amazon Cognito Sync
Group:          Development/Libraries/Java

%description cognitosync
The AWS Java SDK for Amazon Cognito Sync module holds the
client classes that are used for communicating with
Amazon Cognito Sync Service.

%package config
Summary:        AWS Java SDK for AWS Config
Group:          Development/Libraries/Java

%description config
The AWS Java SDK for AWS Config module holds the
client classes that are used for communicating with
AWS Config Service.

%package core
Summary:        AWS SDK for Java - Core
Group:          Development/Libraries/Java

%description core
The AWS SDK for Java - Core module holds the classes that
is used by the individual service clients to interact with
Amazon Web Services. Users need to depend on aws-java-sdk
artifact for accessing individual client classes.

%package datapipeline
Summary:        AWS Java SDK for AWS Data Pipeline
Group:          Development/Libraries/Java

%description datapipeline
The AWS Java SDK for AWS Data Pipeline module holds the
client classes that are used for communicating with
AWS Data Pipeline Service.

%package devicefarm
Summary:        AWS Java SDK for AWS Device Farm
Group:          Development/Libraries/Java

%description devicefarm
The AWS Java SDK for AWS Device Farm module
holds the client classes that are used for
communicating with AWS Device Farm.

%package directconnect
Summary:        AWS Java SDK for AWS Direct Connect
Group:          Development/Libraries/Java

%description directconnect
The AWS Java SDK for AWS Direct Connect module holds the
client classes that are used for communicating with
AWS Direct Connect Service.

%package directory
Summary:        AWS Java SDK for AWS Directory Service
Group:          Development/Libraries/Java

%description directory
The AWS Java SDK for AWS Directory Service module
holds the client classes that is used for
communicating with AWS Directory Service.

%package discovery
Summary:        AWS Java SDK for AWS Application Discovery Service
Group:          Development/Libraries/Java

%description discovery
The AWS Java SDK for AWS Application Discovery Service module
holds the client classes that are used for communicating with
AWS Application Discovery Service.

%package dms
Summary:        AWS Java SDK for AWS Database Migration Service
Group:          Development/Libraries/Java

%description dms
The AWS Java SDK for AWS Database Migration Service module
holds the client classes that are used for communicating
with AWS Database Migration Service.

%package dynamodb
Summary:        AWS Java SDK for Amazon DynamoDB
Group:          Development/Libraries/Java

%description dynamodb
The AWS Java SDK for Amazon DynamoDB module holds the
client classes that are used for communicating with
Amazon DynamoDB Service.

%package ec2
Summary:        AWS Java SDK for Amazon EC2
Group:          Development/Libraries/Java

%description ec2
The AWS Java SDK for Amazon EC2 module holds the
client classes that are used for communicating with
Amazon EC2 Service.

%package ecr
Summary:        AWS Java SDK for the Amazon EC2 Container Registry
Group:          Development/Libraries/Java

%description ecr
The AWS Java SDK for the Amazon EC2 Container Registry
holds the client classes that are used for communicating
with the Amazon EC2 Container Registry Service.

%package ecs
Summary:        AWS Java SDK for the Amazon EC2 Container Service
Group:          Development/Libraries/Java

%description ecs
The AWS Java SDK for the Amazon EC2 Container Service
holds the client classes that are used for communicating
with the Amazon EC2 Container Service.

%package efs
Summary:        AWS Java SDK for Amazon Elastic File System
Group:          Development/Libraries/Java

%description efs
The AWS Java SDK for Amazon Elastic File System module
holds the client classes that are used for communicating
with Amazon Elastic File System.

%package elasticache
Summary:        AWS Java SDK for Amazon ElastiCache
Group:          Development/Libraries/Java

%description elasticache
The AWS Java SDK for Amazon ElastiCache module holds the
client classes that are used for communicating with
Amazon ElastiCache Service.

%package elasticbeanstalk
Summary:        AWS Java SDK for AWS Elastic Beanstalk
Group:          Development/Libraries/Java

%description elasticbeanstalk
The AWS Java SDK for AWS Elastic Beanstalk module holds the
client classes that are used for communicating with
AWS Elastic Beanstalk Service.

%package elasticloadbalancing
Summary:        AWS Java SDK for Elastic Load Balancing
Group:          Development/Libraries/Java

%description elasticloadbalancing
The AWS Java SDK for Elastic Load Balancing module holds the
client classes that are used for communicating with
Elastic Load Balancing Service.

%package elasticsearch
Summary:        AWS Java SDK for Amazon Elasticsearch Service
Group:          Development/Libraries/Java

%description elasticsearch
The AWS Java SDK for Amazon Elasticsearch Service module
holds the client classes that are used for communicating
with Amazon Elasticsearch Service.

%package elastictranscoder
Summary:        AWS Java SDK for Amazon Elastic Transcoder
Group:          Development/Libraries/Java

%description elastictranscoder
The AWS Java SDK for Amazon Elastic Transcoder module
holds the client classes that are used for communicating
with Amazon Elastic Transcoder Service.

%package emr
Summary:        AWS Java SDK for Amazon EMR
Group:          Development/Libraries/Java

%description emr
The AWS Java SDK for Amazon EMR module holds the
client classes that are used for communicating
with Amazon Elastic MapReduce Service.

%package events
Summary:        AWS Java SDK for Amazon CloudWatch Events
Group:          Development/Libraries/Java

%description events
The AWS Java SDK for Amazon CloudWatch Events module
holds the client classes that are used for communicating
with Amazon CloudWatch Events Service.

%package gamelift
Summary:        AWS Java SDK for AWS GameLift
Group:          Development/Libraries/Java

%description gamelift
The AWS Java SDK for AWS GameLift module holds the
client classes that are used for communicating with
AWS GameLift service.

%package glacier
Summary:        AWS Java SDK for Amazon Glacier
Group:          Development/Libraries/Java

%description glacier
The AWS Java SDK for Amazon Glacier module holds the
client classes that are used for communicating with
Amazon Glacier Service.

%package iam
Summary:        AWS Java SDK for AWS IAM
Group:          Development/Libraries/Java

%description iam
The AWS Java SDK for AWS IAM module holds the
client classes that are used for communicating with
AWS Identity and Access Management Service.

%package importexport
Summary:        AWS Java SDK for AWS Import/Export
Group:          Development/Libraries/Java

%description importexport
The AWS Java SDK for AWS Import/Export module
holds the client classes that are used
for communicating with AWS Import/Export Service.

%package inspector
Summary:        AWS Java SDK for Amazon Inspector Service
Group:          Development/Libraries/Java

%description inspector
The AWS Java SDK for Amazon Inspector Service module
holds the client classes that are used for communicating with
Amazon Inspector Service.

%package iot
Summary:        AWS Java SDK for AWS IoT
Group:          Development/Libraries/Java

%description iot
The AWS Java SDK for AWS Iot Service module holds the
client classes that are used for communicating with
AWS IoT Service.

%package kinesis
Summary:        AWS Java SDK for Amazon Kinesis
Group:          Development/Libraries/Java

%description kinesis
The AWS Java SDK for Amazon Kinesis module holds the
client classes that are used for communicating with
Amazon Kinesis Service.

%package kms
Summary:        AWS Java SDK for AWS KMS
Group:          Development/Libraries/Java

%description kms
The AWS Java SDK for AWS KMS module holds the
client classes that are used for communicating with
AWS Key Management Service.

%package lambda
Summary:        AWS Java SDK for AWS Lambda
Group:          Development/Libraries/Java

%description lambda
The AWS Java SDK for AWS Lambda module holds the
client classes that are used for communicating with
AWS Lambda Service.

%package logs
Summary:        AWS Java SDK for Amazon CloudWatch Logs
Group:          Development/Libraries/Java

%description logs
The AWS Java SDK for Amazon CloudWatch Logs module
holds the client classes that are used for communicating
with Amazon CloudWatch Logs Service.

%package machinelearning
Summary:        AWS Java SDK for Amazon Machine Learning
Group:          Development/Libraries/Java

%description machinelearning
The AWS Java SDK for Amazon Machine Learning module
holds the client classes that is used for communicating
with Amazon Machine Learning Service.

%package marketplacecommerceanalytics
Summary:        AWS Java SDK for AWS Marketplace Commerce Analytics
Group:          Development/Libraries/Java

%description marketplacecommerceanalytics
The AWS Java SDK for AWS Marketplace Commerce Analytics Service module
holds the client classes that are used for communicating with
AWS Marketplace Commerce Analytics Service.

%package marketplacemeteringservice
Summary:        AWS Java SDK for AWS Marketplace Metering Service
Group:          Development/Libraries/Java

%description marketplacemeteringservice
The AWS Java SDK for AWS Marketplace Metering Service module
holds the client classes that are used for communicating with
AWS Marketplace Metering Service.

%package opsworks
Summary:        AWS Java SDK for AWS OpsWorks
Group:          Development/Libraries/Java

%description opsworks
The AWS Java SDK for AWS OpsWorks module holds the
client classes that are used for communicating with
AWS OpsWorks Service.

%package pom
Summary:        AWS SDK for Java - Parent POM
Group:          Development/Libraries/Java

%description pom
AWS SDK for Java - Parent POM.

%package rds
Summary:        AWS Java SDK for Amazon RDS
Group:          Development/Libraries/Java

%description rds
The AWS Java SDK for Amazon RDS module holds the
client classes that are used for communicating with
Amazon Relational Database Service.

%package redshift
Summary:        AWS Java SDK for Amazon Redshift
Group:          Development/Libraries/Java

%description redshift
The AWS Java SDK for Amazon Redshift module holds the
client classes that are used for communicating with
Amazon Redshift Service.

%package route53
Summary:        AWS Java SDK for Amazon Route53
Group:          Development/Libraries/Java

%description route53
The AWS Java SDK for Amazon Route53 module holds the
client classes that are used for communicating with
Amazon Route53 Service.

%package s3
Summary:        AWS Java SDK for Amazon S3
Group:          Development/Libraries/Java

%description s3
The AWS Java SDK for Amazon S3 module holds the
client classes that are used for communicating with
Amazon Simple Storage Service.

%package ses
Summary:        AWS Java SDK for Amazon SES
Group:          Development/Libraries/Java

%description ses
The AWS Java SDK for Amazon SES module holds the
client classes that are used for communicating with
Amazon Simple Email Service.

%package simpledb
Summary:        AWS Java SDK for Amazon SimpleDB
Group:          Development/Libraries/Java

%description simpledb
The AWS Java SDK for Amazon SimpleDB module holds the
client classes that are used for communicating with
Amazon SimpleDB Service.

%package simpleworkflow
Summary:        AWS Java SDK for Amazon SWF
Group:          Development/Libraries/Java

%description simpleworkflow
The AWS Java SDK for Amazon SWF module holds the
client classes that are used for communicating with
Amazon Simple Workflow Service.

%package sns
Summary:        AWS Java SDK for Amazon SNS
Group:          Development/Libraries/Java

%description sns
The AWS Java SDK for Amazon SNS module holds the
client classes that are used for communicating with
Amazon Simple Notification Service.

%package sqs
Summary:        AWS Java SDK for Amazon SQS
Group:          Development/Libraries/Java

%description sqs
The AWS Java SDK for Amazon SQS module holds the
client classes that are used for communicating with
Amazon Simple Queue Service.

%package ssm
Summary:        AWS Java SDK for the AWS Simple Systems Management (SSM) Service
Group:          Development/Libraries/Java

%description ssm
The AWS Java SDK for AWS Simple Systems Management Service
holds the client classes that are used for communicating
with the AWS Simple Systems Management Service.

%package storagegateway
Summary:        AWS Java SDK for AWS Storage Gateway
Group:          Development/Libraries/Java

%description storagegateway
The AWS Java SDK for AWS Storage Gateway module holds the
client classes that are used for communicating with
AWS Storage Gateway Service.

%package sts
Summary:        AWS Java SDK for AWS STS
Group:          Development/Libraries/Java

%description sts
The AWS Java SDK for AWS STS module holds the
client classes that are used for communicating with
AWS Security Token Service.

%package support
Summary:        AWS Java SDK for AWS Support
Group:          Development/Libraries/Java

%description support
The AWS Java SDK for AWS Support module holds the
client classes that are used for communicating with
AWS Support Service.

#%% package swf-libraries

%package test-utils
Summary:        AWS SDK for Java - Test Utils
Group:          Development/Libraries/Java

%description test-utils
The AWS SDK for Java - Test Utils module holds the
all the utilities that are used by the tests.

%package waf
Summary:        AWS Java SDK for AWS WAF
Group:          Development/Libraries/Java

%description waf
The AWS Java SDK for AWS WAF Service module holds the
client classes that are used for communicating with
AWS WAF Service.

%package workspaces
Summary:        AWS Java SDK for Amazon WorkSpaces
Group:          Development/Libraries/Java

%description workspaces
The AWS Java SDK for Amazon WorkSpaces module holds the
client classes that are used for communicating with
Amazon WorkSpaces Service.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{githash}

# Remove deprecated httpclient annotations
sed -i '/NotThreadSafe/d' \
 aws-java-sdk-cloudwatchmetrics/src/main/java/com/amazonaws/metrics/internal/cloudwatch/CloudWatchMetricConfig.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/AmazonWebServiceRequest.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/ApacheHttpClientConfig.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/ClientConfiguration.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/DefaultRequest.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/RequestClientOptions.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/http/ExecutionContext.java \
 aws-java-sdk-core/src/test/java/com/amazonaws/http/response/HttpResponseProxy.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/event/ProgressInputStream.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/internal/ReleasableInputStream.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/internal/ResettableInputStream.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/metrics/ServiceLatencyProvider.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/AWSRequestMetrics.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/AWSRequestMetricsFullSupport.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/LengthCheckInputStream.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/TimingInfo.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/TimingInfoFullSupport.java

sed -i '/ThreadSafe/d' \
 aws-java-sdk-autoscaling/src/main/java/com/amazonaws/services/autoscaling/AmazonAutoScalingAsyncClient.java \
 aws-java-sdk-autoscaling/src/main/java/com/amazonaws/services/autoscaling/AmazonAutoScalingClient.java \
 aws-java-sdk-cloudwatchmetrics/src/main/java/com/amazonaws/metrics/internal/cloudwatch/MetricCollectorSupport.java \
 aws-java-sdk-cloudwatchmetrics/src/main/java/com/amazonaws/metrics/internal/cloudwatch/PredefinedMetricTransformer.java \
 aws-java-sdk-cloudwatchmetrics/src/main/java/com/amazonaws/metrics/internal/cloudwatch/RequestMetricCollectorSupport.java \
 aws-java-sdk-cloudwatchmetrics/src/main/java/com/amazonaws/metrics/internal/cloudwatch/ServiceMetricCollectorSupport.java \
 aws-java-sdk-cloudwatchmetrics/src/main/java/com/amazonaws/metrics/internal/cloudwatch/provider/transform/DynamoDBRequestMetricTransformer.java \
 aws-java-sdk-codecommit/src/main/java/com/amazonaws/services/codecommit/AWSCodeCommitAsyncClient.java \
 aws-java-sdk-codecommit/src/main/java/com/amazonaws/services/codecommit/AWSCodeCommitClient.java \
 aws-java-sdk-codedeploy/src/main/java/com/amazonaws/services/codedeploy/AmazonCodeDeployAsyncClient.java \
 aws-java-sdk-codedeploy/src/main/java/com/amazonaws/services/codedeploy/AmazonCodeDeployClient.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/http/AmazonHttpClient.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/http/conn/ssl/SdkTLSSocketFactory.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/http/impl/client/HttpRequestNoRetryHandler.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/event/request/Progress.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/event/request/ProgressSupport.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/http/impl/client/SdkHttpRequestRetryHandler.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/LengthCheckInputStream.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/TimingInfoUnmodifiable.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/util/VersionInfoUtils.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/AmazonDynamoDBAsyncClient.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/AmazonDynamoDBClient.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/AmazonDynamoDBStreamsAsyncClient.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/AmazonDynamoDBStreamsClient.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/DynamoDB.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/Index.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/Table.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/BatchGetItemApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/BatchWriteItemApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/DeleteItemApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/GetItemApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/ListTablesApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/PutItemApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/QueryApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/ScanApi.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/document/api/UpdateItemApi.java \
 aws-java-sdk-elasticloadbalancing/src/main/java/com/amazonaws/services/elasticloadbalancing/AmazonElasticLoadBalancingAsyncClient.java \
 aws-java-sdk-elasticloadbalancing/src/main/java/com/amazonaws/services/elasticloadbalancing/AmazonElasticLoadBalancingClient.java \
 aws-java-sdk-elasticsearch/src/main/java/com/amazonaws/services/elasticsearch/AWSElasticsearchAsyncClient.java \
 aws-java-sdk-elasticsearch/src/main/java/com/amazonaws/services/elasticsearch/AWSElasticsearchClient.java \
 aws-java-sdk-elastictranscoder/src/main/java/com/amazonaws/services/elastictranscoder/AmazonElasticTranscoderAsyncClient.java \
 aws-java-sdk-elastictranscoder/src/main/java/com/amazonaws/services/elastictranscoder/AmazonElasticTranscoderClient.java \
 aws-java-sdk-gamelift/src/main/java/com/amazonaws/services/gamelift/AmazonGameLiftAsyncClient.java \
 aws-java-sdk-gamelift/src/main/java/com/amazonaws/services/gamelift/AmazonGameLiftClient.java \
 aws-java-sdk-s3/src/main/java/com/amazonaws/services/s3/internal/FileLocks.java \
 aws-java-sdk-ssm/src/main/java/com/amazonaws/services/simplesystemsmanagement/AWSSimpleSystemsManagementAsyncClient.java \
 aws-java-sdk-ssm/src/main/java/com/amazonaws/services/simplesystemsmanagement/AWSSimpleSystemsManagementClient.java \
 aws-java-sdk-storagegateway/src/main/java/com/amazonaws/services/storagegateway/AWSStorageGatewayAsyncClient.java \
 aws-java-sdk-storagegateway/src/main/java/com/amazonaws/services/storagegateway/AWSStorageGatewayClient.java

sed -i '/Immutable/d' \
 aws-java-sdk-cloudfront/src/main/java/com/amazonaws/auth/PEMObject.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/event/ProgressEvent.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/auth/profile/internal/Profile.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/retry/RetryPolicy.java \
 aws-java-sdk-core/src/main/java/com/amazonaws/retry/internal/AuthRetryParameters.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/ArrayIndexElement.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/B.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/BOOL.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/BS.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/GetItemExpressionSpec.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/L.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/M.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/N.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/NamedElement.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/NS.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/NULL.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/Path.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/PathOperand.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/Precedence.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/RemoveAction.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/S.java \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/xspec/SS.java \
 aws-java-sdk-s3/src/main/java/com/amazonaws/services/s3/internal/S3V4AuthErrorRetryStrategy.java \
 aws-java-sdk-s3/src/main/java/com/amazonaws/services/s3/model/InstructionFileId.java \
 aws-java-sdk-s3/src/main/java/com/amazonaws/services/s3/model/S3ObjectId.java

sed -i '/GuardedBy/d' \
 aws-java-sdk-dynamodb/src/main/java/com/amazonaws/services/dynamodbv2/datamodeling/DynamoDBReflector.java \
 aws-java-sdk-s3/src/main/java/com/amazonaws/services/s3/internal/crypto/MultipartUploadCryptoContext.java

%pom_remove_plugin -r com.github.siom79.japicmp:japicmp-maven-plugin

# Disable building of super-JAR
%pom_disable_module aws-java-sdk-osgi
# Missing dependency: aspectj{rt,-maven-plugin}
%pom_disable_module aws-java-sdk-swf-libraries
# Missing dependency: org.eclipse:text:3.3.0-v20070606-0010
%pom_disable_module aws-java-sdk-code-generator
# Missing dependency: :aws-java-sdk-code-generator
%pom_disable_module aws-java-sdk-codegen-maven-plugin

%pom_remove_dep :aws-java-sdk-swf-libraries aws-java-sdk

# Convert from dos to unix line ending
dos2unix src/samples/AmazonEC2SpotInstances-Advanced/CreateSecurityGroupApp.java \
 src/samples/AmazonEC2SpotInstances-Advanced/GettingStartedApp.java \
 src/samples/AmazonEC2SpotInstances-Advanced/InlineGettingStartedCodeSampleApp.java \
 src/samples/AmazonEC2SpotInstances-Advanced/InlineTaggingCodeSampleApp.java \
 src/samples/AmazonEC2SpotInstances-Advanced/Requests.java \
 src/samples/AmazonEC2SpotInstances-GettingStarted/CreateSecurityGroupApp.java \
 src/samples/AmazonEC2SpotInstances-GettingStarted/InlineGettingStartedCodeSampleApp.java \
 src/samples/AmazonEC2SpotInstances-GettingStarted/Requests.java \
 src/samples/AmazonKinesisFirehose/batchPutInput.txt \
 src/samples/AmazonKinesisFirehose/putRecordInput.txt \
 src/samples/AwsCloudFormation/CloudFormationSample.java \
 src/samples/AwsCloudFormation/CloudFormationSample.template

# Generate javadoc with source level 1.6 to avoid complaints
# about "_" being used as identifier with newer OpenJDK versions.
%pom_xpath_inject pom:project/pom:properties "<source>1.6</source>"

%build
# Tests require networking and unavailable test deps:
# com.github.tomakehurst:wiremock:1.55
# nl.jqno.equalsverifier:equalsverifier:1.7.5
%{mvn_build} -sf

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-aws-java-sdk
%doc src/samples/AmazonKinesis

%files acm -f .mfiles-aws-java-sdk-acm

%files api-gateway -f .mfiles-aws-java-sdk-api-gateway

%files applicationautoscaling -f .mfiles-aws-java-sdk-applicationautoscaling

%files autoscaling -f .mfiles-aws-java-sdk-autoscaling

%files bom -f .mfiles-aws-java-sdk-bom
%license LICENSE.txt NOTICE.txt

%files cloudformation -f .mfiles-aws-java-sdk-cloudformation
%doc src/samples/AwsCloudFormation

%files cloudfront -f .mfiles-aws-java-sdk-cloudfront

%files cloudhsm -f .mfiles-aws-java-sdk-cloudhsm

%files cloudsearch -f .mfiles-aws-java-sdk-cloudsearch

%files cloudtrail -f .mfiles-aws-java-sdk-cloudtrail

%files cloudwatch -f .mfiles-aws-java-sdk-cloudwatch

%files cloudwatchmetrics -f .mfiles-aws-java-sdk-cloudwatchmetrics
#%% files code-generator -f .mfiles-aws-java-sdk-code-generator
%files codecommit -f .mfiles-aws-java-sdk-codecommit

%files codedeploy -f .mfiles-aws-java-sdk-codedeploy
#%% files codegen-maven-plugin -f .mfiles-aws-java-sdk-codegen-maven-plugin
%files codepipeline -f .mfiles-aws-java-sdk-codepipeline

%files cognitoidentity -f .mfiles-aws-java-sdk-cognitoidentity

%files cognitoidp -f .mfiles-aws-java-sdk-cognitoidp

%files cognitosync -f .mfiles-aws-java-sdk-cognitosync

%files config -f .mfiles-aws-java-sdk-config

%files core -f .mfiles-aws-java-sdk-core
%doc README.md
%license LICENSE.txt NOTICE.txt

%files datapipeline -f .mfiles-aws-java-sdk-datapipeline

%files devicefarm -f .mfiles-aws-java-sdk-devicefarm

%files directconnect -f .mfiles-aws-java-sdk-directconnect

%files directory -f .mfiles-aws-java-sdk-directory

%files discovery -f .mfiles-aws-java-sdk-discovery

%files dms -f .mfiles-aws-java-sdk-dms

%files dynamodb -f .mfiles-aws-java-sdk-dynamodb
%doc src/samples/AmazonDynamoDB*

%files ec2 -f .mfiles-aws-java-sdk-ec2
%doc src/samples/AmazonEC2*

%files ecr -f .mfiles-aws-java-sdk-ecr

%files ecs -f .mfiles-aws-java-sdk-ecs

%files efs -f .mfiles-aws-java-sdk-efs

%files elasticache -f .mfiles-aws-java-sdk-elasticache

%files elasticbeanstalk -f .mfiles-aws-java-sdk-elasticbeanstalk

%files elasticloadbalancing -f .mfiles-aws-java-sdk-elasticloadbalancing

%files elasticsearch -f .mfiles-aws-java-sdk-elasticsearch

%files elastictranscoder -f .mfiles-aws-java-sdk-elastictranscoder

%files emr -f .mfiles-aws-java-sdk-emr

%files events -f .mfiles-aws-java-sdk-events

%files gamelift -f .mfiles-aws-java-sdk-gamelift

%files glacier -f .mfiles-aws-java-sdk-glacier

%files iam -f .mfiles-aws-java-sdk-iam

%files importexport -f .mfiles-aws-java-sdk-importexport

%files inspector -f .mfiles-aws-java-sdk-inspector

%files iot -f .mfiles-aws-java-sdk-iot

%files kinesis -f .mfiles-aws-java-sdk-kinesis
%doc src/samples/AmazonKinesisFirehose
# src/samples/AmazonKinesis require not available https://github.com/awslabs/amazon-kinesis-client

%files kms -f .mfiles-aws-java-sdk-kms

%files lambda -f .mfiles-aws-java-sdk-lambda

%files logs -f .mfiles-aws-java-sdk-logs

%files machinelearning -f .mfiles-aws-java-sdk-machinelearning

%files marketplacecommerceanalytics -f .mfiles-aws-java-sdk-marketplacecommerceanalytics

%files marketplacemeteringservice -f .mfiles-aws-java-sdk-marketplacemeteringservice

%files opsworks -f .mfiles-aws-java-sdk-opsworks

%files pom -f .mfiles-aws-java-sdk-pom
%license LICENSE.txt NOTICE.txt

%files rds -f .mfiles-aws-java-sdk-rds

%files redshift -f .mfiles-aws-java-sdk-redshift

%files route53 -f .mfiles-aws-java-sdk-route53

%files s3 -f .mfiles-aws-java-sdk-s3
%doc src/samples/AmazonS3*

%files ses -f .mfiles-aws-java-sdk-ses
%doc src/samples/AmazonSimpleEmailService

%files simpledb -f .mfiles-aws-java-sdk-simpledb
%doc src/samples/AwsConsoleApp

%files simpleworkflow -f .mfiles-aws-java-sdk-simpleworkflow

%files sns -f .mfiles-aws-java-sdk-sns

%files sqs -f .mfiles-aws-java-sdk-sqs
%doc src/samples/AmazonSimpleQueueService

%files ssm -f .mfiles-aws-java-sdk-ssm

%files storagegateway -f .mfiles-aws-java-sdk-storagegateway

%files sts -f .mfiles-aws-java-sdk-sts

%files support -f .mfiles-aws-java-sdk-support
#%% files swf-libraries -f .mfiles-aws-java-sdk-swf-libraries
#%% doc src/samples/AwsFlowFramework
%files test-utils -f .mfiles-aws-java-sdk-test-utils

%files waf -f .mfiles-aws-java-sdk-waf

%files workspaces -f .mfiles-aws-java-sdk-workspaces

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
