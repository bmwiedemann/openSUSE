#
# spec file for package netty-tcnative
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


%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:           netty-tcnative
Version:        2.0.66
Release:        0
Summary:        Fork of Tomcat Native with improved OpenSSL and mavenized build
License:        Apache-2.0
URL:            https://github.com/netty/netty/wiki/Forked-Tomcat-Native
Source0:        https://github.com/netty/netty-tcnative/archive/%{name}-parent-%{namedversion}.tar.gz
Source1:        fixLibNames.patch.in
Source2:        https://repo1.maven.org/maven2/io/netty/netty-jni-util/0.0.9.Final/netty-jni-util-0.0.9.Final-sources.jar
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  java-devel >= 1.8
BuildRequires:  libtcnative-1-0
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
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
%pom_disable_module openssl-dynamic

%pom_remove_plugin :module-info
%pom_remove_plugin :japicmp-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-antrun-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_xpath_remove pom:project/pom:build/pom:extensions

%pom_remove_dep io.netty:netty-jni-util
%pom_remove_plugin :maven-dependency-plugin
mkdir -p target/netty-jni-util
unzip %{SOURCE2} -d target/netty-jni-util

%build
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
