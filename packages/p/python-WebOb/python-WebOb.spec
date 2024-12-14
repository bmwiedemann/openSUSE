#
# spec file for package python-WebOb
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-WebOb
Version:        1.8.9
Release:        0
Summary:        WSGI request and response object
License:        MIT
URL:            http://webob.org/
Source:         https://files.pythonhosted.org/packages/source/w/webob/webob-%{version}.tar.gz
BuildRequires:  %{python_module legacy-cgi if %python-base >= 3.13}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# Documentation requirements:
BuildRequires:  fdupes
BuildRequires:  python3-Sphinx
%if %{python_version_nodots} >= 313
Requires:       python-legacy-cgi >= 2.6
%endif
BuildArch:      noarch
%python_subpackages

%description
WebOb provides wrappers around the WSGI request environment, and an
object to help create WSGI responses.

The objects map much of the specified behavior of HTTP, including
header parsing and accessors for other standard parts of the
environment.

%if 0%{?suse_version} > 1500
%package -n python-WebOb-doc
Summary:        WSGI request and response object - Documentation
Provides:       %{python_module WebOb-doc = %{version}}

%description -n python-WebOb-doc
This package contains documentation files for %{name}.
%endif

%prep
%autosetup -p1 -n webob-%{version}

%build
%pyproject_wheel
PYTHONPATH=./src sphinx-build -b html docs build/sphinx/html && rm -r build/sphinx/html/.{buildinfo,doctrees}

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license docs/license.txt
%doc CHANGES.txt README.rst
%{python_sitelib}/webob
%{python_sitelib}/WebOb-%{version}.dist-info

%if 0%{?suse_version} > 1500
%files -n python-WebOb-doc
%endif
%doc build/sphinx/html

%changelog
