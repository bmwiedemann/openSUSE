#
# spec file for package python-retry-requests
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-retry-requests
Version:        2.0.0
Release:        0
Summary:        Make requests's sessions auto-retry on failure
License:        GPL-3.0-or-later
URL:            https://github.com/bustawin/retry-requests
Source:         https://files.pythonhosted.org/packages/source/r/retry-requests/retry-requests-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
Requires:       python-urllib3 >= 1.26
BuildArch:      noarch
%python_subpackages

%description
Make requests's sessions auto-retry on failure.

%prep
%autosetup -p1 -n retry-requests-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# test suite requires internet

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/retry_requests
%{python_sitelib}/retry_requests-%{version}.dist-info

%changelog
