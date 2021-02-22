#
# spec file for package python-pylast
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-pylast
Version:        4.1.0
Release:        0
Summary:        A python interface to Last.fm
License:        Apache-2.0
URL:            https://github.com/pylast/pylast
Source0:        https://files.pythonhosted.org/packages/source/p/pylast/pylast-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pyaml}
BuildRequires:  %{python_module pycodestyle}
BuildRequires:  %{python_module pyflakes}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A Python interface to Last.fm and other API-compatible websites such as Libre.fm

Features:
- Simple public interface.
- Access to all the data exposed by the Last.fm webservices.
- Scrobbling support.
- Full object-oriented design.
- Proxy support.
- Internal caching support for some webservices calls (disabled by default).
- No extra dependencies but python itself.
- Support for other API-compatible networks like Libre.fm
- Python3-friendly (Starting from 0.5).

%prep
%setup -q -n pylast-%{version}

%build
%python_build

%install
%python_install
%python_exec %fdupes %{buildroot}/%{python_sitelib}

%check
# every test file has:
# Integration (not unit) tests for pylast.py
# almost all skipped, need internet access
%pytest

%files %{python_files}
%doc README.md
%license COPYING
%dir %{python_sitelib}/pylast
%{python_sitelib}/pylast/*
%{python_sitelib}/pylast-%{version}-py*.egg-info

%changelog
