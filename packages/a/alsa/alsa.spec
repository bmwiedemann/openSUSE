#
# spec file for package alsa
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%if 0%{?suse_version} < 1200
%define _udevrulesdir /lib/udev/rules.d/
%endif

%ifarch %ix86 x86_64 %arm aarch64 ppc64le riscv64
%define enable_topology	1
%else
%define enable_topology	0
%endif

Name:           alsa
Version:        1.2.12
Release:        0
Summary:        Advanced Linux Sound Architecture
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.alsa-project.org
Source:         https://www.alsa-project.org/files/pub/lib/alsa-lib-%{version}.tar.bz2
Source1:        https://www.alsa-project.org/files/pub/lib/alsa-lib-%{version}.tar.bz2.sig
Source2:        baselibs.conf
Source8:        40-alsa.rules
Source11:       alsasound
Source12:       sysconfig.sound
Source13:       joystick
Source14:       sysconfig.joystick
Source16:       set_default_volume
Source17:       test.wav
Source21:       README.testwav
Source30:       all_notes_off
Source31:       all_notes_off.bin
Source32:       all_notes_off.mid
Source34:       alsa-init.sh
# from https://www.alsa-project.org/files/pub/gpg-release-key-v1.txt
Source35:       alsa.keyring
# upstream fixes
# rest suse fixes
Patch101:       alsa-lib-ignore-non-accessible-ALSA_CONFIG_PATH.patch
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  pkgconfig
Requires:       alsa-ucm-conf
Requires:       alsa-utils
Requires(post): %fillup_prereq
Recommends:     alsa-oss
Recommends:     alsa-plugins
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} <= 1310
Requires(post): %insserv_prereq
%endif
%if 0%{?suse_version} > 1200
BuildRequires:  pkgconfig(udev)
%else
BuildRequires:  udev
%endif

%description
ALSA stands for Advanced Linux Sound Architecture.  It supports many
PCI, ISA PnP  and USB sound cards.

This package contains the ALSA init scripts to start the sound system
on your Linux box.  To set it up, run yast2 or alsaconf.

%package devel
Summary:        Header files for ALSA development
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libasound2 = %{version}
Obsoletes:      alsadev < %{version}
Provides:       alsa-lib-devel = %{version}
Provides:       alsadev = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require ALSA.

%if %enable_topology
%package topology-devel
Summary:        Header files for ALSA topology development
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       alsa-devel = %{version}
Requires:       libatopology2 = %{version}

%description topology-devel
This package contains all necessary include files and libraries needed
to develop applications that require ALSA topology.
%endif

%package docs
Summary:        Additional Package Documentation for ALSA
License:        GPL-2.0-or-later
Group:          Documentation/Other
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description docs
This package contains optional documentation provided in addition to
this package's base documentation.

%package -n libasound2
Summary:        Advanced Linux Sound Architecture Library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Provides:       alsa-lib

%description -n libasound2
This package contains the library for ALSA, Advanced Linux Sound
Architecture.

%if %enable_topology
%package -n libatopology2
Summary:        ALSA Topology Library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libatopology2
This package contains the library for ALSA topology support.
%endif

%prep
%autosetup -p1 -n alsa-lib-%{version}

%build
# disable LTO; otherwise some apps confused with versioned symbols (boo#1149461)
%define _lto_cflags %{nil}
export AUTOMAKE_JOBS="%{?_smp_mflags}"
# build alsa-lib
autoreconf -fi
%configure \
  --disable-static \
  --enable-symbolic-functions \
  --disable-aload \
  --disable-alisp \
%if !%enable_topology
  --disable-topology \
%endif
  --disable-python
make V=1 %{?_smp_mflags}
# run doxygen
make -C doc doc %{?_smp_mflags}

%install
# install shared library
%make_install
# clean up unneeded files
rm -f %{buildroot}%{_libdir}/*.*a
# rm -f %%{buildroot}%%{_libdir}/alsa-lib/smixer/*.*a
rm -f %{buildroot}%{_bindir}/aserver
%if !%enable_topology
rm -f %{buildroot}%{_libdir}/pkgconfig/alsa-topology.pc
%endif
#
# install helper scripts
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
install -c -m 0755 %{SOURCE16} %{buildroot}%{_bindir}
install -c -m 0755 %{SOURCE34} %{buildroot}%{_sbindir}/alsa-init
%if 0%{?suse_version} < 1140
sed -i -e 's@%{_localstatedir}/lib/alsa/asound.state@%{_sysconfdir}/asound.state@g' %{buildroot}%{_bindir}/set_default_volume
sed -i -e 's@%{_localstatedir}/lib/alsa/asound.state@%{_sysconfdir}/asound.state@g' %{buildroot}%{_sbindir}/alsa-init
%endif
# install test wave file
mkdir -p %{buildroot}%{_datadir}/sounds/alsa
install -c -m 0644 %{SOURCE17} %{buildroot}%{_datadir}/sounds/alsa/test.wav
# install all_notes_off stuff
install -c -m 0755 %{SOURCE30} %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_prefix}/lib
install -c -m 0644 %{SOURCE31} %{buildroot}%{_prefix}/lib
install -c -m 0644 %{SOURCE32} %{buildroot}%{_prefix}/lib
%if 0%{?suse_version} <= 1310
#
# install init scripts
#
mkdir -p %{buildroot}%{_sysconfdir}/init.d
install -c -m 0755 %{SOURCE11} %{buildroot}%{_sysconfdir}/init.d
install -c -m 0755 %{SOURCE13} %{buildroot}%{_sysconfdir}/init.d
%if 0%{?suse_version} < 1140
sed -i -e 's@%{_localstatedir}/lib/alsa/asound.state@%{_sysconfdir}/asound.state@g' %{buildroot}%{_initddir}/alsasound
%endif
rm -f %{buildroot}%{_sbindir}/rcalsasound
ln -s ../..%{_initddir}/alsasound %{buildroot}%{_sbindir}/rcalsasound
rm -f %{buildroot}%{_sbindir}/rcjoystick
ln -s ../..%{_initddir}/joystick %{buildroot}%{_sbindir}/rcjoystick
%endif
#
# udev rules
#
%if 0%{?suse_version} < 1140
mkdir -p %{buildroot}%{_udevrulesdir}
install -c -m 0644 %{SOURCE8} %{buildroot}%{_udevrulesdir}
%endif
#
# install template to update rc.config and sysconfig files:
# (updating the actual files is done in the %% post-script)
#
mkdir -p -m 755 %{buildroot}%{_fillupdir}
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/sysconfig
install -m 644 %{_sourcedir}/sysconfig.sound %{buildroot}%{_fillupdir}
%if 0%{?suse_version} <= 1310
install -m 644 %{_sourcedir}/sysconfig.joystick %{buildroot}%{_fillupdir}
%endif
#
# documents
#
mkdir -p %{buildroot}%{_docdir}/%{name}
cp %{_sourcedir}/README* %{buildroot}%{_docdir}/%{name}
%if 0%{?suse_version} < 1200
cp COPYING %{buildroot}%{_docdir}/%{name}
%endif
mkdir -p %{buildroot}%{_docdir}/%{name}/alsa-lib
cp ChangeLog TODO MEMORY-LEAK NOTES %{buildroot}%{_docdir}/%{name}/alsa-lib
cp doc/asoundrc.txt %{buildroot}%{_docdir}/%{name}/alsa-lib

%post
%if 0%{?suse_version} > 1310
%{fillup_only -n sound}
%else
%{fillup_and_insserv -ny sound alsasound}
%{fillup_and_insserv -n joystick joystick}
%endif
exit 0

%if 0%{?suse_version} <= 1310
%preun
%stop_on_removal alsasound joystick
exit 0

%postun
%restart_on_update alsasound joystick
%insserv_cleanup
exit 0
%endif

%post -n libasound2 -p /sbin/ldconfig
%postun -n libasound2 -p /sbin/ldconfig

%if %enable_topology
%post -n libatopology2 -p /sbin/ldconfig
%postun -n libatopology2 -p /sbin/ldconfig
%endif

%files
%defattr(-, root, root)
%doc %{_docdir}/%{name}
%if 0%{?suse_version} >= 1200
%license COPYING
%endif
%if 0%{?suse_version} <= 1310
%{_initddir}/*
%endif
%{_sbindir}/*
%{_bindir}/*
%{_prefix}/lib/all_notes_off.*
%{_datadir}/sounds/alsa
%{_fillupdir}/*
%if 0%{?suse_version} < 1140
%{_udevrulesdir}*
%endif

%files devel
%defattr(-, root, root)
%{_libdir}/libasound.so
%{_includedir}/sys/*
%{_includedir}/alsa
%if %enable_topology
%exclude %{_includedir}/alsa/topology.h
%endif
%{_includedir}/asoundlib.h
%{_datadir}/aclocal/*.m4
%{_libdir}/pkgconfig/alsa.pc

%if %enable_topology
%files topology-devel
%defattr(-, root, root)
%{_libdir}/libatopology.so
%{_includedir}/alsa/topology.h
%{_libdir}/pkgconfig/alsa-topology.pc
%endif

%files docs
%defattr(-, root, root)
%doc doc/doxygen/html/*

%files -n libasound2
%defattr(-, root, root)
%{_libdir}/libasound.so.*
%{_datadir}/alsa

%if %enable_topology
%files -n libatopology2
%defattr(-, root, root)
%{_libdir}/libatopology.so.*
%endif

%changelog
