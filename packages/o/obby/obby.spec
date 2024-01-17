#
# spec file for package obby
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           obby
Version:        0.4.8
Release:        0
Summary:        Synced document buffers
License:        GPL-2.0+
Group:          Productivity/Networking/Other
Url:            http://gobby.0x539.de/
Source:         http://releases.0x539.de/obby/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libavahi-devel
BuildRequires:  net6-devel
BuildRequires:  pkg-config
Requires:       %{name}-lang = %{version}
Requires:       libobby-0_4-1 = %{version}

%description
obby is a library which provides synced document buffers. It supports
multiple documents in one session and is portable to both Windows and
Unix-like platforms.



Authors:
--------
    Armin Burgmeier <armin@0x539.de>
    Philipp Kern <phil@0x539.de>

%package -n libobby-0_4-1
Summary:        Synced document buffers
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description -n libobby-0_4-1
obby is a library which provides synced document buffers. It supports
multiple documents in one session and is portable to both Windows and
Unix-like platforms.



Authors:
--------
    Armin Burgmeier <armin@0x539.de>
    Philipp Kern <phil@0x539.de>

%package devel
Summary:        Synced document buffers
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version} net6-devel libavahi-devel libsigc++2-devel

%description devel
obby is a library which provides synced document buffers. It supports
multiple documents in one session and is portable to both Windows and
Unix-like platforms.



Authors:
--------
    Armin Burgmeier <armin@0x539.de>
    Philipp Kern <phil@0x539.de>

%lang_package
%prep
%setup -q

%build
%configure \
	--enable-ipv6 \
	--with-zeroconf \
	--with-pic \
	--disable-static
make %{?_smp_mflags}

%install
%makeinstall
%find_lang %{name}
#warning found pointless la file
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/libobby.la
%fdupes %buildroot/%_prefix

%post -n libobby-0_4-1 -p /sbin/ldconfig

%postun -n libobby-0_4-1 -p /sbin/ldconfig

%files 
%defattr (-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README

%files -n libobby-0_4-1
%defattr(-, root, root)
%{_libdir}/*.so.*

%files devel
%defattr (-, root, root)
%{_includedir}/obby
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files lang -f %{name}.lang

%changelog
