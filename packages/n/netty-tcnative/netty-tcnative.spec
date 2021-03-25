#
# spec file for package netty-tcnative
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


%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:           netty-tcnative
Version:        2.0.36
Release:        0
Summary:        Fork of Tomcat Native with improved OpenSSL and mavenized build
License:        Apache-2.0
URL:            https://github.com/netty/netty/wiki/Forked-Tomcat-Native
Source0:        https://github.com/netty/netty-tcnative/archive/%{name}-parent-%{namedversion}.tar.gz
Source1:        fixLibNames.patch.in
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  libtcnative-1-0
BuildRequires:  maven-local
BuildRequires:  mvn(io.netty:netty-jni-util::sources:)
BuildRequires:  mvn(kr.motd.maven:os-maven-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Requires:       libtcnative-1-0

%description
netty-tcnative is a fork of Tomcat Native. It includes a set of changes
contributed by Twitter, Inc, such as:
 *  Simplified distribution and linkage of native library
 *  Complete mavenization of the project
 *  Improved OpenSSL support
To minimize the maintenance burden, we create a dedicated branch for each stable
upstream release and apply our own changes on top of it, while keeping the
number of maintained branches to minimum

%package javadoc
Summary:        API documentation for %{name}
BuildArch:      noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{name}-parent-%{namedversion}
patch=`mktemp`
sed "s;@PATH@;%{_libdir};g" < %{SOURCE1} > $patch
patch -p1 < $patch

# Build only the openssl-dynamic module
%pom_disable_module openssl-static
%pom_disable_module boringssl-static
%pom_disable_module libressl-static

%pom_remove_plugin :japicmp-maven-plugin .
%pom_remove_plugin :maven-enforcer-plugin .
%pom_remove_plugin :maven-antrun-plugin . openssl-dynamic
%pom_remove_plugin :maven-hawtjni-plugin openssl-dynamic
%pom_xpath_remove pom:project/pom:profiles openssl-dynamic

%build
%{mvn_build} -f -- -Dsource=7

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
