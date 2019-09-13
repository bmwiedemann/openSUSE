#
# spec file for package python-pymetar
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


%define         modname pymetar

Name:           python-%{modname}
Version:        0.20
Release:        0
Summary:        METAR weather report parser
License:        GPL-2.0+
Group:          Development/Languages/Python
Url:            http://www.schwarzvogel.de/software-pymetar.shtml
Source0:        http://www.schwarzvogel.de/pkgs/pymetar-%{version}.tar.gz
BuildRequires:  python-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version}
%py_requires
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif
%endif
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%description
This library downloads the weather report for a given station ID, decodes
it and provides easy access to all the data found in the report.

%prep
%setup -q -n %{modname}-%{version}

%build
python setup.py build

%install
python setup.py install -O1 --skip-build --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{modname}
%{python_sitelib}/%{modname}.*
%{python_sitelib}/%{modname}-%{version}-py%{py_ver}.egg-info
%{_datadir}/doc/%{modname}-%{version}/
%{_mandir}/man1/%{modname}.1%{?ext_man}

%changelog
