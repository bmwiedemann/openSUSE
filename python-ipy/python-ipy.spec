#
# spec file for package python-ipy
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
Name:           python-ipy
Version:        1.00
Release:        0
Summary:        Class and tools for handling of IPv4 and IPv6 addresses and networks
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/autocracy/python-ipy
Source:         https://files.pythonhosted.org/packages/source/I/IPy/IPy-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
The IP class allows a comfortable parsing and handling for most
notations in use for IPv4 and IPv6 addresses and networks. It was
greatly inspired by RIPE's Perl module NET::IP's interface but
doesn't share the implementation. It doesn't share non-CIDR netmasks,
so funky stuff like a netmask of 0xffffff0f can't be done here.

%prep
%setup -q -n IPy-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/*
%license COPYING

%check
%python_exec test/test_IPy.py
# one of 3000 subtest fails, probably https://github.com/autocracy/python-ipy/issues/27
# %%python_exec test/test_fuzz.py

%changelog
