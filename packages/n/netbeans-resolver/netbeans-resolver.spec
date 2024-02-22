#
# spec file for package netbeans-resolver
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


%define patched_resolver_ver 1.2
%define patched_resolver xml-commons-resolver-%{patched_resolver_ver}
Name:           netbeans-resolver
Version:        6.7.1
Release:        0
Summary:        Resolver subproject of xml-commons patched for NetBeans
License:        Apache-1.1
Group:          Development/Libraries/Java
URL:            https://xml.apache.org/commons/
Source0:        http://www.apache.org/dist/xerces/xml-commons/%{patched_resolver}.tar.gz
# see http://hg.netbeans._org/main/file/721f72486327/o.apache.xml.resolver/external/readme.txt
Patch0:         %{name}-%{version}-nb.patch
Patch1:         %{name}-%{version}-resolver.patch
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
Requires:       java >= 1.8
Requires:       javapackages-tools
BuildArch:      noarch

%description
Resolver subproject of xml-commons, version %{patched_resolver_ver} with
a patch for NetBeans.

%prep
%setup -q -n %{patched_resolver}
# remove all binary libs and prebuilt javadocs
find . -name "*.jar" -exec rm -f {} \;
rm -rf docs

%patch -P 0 -p1 -b .sav
%patch -P 1 -p1 -b .sav

dos2unix -k KEYS
dos2unix -k LICENSE.resolver.txt

%build
%{ant} \
    -f resolver.xml \
    -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 \
    jar

%install

# JARs
mkdir -p %{buildroot}%{_javadir}
cp -p build/resolver.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar

%files
%{_javadir}/*
%license LICENSE.resolver.txt
%doc KEYS

%changelog
