#
# spec file for package python-trollius
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


Name:           python-trollius
Version:        2.2
Release:        0
Summary:        Port of the Tulip project (asyncio module, PEP 3156) on Python 2
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/haypo/trollius
Source:         https://files.pythonhosted.org/packages/source/t/trollius/trollius-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-coverage
BuildRequires:  python-futures
BuildRequires:  python-mock
BuildRequires:  python-rpm-macros
BuildRequires:  python-setuptools
BuildRequires:  python-six
BuildRequires:  python-unittest2
Requires:       python-futures
Requires:       python-six
Provides:       python2-trollius = %{version}
BuildArch:      noarch

%description
Trollius provides infrastructure for writing single-threaded concurrent code
using coroutines, multiplexing I/O access over sockets and other resources,
running network clients and servers, and other related primitives.

%prep
%setup -q -n trollius-%{version}
rm -rf trollius.egg-info
# use correct interpreter
sed -e '1c#!python2' -i examples/tcp_echo.py examples/udp_echo.py

%build
%python2_build

%install
%python2_install
%fdupes %{buildroot}%{python2_sitelib}

%check
python2 setup.py test

%files
%license COPYING
%doc AUTHORS README.rst TODO.rst
%doc doc/*.rst doc/trollius.jpg
%doc examples/
%{python2_sitelib}/trollius/
%{python2_sitelib}/trollius-%{version}-*.egg-info/

%changelog
