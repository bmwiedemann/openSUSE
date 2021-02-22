#
# spec file for package hbci4java
#
# Copyright (c) 2021 SUSE LLC
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


Name:           hbci4java
Version:        3.1.53
Release:        0
Summary:        Java online banking client using the HBCI standard
License:        LGPL-2.1-only
Group:          Productivity/Office/Finance
URL:            https://github.com/hbci4j/%{name}
Source:         https://github.com/hbci4j/%{name}/archive/hbci4j-core-%{version}.tar.gz
Patch0:         signed-char.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  java-devel >= 8
BuildRequires:  maven-local
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(org.glassfish.jaxb:jaxb-runtime)
BuildRequires:  mvn(org.jvnet.jaxb2.maven2:maven-jaxb22-plugin)

%description
Fork of HBCI4Java that contains support for chipTAN,
smsTAN, HHD, SEPA and other fixes/enhancements.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description javadoc
Developer documentation of HBCI4Java.

%prep
%setup -q -n %{name}-hbci4j-core-%{version}
%patch0 -p1

# remove prebuilt binaries
rm server/*-bin.zip
rm chipcard/lib/*

# No need of this plugins for rpm build
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :nexus-staging-maven-plugin

%build
pushd chipcard
%make_build
popd

%{mvn_build} -f

%install
%mvn_install
install -Dm0644 chipcard/lib/*.so %{buildroot}%{_jnidir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%{_jnidir}/%{name}

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
