#
# spec file for package jackson-databind
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


Name:           jackson-databind
Version:        2.9.4
Release:        0
Summary:        General data-binding package for Jackson (2.x)
License:        Apache-2.0 AND LGPL-2.1-or-later
URL:            https://github.com/FasterXML/jackson-databind/
Source0:        https://github.com/FasterXML/jackson-databind/archive/%{name}-%{version}.tar.gz
# Taken from https://github.com/FasterXML/jackson-databind/commit/6799f8f10cc78e9af6d443ed6982d00a13f2e7d2
Patch0:         CVE-2018-7489.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:) >= %{version}
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(org.apache.bcel:bcel)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildArch:      noarch

%description
The general-purpose data-binding functionality and tree-model for Jackson Data
Processor. It builds on core streaming parser/generator package, and uses
Jackson Annotations for configuration.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%patch0 -p1

# Remove plugins unnecessary for RPM builds
%pom_remove_plugin ":maven-enforcer-plugin"

cp -p src/main/resources/META-INF/LICENSE .
cp -p src/main/resources/META-INF/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

# The package com.sun.org.apache.bcel.internal.util is not present in latest OpenJDK
%pom_add_dep org.apache.bcel:bcel
sed -i 's/com\.sun\.org\.apache\.bcel\.internal\.util/org\.apache\.bcel\.util/g' \
  src/main/java/com/fasterxml/jackson/databind/jsontype/impl/SubTypeValidator.java \
  src/test/java/com/fasterxml/jackson/databind/interop/IllegalTypesCheckTest.java

%{mvn_file} : %{name}

%build
%{mvn_build} -f -- -Dsource=7

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md release-notes/*
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
