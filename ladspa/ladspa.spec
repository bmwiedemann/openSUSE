#
# spec file for package ladspa
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


Name:           ladspa
Version:        1.15
Release:        0
Summary:        The Linux Audio Developer's Simple Plug-In API
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Sound/Utilities
Url:            http://www.ladspa.org/
Source:         http://www.ladspa.org/download/%{name}_sdk_%{version}.tgz
Source1:        baselibs.conf
BuildRequires:  gcc-c++
AutoReq:        on
Autoprov:       off

%description
The Linux Audio Developer's Simple Plug-in API (LADSPA) provides the
ability to write simple plug-in audio processors in C/C++ and link them
dynamically.  This package contains the plugins built from LADSPA SDK.

%package devel
Summary:        Include Files mandatory for Development
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description devel
This package contains include files to develop LADSPA plugins.

%prep
%setup -q -n %{name}_sdk_%{version}
%autopatch -p0

%build
export LADSPA_PATH="%{_libdir}/ladspa"
make -C src CFLAGS="-I. %{optflags} -fPIC -ggdb -DDEFAULT_LADSPA_PATH=%{_libdir}/ladspa" targets

%install
make -C src \
     INSTALL_PLUGINS_DIR=%{buildroot}%{_libdir}/ladspa \
     INSTALL_INCLUDE_DIR=%{buildroot}%{_includedir} \
     INSTALL_BINARY_DIR=%{buildroot}%{_bindir} install
# devel package
mkdir -p %{buildroot}%{_docdir}/%{name}-devel
cp -av doc/* %{buildroot}%{_docdir}/%{name}-devel
ln -sf %{_includedir}/ladspa.h %{buildroot}%{_docdir}/%{name}-devel/ladspa.h.txt

%files
%defattr(-,root,root)
%doc README
%license doc/COPYING
%{_libdir}/ladspa
%{_bindir}/*

%files devel
%defattr(-,root,root)
%doc %{_docdir}/%{name}-devel
%{_includedir}/*

%changelog
