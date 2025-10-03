#
# spec file for package python-wn
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


Name:           python-wn
Version:        0.13.0
Release:        0
Summary:        Wordnet interface library
License:        MIT
URL:            https://github.com/goodmami/wn
Source:         https://files.pythonhosted.org/packages/source/w/wn/wn-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{pythons}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module starlette}
BuildRequires:  %{python_module tomli}
# /SECTION
BuildRequires:  fdupes
Requires:       python-httpx
Requires:       python-tomli
Recommends:     python-starlette
BuildArch:      noarch
%python_subpackages

%description
Wn is a Python library for exploring information in wordnets.

%prep
%autosetup -p1 -n wn-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/wn/
%{python_sitelib}/wn-%{version}.dist-info/

%changelog
