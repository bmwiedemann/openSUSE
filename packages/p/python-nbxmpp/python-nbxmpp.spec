#
# spec file for package python-nbxmpp
#
# Copyright (c) 2021 SUSE LLC
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


# Requires at least python 3.7
%define skip_python2 1
%define skip_python36 1
%define _name   nbxmpp
Name:           python-nbxmpp
Version:        2.0.2
Release:        0
Summary:        XMPP library by Gajim team
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://dev.gajim.org/gajim/python-nbxmpp
Source:         %{url}/-/archive/nbxmpp-%{version}/python-nbxmpp-nbxmpp-%{version}.tar.bz2
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20200714
# For testing
BuildRequires:  %{python_module gobject-Gdk}
BuildRequires:  %{python_module idna}
BuildRequires:  %{python_module precis-i18n}
BuildRequires:  typelib(Soup)
Recommends:     python-gssapi
BuildArch:      noarch
%{?python_enable_dependency_generator}

%python_subpackages

%description
Python-nbxmpp is a Python library that provides a way for Python
applications to use Jabber/XMPP networks in a non-blocking way.
This library is initialy a fork of xmpppy one, but using
non-blocking sockets.

%package doc
Summary:        Nbxmpp Documentation
Group:          Documentation/Other

%description doc
This packages provides documentation of Nbxmpp API.

%prep
%setup -q -n python-nbxmpp-nbxmpp-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/

%check
%pyunittest discover -v

%files %{python_files}
%license COPYING
%{python_sitelib}/%{_name}/
%{python_sitelib}/%{_name}-*

%files %{python_files doc}
%doc ChangeLog README.md
%doc %{_name}/examples/

%changelog
