#
# spec file for package python-WebHelpers
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define skip_python3 1
%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-WebHelpers
Version:        1.3
Release:        0
Summary:        Web Helpers
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://webhelpers.readthedocs.io/en/latest/
Source:         https://files.pythonhosted.org/packages/source/W/WebHelpers/WebHelpers-%{version}.tar.gz
# From https://bitbucket.org/bbangert/webhelpers/commits/69ce4f780c?at=trunk
# fix of https://bitbucket.org/bbangert/webhelpers/issues/73/ which
# makes tests fail.
Patch0:         69ce4f780c-fix-error-on-webob-1.2.3.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Routes
Requires:       python-nose
BuildArch:      noarch
%ifpython2
Provides:       %{oldpython}-webhelpers = %{version}
Obsoletes:      %{oldpython}-webhelpers < %{version}
%endif
%python_subpackages

%description
Web Helpers is a library of helper functions intended to make writing
web applications easier. It's the standard function library for
Pylons and TurboGears 2, but can be used with any web framework.  It also
contains a large number of functions not specific to the web, including text
processing, number formatting, date calculations, container objects, etc.

%prep
%setup -q -n WebHelpers-%{version}
%patch0 -p1
sed -i "1d" webhelpers/{pylonslib/_jsmin,markdown,textile,pylonslib/minify}.py # Fix non-executable script

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc CHANGELOG README.txt TODO
%{python_sitelib}/*

%changelog
