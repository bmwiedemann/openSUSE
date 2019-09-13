#
# spec file for package paraviewdata
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define major_ver 5.4
Name:           paraviewdata
Version:        5.4.0
Release:        0
Summary:        Examples for Paraview
License:        BSD-3-Clause
Group:          Productivity/Scientific/Physics
Url:            http://www.paraview.org
Source0:        http://www.paraview.org/files/v%{major_ver}/ParaViewData-v%{version}.tar.gz
BuildRequires:  fdupes
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
ParaView is an application for visualizing large data sets.

ParaView runs on distributed and shared memory systems alike. It uses the
Visualization Toolkit as the data processing and rendering engine, and has a
user interface written using a blend of Tcl/Tk and C++.

This package contains some example data for Paraview.

%prep
%setup -q -n ParaView-v%{version}

%build

%install
mkdir -p %{buildroot}%{_docdir}/paraviewdata
mkdir -p %{buildroot}%{_datadir}

cp -a %{_builddir}/ParaView-v%{version} %{buildroot}/%{_datadir}/paraviewdata

%fdupes %{buildroot}%{_datadir}/paraviewdata

%files
%defattr(-,root,root,-)
%doc %{_docdir}/paraviewdata
%{_datadir}/paraviewdata/

%changelog
