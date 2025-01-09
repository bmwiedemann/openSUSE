#
# spec file for package python-slixmpp
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


Name:           python-slixmpp
Version:        1.8.6
Release:        0
Summary:        Python XMPP (Jabber) Library that Implements Everything as a Plugin
License:        MIT
URL:            https://slixmpp.readthedocs.io/
Source:         https://codeberg.org/poezio/slixmpp/archive/slix-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module aiodns}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  gnupg
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libidn)
Requires:       python-aiodns
Requires:       python-aiohttp
Requires:       python-cryptography
Requires:       python-pyasn1
Requires:       python-pyasn1-modules
%python_subpackages

%description
Slixmpp is an XMPP library for Python. Based on SleekXMPP, it uses
asyncio instead of threads. XEP (XMPP Extended Protocol) coverage is
realized as plugins.

%prep
%autosetup -p1 -n slixmpp
sed -i '/\#\!\/usr\/bin\/env\ python3/d' slixmpp/plugins/xep_0454/__init__.py

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}/

%check
%python_exec run_tests.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/slixmpp
%{python_sitearch}/slixmpp-%{version}.dist-info

%changelog
