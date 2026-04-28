#
# spec file for package python-docstring-parser
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


Name:           python-docstring-parser
Version:        0.18.0
Release:        0
Summary:        Parse Python docstrings in reST, Google and Numpydoc format
License:        MIT
URL:            https://github.com/rr-/docstring_parser
Source:         https://files.pythonhosted.org/packages/source/d/docstring-parser/docstring_parser-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Provides:       python-docstring_parser = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
Parse Python docstrings. Currently support ReST, Google, Numpydoc-style and
Epydoc docstrings.

%prep
%autosetup -p1 -n docstring_parser-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.md
%doc README.md
%{python_sitelib}/docstring_parser
%{python_sitelib}/docstring_parser-%{version}.dist-info

%changelog
