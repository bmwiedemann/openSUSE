#
# spec file for package pthread-stubs
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


#
%define name_archive libpthread-stubs

Name:           pthread-stubs
Version:        0.4
Release:        0
BuildRequires:  pkg-config

#BuildRequires:  autoconf >= 2.60
#BuildRequires:  automake
#BuildRequires:  libtool

Url:            http://xorg.freedesktop.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        The X Protocol
License:        MIT
Group:          Development/Libraries/X11 
#Source URL:    http://xcb.freedesktop.org/dist/
Source:         %{name_archive}-%{version}.tar.bz2

%description
The pthread-stubs for for X development

%package -n %{name}-devel
Summary:        The X Protocol
Group:          Development/Libraries/X11

# Added within the 13.2 Development Cycle
Provides:       xorg-x11-proto-devel://usr/%{_lib}/pkgconfig/pthread-stubs.pc

%description -n %{name}-devel
The pthread-stubs for X development

%prep
%setup -n %{name_archive}-%{version} -q

%build
#autoreconf -fi
./configure CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" \
              --prefix=/usr --libdir=%{_libdir}
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"

%files -n %{name}-devel
%defattr(-,root,root)
%doc COPYING
/usr/%{_lib}/pkgconfig/*.pc

%changelog
