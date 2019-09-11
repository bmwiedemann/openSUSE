#
# spec file for package dbus-1-mono
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           dbus-1-mono
BuildRequires:  dbus-1-devel dbus-1-glib mono-devel pkgconfig
BuildRequires:  libtool
Url:            http://dbus.freedesktop.org/
License:        GPL-2.0+ or AFL-2.1
Group:          Development/Libraries/Other
Version:        0.63
Release:        188
Summary:        Mono Bindings for D-Bus
Source0:        dbus-sharp-%{version}.tar.gz
Patch0:         dbus-mono-dont-build-examples-thoenig-01.patch
Patch1:         dbus-mono-libdir-thoenig-01.patch
Patch2:         dbus-mono-exit-on-disconnect-thoenig-01.patch
Patch3:         dbus-mono-api-fix-thoenig-01.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       dbus-1 >= %( echo `rpm -q --queryformat '%%{VERSION}-%%{RELEASE}' dbus-1`)

%description
Mono bindings for D-Bus.

%prep
%setup -n dbus-sharp-%{version} -q
%patch0
%patch1
%patch2
%patch3
autoreconf -fi

%build
export CFLAGS="${RPM_OPT_FLAGS} -fstack-protector -fno-strict-aliasing -fPIC"
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
# all the files live in /usr/lib, just this file has a wrong path
perl -pi -e "s|/usr/lib64|/usr/lib|" $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/dbus-sharp.pc

%post
%{run_ldconfig}

%postun
%{run_ldconfig}

%files 
%defattr(-, root, root)
%dir %{_prefix}/lib/mono/gac/dbus-sharp
%{_libdir}/pkgconfig/dbus-sharp.pc
%{_prefix}/lib/mono/gac/dbus-sharp/*
%dir %{_prefix}/lib/mono/dbus-sharp
%{_prefix}/lib/mono/dbus-sharp/*

%changelog
