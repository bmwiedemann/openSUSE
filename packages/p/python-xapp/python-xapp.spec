#
# spec file for package python-xapp
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


%define skip_python2 1
%define _name python3-xapp
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-xapp
Version:        2.0.1
Release:        0
Summary:        Python XApp library
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/linuxmint/python3-xapp
Source:         https://github.com/linuxmint/python3-xapp/archive/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE python-xapp-xdgsu.patch -- Escalate privileges using xdg-su.
Patch0:         python-xapp-xdgsu.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-psutil
Requires:       xdg-utils
BuildArch:      noarch

%description
This project gathers the components which are common to multiple
desktop environments and required to implement cross-DE solutions.

%python_subpackages

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install

%files %{python_files}
%license COPYING
%doc debian/changelog
%{python_sitelib}/xapp/
%{python_sitelib}/python_xapp-*.egg-info

%changelog
