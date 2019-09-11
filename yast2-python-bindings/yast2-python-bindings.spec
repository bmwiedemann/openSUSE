#
# spec file for package yast2-python-bindings
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%if 0%{?suse_version} > 1310 || 0%{?fedora_version} > 20
%define with_python3 1
%else
%define with_python3 0
%endif

Name:           yast2-python-bindings
Version:        4.1.1
Release:        0
Summary:        Python bindings for the YaST platform
License:        GPL-2.0-only
Group:          System/YaST

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libyui-devel
BuildRequires:  make
BuildRequires:  python
BuildRequires:  python-devel
%if %{with_python3}
BuildRequires:  python3
BuildRequires:  python3-devel
%endif
BuildRequires:  python-rpm-macros
BuildRequires:  swig
BuildRequires:  yast2-core-devel
BuildRequires:  yast2-ycp-ui-bindings
BuildRequires:  yast2-ycp-ui-bindings-devel
Requires:       python
Requires:       yast2-core
Requires:       yast2-ycp-ui-bindings
Obsoletes:      yast2-python-bindings < 4.0.1
Conflicts:      yast2-python3-bindings

%description -n yast2-python-bindings
The bindings allow YaST modules to be written using the Python language
and also Python scripts can use YaST agents, APIs and modules.

%if %{with_python3}
%package -n yast2-python3-bindings
Summary:        Python3 bindings for the YaST platform
Group:          System/YaST
Requires:       python3
Requires:       yast2-core
Requires:       yast2-ycp-ui-bindings
Obsoletes:      yast2-python-bindings == 4.0.1
Conflicts:      yast2-python-bindings

%description -n yast2-python3-bindings
The bindings allow YaST modules to be written using the Python language
and also Python scripts can use YaST agents, APIs and modules.
%endif

%define builddir %{_builddir}/%{name}-%{version}

%prep
%setup -n %{name}-%{version}

%build
make -f Makefile.cvs all
%if %{with_python3}
mkdir py3 && pushd py3
ln -s ../configure configure
%{configure} --enable-python3
%make_build
popd
%endif
mkdir py2 && pushd py2
ln -s ../configure configure
%{configure}
%make_build
popd

%install
%if %{with_python3}
%make_install -C py3
%endif
%make_install -C py2

%if %{with_python3}
%files -n yast2-python3-bindings
%defattr (-, root, root)
%doc %{yast_docdir}
%{python3_sitelib}/*.py
%{python3_sitearch}/_ycp.so
%{yast_plugindir}/libpy2lang_python3.so.*
%{yast_plugindir}/libpy2lang_python3.so
%exclude %dir %{python3_sitelib}/__pycache__
%exclude %{python3_sitelib}/__pycache__/*.pyc
%exclude %{python3_sitelib}/__pycache__/*.pyo
%exclude %{yast_plugindir}/libpy2lang_python3.la
%endif

%files -n yast2-python-bindings
%defattr (-, root, root)
%doc %{yast_docdir}
%{python_sitelib}/*.py
%{python_sitearch}/_ycp.so
%{yast_plugindir}/libpy2lang_python.so.*
%{yast_plugindir}/libpy2lang_python.so
%license COPYING
%exclude %{python_sitelib}/*.pyc
%exclude %{python_sitelib}/*.pyo
%exclude %{yast_plugindir}/libpy2lang_python.la

%changelog
