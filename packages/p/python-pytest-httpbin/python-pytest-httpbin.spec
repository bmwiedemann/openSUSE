#
# spec file for package python-pytest-httpbin
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pytest-httpbin
Version:        1.0.2
Release:        0
Summary:        Web service for testing HTTP libraries
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/kevin1024/pytest-httpbin
Source:         https://files.pythonhosted.org/packages/source/p/pytest-httpbin/pytest-httpbin-%{version}.tar.gz
Source99:       pytest-httpbin-rpmlintrc
# https://github.com/kevin1024/pytest-httpbin/issues/75
Patch0:         python-pytest-httpbin-no-six.patch
BuildRequires:  %{python_module httpbin}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-httpbin
Requires:       python-pytest
BuildArch:      noarch
%python_subpackages

%description
httpbin is a web service for testing HTTP libraries. It has several
endpoints that can test parts needed in a HTTP library.

Pytest-httpbin creates a pytest "fixture" that is
dependency-injected into your tests. It automatically starts up a HTTP server
in a separate thread running httpbin and provides your test with the URL in the
fixture.

%prep
%setup -q -n pytest-httpbin-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Flask 2.1 returns relative URLs again
# gh#kevin1024/pytest-httpbin#64
%pytest -k "not test_redirect_location_is_https_for_secure_server"

%files %{python_files}
%doc README.md DESCRIPTION.rst
%{python_sitelib}/pytest_httpbin
%{python_sitelib}/pytest_httpbin-%{version}*-info

%changelog
