#
# spec file for package alsa
#
# Copyright (c) 2021 SUSE LLC
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
Version:        1.2.4
Release:        0
Summary:        Advanced Linux Sound Architecture
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            http://www.alsa-project.org/
Source:         ftp://ftp.alsa-project.org/pub/lib/alsa-lib-%{version}.tar.bz2
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
Patch1:         0001-dlmisc-the-snd_plugin_dir_set-snd_plugin_dir-must-be.patch
Patch2:         0002-dlmisc-fix-snd_plugin_dir-locking-for-not-DL_ORIGIN_.patch
Patch3:         0003-pcm-snd_pcm_mmap_readi-fix-typo-in-comment.patch
Patch4:         0004-topology-use-inclusive-language-for-bclk.patch
Patch5:         0005-topology-use-inclusive-language-for-fsync.patch
Patch6:         0006-topology-use-inclusive-language-in-documentation.patch
Patch7:         0007-pcm-set-the-snd_pcm_ioplug_status-tstamp-field.patch
Patch9:         0009-pcm-Add-snd_pcm_audio_tstamp_type_t-constants.patch
Patch10:        0010-test-audio_time-Make-use-of-SND_PCM_AUDIO_TSTAMP_TYP.patch
Patch11:        0011-pcm-Fix-a-typo-in-SND_PCM_AUDIO_TSTAMP_TYPE_LAST-def.patch
Patch12:        0012-conf-fix-use-after-free-in-_snd_config_load_with_inc.patch
Patch13:        0013-ucm-fix-bad-frees-in-get_list0-and-get_list20.patch
Patch14:        0014-rawmidi-fix-memory-leak-in-snd_rawmidi_virtual_open.patch
Patch15:        0015-timer-fix-sizeof-operator-mismatch-in-snd_timer_quer.patch
Patch16:        0016-pcm-remove-dead-assignments-from-snd_pcm_rate_-commi.patch
Patch17:        0017-pcm_multi-remove-dead-assignment-from-_snd_pcm_multi.patch
Patch18:        0018-conf-fix-get_hexachar-return-value.patch
Patch19:        0019-pcm-fix-__snd_pcm_state-return-value.patch
Patch20:        0020-confmisc-fix-memory-leak-in-snd_func_concat.patch
Patch21:        0021-conf-fix-return-code-in-_snd_config_load_with_includ.patch
Patch22:        0022-pcm-plugin-status-fix-the-return-value-regression.patch
Patch23:        0023-pcm-plugin-status-revert-the-recent-changes.patch
Patch24:        0024-pcm-plugin-tidy-snd_pcm_plugin_avail_update.patch
Patch25:        0025-pcm-plugin-optimize-sync-in-snd_pcm_plugin_status.patch
Patch26:        0026-Revert-pcm_plugin-fix-delay.patch
Patch27:        0027-pcm-ioplug-fix-the-delay-calculation-in-the-status-c.patch
Patch28:        0028-pcm-rate-tidy-up-snd_pcm_rate_avail_update.patch
Patch29:        0029-pcm-ioplug-fix-the-delay-calculation-for-old-plugins.patch
Patch30:        0030-pcm-rate-use-pcm_frame_diff-in-snd_pcm_rate_playback.patch
Patch31:        0031-pcm-plugin-fix-status-code-for-capture.patch
Patch32:        0032-pcm-rate-use-pcm_frame_diff-on-related-places.patch
Patch33:        0033-pcm-rate-fix-the-capture-delay-values.patch
Patch34:        0034-ucm-fix-possible-memory-leak-in-parse_verb_file.patch
Patch35:        0035-topology-tplg_pprint_integer-fix-coverity-uninitaliz.patch
Patch36:        0036-topology-tplg_add_widget_object-do-not-use-invalid-e.patch
Patch37:        0037-topology-tplg_decode_pcm-add-missing-log-argument-co.patch
Patch38:        0038-topology-parse_tuple_set-remove-dead-condition-code.patch
Patch39:        0039-ucm-uc_mgr_substitute_tree-fix-use-after-free.patch
Patch40:        0040-topology-sort_config-cleanups-use-goto-for-the-error.patch
Patch41:        0041-conf-USB-add-Xonar-U7-MKII-to-USB-Audio.pcm.iec958_d.patch
Patch42:        0042-pcm_plugin-set-the-initial-hw_ptr-appl_ptr-from-the-.patch
Patch43:        0043-pcm-dmix-dshare-delay-calculation-fixes-and-cleanups.patch
Patch44:        0044-topology-fix-parse_tuple_set-remove-dead-condition-c.patch
Patch45:        0045-pcm-direct-Fix-the-missing-appl_ptr-update.patch
Patch46:        0046-pcm-ioplug-Pass-appl_ptr-and-hw_ptr-in-snd_pcm_statu.patch
Patch47:        0047-pcm-null-Pass-appl_ptr-and-hw_ptr-in-snd_pcm_status.patch
Patch48:        0048-pcm-share-Pass-appl_ptr-and-hw_ptr-in-snd_pcm_status.patch
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
%setup -q -n alsa-lib-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
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
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
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
# rm -f %{buildroot}%{_libdir}/alsa-lib/smixer/*.*a
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
