#
# spec file for package python-fakeredis
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
Name:           python-fakeredis
Version:        1.0.5
Release:        0
Summary:        Fake implementation of redis API for testing purposes
License:        BSD-3-Clause AND MIT
Group:          Development/Languages/Python
URL:            https://github.com/jamesls/fakeredis
Source:         https://files.pythonhosted.org/packages/source/f/fakeredis/fakeredis-%{version}.tar.gz
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-redis
Requires:       python-six >= 1.12
Requires:       python-sortedcontainers
Recommends:     python-future
Suggests:       python-lupa
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module lupa}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module six >= 1.12}
BuildRequires:  %{python_module sortedcontainers}
# /SECTION
%python_subpackages

%description
Fake implementation of redis API for testing purposes.

%prep
%setup -q -n fakeredis-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitelib}/*

%changelog
