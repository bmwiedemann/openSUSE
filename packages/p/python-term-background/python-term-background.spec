#
# spec file for package python-term-background
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-term-background
Version:        1.0.5
Release:        0
Summary:        Determine if shell has a light or dark background
License:        GPL-3.0-or-later
URL:            https://github.com/rocky/shell-term-background
Source0:        https://github.com/rocky/shell-term-background/releases/download/%{version}/term_background-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 70.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION For tests
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A python module to determine if a shell has a light or dark background.

%prep
%autosetup -p1 -n term_background-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license COPYING
%doc README.rst
%{python_sitelib}/term_background
%{python_sitelib}/term_background-%{version}.dist-info

%changelog
