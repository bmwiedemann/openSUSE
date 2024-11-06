#
# spec file for package jackson-dataformats-text
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


Name:           jackson-dataformats-text
Version:        2.17.3
Release:        0
Summary:        Jackson standard text-format data format backends
License:        Apache-2.0
URL:            https://github.com/FasterXML/jackson-dataformats-text
Source0:        https://github.com/FasterXML/jackson-dataformats-text/archive/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  jflex
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations) >= 2.17
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) >= 2.17
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind) >= 2.17
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:)
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(org.yaml:snakeyaml)
BuildArch:      noarch

%description
Parent pom for Jackson text-format dataformats.

%package -n jackson-dataformat-csv
Summary:        Support for reading and writing CSV-encoded data via Jackson abstractions

%description -n jackson-dataformat-csv
Jackson data format module for reading and writing CSV encoded data, either
as "raw" data (sequence of String arrays), or via data binding to/from Java
Objects (POJOs).

%package -n jackson-dataformat-properties
Summary:        Support for reading and writing content of "Java Properties" files

%description -n jackson-dataformat-properties
Jackson data format module that supports reading and writing Java Properties
files, using naming convention to determine implied structure (by default
assuming dotted notation, but configurable from non-nested to other
separators).

%package -n jackson-dataformat-yaml
Summary:        Support for reading and writing YAML-encoded data via Jackson abstractions

%description -n jackson-dataformat-yaml
Jackson extension component for reading and writing YAML encoded data.
SnakeYAML library is used for low-level YAML parsing. This project adds
necessary abstractions on top to make things work with other Jackson
functionality.

%package -n jackson-dataformat-toml
Summary:        Support for reading and writing TOML-encoded data via Jackson abstractions

%description -n jackson-dataformat-toml
Jackson extension component for reading and writing TOML encoded data.
This project adds necessary abstractions on top to make things work
with other Jackson functionality.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_remove_plugin -r :gradle-module-metadata-maven-plugin
%pom_remove_plugin -r :moditect-maven-plugin

%pom_remove_plugin :jflex-maven-plugin toml

cp -p yaml/src/main/resources/META-INF/{NOTICE,LICENSE} .
sed -i 's/\r//' LICENSE NOTICE

%{mvn_file} ":{*}" jackson-dataformats/@1

%build
jflex \
    -d toml/src/main/java/com/fasterxml/jackson/dataformat/toml \
    --skel toml/src/main/jflex/skeleton-toml \
    toml/src/main/jflex/com/fasterxml/jackson/dataformat/toml/toml.jflex
%{mvn_build} -sf -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-jackson-dataformats-text
%doc README.md release-notes/*
%license LICENSE NOTICE

%files -n jackson-dataformat-csv -f .mfiles-jackson-dataformat-csv
%doc csv/README.md csv/release-notes/*
%license LICENSE NOTICE

%files -n jackson-dataformat-properties -f .mfiles-jackson-dataformat-properties
%doc properties/README.md properties/release-notes/*
%license LICENSE NOTICE

%files -n jackson-dataformat-yaml -f .mfiles-jackson-dataformat-yaml
%doc yaml/README.md yaml/release-notes/*
%license LICENSE NOTICE

%files -n jackson-dataformat-toml -f .mfiles-jackson-dataformat-toml
%doc toml/README.md
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
