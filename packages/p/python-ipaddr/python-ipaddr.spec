#
# spec file for package python-ipaddr
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
Name:           python-ipaddr
Version:        2.2.0
Release:        0
Summary:        Google's IP address manipulation library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://code.google.com/p/ipaddr-py/
Source:         https://files.pythonhosted.org/packages/source/i/ipaddr/ipaddr-%{version}.tar.gz
BuildRequires:  %{python_module pkginfo}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Google's IP address manipulation library. An IPv4/IPv6 manipulation library
in Python. This library is used to create/poke/manipulate IPv4 and IPv6
addresses and prefixes.

%prep
%setup -q -n ipaddr-%{version}
sed -i "1d" ipaddr.py # Fix non-executable script

%build
%python_build

%install
%python_install

%check
%{python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python ipaddr_test.py}

%files %{python_files}
%license COPYING
%doc README
%{python_sitelib}/*

%changelog
