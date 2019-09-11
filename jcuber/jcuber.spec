#
# spec file for package jcuber
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


Name:           jcuber
Version:        4.4.1
Release:        0
Summary:        Java Cube Reader Library
License:        BSD-3-Clause AND Apache-2.0
Group:          Development/Libraries/Java
URL:            http://www.scalasca.org/software/cube-4.x/download.html
Source0:        http://apps.fz-juelich.de/scalasca/releases/cube/4.4/dist/%{name}-%{version}.tar.gz
BuildRequires:  java-devel
BuildRequires:  xerces-j2
BuildArch:      noarch

%description
Java Cube Reader Library is a native Java library for reading of a
multi-dimensional performance space consisting of the dimensions
(i) performance metric, (ii) call path, and (iii) system resource.
Each dimension can be represented as a tree, where non-leaf nodes
of the tree can be collapsed or expanded to achieve the desired level
of granularity.

%package        doc
Summary:        Documentation for for %{name}
Group:          Development/Libraries/Java

%description    doc
Java Cube Reader Library is a native Java library for reading of a
multi-dimensional performance space consisting of the dimensions
(i) performance metric, (ii) call path, and (iii) system resource.
Each dimension can be represented as a tree, where non-leaf nodes
of the tree can be collapsed or expanded to achieve the desired level
of granularity.
This package contains the documentation and examples for %{name}.

%prep
%setup -q

%build
%configure
# This package won't build in parallel
%define _smp_mflags -j1
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/jcuber-config
%{_bindir}/jcuber-config-frontend
%{_javadir}/CubeReader.jar

%files doc
%{_datadir}/doc/jcuber
%exclude %{_datadir}/jcuber/jcuber.summary

%changelog
