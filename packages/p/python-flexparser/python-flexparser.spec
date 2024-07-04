#
# spec file for package python-flexparser
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


Name:           python-flexparser
Version:        0.3.1
Release:        0
Summary:        Parsing made fun ... using typing
License:        BSD-3-Clause
URL:            https://github.com/hgrecco/flexparser
Source:         https://files.pythonhosted.org/packages/source/f/flexparser/flexparser-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module setuptools_scm >= 3.4.3}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-typing_extensions
BuildArch:      noarch
%python_subpackages

%description
Parsing made fun ... using typing.

%prep
%autosetup -p1 -n flexparser-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS CHANGES README.rst
%license LICENSE
%{python_sitelib}/flexparser
%{python_sitelib}/flexparser-%{version}.dist-info

%changelog
