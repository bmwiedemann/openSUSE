#
# spec file for package jackson-dataformats-binary
#
# Copyright (c) 2024 SUSE LLC
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


%bcond_with extra_dataformats
# Extra formats are disabled because of circular dependencies
Name:           jackson-dataformats-binary
Version:        2.17.3
Release:        0
Summary:        Jackson standard binary data format backends
License:        Apache-2.0 AND BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/FasterXML/jackson-dataformats-binary
Source0:        https://github.com/FasterXML/jackson-dataformats-binary/archive/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations) >= 2.17
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) >= 2.17
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind) >= 2.17
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:) >= 2.17
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildArch:      noarch
%if %{with extra_dataformats}
BuildRequires:  mvn(ch.qos.logback:logback-classic)
BuildRequires:  mvn(com.squareup:protoparser)
BuildRequires:  mvn(org.apache.avro:avro)
BuildRequires:  mvn(org.assertj:assertj-core)
%endif

%description
Parent pom for Jackson binary dataformats.

%if %{with extra_dataformats}
%package -n jackson-dataformat-avro
Summary:        Support for reading and writing AVRO-encoded data via Jackson abstractions
Group:          Development/Libraries/Java

%description -n jackson-dataformat-avro
Jackson extension component for reading and writing data encoded using Apache
Avro data format. Project adds necessary abstractions on top to make things
work with other Jackson functionality. It relies on standard Avro library for
Avro Schema handling, and some parts of deserialization/serialization.

%package -n jackson-dataformat-protobuf
Summary:        Support for reading and writing protobuf-encoded data via Jackson abstractions
Group:          Development/Libraries/Java

%description -n jackson-dataformat-protobuf
Jackson extension component for reading and writing Protobuf encoded data
(see protobuf encoding spec). This project adds necessary abstractions on top
to make things work with other Jackson functionality; mostly just low-level
Streaming components (JsonFactory, JsonParser, JsonGenerator).
%endif

%package -n jackson-dataformat-cbor
Summary:        Support for reading and writing Concise Binary Object Representation
Group:          Development/Libraries/Java

%description -n jackson-dataformat-cbor
Jackson data format module that supports reading and writing CBOR ("Concise
Binary Object Representation") encoded data. Module extends standard Jackson
streaming API (JsonFactory, JsonParser, JsonGenerator), and as such works
seamlessly with all the higher level data abstractions (data binding, tree
model, and pluggable extensions).

%package -n jackson-dataformat-smile
Summary:        Support for reading and writing Smile encoded data using Jackson abstractions
Group:          Development/Libraries/Java

%description -n jackson-dataformat-smile
This Jackson extension handles reading and writing of data encoded in Smile
data format ("binary JSON"). It extends standard Jackson streaming API
(JsonFactory, JsonParser, JsonGenerator), and as such works seamlessly with
all the higher level data abstractions (data binding, tree model, and
pluggable extensions).

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p ion/LICENSE .
cp -p ion/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

%if %{without extra_dataformats}
%pom_disable_module avro
%pom_disable_module protobuf
%endif

# Remove plugins unnecessary for RPM builds
%pom_remove_plugin -r org.moditect:moditect-maven-plugin
%pom_remove_plugin -r :gradle-module-metadata-maven-plugin
%pom_remove_plugin -r :jacoco-maven-plugin

# Deps are not available in packages for this module
%pom_disable_module ion

%{mvn_file} ":{*}" jackson-dataformats/@1

%build
%{mvn_build} -s -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-jackson-dataformats-binary
%doc README.md release-notes/*
%license LICENSE NOTICE

%if %{with extra_dataformats}
%files -n jackson-dataformat-avro -f .mfiles-jackson-dataformat-avro
%doc avro/README.md avro/release-notes/*
%license LICENSE NOTICE

%files -n jackson-dataformat-protobuf -f .mfiles-jackson-dataformat-protobuf
%doc protobuf/README.md protobuf/release-notes/*
%license LICENSE NOTICE
%endif

%files -n jackson-dataformat-cbor -f .mfiles-jackson-dataformat-cbor
%doc cbor/README.md cbor/release-notes/*
%license LICENSE NOTICE

%files -n jackson-dataformat-smile -f .mfiles-jackson-dataformat-smile
%doc smile/README.md smile/release-notes/*
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
