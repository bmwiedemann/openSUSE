#
# spec file for package python-pytest-forked
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-pytest-forked
Version:        1.3.0
Release:        0
Summary:        Run each test in a forked subprocess
License:        MIT
URL:            https://github.com/pytest-dev/pytest-forked
Source:         https://files.pythonhosted.org/packages/source/p/pytest-forked/pytest-forked-%{version}.tar.gz
BuildRequires:  %{python_module pytest >= 3.10}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 3.10
BuildArch:      noarch
%python_subpackages

%description
Extraction of pytest-xdist --forked module used for running tests in forked subprocess

%prep
%setup -q -n pytest-forked-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG
%{python_sitelib}/*

%changelog
