#
# spec file for package python-nbxmpp
#
# Copyright (c) 2024 SUSE LLC
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


# Requires at least python 3.10
%define skip_python38 1
%define skip_python39 1
%{?sle15_python_module_pythons}
%define _name   nbxmpp
Name:           python-nbxmpp
Version:        5.0.0
Release:        0
Summary:        XMPP library by Gajim team
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://dev.gajim.org/gajim/python-nbxmpp
Source:         %{url}/-/archive/%{version}/python-nbxmpp-%{version}.tar.bz2
BuildRequires:  %{python_module setuptools >= 65.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-generators >= 20220912
BuildRequires:  python-rpm-macros >= 20220912
# For testing
BuildRequires:  %{python_module gobject-Gdk >= 3.42}
BuildRequires:  %{python_module idna}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module precis-i18n}
BuildRequires:  %{python_module sqlite3}
BuildRequires:  %{python_module wheel}
BuildRequires:  typelib(Soup) = 3.0
Requires:       python-gobject >= 3.42
Requires:       python-idna
Requires:       python-packaging
Requires:       python-precis-i18n >= 1.0.0
Recommends:     python-gssapi
BuildArch:      noarch

%python_subpackages

%description
Python-nbxmpp is a Python library that provides a way for Python
applications to use Jabber/XMPP networks in a non-blocking way.
This library is initialy a fork of xmpppy one, but using
non-blocking sockets.

%prep
%setup -q

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/

%check
%pyunittest discover -v

%files %{python_files}
%license COPYING
%doc ChangeLog README.md
%{python_sitelib}/%{_name}/
%{python_sitelib}/%{_name}-*

%changelog
