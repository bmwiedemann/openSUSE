#
# spec file for package alsa-utils
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


%define do_autoreconf 1
%define _udevdir %(pkg-config --variable=udevdir udev)
Name:           alsa-utils
Version:        1.2.1
Release:        0
Summary:        Advanced Linux Sound Architecture Utilities
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            http://www.alsa-project.org/
Source:         ftp://ftp.alsa-project.org/pub/utils/alsa-utils-%{version}.tar.bz2
Source1:        01beep.conf
Source2:        sound-extra.service
Source5:        load-sound-modules.sh
Patch1:         0001-treewide-sys-poll-to-poll.patch
Patch2:         0002-treewide-Fix-wrong-formats-on-32-bit.patch
Patch3:         0003-treewide-Fix-printf-formats.patch
Patch4:         0004-aplay-Adjust-buffer-sizes-to-fix-snprintf-warnings.patch
Patch5:         0005-aplay-Limit-VUMeter-progress-bar-to-100-for-negative.patch
Patch6:         0006-alsactl-sysfs-add-sys-kernel-uevent_seqnum-check-to-.patch
Patch7:         0007-alsaucm-use-the-first-sound-card-use-case-name-hw-CA.patch
Patch8:         0008-alsaucm-add-text-dump-command.patch
Patch9:         0009-alsaucm-add-json-dump-command.patch
Patch10:        0010-alsaucm-dump-fix-the-prefixed.patch
Patch11:        0011-alsactl-fix-sched-idle-set-it-really-to-SCHED_IDLE.patch
Patch12:        0012-configure-Fix-linking-of-alsatplg-with-the-older-lib.patch
Patch13:        0013-alsatplg-add-n-normalize-option.patch
Patch14:        0014-alsatplg-add-s-sort-and-fix-memory-leaks.patch
Patch15:        0015-alsatplg-fix-another-small-leak-in-normalize_config.patch
Patch16:        0016-alsa-info.sh-Consolidate-PCI-device-output.patch
Patch17:        0017-alsa-info.sh-Read-from-proc-modules-and-sort-the-res.patch
Patch18:        0018-alsa-info.sh-Simplify-iteration-over-cards-when-call.patch
Patch19:        0019-alsa-info.sh-Use-existing-function-to-print-ALSA-con.patch
Patch20:        0020-alsa-info.sh-Exit-script-after-writing-information-t.patch
Patch21:        0021-alsa-info.sh-Replace-gauge-with-infobox-for-upload-d.patch
Patch22:        0022-alsa-info.sh-Remove-progress-spinner-during-upload-w.patch
Patch23:        0023-alsa-info.sh-Condense-nested-commands-for-file-uploa.patch
Patch24:        0024-alsa-info.sh-Condense-nested-commands-for-formatting.patch
Patch25:        0025-alsa-info.sh-Perform-test-for-wget-earlier.patch
Patch26:        0026-alsa-info.sh-Warn-after-actual-upload-failure-do-not.patch
Patch101:       alsa-utils-configure-version-revert.patch
BuildRequires:  alsa-devel
BuildRequires:  alsa-topology-devel
BuildRequires:  fftw3-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-docutils
BuildRequires:  xmlto
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
%if 0%{?do_autoreconf}
BuildRequires:  automake
%endif
Requires:       alsa
# for alsa-info.sh
Requires:       dialog
Requires:       pciutils

%description
This package contains utility programs supporting ALSA, Advanced Linux
Sound Architecture.

%package -n alsabat
Summary:        Command-line sound tester for ALSA sound card driver
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       alsa-utils = %{version}

%description -n alsabat
BAT (Basic Audio Tester) is a simple command-line utility intended
to help automate audio driver and sound server testing with little human
interaction. BAT can be used to test audio quality, stress test features
and test audio before and after PM state changes.

%prep
%setup -q
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
%if 0%{?do_autoreconf}
%patch101 -p1
# fix stupid automake's automatic action
sed -i -e's/EXTRA_DIST= config.rpath /EXTRA_DIST=/' Makefile.am
%endif

%build
export AUTOMAKE_JOBS="%{?_smp_mflags}"
%if 0%{?do_autoreconf}
gettextize -c -f --no-changelog
autoreconf -fi
%endif
%configure --with-curses=ncursesw \
  --with-systemdsystemunitdir=%{_unitdir} \
  --with-asound-state-dir=%{_sysconfdir} \
  --with-udev-rules-dir=%{_udevdir}/rules.d
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/alsa/init/preinit
mkdir -p %{buildroot}%{_datadir}/alsa/init/postinit
for i in %{_sourcedir}/[0-9]*.conf; do
  install -c -m 0644 $i %{buildroot}%{_datadir}/alsa/init/postinit
done
# remove obsoleted alsaconf script
rm -f %{buildroot}%{_sbindir}/alsaconf
rm -f %{buildroot}%{_datadir}/locale/*/*/alsaconf.mo
rm -f %{buildroot}%{_mandir}/*/man*/alsaconf.*
rm -f %{buildroot}%{_mandir}/man*/alsaconf.*
rmdir --ignore-fail-on-non-empty -p %{buildroot}%{_mandir}/*/man* %{buildroot}%{_mandir}/man*
%find_lang %{name} --all-name
ln -s alsa-restore.service %{buildroot}%{_unitdir}/alsasound.service
mkdir -p %{buildroot}%{_localstatedir}/lib/alsa
# systemd unit files
install -c -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}
ln -s ../sound-extra.service %{buildroot}%{_unitdir}/sound.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/scripts
install -c -m 0755 %{SOURCE5} %{buildroot}%{_prefix}/lib/systemd/scripts

%pre
%service_add_pre sound-extra.service

%post
%service_add_post sound-extra.service

%preun
%service_del_preun sound-extra.service

%postun
%service_del_postun sound-extra.service

%files -f %{name}.lang
%license COPYING
%doc README.md
%doc seq/aconnect/README*
%doc seq/aseqnet/README*
%{_mandir}/man*/*
%{_bindir}/*
%{_sbindir}/*
%exclude %{_bindir}/alsabat
%exclude %{_sbindir}/alsabat-test.sh
%exclude %{_mandir}/man*/alsabat.*
%{_datadir}/sounds/alsa
%{_datadir}/alsa
%{_udevdir}
%{_unitdir}/*.service
%{_unitdir}/sound.target.wants
%{_prefix}/lib/systemd/scripts
%{_localstatedir}/lib/alsa

%files -n alsabat
%license COPYING
%{_bindir}/alsabat
%{_sbindir}/alsabat-test.sh
%{_mandir}/man*/alsabat.*

%changelog
