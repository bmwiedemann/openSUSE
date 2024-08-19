#
# spec file for package python-xapp
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


%define         skip_python2 1
%define         _name python3-xapp
Name:           python-xapp
Version:        2.4.2
Release:        0
Summary:        Python XApp library
License:        GPL-2.0-or-later
URL:            https://github.com/linuxmint/python3-xapp
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        setup.py
# PATCH-FEATURE-OPENSUSE python-xapp-xdgsu.patch -- Escalate privileges using xdg-su.
Patch0:         python-xapp-xdgsu.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-psutil
Requires:       xdg-utils
BuildArch:      noarch

%description
This project gathers the components which are common to multiple
desktop environments and required to implement cross-DE solutions.

%python_subpackages

%prep
%autosetup -p1 -n %{_name}-%{version}
cp %{SOURCE1} .
# let's change the version in setup.py
sed -i 's|version = "0.0.0",|version = "%{version}",|g' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license COPYING
%doc debian/changelog
%{python_sitelib}/xapp/
%{python_sitelib}/python_xapp-*.egg-info

%changelog
