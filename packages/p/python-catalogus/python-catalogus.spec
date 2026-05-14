#
# spec file for package python-catalogus
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


Name:           python-catalogus
Version:        0.1.0
Release:        0
Summary:        Python classes for name-to-object registry-like support
License:        GPL-2.0-or-later
URL:            https://github.com/breezy-team/catalogus
Source:         https://github.com/breezy-team/catalogus/archive/refs/tags/v%{version}.tar.gz#/catalogus-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
A Python library providing classes for name-to-object registry-like support.

%prep
%autosetup -p1 -n catalogus-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license COPYING
%doc README.md
%{python_sitelib}/catalogus
%{python_sitelib}/catalogus-%{version}.dist-info

%changelog
