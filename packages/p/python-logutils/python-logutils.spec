#
# spec file for package python-logutils
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-logutils
Version:        0.3.5
Release:        0
Summary:        Logging utilities
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://logutils.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/l/logutils/logutils-%{version}.tar.gz
Patch0:         sphinx4.patch
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
BuildRequires:  redis
BuildArch:      noarch
%python_subpackages

%description
The logutils package provides a set of handlers for the Python standard
library's logging package.

Some of these handlers are out-of-scope for the standard library, and
so they are packaged here. Others are updated versions which have
appeared in recent Python releases, but are usable with older versions
of Python and so are packaged here.

%package -n python-logutils-doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Provides:       %{python_module logutils-doc = %{version}}

%description -n python-logutils-doc
The logutils package provides a set of handlers for the Python standard
library's logging package.

Some of these handlers are out-of-scope for the standard library, and
so they are packaged here. Others are updated versions which have
appeared in recent Python releases, but are usable with older versions
of Python and so are packaged here.

This package contains the documentation.

%prep
%setup -q -n logutils-%{version}
%autopatch -p1

%build
%python_build
cd doc && make html

%install
%python_install

%check
export PATH="$PATH:/sbin:/usr/sbin"
%pyunittest discover -v tests

%files %{python_files}
%license LICENSE.txt
%doc NEWS.txt README.rst
%{python_sitelib}/*

%files -n python-logutils-doc
%license LICENSE.txt
%doc doc/_build/html

%changelog
