#
# spec file for package brotli4j
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           brotli4j
Version:        1.23.0
Release:        0
Summary:        Brotli compression and decompression for Java
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/hyperxpro/Brotli4j
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        %{name}-build.tar.xz
Patch0:         brotli4j-loadlibrary.patch
Patch1:         brotli4j-no-netty.patch
BuildRequires:  ant
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6

%description
Brotli4j provides Brotli compression and decompression for Java.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description javadoc
API documentation for %{name}

%prep
%setup -q -n Brotli4j-%{version} -a1
%patch -P 0 -p1
%patch -P 1 -p1

%pom_remove_dep -r :netty-buffer 

sed -i 's|@LIBDIR@|%{_libdir}/%{name}|' \
    brotli4j/src/main/java/com/aayushatharva/brotli4j/Brotli4jLoader.java

%build
mkdir -p lib
ant jar javadoc
%cmake
%cmake_build

%install
# native
install -dm 0755 %{buildroot}%{_libdir}/%{name}
install -pm 0755 build/libbrotli.so %{buildroot}%{_libdir}/%{name}/
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 service/target/service-%{version}.jar %{buildroot}%{_javadir}/%{name}/service.jar
install -dm 0755 %{buildroot}%{_jnidir}/%{name}
install -pm 0644 brotli4j/target/%{name}-%{version}.jar %{buildroot}%{_jnidir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%mvn_install_pom service/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/service.pom
%add_maven_depmap %{name}/service.pom %{name}/service.jar
%mvn_install_pom %{name}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr service/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/service
cp -pr %{name}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/%{name}
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%{_libdir}/%{name}
%license LICENSE NOTICE.txt LICENSES/*
%doc README.md

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE NOTICE.txt LICENSES/*

%changelog
