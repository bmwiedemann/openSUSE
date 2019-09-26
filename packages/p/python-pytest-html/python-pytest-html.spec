#
# spec file for package python-pytest-html
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
%define skip_python2 1
Name:           python-pytest-html
Version:        2.0.0
Release:        0
Summary:        Pytest plugin for generating HTML reports
License:        MPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pytest-dev/pytest-html
Source:         https://files.pythonhosted.org/packages/source/p/pytest-html/pytest-html-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ansi2html
Requires:       python-pytest >= 3.0
Requires:       python-pytest-metadata
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ansi2html}
BuildRequires:  %{python_module pytest >= 3.0}
BuildRequires:  %{python_module pytest-metadata}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-rerunfailures}
BuildRequires:  %{python_module pytest-xdist}
# /SECTION
%python_subpackages

%description
pytest plugin for generating HTML reports

%prep
%setup -q -n pytest-html-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/*

%changelog
