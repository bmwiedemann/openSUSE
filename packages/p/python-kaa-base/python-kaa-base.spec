#
# spec file for package python-kaa-base
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name   kaa-base
%if 0%{?suse_version} <= 1110
%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(True))")}
%endif
Name:           python-kaa-base
Version:        0.6.0
Release:        0
Summary:        The Kaa Media Repository Base Library
License:        LGPL-2.1+
Group:          Development/Languages/Python
Url:            http://api.freevo.org/kaa-base
Source:         https://github.com/freevo/%{_name}/archive/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  glib2-devel
BuildRequires:  python-devel
Requires:       python-sqlite2
%if 0%{?suse_version} >= 1220
BuildRequires:  python-libxml2
BuildRequires:  python-xml
Requires:       python-libxml2
Requires:       python-xml
%else
BuildRequires:  libxml2-python
BuildRequires:  pyxml
Requires:       libxml2-python
Requires:       pyxml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%py_requires
%endif

%description
The Kaa Media Repository is a set of python modules related to
media. This module contains some basic code needed in all kaa
modules. This is a requirement for all the other modules in the
repository.

%prep
%setup -q -n %{_name}-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
python2 setup.py build

%install
python2 setup.py install \
  --root=%{buildroot} --prefix=%{_prefix}

%fdupes %{buildroot}%{python_sitearch}/

%files
%defattr(-,root,root)
%doc doc/ API_CHANGES AUTHORS COPYING NEWS README TODO
%{python_sitearch}/kaa/
%{python_sitearch}/kaa_base*

%changelog
