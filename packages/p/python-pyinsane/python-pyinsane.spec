#
# spec file for package python-pyinsane
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           python-pyinsane
Version:        1.4.0
Release:        0
License:        GPL-3.0+
Summary:        Python wrapper for SANE
Url:            https://github.com/jflesch/pyinsane
Group:          Development/Languages/Python
Source:         https://pypi.io/packages/source/p/pyinsane/pyinsane-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-Pillow
BuildRequires:  python-nose
Requires:       python-Pillow
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Python library to access and use image scanners (devices).

%prep
%setup -q -n pyinsane-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
