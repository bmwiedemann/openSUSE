#
# spec file for package hbci4java
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           hbci4java
Summary:        Java online banking client using the HBCI standard
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Productivity/Office/Finance
Version:        2.5.12.hibiscus.2.6.18
Release:        0
Url:            https://github.com/willuhn/hbci4java
Source:         https://github.com/willuhn/hibiscus/raw/V_2_6_18_BUILD_361/lib.src/hbci4java-2.5.12-src.zip
# extracted from https://github.com/willuhn/hbci4java
Source1:        build.xml
Source2:        cryptalgs4java.zip
Source3:        chipcard.zip
Patch0:         hbci4java-jdk9.patch
Patch1:         hbci4java-jdk10.patch
Patch2:         signed-char.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ant
BuildRequires:  gcc-c++
BuildRequires:  unzip

%description
Fork of HBCI4Java for Hibiscus, that contains support for
chipTAN, smsTAN, HHD, SEPA and other fixes/enhancements.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
Developer documentation of HBCI4Java for Hibiscus.

%prep
%setup -q -c %{name}-%{version} -a 2 -a 3
cp %{S:1} .
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
pushd chipcard
make
popd

%ant dist

%install
mkdir -p %{buildroot}%{_libdir}/hbci4java
install chipcard/lib/*.so %{buildroot}%{_libdir}/hbci4java
cp -r dist/jar/* %{buildroot}%{_libdir}/hbci4java

mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -r doc/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}

%clean
%ant clean

%files
%defattr(-,root,root)
%{_libdir}/hbci4java

%files javadoc
%defattr(-,root,root)
%{_javadocdir}/%{name}-%{version}

%changelog
