#
# spec file for package avrdude
#
# Copyright (c) 2023 SUSE LLC
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


%global modprobe_d_files 50-avrdude_parport.conf
%define         libname   lib%{name}
%define         libsoname %{libname}1
%if 0%{?suse_version} < 1550 && 0%{?sle_version} <= 150300
# systemd-rpm-macros is wrong in 15.3 and below
%define _modprobedir /lib/modprobe.d
%endif
Name:           avrdude
Version:        7.3
Release:        0
Summary:        Upload tool for AVR microcontrollers
License:        GPL-2.0-or-later
URL:            https://github.com/avrdudes/avrdude
Source0:        https://github.com/avrdudes/avrdude/archive/refs/tags/v%{version}.tar.gz#/avrdude-%{version}.tar.gz
Source1:        https://github.com/avrdudes/avrdude/releases/download/v%{version}/avrdude-%{version}.tar.gz.sig
Source2:        avrdude.keyring
Source3:        modprobe.avrdude_parport
Source4:        avrdude-usbdevices
Source6:        debian.avrdude.udev
Patch0:         avrdude-5.11-no-builddate.diff
Patch1:         avrdude-ipv6.patch
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  libelf-devel
BuildRequires:  libhidapi-devel
BuildRequires:  libusb-devel
BuildRequires:  readline-devel
Requires(post): /sbin/modprobe
Provides:       avr-programmer
Requires:       %{libsoname} >= %{version}
%if 0%{?is_opensuse}
BuildRequires:  libftdi1-devel
%endif

%description
avrdude is a tool for AVR microcontrollers and drives many hardware
in-system programmers. avrdude allows programming microcontrollers
through a USB or parallel port of the computer.

%package -n %{libsoname}
Summary:        Shared library of %{name}

%description -n %{libsoname}
This package contains the shared lib%{name} library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description devel
This package contains development files for %{name}.

%prep
%setup -q
# avrdude-5.11-no-builddate.diff
# %patch -P 0 -p1
# %patch -P 1
#touch lexer.l

%build
# 15.4 at least has "-Wl,--no-undefined" in there which breaks library build
EXTRA_CMAKE="-DCMAKE_SHARED_LINKER_FLAGS='-Wl,--as-needed -Wl,-z,now'"
%cmake -DHAVE_LINUXGPIO=1 -DHAVE_LINUXSPI=1 -DBUILD_DOC=0 "$EXTRA_CMAKE"
%cmake_build

%install
%cmake_install
install -D -m 644 %{SOURCE3} %{buildroot}%{_modprobedir}/50-avrdude_parport.conf

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

# pre-usrmerged
%if 0%{?suse_version} < 1600
mv %{buildroot}/usr/etc %{buildroot}
%endif

%pre
# Avoid restoring outdated stuff in posttrans
for _f in %{?modprobe_d_files}; do
    [ ! -f "%{_sysconfdir}/modprobe.d/${_f}.rpmsave" ] || \
        mv -f "%{_sysconfdir}/modprobe.d/${_f}.rpmsave" "%{_sysconfdir}/modprobe.d/${_f}.rpmsave.old" || :
done

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
%posttrans
# Migration of modprobe.conf files to _modprobedir
for _f in %{?modprobe_d_files}; do
    [ ! -f "%{_sysconfdir}/modprobe.d/${_f}.rpmsave" ] || \
        mv -fv "%{_sysconfdir}/modprobe.d/${_f}.rpmsave" "%{_sysconfdir}/modprobe.d/${_f}" || :
done

%files
%dir %{_modprobedir}
%doc NEWS README.md
%license COPYING
%{_bindir}/avrdude
%{_mandir}/*/*
%if 0%{?suse_version} < 1600
%{_sysconfdir}/avrdude.conf
%else
%{_prefix}%{_sysconfdir}/avrdude.conf
%endif
%{_modprobedir}/50-avrdude_parport.conf
%{udevdir}

%files devel
%{_includedir}/libavrdude.h
%{_libdir}/libavrdude.so

%files -n %{libsoname}
%{_libdir}/libavrdude.so.*

%changelog
