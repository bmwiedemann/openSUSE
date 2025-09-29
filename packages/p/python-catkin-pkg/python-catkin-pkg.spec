#
# spec file for package python-catkin-pkg
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%bcond_without libalternatives
%define commands create_pkg find_pkg generate_changelog package_version prepare_release tag_changelog test_changelog
Name:           python-catkin-pkg
Version:        1.1.0
Release:        0
Summary:        Catkin package library
License:        BSD-3-Clause
URL:            https://wiki.ros.org/catkin_pkg
Source0:        https://github.com/ros-infrastructure/catkin_pkg/archive/%{version}.tar.gz
Source99:       python-catkin-pkg.rpmlintrc
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-docutils
Requires:       python-pyparsing
Requires:       python-python-dateutil
Requires:       python-setuptools
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
# /SECTION
%python_subpackages

%description
Library for retrieving information about catkin packages.

%prep
%autosetup -p1 -n catkin_pkg-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
for c in %{commands}; do
  %python_clone -a %{buildroot}%{_bindir}/catkin_$c
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=$PWD/src
# flake8 line length checks failing (E501)
%pytest -k 'not test_flake8'

%pre
# If libalternatives is used: Removing old update-alternatives entries.
for c in %{commands}; do
  %python_libalternatives_reset_alternative catkin_$c
done

# post and postun macro call is not needed with only libalternatives

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/catkin_create_pkg
%python_alternative %{_bindir}/catkin_find_pkg
%python_alternative %{_bindir}/catkin_generate_changelog
%python_alternative %{_bindir}/catkin_package_version
%python_alternative %{_bindir}/catkin_prepare_release
%python_alternative %{_bindir}/catkin_tag_changelog
%python_alternative %{_bindir}/catkin_test_changelog
%{python_sitelib}/catkin_pkg
%{python_sitelib}/catkin_pkg*-info

%changelog
