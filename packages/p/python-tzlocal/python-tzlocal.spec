#
# spec file for package python-tzlocal
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define modname tzlocal
%{?sle15_python_module_pythons}
Name:           python-%{modname}
Version:        5.3.1
Release:        0
Summary:        Timezone information (tzinfo) object for the local timezone
License:        MIT
URL:            https://github.com/regebro/tzlocal
Source:         https://github.com/regebro/tzlocal/archive/%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tzdata}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-tzdata
BuildArch:      noarch
%python_subpackages

%description
This Python module returns the IANA time zone name for your local time zone
or a tzinfo object with the local timezone information, under Unix and
Windows.

This module attempts to fix a glaring hole in the pytz and zoneinfo modules,
that there is no way to get the local timezone information, unless you know
the zoneinfo name, and under several Linux distros that's hard or impossible
to figure out.

With tzlocal you only need to call get_localzone() and you will get a tzinfo
object with the local time zone info. On some Unices you will still not get
to know what the timezone name is, but you don't need that when you have the
tzinfo file. However, if the timezone name is readily available it will be
used.

%prep
%setup -q -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.rst CHANGES.txt
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}.dist-info

%changelog
