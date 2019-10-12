#
# spec file for package pilot-link
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


Name:           pilot-link
BuildRequires:  bluez-devel
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  libusb-devel
BuildRequires:  pkg-config
BuildRequires:  popt-devel
BuildRequires:  python-devel
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(udev)
Url:            http://www.pilot-link.org/
Version:        0.12.5
Release:        0
Obsoletes:      plink < %{version}
Provides:       plink = %{version}
Summary:        Pilot-Link Based Synchronization Development Header Files
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Hardware/Palm
Source:         http://downloads.pilot-link.org/%{name}-%{version}.tar.bz2
Source1:        10-usb-raw-pda.fdi
Patch0:         %{name}-gcc.patch
Patch1:         %{name}-0.12.1-appointment_buf.diff
Patch2:         %{name}-0.12.1-strncat.diff
Patch4:         %{name}-0.12.3-man.patch
Patch5:         %{name}-0.12.3-free.patch
Patch6:         %{name}-0.12.3-fclose.patch
Patch7:         %{name}-0.12.3-usb-fixes.patch
# PATCH-FIX-UPSTREAM pilot-link-0.12.3-fclose_after_read.patch
Patch8:         %{name}-0.12.3-fclose_after_read.patch
Patch9:         perl-PDA-Pilot-0.12.1-pilotxs.diff
Patch10:        pilot-link-0.12.5-libpng-include.patch
# PATCH-FIX-UPSTREAM pilot-link-0.12.5-perl514.patch idoenmez@suse.de -- Fix compilation with Perl 5.14
Patch11:        pilot-link-0.12.5-perl514.patch
Patch12:        pilot-link-0.12.5-udev-rules.patch
# PATCH-FIX-OPENSUSE pilot-link-stop-messing-with-cflags.patch dimstar@opensuse.org -- Stop mangling Werror from cflags - it's not correcly done anyway
Patch13:        pilot-link-stop-messing-with-cflags.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
pilot-link is a suite of tools used to connect your Palm or PalmOS compatible
handheld with Unix, Linux, and any other POSIX-compatible machine. pilot-link
works with all PalmOS handhelds, including those made by Handspring, Sony,
and Palm, as well as others.

pilot-link includes userspace "conduits" that allow you to synchronize
information to and from your Palm device, as well as libraries of
Palm-compatible functions that allow other applications to take advantage of
the code included in pilot-link.

There are also several language "bindings" that allow you to use your favorite
development language with pilot-link, such as Java, Tcl, Perl, and Python.

Authors:
--------
    Kenneth Albanowski <kjahds@kjahds.com>

%package -n libpisock9
Summary:        Pilot-Link Library for Palm devices
Group:          Hardware/Palm

%description -n libpisock9
Pilot-Link Library for Palm Devices.

If you want to develop Palm synchronization applications, you will need
to install libpisock-devel.

Authors:
--------
    Kenneth Albanowski <kjahds@kjahds.com>

%package -n libpisock-devel
Requires:       libpisock9 = %{version}
Provides:       pilot-link-devel = %{version}
Obsoletes:      pilot-link-devel < %{version}
Summary:        PalmPilot Development Header Files
Group:          Hardware/Palm

%description -n libpisock-devel
This package contains the development headers of libpisock.

Authors:
--------
    Kenneth Albanowski <kjahds@kjahds.com>

%package -n libpisync1
Summary:        Pilot-Link based Synchronization Library for Palm devices
Group:          Hardware/Palm

%description -n libpisync1
Pilot-Link Library for Palm Devices.

If you want to develop Palm synchronization applications, you will need
to install libpisock-devel.

Authors:
--------
    Kenneth Albanowski <kjahds@kjahds.com>

%package -n libpisync-devel
Requires:       libpisync1 = %{version}
Summary:        Pilot-Link based Synchronization Library for Palm devices
Group:          Hardware/Palm

%description -n libpisync-devel
Pilot-Link Library for Palm Devices.

If you want to develop Palm synchronization applications, you will need
to install libpisock-devel.

Authors:
--------
    Kenneth Albanowski <kjahds@kjahds.com>

%package -n python-pisock
Requires:       python
Summary:        Pilot-Link Library for Palm devices - Python bindings
Group:          Development/Libraries/Python

%description -n python-pisock
Pilot-Link Library for Palm Devices.

This package contains the python bindings of libpisock.

Authors:
--------
    Kenneth Albanowski <kjahds@kjahds.com>

%package -n perl-PDA-Pilot
Requires:       perl = %{perl_version}
Summary:        Pilot-Link Library for Palm devices - Perl bindings
Group:          Development/Libraries/Perl

%description -n perl-PDA-Pilot
This package contains Perl modules for communicating with the Palm
Pilot.


%prep
%setup -q
%patch0
%patch1
%patch2
%patch4
%patch5
%patch6
%patch7
%patch8
%patch9
%patch10
%patch11
%patch12
%patch13 -p1
# Force updating bindings/Perl/Pilot.c
rm -f bindings/Perl/Pilot.c

%build
#%{?suse_update_config:%{suse_update_config -f scripts}}
autoreconf -sfi
sed -i 1i\ '#include <sys/socket.h>' libpisock/linuxusb.c 
%configure --enable-threads --enable-conduits --enable-libusb --with-png=/usr --with-bluez --with-libiconv=/usr
make
#
#python subpackage
cd bindings/Python
python setup.py build
#
#perl subpackage
cd ../Perl
perl Makefile.PL

%install
make DESTDIR=$RPM_BUILD_ROOT install
#chmod a+x $RPM_BUILD_ROOT/%{_libdir}/libpisock.so*
# drop udev rule somewhere else...
mkdir -p %{buildroot}%{_udevrulesdir}
sed -i 's/modem/uucp/g' $RPM_BUILD_ROOT/usr/share/pilot-link/udev/60-libpisock.rules
cp $RPM_BUILD_ROOT/usr/share/pilot-link/udev/60-libpisock.rules  %{buildroot}%{_udevrulesdir}
mkdir -p $RPM_BUILD_ROOT/etc/profile.d
echo -e '# use USB by default\nexport PILOTPORT="usb:"' > $RPM_BUILD_ROOT/etc/profile.d/pilot-link.sh
rm $RPM_BUILD_ROOT/%{_libdir}/*.a
rm $RPM_BUILD_ROOT/%{_libdir}/*.la
mkdir -p  $RPM_BUILD_ROOT/usr/share/pilot-link/hal
cp %{S:1} $RPM_BUILD_ROOT/usr/share/pilot-link/hal
#
#python subpackage
cd bindings/Python
mkdir -p "$RPM_BUILD_ROOT"
python setup.py install --prefix=%{_prefix} --optimize=2 --record-rpm=INSTALLED_FILES \
      --root="$RPM_BUILD_ROOT"
#
#perl subpackage
cd ../Perl
make DESTDIR=$RPM_BUILD_ROOT install_vendor INSTALLDIRS=vendor
%perl_process_packlist

%post -n libpisock9 
/sbin/ldconfig
%{?udev_rules_update}

%post -n libpisync1 -p /sbin/ldconfig

%postun -n libpisock9 -p /sbin/ldconfig

%postun -n libpisync1 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING ChangeLog README doc/README.* doc/TODO doc/Coding*
%{_bindir}/*
%{_mandir}/man[17]/*
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/pix/
%dir %{_datadir}/%{name}/prc/
%dir %{_datadir}/%{name}/udev/
%dir %{_datadir}/%{name}/hal/
%{_datadir}/%{name}/pix/*
%{_datadir}/%{name}/prc/*
%{_datadir}/%{name}/udev/*
%{_datadir}/%{name}/hal/*

%files -n libpisock9
%defattr(-,root,root)
%{_libdir}/libpisock*.so.9*
%{_udevrulesdir}/*.rules
%attr(0644,root,root) /etc/profile.d/*

%files -n libpisock-devel
%defattr(-,root,root)
%{_libdir}/libpisock*.so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/pilot-link.m4
%{_includedir}/*
%exclude %{_includedir}/pi-sync.h

%files -n libpisync1
%defattr(-,root,root)
%{_libdir}/libpisync*.so.1*

%files -n libpisync-devel
%defattr(-,root,root)
%{_libdir}/libpisync*.so
%{_includedir}/pi-sync.h

%files -n python-pisock -f bindings/Python/INSTALLED_FILES
%defattr(-,root,root)
%doc bindings/Python/TODO bindings/Python/README

%files -n perl-PDA-Pilot
%defattr(-,root,root)
%doc bindings/Perl/README bindings/Perl/test.pl
%doc %{_mandir}/man3/PDA::Pilot*
%if %suse_version < 1140
/var/adm/perl-modules/%{name}
%endif
%{perl_vendorarch}/PDA
%dir %{perl_vendorarch}/auto/PDA
%{perl_vendorarch}/auto/PDA/Pilot

%changelog
