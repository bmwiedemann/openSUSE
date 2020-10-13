#
# spec file for package python-torch
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

%define srcname vision
%define skip_python2 1

Name:           python-torchvision
Version:        0.6.1
Release:        0
Summary:        Popular datasets, model architectures, and common image transformations for computer vision
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pytorch/vision
Source0:        https://github.com/pytorch/vision/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildRequires:  %{python_module torch-devel} >= 1.5.1
BuildRequires:  %{python_module devel} >= 3.6
BuildRequires:  %{python_module rpm-macros}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
BuildRequires:  cmake >= 3.1
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ninja
# Same as in python-torch
ExcludeArch:    %ix86
%python_subpackages

%description
The torchvision package consists of popular datasets, 
model architectures, and common image transformations
for computer vision.

%prep
%setup -q -n %{srcname}-%{version}

%build
%python_build

%install
%python_install
sed -i -e 's#/usr/bin/env python3#/usr/bin/python3#' %{buildroot}%{python_sitearch}/torchvision/transforms/_transforms_video.py
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%defattr(-,root,root)
%doc README.rst
%license LICENSE
%{python_sitearch}/torchvision/
%{python_sitearch}/torchvision-*.egg-info/

%changelog
