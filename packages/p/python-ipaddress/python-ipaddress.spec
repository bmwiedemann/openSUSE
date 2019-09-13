#
# spec file for package python-ipaddress
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           python-ipaddress
Version:        1.0.22
Release:        0
Summary:        Backport of the Python3 IPv4/IPv6 manipulation library to older Python versions
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/phihag/ipaddress
Source:         https://files.pythonhosted.org/packages/source/i/ipaddress/ipaddress-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Provides:       python2-ipaddress
BuildArch:      noarch

%description
Backport of the Python 3.3+ IPv4/IPv6 manipulation library to older Python versions

%prep
%setup -q -n ipaddress-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%license LICENSE
%doc README.md README
%{python_sitelib}/*

%changelog
