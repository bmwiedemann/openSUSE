#
# spec file for package python-pytest-httpbin
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
Name:           python-pytest-httpbin
Version:        1.0.0
Release:        0
Summary:        Web service for testing HTTP libraries
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/kevin1024/pytest-httpbin
Source:         https://github.com/kevin1024/pytest-httpbin/archive/v%{version}.tar.gz
BuildRequires:  %{python_module httpbin}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-httpbin
Requires:       python-pytest
Requires:       python-six
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v

%files %{python_files}
%doc README.md DESCRIPTION.rst
%{python_sitelib}/*

%changelog
