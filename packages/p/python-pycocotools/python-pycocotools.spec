#
# spec file for package python-pycocotools
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python36 1
Name:           python-pycocotools
Version:        2.0~post.1582219528.8c9bcc3
Release:        0
Summary:        Python cocoapi
License:        BSD-2-Clause
URL:            https://github.com/cocodataset/cocoapi
Source:         cocoapi-%{version}.tar.xz
BuildRequires:  %{python_module Cython >= 0.27.3}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module matplotlib >= 2.1.0}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools >= 18.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Cython >= 0.27.3
Requires:       python-matplotlib >= 2.1.0
Requires:       python-setuptools >= 18.0
# old non PyPI name we used to have around
Provides:       python-cocotools = %{version}
%python_subpackages

%description
COCO is a large image dataset designed for object detection, segmentation,
person keypoints detection, stuff segmentation, and caption generation.
This package provides Matlab, Python, and Lua APIs that assists in loading,
parsing, and visualizing the annotations in COCO.

%prep
%setup -q -n cocoapi-%{version}/PythonAPI

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license ../license.txt
%doc ../README.txt
%{python_sitearch}/*

%changelog
