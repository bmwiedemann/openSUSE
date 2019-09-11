#
# spec file for package sat4j
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


%define eclipse_base %{_libdir}/eclipse
# We want the version to match that shipped in Eclipse's Orbit project
%define qualifier 20181123
Name:           sat4j
Version:        2.3.5
Release:        0
Summary:        A library of SAT solvers written in Java
License:        EPL-1.0 AND LGPL-2.0-only
Group:          Development/Libraries/Java
URL:            http://www.sat4j.org/
Source0:        %{name}-%{version}.tar.xz
Patch0:         sat4j-sourcetarget.patch
Patch1:         sat4j-manifest.patch
BuildRequires:  ant
BuildRequires:  javapackages-local
Requires:       java
BuildArch:      noarch

%description
The aim of the SAT4J library is to provide an efficient library of SAT
solvers in Java. The SAT4J library targets first users of SAT "black
boxes", those willing to embed SAT technologies into their application
without worrying about the details.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
ant \
    -Dbuild.compiler=modern -Drelease=%{version} \
	-DBUILD_DATE=%{qualifier} -Dsource=1.6 -Dtarget=1.6 p2

%install
install -d -m 755 %{buildroot}%{_javadir}
install -m 0644 dist/%{version}/org.sat4j.core.jar %{buildroot}%{_javadir}/org.sat4j.core-%{version}.jar
install -m 0644 dist/%{version}/org.sat4j.pb.jar   %{buildroot}%{_javadir}/org.sat4j.pb-%{version}.jar
(cd %{buildroot}%{_javadir}/ && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

%files
%{_javadir}/org.%{name}*.jar

%changelog
