#
# spec file for package meanwhile
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


%define soname  libmeanwhile
%define sover   1
Name:           meanwhile
Version:        1.1.1
Release:        0
Summary:        IBM Sametime Community Client Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/obriencj/meanwhile
Source:         https://github.com/obriencj/meanwhile/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE meanwhile-use-libtommath.patch boo#1086826 sor.alexei@meowr.ru -- Use LibTomMath as an MPI instead of the bundled code.
Patch0:         meanwhile-use-libtommath.patch
# PATCH-FIX-OPENSUSE meanwhile-fix-warnings.patch -- Fix various warnings.
Patch1:         meanwhile-fix-warnings.patch
# PATCH-FIX-OPENSUSE meanwhile-fix-groupchat.patch pidgin#12637 -- Fix for group chat crashes with IBM Notes version 8.5.1 by Jonathan Rice.
Patch2:         meanwhile-fix-groupchat.patch
# PATCH-FIX-OPENSUSE meanwhile-fix-filetransfer.patch mikael.berthe@lilotux.net -- Fix file transfers with recent Sametime servers.
Patch3:         meanwhile-fix-filetransfer.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtommath-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)

%description
A library to establish instant messaging connections to the IBM
Sametime IM server.

%package -n %{soname}%{sover}
Summary:        IBM Sametime Community Client Library
# libmeanwhile was last used in openSUSE 12.2.
Group:          System/Libraries
Obsoletes:      %{soname} < %{version}
Provides:       %{soname} = %{version}

%description -n %{soname}%{sover}
A library to establish instant messaging connections to the IBM
Sametime IM server.

%package devel
Summary:        IBM Sametime Community Client library
Group:          Development/Libraries/C and C++
Requires:       %{soname}%{sover} = %{version}
Requires:       pkgconfig(glib-2.0)

%description devel
A library to establish instant messaging connections to the IBM
Sametime IM server.

%package doc
Summary:        IBM Sametime Community Client library
Group:          Development/Libraries/C and C++

%description doc
A library to establish instant messaging connections to the IBM
Sametime IM server.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
touch configwrap && chmod a+x configwrap

%build
./autogen.sh
%configure \
  --disable-doxygen \
  --disable-mailme  \
  --disable-static
make %{?_smp_mflags} V=1

%install
%make_install \
  sampledir=%{_docdir}/%{name}/samples

chmod a-x %{buildroot}%{_docdir}/%{name}/samples/build
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files -n %{soname}%{sover}
%license COPYING
%doc ChangeLog README
%{_libdir}/%{soname}.so.%{sover}*

%files devel
%{_includedir}/meanwhile/
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/meanwhile.pc

%files doc
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/samples/

%changelog
