#
# spec file for package input-pad
#
# Copyright (c) 2024 SUSE LLC
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


%define libinput_paddir %{_libdir}/%{name}-1.1
%define moduledir       %{_libdir}/%{name}-1.1/modules
%define kbduidir        %{_libdir}/%{name}-1.1/modules/kbdui
%define xkeysenddir     %{_libdir}/%{name}-1.1/modules/xkeysend
%define build_xtest    (0%{suse_version} > 1210)

Name:           input-pad
Version:        1.0.99.20210817
Release:        0
Summary:        On-screen Input Pad to Send Characters with Mouse
License:        LGPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/fujiwarat/input-pad
Source0:        https://github.com/fujiwarat/input-pad/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gettext-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libtool
%if 0%{suse_version} > 1210
BuildRequires:  libxkbfile-devel
%endif
BuildRequires:  intltool
BuildRequires:  libxklavier-devel >= 4.0
BuildRequires:  libxml2-devel >= 2.0
BuildRequires:  pkgconfig
%if %{build_xtest}
BuildRequires:  libXtst-devel
%endif
BuildRequires:  eekboard-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  swig
BuildRequires:  pkgconfig(glib-2.0) >= 2.37
Requires:       python3-gobject
Obsoletes:      python-input-pad

%description
The input pad is a tool to send a character on button to text applications.

%package devel
Summary:        Development tools for input-pad
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}

%description devel
The input-pad-devel package contains the header files.


%if %{build_xtest}
%package xtest
Summary:        Input Pad with XTEST extension
Group:          System/Libraries
Requires:       %{name} = %{version}-%{release}

%description xtest
The input-pad-xtest package contains XTEST extension module
%endif

%package eek
Summary:        Input Pad with eekboard extension
Group:          System/Libraries
Requires:       %{name} = %{version}-%{release}

%description eek
The input-pad-eek package contains eekboard extension module

%prep
%setup -q

%build
%if %{suse_version} > 1500
export CFLAGS='-O2 -Wall -D_FORTIFY_SOURCE=2 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -flto=8'
export CXXFLAGS='-O2 -Wall -D_FORTIFY_SOURCE=2 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -flto=8'
export FFLAGS='-O2 -Wall -D_FORTIFY_SOURCE=2 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -flto=8 '
export FCFLAGS='-O2 -Wall -D_FORTIFY_SOURCE=2 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -flto=8 '
%endif
%configure    --enable-pygobject2         \
              --enable-eek                \
%if %{build_xtest}
             --enable-xtest              \
%endif
             --disable-static

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'

if [ ! -d $RPM_BUILD_ROOT%kbduidir ] ; then
    mkdir -p $RPM_BUILD_ROOT%kbduidir
fi
if [ ! -d $RPM_BUILD_ROOT%xkeysenddir ] ; then
    mkdir -p $RPM_BUILD_ROOT%xkeysenddir
fi

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
%if %{build_xtest}
rm -f $RPM_BUILD_ROOT%{xkeysenddir}/*.la
rm -f $RPM_BUILD_ROOT%{xkeysenddir}/*.a
%endif
rm -f $RPM_BUILD_ROOT%{kbduidir}/*.la
rm -f $RPM_BUILD_ROOT%{kbduidir}/*.a

%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_bindir}/input-pad
%dir %libinput_paddir
%dir %moduledir
%dir %xkeysenddir
%dir %kbduidir
%{_libdir}/libinput-pad-*.so.*
%{_libdir}/girepository-1.0/InputPad-1.1.typelib
%{_datadir}/%name
%{_datadir}/pixmaps/input-pad.png
%{_mandir}/man1/input-pad.1.gz

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}-1.1
%{_libdir}/libinput-pad-*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/InputPad-1.1.gir

%if %{build_xtest}
%files xtest
%defattr(-,root,root,-)
%xkeysenddir/libinput-pad-xtest-gdk.so
%endif

%files eek
%defattr(-,root,root,-)
%kbduidir/libinput-pad-eek-gtk.so

%changelog
