#
# spec file for package alsa-tools
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


%define build_hwdep_loader	0
%if 0%{?suse_version} >  1140
%define have_gtk3	1
%else
%define have_gtk3	0
%endif
Name:           alsa-tools
Version:        1.2.11
Release:        0
Summary:        Various ALSA Tools
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://www.alsa-project.org/
Source:         https://www.alsa-project.org/files/pub/tools/alsa-tools-%{version}.tar.bz2
Source1:        https://www.alsa-project.org/files/pub/tools/alsa-tools-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
Source3:        README.SUSE
Source4:        sbipatches.tar.bz2
Source5:        rmedigicontrol.desktop
Source7:        rmedigicontrol.png
# upstream fixes
Patch1:         0001-hdajackretask-Fix-build-with-gcc7.patch
# build fixes
Patch101:       alsa-tools-no_m4_dir.dif
BuildRequires:  alsa-devel
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection
BuildRequires:  gtk2-devel
BuildRequires:  libtool
BuildRequires:  update-desktop-files
%if %{have_gtk3}
BuildRequires:  gtk3-devel
%endif

%description
This is a meta package for collection of sub-packages.

%package -n as10k1
Version:        A0.99
Release:        0
Summary:        Emu10k1 DSP assembler
Group:          Productivity/Multimedia/Sound/Utilities
Provides:       alsa-tools = 1.0.28
Obsoletes:      alsa-tools <= 1.0.28

%description -n as10k1
Assmbler for emu10k1 DSP chip present in Creative SB Live, PCI 512 and
Emu APS sound cards.

%package -n hda-verb
Version:        0.4
Release:        0
Summary:        HD-audio jack retasking tool
Group:          Productivity/Multimedia/Sound/Utilities
Provides:       alsa-tools:/usr/bin/hda-verb

%description -n hda-verb
hda-verb is a small program to send HD-audio commands to the given
ALSA hwdep device on the hd-audio interface.

%package -n hdsploader
Version:        1.2
Release:        0
Summary:        Firmware loader for RME Hammerfall DSP cards
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       alsa-firmware
Provides:       alsa-tools:/usr/bin/hdsploader

%description -n hdsploader
This is the firmware loader program for RME Hammerfall DSP cards.

%package -n ld10k1
Version:        0.1.8p1
Release:        0
Summary:        Emu10k1 patch loader for ALSA
Group:          Productivity/Multimedia/Sound/Utilities
Provides:       alsa-tools:/usr/bin/lo10k1

%description -n ld10k1
This package contains the patch loader program for Emu10k1 and Emu10k1 on ALSA.

%package -n liblo10k1-0
Version:        0.1.8p1
Release:        0
Summary:        Emu10k1 patch loader library
Group:          System/Libraries

%description -n liblo10k1-0
This package contains the patch loader program for Emu10k1 and Emu10k1 on ALSA.

%package -n ld10k1-devel
Version:        0.1.8p1
Release:        0
Summary:        Header files for the Emu10k1 patch loader
Group:          Development/Libraries/C and C++
Requires:       liblo10k1-0 = 0.1.8p1
Provides:       alsa-tools-devel = 1.0.28
Obsoletes:      alsa-tools-devel <= 1.0.28

%description -n ld10k1-devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package -n us428control
Version:        0.4.6
Release:        0
Summary:        Sound Blaster 16 ASP/CSP control program
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       alsa-firmware
Provides:       alsa-tools:/usr/bin/us428control

%description -n us428control
This package contains a control tool for Tascam US-X2Y audio devices

%package -n usx2yloader
Version:        0.3
Release:        0
Summary:        Second phase firmware loader for Tascam USX2Y USB soundcards
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       alsa-firmware
Requires:       fxload
Provides:       alsa-tools:/usr/bin/usx2yloader

%description -n usx2yloader
Usx2yloader is a helper program to load the 2nd Phase firmware binaries
onto the Tascam USX2Y USB soundcards.

%package -n sbiload
Version:        0.4.0
Release:        0
Summary:        OPL2/3 FM instrument loader
Group:          Productivity/Multimedia/Sound/Utilities
Provides:       alsa-tools:/usr/bin/sbiload

%description -n sbiload
sbiload is an OPL2/3 FM instrument loader for ALSA hwdep.

%package -n cspctl
Version:        0.3.5a
Release:        0
Summary:        Sound Blaster 16 ASP/CSP control program
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       kernel-firmware
Provides:       alsa-tools:/usr/bin/cspctl

%description -n cspctl
cspctl is a control program for Sound Blaster 16 ASP/CSP chips.

%package -n sscape-ctl
Version:        0.1.0
Release:        0
Summary:        Sound Blaster 16 ASP/CSP control program
Group:          Productivity/Multimedia/Sound/Utilities
Provides:       alsa-tools:/usr/bin/sscape_ctl

%description -n sscape-ctl
This package contains a control utility program for SoundScape cards

%package -n mixartloader
Version:        1.0
Release:        0
Summary:        Firmware loader for Digigram miXart boards
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       alsa-firmware

%description -n mixartloader
mixartloader is a helper program to load the firmware binaries
onto the Digigram miXart board sound drivers.

%package -n pcxhrloader
Version:        1.0
Release:        0
Summary:        Firmware loader for Digigram pcxhr boards
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       alsa-firmware

%description -n pcxhrloader
pcxhrloader is a helper program to load the firmware binaries
onto Digigram PCXHR compatible board sound drivers.

%package -n vxloader
Version:        1.0
Release:        0
Summary:        Firmware loader for Digigram VX-board sound cards
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       alsa-firmware

%description -n vxloader
mixartloader is a helper program to load the firmware binaries
onto the Digigram VX-board sound drivers.

%package -n hwmixvolume
Version:        0.9
Release:        0
Summary:        GUI tool to set individual hardware stream volumes
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       python3-alsa
Provides:       alsa-tools-gui = 1.0.28
Obsoletes:      alsa-tools-gui <= 1.0.28

%description -n hwmixvolume
This tool allows you to control the volume of individual streams on
sound cards that use hardware mixing, i.e., those based on the
following chips: Creative Emu10k1, VIA VT823x southbridge, Yamaha DS-1

%package -n echomixer
Version:        1.0.5
Release:        0
Summary:        Echoaudio console application
Group:          Productivity/Multimedia/Sound/Utilities
Provides:       alsa-tools-gui:/usr/bin/echomixer

%description -n echomixer
This is Linux-equivalent of the Echoaudio console application.

%package -n envy24control
Version:        0.6.0
Release:        0
Summary:        Control tool for Envy24 (ice1712) based soundcards
Group:          Productivity/Multimedia/Sound/Utilities
Provides:       alsa-tools-gui:/usr/bin/envy24control

%description -n envy24control
envy24control is a GUI control tool for Envy24 (ice1712) based sound cards.

%package -n rmedigicontrol
Version:        0.3.5a
Release:        0
Summary:        GUI control tool for RME Digi32 and RME Digi96 soundcards
Group:          Productivity/Multimedia/Sound/Utilities
Provides:       alsa-tools-gui:/usr/bin/rmedigicontrol

%description -n rmedigicontrol
Rmedigicontrol is a control tool for RME Digi32 and RME Digi96 soundcards.
It depends on ALSA and GTK+ and offers a graphical frontend for all your
switches.

%package -n hdajackretask
Version:        0.20120413
Release:        0
Summary:        HD-audio jack retasking tool
Group:          Productivity/Multimedia/Sound/Utilities
Provides:       alsa-tools-gui:/usr/bin/hdajackretask

%description -n hdajackretask
hdajackretask is a GUI tool to make it easy to retask HD-audio jacks.

%package -n hdajacksensetest
Version:        0.20141006
Release:        0
Summary:        Tool to check HD-audio jack/pin status
Group:          Productivity/Multimedia/Sound/Utilities

%description -n hdajacksensetest
hdajacksensetest is a small program to check the current pin/jack status
of the HD-audio codec.

%package -n hdspconf
Version:        1.4
Release:        0
Summary:        GUI to control Hammerfall HDSP settings
Group:          Productivity/Multimedia/Sound/Utilities
Provides:       alsa-tools-gui:/usr/bin/hdspconf

%description -n hdspconf
HDSPConf is a GUI to control the Hammerfall HDSP Alsa Settings.
Up to four hdsp cards are supported.

%package -n hdspmixer
Version:        1.11
Release:        0
Summary:        GUI tool to control advanced routing of RME Hammerfall DSP cards
Group:          Productivity/Multimedia/Sound/Utilities
Provides:       alsa-tools-gui:/usr/bin/hdspmixer

%description -n hdspmixer
HDSPMixer is the Linux equivalent of the Totalmix application from RME.
It is a tool to control the advanced routing features of the RME
Hammerfall DSP soundcard series.

%prep
%setup -q -a 4
%patch -P 1 -p1
cp %{SOURCE3} .
%patch -P 101 -p1

sed -i '1s@/usr/bin/env python$@/usr/bin/python3@' hwmixvolume/hwmixvolume

ALL_PACKS="seq/sbiload hdsploader usx2yloader us428control as10k1 ld10k1 hwmixvolume hda-verb"
%ifarch %ix86
ALL_PACKS="$ALL_PACKS sb16_csp sscape_ctl"
%endif

%if %{build_hwdep_loader}
ALL_PACKS="$ALL_PACKS pcxhrloader mixartloader vxloader"
%endif

ALL_PACKS="$ALL_PACKS envy24control rmedigicontrol echomixer"

%if %{have_gtk3}
ALL_PACKS="$ALL_PACKS hdajackretask hdajacksensetest"
%endif

ALL_PACKS="$ALL_PACKS hdspconf hdspmixer"
echo "$ALL_PACKS" > .allpacks

%build
export AUTOMAKE_JOBS="%{?_smp_mflags}"
for d in `cat .allpacks`; do
  (cd $d
  autoreconf -fi
  %configure
  make %{?_smp_mflags}
  )
done
# compile as10k1 examples
make -C as10k1/examples dsp %{?_smp_mflags}

%install
for d in `cat .allpacks`; do
  (cd $d
make DESTDIR=%{buildroot} install %{?_smp_mflags}
  )
done
find %{buildroot} -type f -name "*.la" -delete -print
# remove obsolete hotplug files
rm -rf %{buildroot}%{_sysconfdir}/hotplug
# install desktop files
%suse_update_desktop_file envy24control AudioVideo Mixer GTK
%suse_update_desktop_file -i rmedigicontrol AudioVideo Mixer GTK
%suse_update_desktop_file hdspconf AudioVideo Utility
%suse_update_desktop_file hdspmixer AudioVideo Mixer
%suse_update_desktop_file hdajackretask AudioVideo Utility
%suse_update_desktop_file hwmixvolume AudioVideo Mixer
%suse_update_desktop_file echomixer AudioVideo Mixer
# opl3 sounds
mkdir -p %{buildroot}%{_datadir}/sounds/opl3
install -c -m 0644 *.o3 *.sb %{buildroot}%{_datadir}/sounds/opl3
# clean up Makefiles in doc and examples subdirs for installation
rm -f as10k1/examples/Makefile*
rm -f ld10k1/doc/Makefile*

%post -n envy24control
%{?desktop_database_post}
exit 0

%postun -n envy24control
%{?desktop_database_postun}
exit 0

%post -n rmedigicontrol
%{?desktop_database_post}
exit 0

%postun -n rmedigicontrol
%{?desktop_database_postun}
exit 0

%post -n hdspconf
%{?desktop_database_post}
exit 0

%postun -n hdspconf
%{?desktop_database_postun}
exit 0

%post -n hdspmixer
%{?desktop_database_post}
exit 0

%postun -n hdspmixer
%{?desktop_database_postun}
exit 0

%post -n hwmixvolume
%{?desktop_database_post}
exit 0

%postun -n hwmixvolume
%{?desktop_database_postun}
exit 0

%post -n echomixer
%{?desktop_database_post}
exit 0

%postun -n echomixer
%{?desktop_database_postun}
exit 0

%post -n hdajackretask
%{?desktop_database_post}
exit 0

%postun -n hdajackretask
%{?desktop_database_postun}
exit 0

%post   -n liblo10k1-0 -p /sbin/ldconfig
%postun -n liblo10k1-0 -p /sbin/ldconfig

%files -n as10k1
%{_bindir}/as10k1
%doc as10k1/COPYING
%doc as10k1/README
%doc as10k1/examples

%files -n hda-verb
%{_bindir}/hda-verb
%doc hda-verb/ChangeLog
%doc hda-verb/README

%files -n ld10k1
%{_sbindir}/ld10k1
%{_sbindir}/ld10k1d
%{_sbindir}/dl10k1
%{_bindir}/lo10k1
%{_bindir}/init_*
%{_datadir}/ld10k1
%doc ld10k1/AUTHORS
%doc ld10k1/COPYING
%doc ld10k1/README
%doc ld10k1/doc

%files -n liblo10k1-0
%{_libdir}/liblo10k1.so.*

%files -n ld10k1-devel
%{_includedir}/lo10k1
%{_libdir}/liblo10k1.so
%{_datadir}/aclocal/*.m4

%files -n sbiload
%{_bindir}/sbiload
%{_datadir}/sounds/opl3
%doc seq/sbiload/COPYING
%doc seq/sbiload/README

%files -n hdsploader
%{_bindir}/hdsploader
%doc hdsploader/AUTHORS
%doc hdsploader/COPYING
%doc hdsploader/README

%files -n usx2yloader
%{_bindir}/usx2yloader
%doc usx2yloader/README

%files -n us428control
%{_bindir}/us428control

%files -n hwmixvolume
%{_bindir}/hwmixvolume
%{_datadir}/applications/hwmixvolume.desktop
%{_datadir}/icons/hicolor/*/apps/hwmixvolume.png
%doc hwmixvolume/README

%if %{build_hwdep_loader}
%files -n pcxhrloader
%{_bindir}/pcxhrloader
%doc pcxhrloader/README

%files -n mixartloader
%{_bindir}/mixartloader
%doc mixartloader/README

%files -n vxloader
%{_bindir}/vxloader
%doc vxloader/README
%endif

%ifarch %ix86
%files -n sscape-ctl
%{_bindir}/sscape_ctl

%files -n cspctl
%{_bindir}/cspctl
%doc sb16_csp/README
%{_mandir}/man?/cspctl.*
%endif

%files -n envy24control
%{_bindir}/envy24control
%{_datadir}/applications/envy24control.desktop
%{_datadir}/icons/hicolor/*/apps/envy24control.png
%{_mandir}/man?/envy24control.*
%doc envy24control/AUTHORS
%doc envy24control/COPYING
%doc envy24control/README*

%files -n rmedigicontrol
%{_bindir}/rmedigicontrol
%{_datadir}/applications/rmedigicontrol.desktop
%{_datadir}/pixmaps/rmedigicontrol.png
%doc rmedigicontrol/AUTHORS
%doc rmedigicontrol/COPYING
%doc rmedigicontrol/README

%files -n echomixer
%{_bindir}/echomixer
%{_datadir}/applications/echomixer.desktop
%{_datadir}/icons/hicolor/*/apps/echomixer.png
%doc echomixer/AUTHORS
%doc echomixer/ChangeLog
%doc echomixer/COPYING
%doc echomixer/README

%if %{have_gtk3}
%files -n hdajackretask
%{_bindir}/hdajackretask
%{_datadir}/applications/hdajackretask.desktop
%{_datadir}/icons/hicolor/*/apps/hdajackretask.png
%doc hdajackretask/AUTHORS
%doc hdajackretask/README

%files -n hdajacksensetest
%{_bindir}/hdajacksensetest
%endif

%files -n hdspconf
%{_bindir}/hdspconf
%{_datadir}/applications/hdspconf.desktop
%{_datadir}/icons/hicolor/*/apps/hdspconf.png
%doc hdspconf/AUTHORS
%doc hdspconf/ChangeLog
%doc hdspconf/COPYING
%doc hdspconf/README

%files -n hdspmixer
%{_bindir}/hdspmixer
%{_datadir}/applications/hdspmixer.desktop
%{_datadir}/icons/hicolor/*/apps/hdspmixer.png
%doc hdspconf/AUTHORS
%doc hdspconf/ChangeLog
%doc hdspconf/COPYING
%doc hdspconf/README

%changelog
