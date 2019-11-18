#
# spec file for package netty-tcnative
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


%global namedreltag .Fork2
%global namedversion %{version}%{?namedreltag}
Name:           netty-tcnative
Version:        1.1.30
Release:        0
Summary:        Fork of Tomcat Native with improved OpenSSL and mavenized build
License:        Apache-2.0
URL:            https://github.com/netty/netty/wiki/Forked-Tomcat-Native
Source0:        https://github.com/netty/netty-tcnative/archive/%{name}-%{namedversion}.tar.gz
Source1:         fixLibNames.patch.in
Patch2:         i388aprFix.patch
BuildRequires:  apr-devel
BuildRequires:  autoconf fdupes
BuildRequires:  automake
BuildRequires:  glibc-devel
BuildRequires:  libopenssl-1_0_0-devel
BuildRequires:  libtool
BuildRequires:  maven-local
BuildRequires:  mvn(io.netty:netty-parent:pom:)
BuildRequires:  mvn(kr.motd.maven:os-maven-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.fusesource.hawtjni:maven-hawtjni-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
#!BuildIgnore:  openssl

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
%setup -q -n %{name}-%{name}-%{namedversion}
patch=`mktemp`
sed "s;@PATH@;%{_libdir}/%{name};g" < %{SOURCE1} > $patch
patch -p1 < $patch
%patch2 -p1

%build
%{mvn_build} -f -- -Dsource=7

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}
mkdir -p %{buildroot}%{_libdir}/%{name}/
cp target/native-build/target/lib/lib%{name}-%{namedversion}.so %{buildroot}%{_libdir}/%{name}/lib%{name}.so

%files -f .mfiles
%dir %{_libdir}/%{name}
%dir %{_jnidir}/%{name}
%dir %{_mavenpomdir}/%{name}
%{_libdir}/%{name}/lib%{name}.so

%files javadoc -f .mfiles-javadoc

%changelog
