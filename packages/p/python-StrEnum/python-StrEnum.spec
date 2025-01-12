#
# spec file for package python-StrEnum
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-StrEnum
Version:        0.4.15
Release:        0
Summary:        An Enum that inherits from str
License:        MIT
URL:            https://github.com/irgeek/StrEnum
Source:         https://github.com/irgeek/StrEnum/archive/refs/tags/v%{version}.tar.gz#/StrEnum-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#irgeek/StrEnum#34
Patch0:         support-python-312.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-sphinx
Suggests:       python-sphinx_rtd_theme
Suggests:       python-myst-parser
BuildArch:      noarch
%python_subpackages

%description
An Enum that inherits from str.

%prep
%autosetup -p1 -n StrEnum-%{version}
# We don't need coverage or linting
grep -v '^addopts' pytest.ini > new-pytest.ini
mv new-pytest.ini pytest.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/strenum
%{python_sitelib}/StrEnum-%{version}.dist-info

%changelog
