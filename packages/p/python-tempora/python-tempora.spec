#
# spec file for package python-tempora
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
Name:           python-tempora
Version:        1.14.1
Release:        0
Summary:        Objects and routines pertaining to date and time (tempora)
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/tempora
Source:         https://files.pythonhosted.org/packages/source/t/tempora/tempora-%{version}.tar.gz
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module jaraco.functools >= 1.20}
BuildRequires:  %{python_module pytest-flake8}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-backports.unittest_mock
Requires:       python-jaraco.functools >= 1.20
Requires:       python-pytz
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Objects and routines pertaining to date and time (tempora)

Modules include:
* tempora (top level package module) contains miscellaneous utilities and constants.
* timing contains routines for measuring and profiling.
* schedule contains an event scheduler.

%prep
%setup -q -n tempora-%{version}

%build
%python_build

%install
%python_install
%fdupes %{buildroot}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst docs/*rst
%python3_only %{_bindir}/calc-prorate
%{python_sitelib}/*

%changelog
