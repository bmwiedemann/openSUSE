#
# spec file for package python-socksio
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-socksio
Version:        1.0.0
Release:        0
Summary:        Sans-I/O implementation of SOCKS4, SOCKS4A, and SOCKS5
License:        MIT
URL:            https://github.com/sethmlarson/socksio
Source:         https://files.pythonhosted.org/packages/source/s/socksio/socksio-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module flit-core >= 2}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
# Test requirements
BuildRequires:  %{python_module pytest}
#
BuildArch:      noarch
%python_subpackages

%description
Client-side sans-I/O SOCKS proxy implementation.
Supports SOCKS4, SOCKS4A, and SOCKS5.

`socksio` is a sans-I/O library similar to
[`h11`](https://github.com/python-hyper/h11) or
[`h2`](https://github.com/python-hyper/hyper-h2/), this means the library itself
does not handle the actual sending of the bytes through the network, it only
deals with the implementation details of the SOCKS protocols so you can use
it in any I/O library you want.

%prep
%autosetup -p1 -n socksio-%{version}

# no coverage
rm pytest.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/socksio
%{python_sitelib}/socksio-%{version}.dist-info

%changelog
