#
# spec file for package libexttextcat
#
# Copyright (c) 2022 SUSE LLC
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


%{!?make_build:%global make_build make %{?_smp_mflags}}
%define libname libexttextcat-2_0-0
Name:           libexttextcat
Version:        3.4.6
Release:        0
Summary:        Text categorization library datafiles and documents
License:        BSD-4-Clause
Group:          Productivity/Text/Convertors
URL:            https://wiki.documentfoundation.org/Libexttextcat
Source0:        http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  xz
Obsoletes:      libtextcat < 3.2.0
Provides:       libtextcat = %{version}

%description
The %{name} is a library implementing N-gram-based text categorization

%package -n %{libname}
Summary:        Text categorization library
Group:          System/Libraries
Requires:       %{name} = %{version}

%description -n %{libname}
The %{name} is a library implementing N-gram-based text categorization

%package devel
Summary:        Files for Developing with %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Obsoletes:      libtextcat-devel < 3.2.0
Provides:       libtextcat-devel = %{version}

%description devel
The %{name} is a library implementing N-gram-based text categorization

This package contains the libexttextcat development files.

%package tools
Summary:        Tool for creating custom document fingerprints
Group:          Productivity/Text/Convertors

%description tools
The %{name}-tools package contains the createfp program that allows
you to easily create your own document fingerprints.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--disable-werror \
	--docdir=%{_docdir}/%{name}
%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%license LICENSE
%doc README*
%{_datadir}/%{name}*

%files -n %{libname}
%{_libdir}/*.so.0*

%files devel
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}*.pc
%{_includedir}/%{name}*
%{_datadir}/vala/vapi/%{name}.vapi

%files tools
%{_bindir}/*

%changelog
