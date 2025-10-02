#
# spec file for package python-pyprojroot
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


Name:           python-pyprojroot
Version:        0.3.0
Release:        0
Summary:        Project-oriented workflow in Python
License:        MIT
URL:            https://github.com/chendaniely/pyprojroot
Source:         https://files.pythonhosted.org/packages/source/p/pyprojroot/pyprojroot-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing-extensions}
# /SECTION
BuildRequires:  fdupes
Requires:       python-typing-extensions
BuildArch:      noarch
%python_subpackages

%description
Project-oriented workflow in Python

%prep
%autosetup -p1 -n pyprojroot-%{version}

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
%{python_sitelib}/pyprojroot/
%{python_sitelib}/pyprojroot-%{version}.dist-info/

%changelog
