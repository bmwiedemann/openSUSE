#
# spec file for package python-feedgen
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
Name:           python-feedgen
Version:        0.9.0
Release:        0
Summary:        Python feed generator module (ATOM, RSS, Podcasts)
License:        BSD-2-Clause AND LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://lkiesow.github.io/python-feedgen
# Use GitHub tarball as PyPI release lacks tests
Source:         https://github.com/lkiesow/python-feedgen/archive/v%{version}.tar.gz#/feedgen-%{version}.tar.gz
# Source:         https://files.pythonhosted.org/packages/source/f/feedgen/feedgen-%%{version}.tar.gz
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lxml
Requires:       python-python-dateutil
BuildArch:      noarch
%python_subpackages

%description
This module can be used to generate web feeds in both ATOM and RSS
format. It has support for extensions.

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/*
%doc readme.rst
%license license.bsd license.lgpl

%changelog
