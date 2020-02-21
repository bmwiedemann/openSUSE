#
# spec file for package alsa
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.2.1.2
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
Patch1:         0001-ucm-Use-strncmp-to-avoid-access-out-of-boundary.patch
Patch2:         0002-ucm-return-always-at-least-NULL-if-no-list-is-availa.patch
Patch3:         0003-ucm-add-_identifiers-list.patch
Patch4:         0004-namehint-correct-the-args-check.patch
Patch5:         0005-namehint-improve-the-previous-patch-check-the-return.patch
Patch6:         0006-ucm-docs-allow-spaces-in-device-names-for-JackHWMute.patch
Patch7:         0007-use-case-docs-add-PlaybackMixerCopy-and-CaptureMixer.patch
Patch8:         0008-ucm-docs-add-JackCTL-rearrange-JackControl-and-JackD.patch
Patch9:         0009-ucm-Do-not-fail-to-parse-configs-on-cards-with-an-em.patch
Patch10:        0010-src-ucm-main.c-fix-build-without-mixer.patch
Patch11:        0011-alsa.m4-another-try-to-fix-the-libatopology-detectio.patch
Patch12:        0012-ucm-docs-add-Mic-DigitalMic-and-multiple-devices-com.patch
Patch13:        0013-ucm-docs-remove-DigitalMic-it-does-not-have-sense.patch
Patch14:        0014-ucm-docs-change-the-Mic-description-to-simple-Microp.patch
Patch15:        0015-ucm-docs-add-note-about-the-sequences-and-device-spl.patch
Patch16:        0016-ucm-docs-remove-MixerCopy-values-add-Priority-for-ve.patch
Patch17:        0017-ucm-setup-conf_format-after-getting-ALSA_CONFIG_UCM_.patch
Patch18:        0018-alsa-lib-fix-the-array-parser-unique-compound-keys.patch
Patch19:        0019-topology-remove-vendor_fd-name-from-snd_tplg-structu.patch
Patch20:        0020-topology-file-position-and-size-cleanups.patch
Patch21:        0021-topology-use-an-array-describing-blocks-for-the-main.patch
Patch22:        0022-topology-use-size_t-for-calc_block_size.patch
Patch23:        0023-topology-merge-write_block-to-tplg_write_data.patch
Patch24:        0024-topology-make-vebose-output-more-nice.patch
Patch25:        0025-topology-use-list_insert-macro-in-tplg_elem_insert.patch
Patch26:        0026-topology-dapm-coding-fixes.patch
Patch27:        0027-topology-dapm-merge-identical-index-blocks-like-for-.patch
Patch28:        0028-topology-more-coding-fixes.patch
Patch29:        0029-Fix-alsa-sound-.h-for-external-programs.patch
Patch30:        0030-type_compat-Add-missing-__s64-and-__u64-definitions-.patch
Patch31:        0031-uapi-Move-typedefs-from-uapi-to-sound.patch
Patch32:        0032-Update-the-attributes.m4-macro-file-from-xine.patch
Patch33:        0033-topology-avoid-to-use-the-atoi-directly-when-expecte.patch
Patch34:        0034-topology-use-snd_config_get_bool-instead-own-impleme.patch
Patch35:        0035-topology-fix-tplg_get_integer-handle-errno-ERANGE.patch
Patch36:        0036-topology-add-tplg_get_unsigned-function.patch
Patch37:        0037-topology-convert-builder-to-use-the-mallocated-memor.patch
Patch38:        0038-topology-add-binary-output-from-the-builder.patch
Patch39:        0039-topology-parser-recode-tplg_parse_config.patch
Patch40:        0040-topology-add-snd_tplg_load-remove-snd_tplg_build_bin.patch
Patch41:        0041-topology-move-the-topology-element-table-from-builde.patch
Patch42:        0042-topology-add-parser-to-the-tplg_table.patch
Patch43:        0043-topology-add-snd_tplg_save.patch
Patch44:        0044-topology-add-snd_tplg_create-with-flags.patch
Patch45:        0045-topology-add-snd_tplg_version-function.patch
Patch46:        0046-topology-cleanup-the-SNDERR-calls.patch
Patch47:        0047-topology-dapm-fix-the-SNDERR-Undefined.patch
Patch48:        0048-topology-fix-the-unitialized-tuples.patch
Patch49:        0049-topology-implement-shorter-hexa-uuid-00-00-parser.patch
Patch50:        0050-topology-fix-the-TPLG_DEBUG-compilation.patch
Patch51:        0051-topology-fix-the-ops-parser-accept-integer-hexa-valu.patch
Patch52:        0052-topology-fix-the-wrong-memory-access-object-realloc.patch
Patch53:        0053-topology-implement-snd_tplg_decode.patch
Patch54:        0054-topology-move-the-elem-list-delete-to-tplg_elem_free.patch
Patch55:        0055-topology-unify-the-log-mechanism.patch
Patch56:        0056-topology-tplg_dbg-cleanups.patch
Patch57:        0057-topology-cosmetic-changes-functions.patch
Patch58:        0058-mixer-Fix-memory-leak-for-more-than-16-file-descript.patch
Patch59:        0059-Quote-strings-containing-or-when-saving-an-alsa-conf.patch
Patch60:        0060-ucm-fix-the-configuration-directory-longname-for-ucm.patch
Patch61:        0061-ucm-split-conf_file_name-and-conf_dir_name.patch
Patch62:        0062-ucm-remove-MAX_FILE-definition-and-use-correct-PATH_.patch
Patch63:        0063-topology-remove-MAX_FILE-definition-and-use-correct-.patch
Patch64:        0064-ucm-parser-cosmetic-fixes-in-the-comments.patch
Patch65:        0065-configure.ac-remove-an-unnecessary-libtool-fix.patch
Patch66:        0066-ucm-parser-use-correct-filename-in-parser_master_fil.patch
Patch67:        0067-ucm-the-ucm2-subdirectory-is-driver-name-based.patch
Patch68:        0068-ucm-implement-RenameDevice-and-RemoveDevice-verb-man.patch
Patch69:        0069-ucm-fill-missing-device-entries-conflicting-supporte.patch
Patch70:        0070-control-Remove-access-to-the-deprecated-dimen-fields.patch
Patch71:        0071-topology-Drop-SNDRV_CTL_ELEM_ACCESS_TIMESTAMP-access.patch
Patch72:        0072-uapi-Sync-with-5.6-kernel-ABI.patch
Patch73:        0073-ucm-parser-add-error-message-to-verb_dev_list_add.patch
Patch74:        0074-do-not-set-close-on-exec-flag-on-descriptor-if-it-wa.patch
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

%package topology-devel
Summary:        Header files for ALSA topology development
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       alsa-devel = %{version}
Requires:       libatopology2 = %{version}

%description topology-devel
This package contains all necessary include files and libraries needed
to develop applications that require ALSA topology.

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

%package -n libatopology2
Summary:        ALSA Topology Library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libatopology2
This package contains the library for ALSA topology support.

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
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
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

%post -n libatopology2 -p /sbin/ldconfig
%postun -n libatopology2 -p /sbin/ldconfig

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
%exclude %{_includedir}/alsa/topology.h
%{_includedir}/asoundlib.h
%{_datadir}/aclocal/*.m4
%{_libdir}/pkgconfig/alsa.pc

%files topology-devel
%defattr(-, root, root)
%{_libdir}/libatopology.so
%{_includedir}/alsa/topology.h
%{_libdir}/pkgconfig/alsa-topology.pc

%files docs
%defattr(-, root, root)
%doc doc/doxygen/html/*

%files -n libasound2
%defattr(-, root, root)
%{_libdir}/libasound.so.*
%{_datadir}/alsa

%files -n libatopology2
%defattr(-, root, root)
%{_libdir}/libatopology.so.*

%changelog
