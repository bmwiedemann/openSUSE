#
# spec file for package python-slixmpp
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


%define skip_python2 1
%define skip_python36 1
%define _name   slixmpp
Name:           python-slixmpp
Version:        1.8.3
Release:        0
Summary:        Python XMPP (Jabber) Library that Implements Everything as a Plugin
License:        MIT
URL:            https://slixmpp.readthedocs.io/
Source:         https://lab.louiz.org/poezio/slixmpp/-/archive/slix-%{version}/slixmpp-slix-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE slixmpp-fix-legacyauth.patch nyov@nexnode.net -- Fix an error in legacyauth support.
Patch0:         %{_name}-fix-legacyauth.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module dnspython}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  gnupg
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libidn)
Requires:       python-aiohttp
Requires:       python-dnspython
%python_subpackages

%description
Slixmpp is an XMPP library for Python. Based on SleekXMPP, it uses
asyncio instead of threads. XEP (XMPP Extended Protocol) coverage is
realized as plugins.

%prep
%setup -q -n %{_name}-slix-%{version}
%patch0 -p1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}/

%check
%pyunittest -v tests

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/%{_name}/
%{python_sitearch}/%{_name}-*

%changelog
