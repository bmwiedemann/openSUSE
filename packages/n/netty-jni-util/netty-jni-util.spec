#
# spec file for package netty-jni-util
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


%global _lto_cflags %{nil}
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:           netty-jni-util
Version:        0.0.2
Release:        0
Summary:        Helper functions used by netty
License:        Apache-2.0
URL:            https://github.com/netty/%{name}
Source0:        https://github.com/netty/%{name}/archive/%{name}-%{namedversion}.tar.gz
BuildRequires:  cmake >= 2.8.6
BuildRequires:  gcc-c++
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

%description
Helper functions used by netty (and its subprojects) that use JNI.
This is for internal usage only, no guarantees about API is made.

%package sources
Summary:        Helper functions used by netty (sources)
BuildArch:      noarch

%description sources
Helper functions used by netty (and its subprojects) that use JNI.
This is for internal usage only, no guarantees about API is made.

%prep
%setup -q -n %{name}-%{name}-%{namedversion}
mkdir -p build

%mvn_package :::sources: sources

%build
%{mvn_build} -fj -- -Dsource=8
%cmake -DCMAKE_C_STANDARD_LIBRARIES="-ldl"
%make_build

%install
%mvn_install
install -dm 0755 %{buildroot}%{_libdir}/%{name}
install -pm 0644 build/out/libnetty_jni_util.so %{buildroot}%{_libdir}/%{name}/

%files -f .mfiles
%{_libdir}/%{name}
%license LICENSE
%doc README.md

%files sources -f .mfiles-sources

%changelog
