#
# spec file for package python-retry_decorator
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
Name:           python-retry_decorator
Version:        1.0.0
Release:        0
Summary:        Retry Decorator
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/pnpnpn/retry-decorator
# https://github.com/pnpnpn/retry-decorator/issues/15
Source:         https://github.com/pnpnpn/retry-decorator/archive/v%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
Decorator to support retry when an exception occurs.

%prep
%setup -q -n retry-decorator-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%doc README.rst CHANGES.txt
%{python_sitelib}/*

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python tests/test_retry.py

%changelog
