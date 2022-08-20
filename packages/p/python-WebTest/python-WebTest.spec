#
# spec file for package python-WebTest
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-WebTest
Version:        3.0.0
Release:        0
Summary:        Helper to test WSGI applications
License:        MIT
Group:          Development/Languages/Python
URL:            https://docs.pylonsproject.org/projects/webtest/
Source:         https://files.pythonhosted.org/packages/source/W/WebTest/WebTest-%{version}.tar.gz
BuildRequires:  %{python_module PasteDeploy}
BuildRequires:  %{python_module WSGIProxy2}
BuildRequires:  %{python_module WebOb >= 1.2}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module cssselect}
BuildRequires:  %{python_module pyquery}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module waitress >= 0.8.5}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Documentation build requirements:
BuildRequires:  python3-Sphinx
BuildRequires:  python3-pylons-sphinx-themes
Requires:       python-WebOb >= 1.2
Requires:       python-beautifulsoup4
Requires:       python-waitress >= 0.8.5
BuildArch:      noarch
%python_subpackages

%description
This wraps any WSGI application and makes it easy to send test
requests to that application, without starting up an HTTP server.

This provides convenient full-stack testing of applications written
with any WSGI-compatible framework.

%package -n %{name}-doc
Summary:        Helper to test WSGI applications - Documentation
Group:          Documentation/HTML
Provides:       %{python_module WebTest-doc = %{version}}

%description  -n %{name}-doc
This package contains documentation files for %{name}.

%prep
%setup -q -n WebTest-%{version}

%build
%python_build
python3 setup.py build_sphinx && rm build/sphinx/html/.buildinfo

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license license.rst
%doc CHANGELOG.rst README.rst
%{python_sitelib}/webtest/
%{python_sitelib}/WebTest-%{version}*-info

%files -n %{name}-doc
%doc build/sphinx/html

%changelog
