#
# spec file for package python-WebTest
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


%{?sle15_python_module_pythons}
Name:           python-WebTest
Version:        3.0.3
Release:        0
Summary:        Helper to test WSGI applications
License:        MIT
URL:            https://docs.pylonsproject.org/projects/webtest/
Source:         https://files.pythonhosted.org/packages/source/w/webtest/webtest-%{version}.tar.gz
Patch0:         sphinx-7-fix.patch
BuildRequires:  %{python_module PasteDeploy}
BuildRequires:  %{python_module WSGIProxy2}
BuildRequires:  %{python_module WebOb >= 1.2}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module cssselect}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyquery}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module waitress >= 3.0.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Documentation build requirements:
%if 0%{?suse_version} == 1500
BuildRequires:  python311-Sphinx
BuildRequires:  python311-pylons-sphinx-themes
%else
BuildRequires:  python3-Sphinx
BuildRequires:  python3-pylons-sphinx-themes
%endif
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
%autosetup -p1 -n webtest-%{version}

%build
%pyproject_wheel
sphinx-build -b html docs build/sphinx/html && rm -r build/sphinx/html/.{buildinfo,doctrees}

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license license.rst
%doc CHANGELOG.rst README.rst
%{python_sitelib}/webtest/
%{python_sitelib}/[Ww]eb[Tt]est-%{version}.dist-info

%files -n %{name}-doc
%doc build/sphinx/html

%changelog
