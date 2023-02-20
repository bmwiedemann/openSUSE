#
# spec file for package vtkdata
#
# Copyright (c) 2023 SUSE LLC
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


Name:           vtkdata
Version:        9.2.6
Release:        0
%define series  9.2
Summary:        Kitware VTK Library Data
License:        BSD-3-Clause
Group:          Productivity/Scientific/Other
URL:            https://www.vtk.org
Source0:        https://www.vtk.org/files/release/%{series}/VTKData-%{version}.tar.gz
Source1:        https://www.vtk.org/files/release/%{series}/VTKLargeData-%{version}.tar.gz
Source10:       https://gitlab.kitware.com/vtk/vtk/raw/v%{version}/Copyright.txt
Source99:       vtkdata-rpmlintrc
BuildRequires:  cmake >= 3.4
BuildRequires:  fdupes
Provides:       vtklargedata = %{version}
BuildArch:      noarch

%description
The Visualization ToolKit (VTK) is an open source, freely available
software system for 3D computer graphics, image processing, and
visualization used by thousands of researchers and developers around
the world.

This package contains some example data for the Toolkit.

%prep
%setup -q -n VTK-%{version}
%setup -T -D -b 1 -q -n VTK-%{version}
cp %{SOURCE10} .

%build
# Not needed

%install
mkdir -p %{buildroot}%{_datadir}/vtkdata

cp -a .ExternalData %{buildroot}%{_datadir}/vtkdata/

%fdupes %{buildroot}%{_datadir}/vtkdata

%files
%license Copyright.txt
%doc %{_datadir}/vtkdata/.ExternalData/README.rst
%{_datadir}/vtkdata/

%changelog
