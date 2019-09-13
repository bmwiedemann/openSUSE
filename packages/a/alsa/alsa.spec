#
# spec file for package alsa
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%if 0%{?suse_version} < 1200
%define _udevrulesdir /lib/udev/rules.d/
%endif

Name:           alsa
Version:        1.1.9
Release:        0
Summary:        Advanced Linux Sound Architecture
License:        LGPL-2.1-or-later
Group:          System/Libraries
Url:            http://www.alsa-project.org/
Source:         ftp://ftp.alsa-project.org/pub/lib/alsa-lib-%{version}.tar.bz2
Source2:        baselibs.conf
Source8:        40-alsa.rules
Source9:        42-hd-audio-pm.rules
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
# upstream fixes
Patch1:         0001-pcm-direct-Add-generic-hw_ptr_alignment-function-for.patch
Patch2:         0002-pcm-dshare-Added-hw_ptr_alignment-option-in-configur.patch
Patch3:         0003-pcm-dsnoop-Added-hw_ptr_alignment-option-in-configur.patch
Patch4:         0004-pcm-file-add-support-for-infile-reading-in-non-inter.patch
Patch5:         0005-pcm-file-use-snd_pcm_file_areas_read_infile-for-read.patch
Patch6:         0006-pcm-file-add-missing-unlock-on-early-return.patch
Patch7:         0007-ucm-Add-UCM-profile-for-CX2072X-codec-on-Baytrail-Ch.patch
Patch8:         0008-pcm-add-mmap_begin-callback-to-snd_pcm_fast_ops_t-ap.patch
Patch9:         0009-pcm-file-add-infile-read-support-for-mmap-mode.patch
Patch10:        0010-aserver-fix-resource-leak-coverity.patch
Patch11:        0011-src-conf.c-add-missing-va_end-call-coverity.patch
Patch12:        0012-config-parse_string-fix-the-dynamic-buffer-allocatio.patch
Patch13:        0013-control_shm-remove-duplicate-code-coverity.patch
Patch14:        0014-control_shm-add-missing-socket-close-to-the-error-pa.patch
Patch15:        0015-pcm-fix-memory-leak-in-_snd_pcm_parse_config_chmaps-.patch
Patch16:        0016-pcm_file-call-pclose-correctly-for-popen-coverity.patch
Patch17:        0017-pcm_hw-close-file-descriptor-in-the-error-path-in-sn.patch
Patch18:        0018-rawmidi-use-snd_dlobj_cache_get2-in-rawmidi-open-cov.patch
Patch19:        0019-rawmidi_hw-add-sanity-check-for-the-invalid-stream-a.patch
Patch20:        0020-topology-various-coverity-fixes.patch
Patch21:        0021-ucm-coverity-fixes.patch
Patch22:        0022-pcm_file-coverity-fixes-including-double-locking.patch
Patch23:        0023-topology-next-round-of-coverity-fixes.patch
Patch24:        0024-pcm_file-another-locking-fix-coverity.patch
Patch25:        0025-ucm-another-coverity-fix-in-uc_mgr_config_load.patch
# rest suse fixes
Patch101:       alsa-lib-ignore-non-accessible-ALSA_CONFIG_PATH.patch
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  pkgconfig
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

%prep
%setup -q -n alsa-lib-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch101 -p1

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
  --disable-python
make V=1 %{?_smp_mflags}
# run doxygen
make -C doc doc %{?_smp_mflags}

%install
# install shared library
%make_install
# clean up unneeded files
rm -f %{buildroot}%{_libdir}/*.*a
# rm -f %{buildroot}%{_libdir}/alsa-lib/smixer/*.*a
rm -f %{buildroot}%{_bindir}/aserver
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
mkdir -p %{buildroot}%{_udevrulesdir}
%if 0%{?suse_version} < 1140
install -c -m 0644 %{SOURCE8} %{buildroot}%{_udevrulesdir}
%endif
install -c -m 0644 %{SOURCE9} %{buildroot}%{_udevrulesdir}
#
# install template to update rc.config and sysconfig files:
# (updating the actual files is done in the %post-script)
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
cp ChangeLog INSTALL TODO MEMORY-LEAK %{buildroot}%{_docdir}/%{name}/alsa-lib
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
%{_udevrulesdir}*

%files devel
%defattr(-, root, root)
%{_libdir}/libasound.so
%{_includedir}/sys/*
%{_includedir}/alsa
%{_includedir}/asoundlib.h
%{_datadir}/aclocal/*.m4
%{_libdir}/pkgconfig/*.pc

%files docs
%defattr(-, root, root)
%doc doc/doxygen/html/*

%files -n libasound2
%defattr(-, root, root)
%{_libdir}/libasound.so.*
%{_datadir}/alsa

%changelog
