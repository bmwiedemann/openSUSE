#
# spec file for package python-WebOb
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
%define oldpython python
Name:           python-WebOb
Version:        1.8.7
Release:        0
Summary:        WSGI request and response object
License:        MIT
Group:          Development/Languages/Python
URL:            http://webob.org/
Source:         https://files.pythonhosted.org/packages/source/W/WebOb/WebOb-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# Documentation requirements:
BuildRequires:  fdupes
BuildRequires:  python3-Sphinx
BuildArch:      noarch
%ifpython2
# We need SSL support
BuildRequires:  %{oldpython}
Requires:       %{oldpython}
Obsoletes:      %{oldpython}-webob < %{version}
Provides:       %{oldpython}-webob = %{version}
%endif
%python_subpackages

%description
WebOb provides wrappers around the WSGI request environment, and an
object to help create WSGI responses.

The objects map much of the specified behavior of HTTP, including
header parsing and accessors for other standard parts of the
environment.

%package -n python-WebOb-doc
Summary:        WSGI request and response object - Documentation
Group:          Documentation/HTML
Provides:       %{python_module WebOb-doc = %{version}}

%description -n python-WebOb-doc
This package contains documentation files for %{name}.

%prep
%setup -q -n WebOb-%{version}
# gh#Pylons/webob#390 -- Thread.is_alive is present since Python 2.6, Thread.isAlive was removed in 3.9.
sed -i 's/worker.isAlive/worker.is_alive/' tests/conftest.py

%build
%python_build
PYTHONPATH=./src python3 setup.py build_sphinx && rm build/sphinx/html/.buildinfo

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license docs/license.txt
%doc CHANGES.txt README.rst
%{python_sitelib}/webob
%{python_sitelib}/WebOb-%{version}*-info

%files -n python-WebOb-doc
%doc build/sphinx/html

%changelog
