#
# spec file for package protobuf-java
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define tarname protobuf
Name:           protobuf-java
Version:        33.1
Release:        0
Summary:        Java Bindings for Google Protocol Buffers
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/protocolbuffers/protobuf
Source0:        https://github.com/protocolbuffers/protobuf/releases/download/v%{version}/%{tarname}-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/com/google/protobuf/%{name}/4.%{version}/%{name}-4.%{version}.pom
Source2:        https://repo1.maven.org/maven2/com/google/protobuf/%{name}lite/4.%{version}/%{name}lite-4.%{version}.pom
Source3:        https://repo1.maven.org/maven2/com/google/protobuf/%{name}-util/4.%{version}/%{name}-util-4.%{version}.pom
Patch0:         protobuf-java-util-removescope.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  protobuf-devel >= %{version}
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(com.google.errorprone:error_prone_annotations)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(com.google.j2objc:j2objc-annotations)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
Requires:       java >= 1.8
BuildArch:      noarch

%description
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

This package contains the Java bindings.

%package parent
Summary:        Java Bindings for Google Protocol Buffers (parent pom)

%description parent
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

This package contains the parent pom of the Java bindings.

%package bom
Summary:        Java Bindings for Google Protocol Buffers (bom)

%description bom
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. Google uses Protocol Buffers for almost all of its internal
RPC protocols and file formats.

This package contains the bill-of-materials pom of the Java bindings.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{tarname}-%{version}
cp %{SOURCE1} java/core/pom.xml
cp %{SOURCE2} java/lite/pom.xml
cp %{SOURCE3} java/util/pom.xml
%autopatch -p1

pushd java

%pom_disable_module kotlin
%pom_disable_module kotlin-lite
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_xpath_set "pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration/pom:source" "1.8"
%pom_xpath_set "pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration/pom:target" "1.8"

%{mvn_package} :{*}-parent parent
%{mvn_package} :{*}-bom bom

%{mvn_file} :{*} @1
%{mvn_file} :%{name} %{tarname}

popd

%build
pushd java
# Core build
protoc \
  --java_out=core/src/main/java \
  --proto_path=../src \
  --proto_path=core/src/main/resources/google/protobuf \
  core/src/main/resources/google/protobuf/java_features.proto \
  ../src/google/protobuf/any.proto \
  ../src/google/protobuf/api.proto \
  ../src/google/protobuf/descriptor.proto \
  ../src/google/protobuf/duration.proto \
  ../src/google/protobuf/empty.proto \
  ../src/google/protobuf/field_mask.proto \
  ../src/google/protobuf/source_context.proto \
  ../src/google/protobuf/struct.proto \
  ../src/google/protobuf/timestamp.proto \
  ../src/google/protobuf/type.proto \
  ../src/google/protobuf/wrappers.proto \
  ../src/google/protobuf/compiler/plugin.proto
cp \
  ../src/google/protobuf/any.proto \
  ../src/google/protobuf/api.proto \
  ../src/google/protobuf/descriptor.proto \
  ../src/google/protobuf/duration.proto \
  ../src/google/protobuf/empty.proto \
  ../src/google/protobuf/field_mask.proto \
  ../src/google/protobuf/source_context.proto \
  ../src/google/protobuf/struct.proto \
  ../src/google/protobuf/timestamp.proto \
  ../src/google/protobuf/type.proto \
  ../src/google/protobuf/wrappers.proto \
  ../src/google/protobuf/compiler/plugin.proto \
  core/src/main/resources/google/protobuf/
# Lite build
mkdir -p lite/src/main/resources/google/protobuf
mkdir -p lite/src/main/java/com/google/protobuf
# lite sources from lite/BUILD.bazel
cp \
  core/src/main/java/com/google/protobuf/AbstractMessageLite.java \
  core/src/main/java/com/google/protobuf/AbstractParser.java \
  core/src/main/java/com/google/protobuf/AbstractProtobufList.java \
  core/src/main/java/com/google/protobuf/AllocatedBuffer.java \
  core/src/main/java/com/google/protobuf/Android.java \
  core/src/main/java/com/google/protobuf/ArrayDecoders.java \
  core/src/main/java/com/google/protobuf/BinaryReader.java \
  core/src/main/java/com/google/protobuf/BinaryWriter.java \
  core/src/main/java/com/google/protobuf/BooleanArrayList.java \
  core/src/main/java/com/google/protobuf/BufferAllocator.java \
  core/src/main/java/com/google/protobuf/ByteBufferWriter.java \
  core/src/main/java/com/google/protobuf/ByteOutput.java \
  core/src/main/java/com/google/protobuf/ByteString.java \
  core/src/main/java/com/google/protobuf/CanIgnoreReturnValue.java \
  core/src/main/java/com/google/protobuf/CheckReturnValue.java \
  core/src/main/java/com/google/protobuf/CodedInputStream.java \
  core/src/main/java/com/google/protobuf/CodedInputStreamReader.java \
  core/src/main/java/com/google/protobuf/CodedOutputStream.java \
  core/src/main/java/com/google/protobuf/CodedOutputStreamWriter.java \
  core/src/main/java/com/google/protobuf/CompileTimeConstant.java \
  core/src/main/java/com/google/protobuf/DoubleArrayList.java \
  core/src/main/java/com/google/protobuf/ExperimentalApi.java \
  core/src/main/java/com/google/protobuf/ExtensionLite.java \
  core/src/main/java/com/google/protobuf/ExtensionRegistryFactory.java \
  core/src/main/java/com/google/protobuf/ExtensionRegistryLite.java \
  core/src/main/java/com/google/protobuf/ExtensionSchema.java \
  core/src/main/java/com/google/protobuf/ExtensionSchemaLite.java \
  core/src/main/java/com/google/protobuf/ExtensionSchemas.java \
  core/src/main/java/com/google/protobuf/FieldInfo.java \
  core/src/main/java/com/google/protobuf/FieldSet.java \
  core/src/main/java/com/google/protobuf/FieldType.java \
  core/src/main/java/com/google/protobuf/FloatArrayList.java \
  core/src/main/java/com/google/protobuf/GeneratedMessageInfoFactory.java \
  core/src/main/java/com/google/protobuf/GeneratedMessageLite.java \
  core/src/main/java/com/google/protobuf/Generated.java \
  core/src/main/java/com/google/protobuf/InlineMe.java \
  core/src/main/java/com/google/protobuf/IntArrayList.java \
  core/src/main/java/com/google/protobuf/Internal.java \
  core/src/main/java/com/google/protobuf/InvalidProtocolBufferException.java \
  core/src/main/java/com/google/protobuf/IterableByteBufferInputStream.java \
  core/src/main/java/com/google/protobuf/Java8Compatibility.java \
  core/src/main/java/com/google/protobuf/JavaType.java \
  core/src/main/java/com/google/protobuf/LazyField.java \
  core/src/main/java/com/google/protobuf/LazyFieldLite.java \
  core/src/main/java/com/google/protobuf/LazyStringArrayList.java \
  core/src/main/java/com/google/protobuf/LazyStringList.java \
  core/src/main/java/com/google/protobuf/ListFieldSchema.java \
  core/src/main/java/com/google/protobuf/ListFieldSchemaLite.java \
  core/src/main/java/com/google/protobuf/ListFieldSchemas.java \
  core/src/main/java/com/google/protobuf/LongArrayList.java \
  core/src/main/java/com/google/protobuf/ManifestSchemaFactory.java \
  core/src/main/java/com/google/protobuf/MapEntryLite.java \
  core/src/main/java/com/google/protobuf/MapFieldLite.java \
  core/src/main/java/com/google/protobuf/MapFieldSchema.java \
  core/src/main/java/com/google/protobuf/MapFieldSchemaLite.java \
  core/src/main/java/com/google/protobuf/MapFieldSchemas.java \
  core/src/main/java/com/google/protobuf/MessageInfo.java \
  core/src/main/java/com/google/protobuf/MessageInfoFactory.java \
  core/src/main/java/com/google/protobuf/MessageLite.java \
  core/src/main/java/com/google/protobuf/MessageLiteOrBuilder.java \
  core/src/main/java/com/google/protobuf/MessageLiteToString.java \
  core/src/main/java/com/google/protobuf/MessageSchema.java \
  core/src/main/java/com/google/protobuf/MessageSetSchema.java \
  core/src/main/java/com/google/protobuf/MutabilityOracle.java \
  core/src/main/java/com/google/protobuf/NewInstanceSchema.java \
  core/src/main/java/com/google/protobuf/NewInstanceSchemaLite.java \
  core/src/main/java/com/google/protobuf/NewInstanceSchemas.java \
  core/src/main/java/com/google/protobuf/OneofInfo.java \
  core/src/main/java/com/google/protobuf/Parser.java \
  core/src/main/java/com/google/protobuf/PrimitiveNonBoxingCollection.java \
  core/src/main/java/com/google/protobuf/ProtoSyntax.java \
  core/src/main/java/com/google/protobuf/Protobuf.java \
  core/src/main/java/com/google/protobuf/ProtobufArrayList.java \
  core/src/main/java/com/google/protobuf/ProtocolStringList.java \
  core/src/main/java/com/google/protobuf/RawMessageInfo.java \
  core/src/main/java/com/google/protobuf/Reader.java \
  core/src/main/java/com/google/protobuf/RopeByteString.java \
  core/src/main/java/com/google/protobuf/RuntimeVersion.java \
  core/src/main/java/com/google/protobuf/Schema.java \
  core/src/main/java/com/google/protobuf/SchemaFactory.java \
  core/src/main/java/com/google/protobuf/SchemaUtil.java \
  core/src/main/java/com/google/protobuf/SmallSortedMap.java \
  core/src/main/java/com/google/protobuf/StructuralMessageInfo.java \
  core/src/main/java/com/google/protobuf/TextFormatEscaper.java \
  core/src/main/java/com/google/protobuf/UninitializedMessageException.java \
  core/src/main/java/com/google/protobuf/UnknownFieldSchema.java \
  core/src/main/java/com/google/protobuf/UnknownFieldSetLite.java \
  core/src/main/java/com/google/protobuf/UnknownFieldSetLiteSchema.java \
  core/src/main/java/com/google/protobuf/UnmodifiableLazyStringList.java \
  core/src/main/java/com/google/protobuf/UnsafeByteOperations.java \
  core/src/main/java/com/google/protobuf/UnsafeUtil.java \
  core/src/main/java/com/google/protobuf/Utf8.java \
  core/src/main/java/com/google/protobuf/WireFormat.java \
  core/src/main/java/com/google/protobuf/Writer.java \
  lite/src/main/java/com/google/protobuf/
protoc \
  --java_out=lite:lite/src/main/java \
  --proto_path=../src \
  --proto_path=core/src/main/resources/google/protobuf \
  ../src/google/protobuf/any.proto \
  ../src/google/protobuf/api.proto \
  ../src/google/protobuf/descriptor.proto \
  ../src/google/protobuf/duration.proto \
  ../src/google/protobuf/empty.proto \
  ../src/google/protobuf/field_mask.proto \
  ../src/google/protobuf/source_context.proto \
  ../src/google/protobuf/struct.proto \
  ../src/google/protobuf/timestamp.proto \
  ../src/google/protobuf/type.proto \
  ../src/google/protobuf/wrappers.proto
cp \
  ../src/google/protobuf/any.proto \
  ../src/google/protobuf/api.proto \
  ../src/google/protobuf/descriptor.proto \
  ../src/google/protobuf/duration.proto \
  ../src/google/protobuf/empty.proto \
  ../src/google/protobuf/field_mask.proto \
  ../src/google/protobuf/source_context.proto \
  ../src/google/protobuf/struct.proto \
  ../src/google/protobuf/timestamp.proto \
  ../src/google/protobuf/type.proto \
  ../src/google/protobuf/wrappers.proto \
  lite/src/main/resources/google/protobuf/

%{mvn_build} -f -- -Dprotoc=$(type -p protoc)
popd

%install
pushd java
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f java/.mfiles
%license LICENSE

%files bom -f java/.mfiles-bom

%files parent -f java/.mfiles-parent

%files javadoc -f java/.mfiles-javadoc
%license LICENSE

%changelog
