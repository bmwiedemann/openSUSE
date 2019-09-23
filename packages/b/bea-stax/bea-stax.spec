#
# spec file for package bea-stax
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define section         free
%global apiver  1.0.1
Name:           bea-stax
Version:        1.2.0
Release:        0
Summary:        Streaming API for XML
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://stax.codehaus.org/Home
# http://dist.codehaus.org/stax/distributions/stax-src-%{version}.zip
Source0:        stax-src-%{version}.zip
# http://dist.codehaus.org/stax/jars/stax-%{version}.pom
Source1:        stax-%{version}.pom
# http://dist.codehaus.org/stax/jars/stax-api-%{apiver}.pom
Source2:        stax-api-%{apiver}.pom
Source10:       http://apache.org/licenses/LICENSE-2.0.txt
Patch0:         bea-stax-target8.patch
Patch2:         bea-stax-gcj-build.patch
BuildRequires:  ant
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  unzip
BuildRequires:  xml-apis
BuildRequires:  xml-resolver
#!BuildIgnore:  antlr
#!BuildIgnore:  antlr-java
Requires:       %{name}-api = %{version}-%{release}
BuildArch:      noarch

%description
The Streaming API for XML (StAX) is a groundbreaking new Java API for
parsing and writing XML easily and efficiently.

%package api
Summary:        The StAX API
Group:          Development/Libraries/Java

%description api
Streaming API for XML

%{summary}

%prep
%setup -q -c
%patch0 -b .target15
%patch2 -b .gcj-build
cp %{SOURCE10} LICENSE

%build
ant all

%install
# jar
install -d -m 0755 %{buildroot}%{_javadir}
install -p -m 0644 build/stax-api-%{apiver}.jar %{buildroot}%{_javadir}/%{name}-api-%{version}.jar
install -p -m 0644 build/stax-%{version}-dev.jar %{buildroot}%{_javadir}/%{name}-ri-%{version}.jar
ln -s %{name}-api-%{version}.jar %{buildroot}%{_javadir}/%{name}-api.jar
ln -s %{name}-ri-%{version}.jar %{buildroot}%{_javadir}/%{name}-ri.jar
# pom
install -d -m 0755 %{buildroot}%{_mavenpomdir}
install -p -m 0644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}-ri-%{version}.pom
%add_maven_depmap %{name}-ri-%{version}.pom %{name}-ri-%{version}.jar
install -p -m 0644 %{SOURCE2} %{buildroot}%{_mavenpomdir}/%{name}-api-%{version}.pom
%add_maven_depmap %{name}-api-%{version}.pom %{name}-api-%{version}.jar -f api -a javax.xml.stream:stax-api

%files
%license LICENSE
%{_javadir}/%{name}-ri-%{version}.jar
%{_javadir}/%{name}-ri.jar
%{_mavenpomdir}/%{name}-ri-%{version}.pom
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}
%else
%{_datadir}/maven-metadata/%{name}.xml*
%endif

%files api
%license LICENSE
%{_javadir}/%{name}-api-%{version}.jar
%{_javadir}/%{name}-api.jar
%{_mavenpomdir}/%{name}-api-%{version}.pom
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}-api
%else
%{_datadir}/maven-metadata/%{name}-api.xml*
%endif

%changelog
