#
# spec file for package paraviewdata
#
# Copyright (c) 2020 SUSE LLC
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


%define major_ver 5.8
Name:           paraviewdata
Version:        5.8.0
Release:        0
Summary:        Examples for Paraview
License:        BSD-3-Clause
Group:          Productivity/Scientific/Physics
URL:            https://www.paraview.org
Source0:        https://www.paraview.org/files/v%{major_ver}/ParaViewData-v%{version}.tar.xz
Source1:        https://gitlab.kitware.com/paraview/paraview/raw/v%{version}/Copyright.txt
BuildRequires:  fdupes
BuildArch:      noarch

%description
ParaView is an application for visualizing large data sets.

ParaView runs on distributed and shared memory systems alike. It uses the
Visualization Toolkit as the data processing and rendering engine, and has a
user interface written using a blend of Tcl/Tk and C++.

This package contains some example data for Paraview.

%prep
%setup -q -n ParaView-v%{version}
cp %{SOURCE1} ./.ExternalData/

%build

%install
mkdir -p %{buildroot}%{_datadir}/paraviewdata-%{major_ver}
cp -a %{_builddir}/ParaView-v%{version}/* %{buildroot}/%{_datadir}/paraviewdata-%{major_ver}/
%fdupes %{buildroot}%{_datadir}/

%files
%license .ExternalData/Copyright.txt
%doc .ExternalData/README.rst
%{_datadir}/paraviewdata-%{major_ver}/

%changelog
