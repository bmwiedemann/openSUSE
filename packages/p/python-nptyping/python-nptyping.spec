#
# spec file for package python-nptyping
#
# Copyright (c) 2022 SUSE LLC
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


%define modname nptyping
Name:           python-nptyping
Version:        2.4.1
Release:        0
Summary:        Type hints for NumPy
License:        MIT
URL:            https://github.com/ramonhagenaars/nptyping
Source:         https://github.com/ramonhagenaars/%{modname}/archive/refs/tags/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE use_system_packages.patch gh#ramonhagenaars/nptyping#72 mcepl@suse.com
# Don't need to build the wheel a second time, when creating venv for install check, allow use of system packages
Patch0:         use_system_packages.patch
# PATCH-FIX-UPSTREAM skip_on_other_archs.patch gh#ramonhagenaars/nptyping#73 mcepl@suse.com
# test_instance_check_performance doesn't seem to work well on some architectures
Patch1:         skip_on_other_archs.patch
# PATCH-FIX-OPENSUSE skip-pyright-tests.patch code@bnavigator.de -- pyright is a nodejs package and nobody dares to package it for openSUSE
Patch2:         skip-pyright-tests.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-numpy >= 1.20.0
%if 0%{python_version_nodots} < 310
Requires:       python-typing_extensions >= 4.0.0
%endif
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module beartype}
BuildRequires:  %{python_module feedparser}
BuildRequires:  %{python_module mypy}
BuildRequires:  %{python_module numpy >= 1.20.0}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module typeguard}
BuildRequires:  %{python_module typing_extensions >= 4.0.0 if %python-base < 3.10}
# /SECTION
%python_subpackages

%description
Type hints for NumPy.

%prep
%autosetup -p1 -n nptyping-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# wheel in dist/ used by test/test_wheel.py
mkdir -p dist/
cp build/nptyping-%{version}-py3-none-any.whl dist/
# There's no python-pandas-stubs package in Factory yet
%pyunittest -v -k 'not test_mypi'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}*-info

%changelog
