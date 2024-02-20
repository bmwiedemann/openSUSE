#
# spec file for package python-nptyping
#
# Copyright (c) 2024 SUSE LLC
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


# pyright is a nodejs package and nobody dares to package it for openSUSE
%bcond_with pyright
# beartype and typeguard: https://github.com/ramonhagenaars/nptyping/issues/115
%bcond_with beartype
%bcond_with typeguard
# mypy tests expect pandas_stubs, which are not in the distribution
%bcond_with pandas_stubs
Name:           python-nptyping
Version:        2.5.0
Release:        0
Summary:        Type hints for NumPy
License:        MIT
URL:            https://github.com/ramonhagenaars/nptyping
Source:         https://files.pythonhosted.org/packages/source/n/nptyping/nptyping-%{version}.tar.gz
# PATCH-FIX-UPSTREAM skip_on_other_archs.patch gh#ramonhagenaars/nptyping#73 mcepl@suse.com
# test_instance_check_performance doesn't seem to work well on some architectures
Patch0:         skip_on_other_archs.patch
# PATCH-FIX-OPENSUSE use_system_packages.patch gh#ramonhagenaars/nptyping#72 mcepl@suse.com
# Don't need to build the wheel a second time, when creating venv for install check, allow use of system packages
Patch1:         use_system_packages.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       (python-numpy >= 1.21.5 with python-numpy < 2)
%if 0%{python_version_nodots} < 310
Requires:       (python-typing_extensions >= 4.0.0 with python-typing_extensions < 5)
%endif
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module feedparser}
%{?_with_pandas_stubs:BuildRequires:  %{python_module mypy}}
%{?_with_beartype:BuildRequires:  %{python_module beartype}}
%{?_with_typeguard:BuildRequires:  %{python_module typeguard}}
BuildRequires:  %{python_module numpy >= 1.20.0 with %python-numpy < 2}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module typing_extensions < 5 if %python-base < 3.10}
BuildRequires:  %{python_module typing_extensions >= 4.0.0 if %python-base < 3.10}
# /SECTION
%python_subpackages

%description
Type hints for NumPy.

%prep
%autosetup -p1 -n nptyping-%{version}

sed -i -e 's/\r//g' README.md

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# wheel in dist/ used by test/test_wheel.py
mkdir -p dist/
cp build/nptyping-%{version}-py3-none-any.whl dist/
%{!?_with_pyright:rm tests/test_pyright.py}
%{!?_with_beartype:rm tests/test_beartype.py}
%{!?_with_typeguard:rm tests/test_typeguard.py}
%{!?_with_pandas_stubs:rm tests/test_mypy.py tests/pandas_/test_mypy_dataframe.py tests/pandas_/test_fork_sync.py}
%pyunittest -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/nptyping
%{python_sitelib}/nptyping-%{version}.dist-info

%changelog
