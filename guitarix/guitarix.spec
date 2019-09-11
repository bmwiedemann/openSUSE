#
# spec file for package guitarix
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%bcond_without ladspa

Name:           guitarix
Version:        0.37.3
Release:        0
Summary:        Simple Linux amplifier for jack
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
Url:            http://guitarix.sourceforge.net/
Source:         http://downloads.sourceforge.net/project/guitarix/guitarix/guitarix2-%{version}.tar.xz
Patch0:         fpexception.patch
Patch1:         guitarix-boost69.patch
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_context-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%else
BuildRequires:  boost-devel >= 1.56
%endif
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  intltool
%if %{with ladspa}
BuildRequires:  ladspa-devel
%endif
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  zita-convolver-devel
#BuildRequires:  zita-resampler-devel
BuildRequires:  pkgconfig(avahi-gobject)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(fftw3l)
BuildRequires:  pkgconfig(gail)
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(gdk-x11-2.0)
BuildRequires:  pkgconfig(gdkmm-2.4)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-unix-print-2.0)
BuildRequires:  pkgconfig(gtk+-x11-2.0)
BuildRequires:  pkgconfig(gtkmm-2.4)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(lrdf)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(sndfile)
Requires:       jack
Requires:       meterbridge
Requires:       vorbis-tools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
guitarix is a simple mono amplifier to jack with one input and two
outputs. Designed to get nice trash/metal/rock/guitar sounds.

Available are the controls for bass, treble, gain, balance,
distortion, freeverb, impulse response (pre state), crybaby(wah),
feedback/feedforward-filter and echo. A fixed resonator will use,
when distortion is disabled.

%package -n libgxw0
Summary:        Guitarix runtime library
# Earlier weird packaging of internal libraries
Group:          System/Libraries
Obsoletes:      %{name}-devel < %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n libgxw0
guitarix is a simple mono amplifier to jack with one input and two
outputs.

%package -n libgxwmm0
Summary:        Guitarix runtime library
# Earlier weird packaging of internal libraries
Group:          System/Libraries
Obsoletes:      %{name}-devel < %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n libgxwmm0
guitarix is a simple mono amplifier to jack with one input and two
outputs.

%if %{with ladspa}
%package -n ladspa-%{name}
Summary:        Guitarix - ladspa plugins
Group:          Productivity/Multimedia/Sound/Utilities

%description -n ladspa-%{name}
guitarix is a simple mono amplifier to jack with one input and two
outputs. Designed to get nice trash/metal/rock/guitar sounds.

Available are the controls for bass, treble, gain, balance,
distortion, freeverb, impulse response (pre state), crybaby(wah),
feedback/feedforward-filter and echo. A fixed resonator will use,
when distortion is disabled.

This package contains the  LADSPA plugins (UniqID 4061 - 4068).
%endif

%package -n lv2-%{name}
Summary:        Guitarix - LV2 plugins
Group:          Productivity/Multimedia/Sound/Utilities

%description -n lv2-%{name}
guitarix is a simple mono amplifier to jack with one input and two
outputs. Designed to get nice trash/metal/rock/guitar sounds.

Available are the controls for bass, treble, gain, balance,
distortion, freeverb, impulse response (pre state), crybaby(wah),
feedback/feedforward-filter and echo. A fixed resonator will use,
when distortion is disabled.

This package contains the LV2 plugins.

%package -n bestplugins
Summary:        Best Mega Pack 1+3
Group:          Productivity/Multimedia/Sound/Utilities

%description -n bestplugins
Bestplugins Mega Pack 1+3 contains dozens of guitar sounds from famous bands.

%prep
%setup -q -n guitarix-%{version}
%autopatch -p0

%build
#todo: add faust package to openSUSE
# TODO: Convert to python3, only builds with python2 so far.
#find . -name "*.py" -print -exec 2to3 -wn {} \;
#find . -name "*.py" -print -exec 2to3 -wn {} \;
#for i in `grep -rl "/usr/bin/env python"`;do 2to3 -wn ${i} ;done
#for i in `grep -rl "/usr/bin/env python"`;do sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' ${i} ;done

export LDFLAGS="-ldl"
%if 1 == 0
%define gcc_version 7
export CC=gcc-7
export CPP=cpp-7
export CXX=g++-7
%endif
./waf configure -v --faust \
                   --libdir=%{_libdir} \
                   --includeresampler \
%if %{with ladspa}
                   --ladspadir=%{_libdir}/ladspa  \
                   --ladspa \
                   --new-ladspa \
%endif
                   --prefix=%{_prefix} \
                   --cxxflags="%{optflags} \
                   -std=gnu++0x"
./waf build -v %{?_smp_mflags}

%install
./waf install --destdir=%{buildroot}
%suse_update_desktop_file -i %{name} AudioVideo Music
%find_lang %{name}
# No header files installed for this lib
rm -f "%{buildroot}/%{_libdir}/"*.so

%fdupes -s %{buildroot}/%{_datadir}/gx_head/
%fdupes -s %{buildroot}/%{_libdir}/lv2/

%post   -n libgxw0 -p /sbin/ldconfig
%postun -n libgxw0 -p /sbin/ldconfig

%post   -n libgxwmm0 -p /sbin/ldconfig
%postun -n libgxwmm0 -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc changelog README
%license COPYING
%dir %{_datadir}/gx_head
%dir %{_datadir}/gx_head/builder
%dir %{_datadir}/gx_head/skins
%dir %{_datadir}/gx_head/sounds/
%{_bindir}/%{name}
%{_datadir}/gx_head/builder/*.glade
%{_datadir}/gx_head/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/gx_head*.png
%{_datadir}/pixmaps/gx_bypass.png
%{_datadir}/pixmaps/gx_off.png
%{_datadir}/pixmaps/gx_on.png
%{_datadir}/pixmaps/gx_log_grey.png
%{_datadir}/pixmaps/gx_log_red.png
%{_datadir}/pixmaps/gx_log_yellow.png
%{_datadir}/pixmaps/gx_splash.png
%{_datadir}/pixmaps/insert_off.png
%{_datadir}/pixmaps/insert_on.png
%{_datadir}/pixmaps/jackd_off.png
%{_datadir}/pixmaps/jackd_on.png

%files -n libgxw0
%defattr(-,root,root)
%{_libdir}/libgxw.so.0
%{_libdir}/libgxw.so.0.1

%files -n libgxwmm0
%defattr(-,root,root)
%{_libdir}/libgxwmm.so.0
%{_libdir}/libgxwmm.so.0.1

%files -n lv2-%{name}
%defattr(-,root,root)
%{_libdir}/lv2/

%if %{with ladspa}
%files -n ladspa-%{name}
%defattr(-,root,root)
%dir %{_libdir}/ladspa
%{_libdir}/ladspa/*.so
%dir %{_datadir}/ladspa
%dir %{_datadir}/ladspa/rdf
%{_datadir}/ladspa/rdf/%{name}_amp.rdf
%{_datadir}/ladspa/rdf/%{name}.rdf
%endif

%files -n bestplugins
%defattr(-,root,root)
%dir %{_datadir}/gx_head/sounds/bands/

%changelog
