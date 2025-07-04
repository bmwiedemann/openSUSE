#
# spec file for package netty-tcnative
#
# Copyright (c) 2025 SUSE LLC
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
%if 0%{?suse_version} < 1500 || 0%{?gcc_version} < 11
%define with_gcc 11
%endif
Name:           netty-tcnative
Version:        2.0.72
Release:        0
Summary:        Fork of Tomcat Native with improved OpenSSL and mavenized build
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/netty/netty/wiki/Forked-Tomcat-Native
Source0:        https://github.com/netty/netty-tcnative/archive/%{name}-parent-%{namedversion}.tar.gz
Source1:        fixLibNames.patch.in
Source2:        https://repo1.maven.org/maven2/io/netty/netty-jni-util/0.0.9.Final/netty-jni-util-0.0.9.Final-sources.jar
Source100:      %{name}-rpmlintrc
BuildRequires:  apr-devel
BuildRequires:  fdupes
BuildRequires:  gcc%{?with_gcc}-c++
BuildRequires:  java-devel >= 1.8
BuildRequires:  libopenssl-devel
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(ant-contrib:ant-contrib)
BuildRequires:  mvn(kr.motd.maven:os-maven-plugin)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-commons-net)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.fusesource.hawtjni:hawtjni-maven-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

%description
netty-tcnative is a fork of Tomcat Native. It includes a set of changes
contributed by Twitter, Inc, such as:
 *  Simplified distribution and linkage of native library
 *  Complete mavenization of the project
 *  Improved OpenSSL support
To minimize the maintenance burden, we create a dedicated branch for each stable
upstream release and apply our own changes on top of it, while keeping the
number of maintained branches to minimum

%package openssl-dynamic
Summary:        Netty/TomcatNative [OpenSSL - Dynamic]]
Group:          Development/Libraries/Java

%description openssl-dynamic
A Mavenized fork of Tomcat Native which incorporates various patches.

This artifact is dynamically linked to OpenSSL and Apache APR.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{name}-parent-%{namedversion}

for i in openssl-classes openssl-dynamic; do
  mkdir -p ${i}/target/netty-jni-util
  unzip %{SOURCE2} -d ${i}/target/netty-jni-util
done

# Will be regenerated by hawtjni-maven-plugin
rm -rf openssl-dynamic/src/main/native-package/configure.*

sed "s;@PATH@;%{_libdir};g" < %{SOURCE1} | patch -p1

# Build only the openssl-dynamic module
%pom_disable_module openssl-static
%pom_disable_module boringssl-static
%pom_disable_module libressl-static

%pom_remove_plugin :module-info
%pom_remove_plugin :japicmp-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_remove_dep io.netty:netty-jni-util
%pom_remove_plugin :maven-dependency-plugin

%pom_remove_plugin :maven-scm-plugin boringssl-static

%pom_remove_plugin :maven-source-plugin openssl-classes

# Tell xmvn to install attached artifact, which it does not
# do by default. In this case install all attached artifacts with
# the linux classifier.
%{mvn_package} ":{*}-parent" __noinstall
%{mvn_package} ":::sources:" __noinstall
%{mvn_package} ":::javadoc:" __noinstall
%{mvn_package} ":{*}-classes"
%{mvn_package} ":{*}::linux*:" @1
%{mvn_package} ":{*}" @1

%{mvn_alias} :netty-tcnative :netty-tcnative-openssl-static :netty-tcnative-boringssl-static :netty-tcnative-libressl-static

%build
%if 0%{?with_gcc}
export CXX=g++-%{with_gcc}
export CC=gcc-%{with_gcc}
%endif
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

install -dm 0755 %{buildroot}%{_libdir}
install -pm 0755 openssl-dynamic/target/native-build/target/lib/libnetty_tcnative.so %{buildroot}%{_libdir}/

%files -f .mfiles

%files openssl-dynamic -f .mfiles-%{name}
%{_libdir}/libnetty_tcnative.so

%files javadoc -f .mfiles-javadoc

%changelog
