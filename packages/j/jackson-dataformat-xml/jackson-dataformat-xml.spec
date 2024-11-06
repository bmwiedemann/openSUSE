#
# spec file for package jackson-dataformat-xml
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


Name:           jackson-dataformat-xml
Version:        2.17.3
Release:        0
Summary:        Jackson extension component for reading and writing XML encoded data
License:        Apache-2.0
URL:            https://github.com/FasterXML/jackson-dataformat-xml
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:)
BuildRequires:  mvn(com.fasterxml.woodstox:woodstox-core)
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.woodstox:stax2-api)
BuildArch:      noarch

%description
Data format extension for Jackson (http://jackson.codehaus.org)
to offer alternative support for serializing POJOs as XML and
deserializing XML as POJOs. Support implemented on top of Stax API
(javax.xml.stream), by implementing core Jackson Streaming API types
like JsonGenerator, JsonParser and JsonFactory. Some data-binding types
overridden as well (ObjectMapper sub-classed as XmlMapper).

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_remove_plugin :moditect-maven-plugin
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :gradle-module-metadata-maven-plugin

%{mvn_file} ":{*}" jackson-dataformats/@1

%build
%{mvn_build} -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md release-notes/*
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
