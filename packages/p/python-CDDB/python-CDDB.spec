#
# spec file for package python-CDDB
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python3 1
Name:           python-CDDB
Version:        1.4
Release:        0
Summary:        Python CDDB module
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            http://cddb-py.sourceforge.net
Source:         http://downloads.sourceforge.net/cddb-py/cddb-py/%{version}/CDDB-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
The duo of CDDB.py and DiscID.py, along with their C
module cdrommodule.so, provide a way for Python programs to
fetch information about audio CDs from CDDB (http://www.cddb.com/) -- a
large online database of track listings and other information on
audio CDs.

%prep
%setup -q -n CDDB-%{version}
sed -i -e '/^#!\//, 1d' CDDB.py DiscID.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc CHANGES README
%license COPYING
%{python_sitearch}/CDDB*
%{python_sitearch}/DiscID.*
%{python_sitearch}/cdrom.so

%changelog
