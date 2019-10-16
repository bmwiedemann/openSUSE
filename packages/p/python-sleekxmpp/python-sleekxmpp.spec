#
# spec file for package python-sleekxmpp
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
%define _name   sleekxmpp
Name:           python-sleekxmpp
Version:        1.3.3
Release:        0
Summary:        Python XMPP (Jabber) Library that Implements Everything as a Plugin
License:        MIT
URL:            https://github.com/fritzy/SleekXMPP
# https://github.com/fritzy/SleekXMPP/issues/505
Source:         https://github.com/fritzy/SleekXMPP/archive/sleek-%{version}.tar.gz
# PATCH-FIX-OPENSUSE sleekxmpp-fix-dnspython.patch sor.alexei@meowr.ru -- Fix compatibility with recent dnspython.
Patch0:         %{_name}-fix-dnspython.patch
# PATCH-FIX-OPENSUSE sleekxmpp-fix-legacyauth.patch nyov@nexnode.net -- Fix an error in legacyauth support.
Patch1:         %{_name}-fix-legacyauth.patch
# PATCH-FIX-OPENSUSE sleekxmpp-check-roster-push-origin.patch bsc#1014976 mathieui@mathieui.net -- Check origin of roster pushes (slixmpp commits ffdb6ff, ffd9436).
Patch2:         %{_name}-check-roster-push-origin.patch
BuildRequires:  %{python_module dnspython}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2
BuildRequires:  python3
Requires:       python-dnspython
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  gpg
# /SECTION

%description
SleekXMPP is an MIT licensed XMPP library for Python. The goals of
the project are ease of implementation, and complete draft XEP
(XMPP Extended Protocol) coverage. Ideally the community will be
able to use this for bots, easy XEP protocoling, etc.

%python_subpackages

%prep
%setup -q -n SleekXMPP-sleek-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/

%check
# test_overall.py is skipped by upstream testall.py, too
rm tests/{live_*.py,test_overall.py}
# https://github.com/fritzy/SleekXMPP/issues/504
%pytest -k 'not testUnknownException'

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/%{_name}/
%{python_sitelib}/%{_name}-%{version}-py%{python_version}.egg-info

%changelog
