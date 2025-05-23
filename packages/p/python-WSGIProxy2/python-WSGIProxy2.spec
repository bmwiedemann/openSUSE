#
# spec file for package python-WSGIProxy2
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-WSGIProxy2%{psuffix}
Version:        0.5.1
Release:        0
Summary:        WSGI Proxy Implementation
License:        MIT
URL:            https://github.com/gawel/WSGIProxy2/
Source:         https://files.pythonhosted.org/packages/source/W/WSGIProxy2/WSGIProxy2-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-WebOb
Requires:       python-requests
Requires:       python-urllib3
Conflicts:      python-WSGIProxy
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module WebOb}
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module urllib3}
%endif
%python_subpackages

%description
Proxy support for WebOb or classic WSGI applications

%prep
%setup -q -n WSGIProxy2-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# test_quoted_utf8_url: randomly fails
%pytest -k 'not test_quoted_utf8_url'
%endif

%if !%{with test}
%files %{python_files}
%license COPYING
%doc CHANGES.rst README.rst
%{python_sitelib}/wsgiproxy
%{python_sitelib}/[Ww][Ss][Gg][Ii][Pp]roxy2-%{version}*-info
%endif

%changelog
