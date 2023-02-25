#
# spec file for package yast2-python-bindings
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_without python3
%if 0%{?sle_version} <= 150300
%bcond_without python2
%else
%bcond_with python2
%endif
Name:           yast2-python-bindings
Version:        4.5.2
Release:        0
Summary:        Python bindings for the YaST platform
License:        GPL-2.0-only
Group:          System/YaST
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libyui-devel
BuildRequires:  make
%if %{with python2}
BuildRequires:  python
%endif
BuildRequires:  python-rpm-macros
BuildRequires:  swig
BuildRequires:  yast2-core-devel
BuildRequires:  yast2-ycp-ui-bindings
BuildRequires:  yast2-ycp-ui-bindings-devel
%if %{with python2}
Requires:       python
%endif
Requires:       yast2-core
Requires:       yast2-ycp-ui-bindings
Conflicts:      yast2-python3-bindings
Obsoletes:      yast2-python-bindings < 4.0.1
%if %{with python2}
BuildRequires:  python-devel
%endif
%if %{with python3}
BuildRequires:  python3-devel
%endif

%description -n yast2-python-bindings
The bindings allow YaST modules to be written using the Python language
and also Python scripts can use YaST agents, APIs and modules.

%package -n yast2-python3-bindings
Summary:        Python3 bindings for the YaST platform
Group:          System/YaST
BuildRequires:  python3
Requires:       python3
Requires:       yast2-core
Requires:       yast2-ycp-ui-bindings
Conflicts:      yast2-python-bindings
Obsoletes:      yast2-python-bindings = 4.0.1

%description -n yast2-python3-bindings
The bindings allow YaST modules to be written using the Python language
and also Python scripts can use YaST agents, APIs and modules.

%prep
%setup -q

%build
make %{?_smp_mflags} -f Makefile.cvs all
%if %{with python3}
mkdir py3 && pushd py3
ln -s ../configure configure
%configure --enable-python3
%make_build
popd
%endif
%if %{with python2}
mkdir py2 && pushd py2
ln -s ../configure configure
%configure
%make_build
popd
%endif

%install
%if %{with_python3}
%make_install -C py3
%endif
%if %{with python2}
%make_install -C py2
%endif

%if %{with python3}
%files -n yast2-python3-bindings
%doc %{yast_docdir}
%{python3_sitelib}/*
%{python3_sitearch}/_ycp.so
%{yast_plugindir}/libpy2lang_python3.so.*
%{yast_plugindir}/libpy2lang_python3.so
%exclude %{yast_plugindir}/libpy2lang_python3.la
%endif

%if %{with python2}
%files -n yast2-python-bindings
%doc %{yast_docdir}
%{python_sitelib}/*
%{python_sitearch}/_ycp.so
%{yast_plugindir}/libpy2lang_python.so.*
%{yast_plugindir}/libpy2lang_python.so
%license COPYING
%exclude %{yast_plugindir}/libpy2lang_python.la
%endif

%changelog
