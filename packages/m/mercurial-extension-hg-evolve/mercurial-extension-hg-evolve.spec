#
# spec file for package mercurial-extension-hg-evolve
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


%if 0%{?suse_version} > 1600
# Tumbleweed
%define pythons python3
%else
%if 0%{?sle_version} >= 150600
%{?sle15_python_module_pythons}
%else
%define pythons python3
%endif
%endif

Name:           mercurial-extension-hg-evolve
Version:        11.1.7.post1
Release:        0
Summary:        Flexible evolution of Mercurial history
License:        GPL-2.0-or-later
Group:          Development/Tools/Version Control
URL:            https://www.mercurial-scm.org/doc/evolution/
Source0:        https://files.pythonhosted.org/packages/source/h/hg-evolve/hg-evolve-%{version}.tar.gz
Source90:       tests.blacklist
BuildRequires:  %{pythons}
# python311-flake8 is not available on Leap 15.6.
%if 0%{?suse_version} > 1600 || 0%{?sle_version} < 150600
BuildRequires:  %{python_module flake8}
%endif
BuildRequires:  %{python_module pyflakes}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  mercurial
BuildRequires:  mercurial-tests
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       mercurial
BuildArch:      noarch

%description
Flexible evolution of Mercurial history.

%prep
%setup -q -n hg-evolve-%{version}

%build
%python_build

%install
%python_install

# Delete hgext3rd/__init__.py and its cached version because it is already delivered by mercurial.
rm %{buildroot}%{python_sitelib}/hgext3rd/__init__.py
rm %{buildroot}%{python_sitelib}/hgext3rd/__pycache__/__init__*.pyc

%fdupes %{buildroot}%{python_sitelib}

%check
cd tests
%python_exec %{_datadir}/mercurial/tests/run-tests.py --with-hg=%{_bindir}/hg --blacklist=%{SOURCE90}

%files
%doc CHANGELOG README.rst
%license COPYING
%{python_sitelib}/*

%changelog
