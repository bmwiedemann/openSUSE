#
# spec file for package python-pytest-datadir
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pytest-datadir
Version:        1.3.1
Release:        0
Summary:        Plugin for test data directories and files
License:        MIT
URL:            https://github.com/gabrielcnr/pytest-datadir
Source:         https://files.pythonhosted.org/packages/source/p/pytest-datadir/pytest-datadir-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 2.7.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pytest >= 2.7.0}
BuildRequires:  %{python_module pytest-runner}
# /SECTION
%python_subpackages

%description
pytest plugin for test data directories and files.

%prep
%setup -q -n pytest-datadir-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
rm %{buildroot}%{_prefix}/LICENSE

%check
%pytest

%files %{python_files}
%doc AUTHORS CHANGELOG.rst README.md
%license LICENSE
%{python_sitelib}/*

%changelog
