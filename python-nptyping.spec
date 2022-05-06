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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define modname nptyping
Name:           python-nptyping
Version:        2.0.1
Release:        0
Summary:        Type hints for NumPy
License:        MIT
URL:            https://github.com/ramonhagenaars/nptyping
Source:         https://github.com/ramonhagenaars/%{modname}/archive/refs/tags/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM use_system_packages.patch gh#ramonhagenaars/nptyping#72 mcepl@suse.com
# When creating venv allow use of system packages
Patch0:         use_system_packages.patch
# PATCH-FIX-UPSTREAM skip_on_other_archs.patch gh#ramonhagenaars/nptyping#73 mcepl@suse.com
# test_instance_check_performance doesn't seem to work well on some architectures
Patch1:         skip_on_other_archs.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-numpy >= 1.20.0
Suggests:       python-autoflake
Suggests:       python-beartype < 0.10.0
Suggests:       python-beartype >= 0.10.0
Suggests:       python-black
Suggests:       python-codecov >= 2.1.0
Suggests:       python-coverage
Suggests:       python-invoke >= 1.6.0
Suggests:       python-isort
Suggests:       python-mypy
Suggests:       python-pip-tools >= 6.5.0
Suggests:       python-pylint
Suggests:       python-setuptools
Suggests:       python-typeguard
Suggests:       python-typing_extensions
Suggests:       python-wheel
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module beartype}
BuildRequires:  %{python_module mypy}
BuildRequires:  %{python_module numpy >= 1.20.0}
BuildRequires:  %{python_module typeguard}
BuildRequires:  %{python_module typing_extensions if %python-base < 3.10}
# /SECTION
%python_subpackages

%description
Type hints for NumPy.

%prep
%autosetup -p1 -n nptyping-%{version}

sed -i -e 's/typing-extensions/typing_extensions/' constraints.txt

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}*-info

%changelog
