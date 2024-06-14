#
# spec file for package alsa-utils
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


%define do_autoreconf 0
%define _udevdir %(pkg-config --variable=udevdir udev)
%ifarch %ix86 x86_64 %arm aarch64 ppc64le riscv64
%define enable_topology	1
%else
%define enable_topology	0
%endif

Name:           alsa-utils
Version:        1.2.12
Release:        0
Summary:        Advanced Linux Sound Architecture Utilities
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            http://www.alsa-project.org/
Source:         https://www.alsa-project.org/files/pub/utils/alsa-utils-%{version}.tar.bz2
Source1:        https://www.alsa-project.org/files/pub/utils/alsa-utils-%{version}.tar.bz2.sig
Source2:        01beep.conf
Source3:        sound-extra.service
Source5:        load-sound-modules.sh
# from https://www.alsa-project.org/files/pub/gpg-release-key-v1.txt
Source6:        alsa-utils.keyring
# upstream fixes
# downstream fixes
Patch100:       alsa-info-no-update-for-distro-script.patch
Patch101:       alsa-utils-configure-version-revert.patch
BuildRequires:  alsa-devel
%if %enable_topology
BuildRequires:  alsa-topology-devel
%endif
BuildRequires:  fftw3-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
%if 0%{?suse_version} < 1500
BuildRequires:  python-docutils
%else
BuildRequires:  python3-docutils
%endif
BuildRequires:  xmlto
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
%if 0%{?do_autoreconf}
BuildRequires:  automake
BuildRequires:  libtool
%endif
Requires:       alsa
# for alsa-info.sh
Requires:       dialog
Requires:       pciutils
Requires:       tree

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
%patch -P 100 -p1
%if 0%{?do_autoreconf}
%patch -P 101 -p1
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
  --with-udev-rules-dir=%{_udevdir}/rules.d \
  --with-alsactl-lock-dir=/run/lock
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/alsa/init/preinit
mkdir -p %{buildroot}%{_datadir}/alsa/init/postinit
%if %enable_topology
rm -f %{_libdir}/alsa-topology/*.la
%endif
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
install -c -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}
ln -s ../sound-extra.service %{buildroot}%{_unitdir}/sound.target.wants
mkdir -p %{buildroot}%{_prefix}/lib/systemd/scripts
install -c -m 0755 %{SOURCE5} %{buildroot}%{_prefix}/lib/systemd/scripts

%pre
%service_add_pre sound-extra.service

%post
%service_add_post sound-extra.service
# migrate the old asound.state
if [ ! -f %{_localstatedir}/lib/alsa/asound.state ]; then
  test -f /etc/asound.state && \
    cp -a /etc/asound.state %{_localstatedir}/lib/alsa/asound.state
fi
exit 0

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
%if %enable_topology
%{_libdir}/alsa-topology
%endif
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
