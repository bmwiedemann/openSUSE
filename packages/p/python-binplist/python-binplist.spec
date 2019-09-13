#
# spec file for package python-binplist
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define upname binplist

# Temporarily switch off python3 build as the upstream package has not
# been converted yet, and the port is not trivial.
%define skip_python3 1

Name:           python-%{upname}
Version:        0.1.5
Release:        0
Summary:        Binary property list (plist) parser module written in python
License:        Apache-2.0
Group:          Development/Libraries/Python
URL:            https://github.com/google/%{upname}
Source:         https://github.com/google/%{upname}/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
binplist is a binary property list (plist) parser module written in python.

%prep
%autosetup -p1 -n %{upname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test -v

%files %{python_files}
%license COPYING
%{_bindir}/plist.py
%{python_sitelib}/binplist-%{version}-py%{python_version}.egg-info
%{python_sitelib}/binplist

%changelog
