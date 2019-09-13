#
# spec file for package python-dfwinreg
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
#


%define timestamp 20160428
Name:           python-dfwinreg
Version:        0~%{timestamp}
Release:        0
Summary:        Digital Forensics Windows Registry
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/log2timeline/dfwinreg
Source:         https://github.com/log2timeline/dfwinreg/releases/download/%{timestamp}/dfwinreg-%{timestamp}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  python-setuptools
BuildRequires:  pkgconfig(python)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
dfwinreg, or Digital Forensics Windows Registry, is a Python module that provides read-only access to Windows Registry objects.

%package -n python3-dfwinreg
Summary:        Digital Forensics Date and Time (dfDateTime)
Group:          Development/Languages/Python
BuildRequires:  pkgconfig
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(python3)

%description -n python3-dfwinreg
Python3 version of dfwinreg, or Digital Forensics Windows Registry, a Python module that provides read-only access to Windows Registry objects.

%prep
%setup -q -n dfwinreg-%{timestamp}

%build
python2 setup.py build
python3 setup.py build

%install
python2 setup.py install -O1 --root=%{buildroot}
python3 setup.py install -O1 --root=%{buildroot}
#delete all precombied PYO files
find %{buildroot} -name \*.pyc -delete
find %{buildroot} -name \*.pyo -delete
# these are installed into the wrong place
rm -rf %{buildroot}/usr/share/doc/dfwinreg


%files
%defattr(-,root,root)
%doc ACKNOWLEDGEMENTS AUTHORS README LICENSE
%{_prefix}/lib/python2*/*

%files -n python3-dfwinreg
%defattr(-,root,root)
%doc ACKNOWLEDGEMENTS AUTHORS README LICENSE
%{_prefix}/lib/python3*/*

%changelog
