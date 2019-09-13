#
# spec file for package avrdude
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


%define         libname   lib%{name}
%define         libsoname %{libname}1
Name:           avrdude
Version:        6.3
Release:        0
Summary:        Upload tool for AVR microcontrollers
License:        GPL-2.0+
Group:          Development/Tools/Other
Url:            http://savannah.nongnu.org/projects/avrdude
Source0:        http://download.savannah.gnu.org/releases/avrdude/%{name}-%{version}.tar.gz
Source1:        http://download.savannah.gnu.org/releases/avrdude/%{name}-%{version}.tar.gz.sig
Source3:        modprobe.avrdude_parport
Source4:        avrdude-usbdevices
Source5:        avrdude.keyring
Source6:        debian.avrdude.udev
Patch0:         avrdude-5.11-no-builddate.diff
Patch1:         avrdude-ipv6.patch
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libelf-devel
BuildRequires:  libtool
BuildRequires:  libusb-devel
BuildRequires:  readline-devel
BuildRequires:  texinfo
Requires(post): %{install_info_prereq}
Requires(postun): %{install_info_prereq}
Requires(post): /sbin/modprobe
Provides:       avr-programmer
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?is_opensuse}
BuildRequires:  libftdi1-devel
%endif

%description
avrdude is a tool for AVR microcontrollers and drives many hardware
in-system programmers. avrdude allows programming microcontrollers
through a USB or parallel port of the computer.

%package -n %{libsoname}
Summary:        Shared library of %{name}
Group:          System/Libraries

%description -n %{libsoname}
This package contains the shared lib%{name} library.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This package contains development files for %{name}.

%prep
%setup -q
# avrdude-5.11-no-builddate.diff
%patch0 -p1
# %patch1
touch lexer.l

%build
./bootstrap
sed -i 's/--clean /--tidy /g' doc/Makefile.in
%configure \
        --enable-linuxgpio \
        --disable-static
make %{?_smp_mflags}
make %{?_smp_mflags} -C doc info

%install
%make_install DOC_INST_DIR=%{buildroot}%{_docdir}/%{name}
make -C doc install-info DESTDIR=%{buildroot}
install -D -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/modprobe.d/50-avrdude_parport.conf
rm %{buildroot}%{_libdir}/lib%{name}.la

%if 0%{?suse_version} >= 1230
%global udevdir %{_prefix}/lib/udev
%global tag uaccess
%else
%global udevdir %{_sysconfdir}/udev
%global tag udev-acl
%endif
RULESFILE=%{buildroot}%{udevdir}/rules.d/50-avrdude.rules
mkdir -p ${RULESFILE%/*}
echo '# parport access not supported anymore with avrdude' > $RULESFILE
while IFS=" " read major minor comment;do
    echo "# $comment"
    echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="'$major'", ATTRS{idProduct}=="'$minor'", TAG+="%{tag}"'
done <%{SOURCE4} >> $RULESFILE
chmod 644 $RULESFILE

install -d -m 755 %{buildroot}%{_docdir}/%{name}
install -m 644 AUTHORS COPYING NEWS README %{buildroot}%{_docdir}/%{name}

%post
%if %{?suse_version:1}0
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
if [ "$1" -eq 1 ]; then
  # $1==0 is binary uninstall.
  # $1==1 is binary install.
  # $1==2 is during build
  if [  "$YAST_IS_RUNNING" = "yes" ]; then
    # make life trivial for yast users.
    /sbin/modprobe ppdev
  fi
fi
%endif

%postun
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%post -n %{libsoname} -p /sbin/ldconfig
%postun -n %{libsoname} -p /sbin/ldconfig

%files
%defattr (-, root, root)
%{_docdir}/%{name}
%{_mandir}/*/*
%{_infodir}/%{name}.info%{ext_info}
%config %{_sysconfdir}/avrdude.conf
%dir %{_sysconfdir}/modprobe.d
%config %{_sysconfdir}/modprobe.d/50-avrdude_parport.conf
%{udevdir}
%{_bindir}/*

%files devel
%defattr (-, root, root)
%{_includedir}/libavrdude.h
%{_libdir}/libavrdude.so

%files -n %{libsoname}
%defattr(-,root,root)
%{_libdir}/libavrdude.so.*

%changelog
