#
# spec file for package python-caldav
#
# Copyright (c) 2020 SUSE LLC
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
%global modname caldav
Name:           python-%{modname}
Version:        0.7.1
Release:        0
Summary:        CalDAV (RFC4791) client library for Python
License:        GPL-3.0-or-later AND Apache-2.0
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/%{modname}
Source:         https://files.pythonhosted.org/packages/source/c/caldav/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module vobject}
BuildRequires:  python-rpm-macros
Requires:       python-lxml
Requires:       python-requests
Requires:       python-six
Requires:       python-vobject
BuildArch:      noarch
%ifpython2
Requires:       python-pytz
Requires:       python-tzlocal
%endif
%python_subpackages

%description
This project is a CalDAV (RFC4791) client library for Python.

It can read all the tags, but only write a few things (create calendars,
events, modify events and properties).

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%check
# almost all tests are online, would require
# caldav server to run

%install
%python_install

%files %{python_files}
%license COPYING.APACHE COPYING.GPL
%{python_sitelib}/%{modname}-%{version}-py*.egg-info
%{python_sitelib}/%{modname}/

%changelog
