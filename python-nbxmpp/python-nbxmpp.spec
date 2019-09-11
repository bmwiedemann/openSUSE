#
# spec file for package python-nbxmpp
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define _name   nbxmpp
Name:           python-nbxmpp
Version:        0.6.10
Release:        0
Summary:        XMPP library by Gajim team
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://dev.gajim.org/gajim/python-nbxmpp
Source:         https://files.pythonhosted.org/packages/source/n/%{_name}/%{_name}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%description
Python-nbxmpp is a Python library that provides a way for Python
applications to use Jabber/XMPP networks in a non-blocking way.
This library is initialy a fork of xmpppy one, but using
non-blocking sockets.

%python_subpackages

%package doc
Summary:        Nbxmpp Documentation
Group:          Documentation/Other

%description doc
This packages provides documentation of Nbxmpp API.

%prep
%setup -q -n %{_name}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/

%files %{python_files}
%license COPYING
%{python_sitelib}/%{_name}/
%{python_sitelib}/%{_name}-*

%files %{python_files doc}
%doc ChangeLog README
%doc doc/apidocs/ doc/examples/

%changelog
