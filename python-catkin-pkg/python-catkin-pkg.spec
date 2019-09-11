#
# spec file for package python-catkin-pkg
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-catkin-pkg
Version:        0.4.13
Release:        0
Summary:        Catkin package library
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://wiki.ros.org/catkin_pkg
Source:         https://github.com/ros-infrastructure/catkin_pkg/archive/%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-docutils
Requires:       python-pyparsing
Requires:       python-python-dateutil
Requires:       python-setuptools
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module python-dateutil}
# /SECTION
%python_subpackages

%description
Library for retrieving information about catkin packages.

%prep
%setup -q -n catkin_pkg-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=$PWD/src
cd test
# flake8 line length checks failing (E501)
%python_exec %{_bindir}/nosetests --exclude=test/test_flake8.py

%files %{python_files}
%license LICENSE
%python3_only %{_bindir}/catkin_create_pkg
%python3_only %{_bindir}/catkin_find_pkg
%python3_only %{_bindir}/catkin_generate_changelog
%python3_only %{_bindir}/catkin_package_version
%python3_only %{_bindir}/catkin_prepare_release
%python3_only %{_bindir}/catkin_tag_changelog
%python3_only %{_bindir}/catkin_test_changelog
%{python_sitelib}/*

%changelog
