#
# spec file for package python-caldav
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


%{?sle15_python_module_pythons}

%global modname caldav
Name:           python-%{modname}
Version:        1.4.0
Release:        0
Summary:        CalDAV (RFC4791) client library for Python
License:        Apache-2.0 AND GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/%{modname}
Source:         https://files.pythonhosted.org/packages/source/c/caldav/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module vobject}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-icalendar
Requires:       python-lxml
Requires:       python-requests
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
%autosetup -p1 -n %{modname}-%{version}
# Remove shebangs
find caldav -name "*.py" | xargs sed -i '1 {/^#!/d}'

%build
%pyproject_wheel

%check
# almost all tests are online, would require
# caldav server to run

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license COPYING.APACHE COPYING.GPL
%{python_sitelib}/%{modname}-*.dist-info
%{python_sitelib}/%{modname}/

%changelog
