#
# spec file for package libpt2
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define build_avc 1
%define build_dc 0
# Video4Linux is obsolete on Kernel 3.0, which we have after openSUSE 11.4
%define build_v4l 0%{?suse_version} <= 1140

Name:           libpt2
%define _name   ptlib
Version:        2.10.11
Release:        0
# FIXME: when upgrading, check if the dc plugin builds with the current version of libdc1394. - Last check: 2.10.9 / 3.12.2012
%define _version 2_10_11
Summary:        Portable Windows Library from Equivalence Pty. Ltd. version 2
License:        MPL-1.0
Group:          System/Libraries
Url:            http://www.opalvoip.org/
# https://sourceforge.net/projects/opalvoip
Source:         http://download.gnome.org/sources/ptlib/2.10/%{_name}-%{version}.tar.xz
# PATCH-MISSING-TAG libpt2-fix-avc-plugin.patch jeffm@suse.com -- Fix build for avc-plugin. 
Patch1:         libpt2-fix-avc-plugin.patch 
# PATCH-FIX-UPSTREAM libpt2-aarch64.patch schwab@suse.de -- Add support for aarch64
Patch2:         libpt2-aarch64.patch
Patch3:         libpt2-ppc64le.patch
# PATCH-FIX-UPSTREAM libpt2-bison-3.0.patch sf#259 dimstar@opensuse.org -- Fix build with bison 3.0
Patch4:         libpt2-bison-3.0.patch
# PATCH-FIX-OPENSUSE libpt2-gcc5-fixes.patch dmueller@suse.com -- Fix build against GCC 5
Patch5:         libpt2-gcc5-fixes.patch
# PATCH-FIX-OPENSUSE libpt2-2.10.11-gcc6.patch dimstar@opensuse.org -- Fix build against GCC 6
Patch6:         libpt2-2.10.11-gcc6.patch
# PATCH-FIX-UPSTREAM missing-decls.patch -- Fix missing declarations
Patch7:         missing-decls.patch
# PATCH-FIX-UPSTREAM libpt2-openssl11.patch boo#1055477 mgorse@suse.com -- port to OpenSSL 1.1.
Patch8:         libpt2-openssl11.patch
Patch9:         reproducible.patch
BuildRequires:  SDL-devel
BuildRequires:  alsa-devel
BuildRequires:  bison
BuildRequires:  cyrus-sasl-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
%if %{build_avc}
BuildRequires:  libavc1394-devel
%endif
%if %{build_dc}
BuildRequires:  libdc1394-devel
%endif
BuildRequires:  libdv-devel
BuildRequires:  libexpat-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libstdc++-devel
%if %{?build_v4l}
BuildRequires:  libv4l-devel
%endif
BuildRequires:  openldap2-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libpulse)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is a moderately large class library that was created many years
ago as a method to produce applications that run on both Microsoft
Windows and the X Window System.

%package -n libpt%{_version}

Summary:        Portable Windows Library from Equivalence Pty. Ltd. version 2
Group:          System/Libraries
# This used to be a subpackage
Provides:       libpt2-plugins-v4l2 = %{version}
Obsoletes:      libpt2-plugins-v4l2 < %{version}
# After openSUSE 11.4, there is no more v4l available. We obsolete it to ease upgrades
%if ! (%{build_v4l})
Obsoletes:      libpt%{_version}-plugins-v4l <= %{version}
%endif
%if ! %{build_avc}
Obsoletes:      libpt%{_version}-plugins-avc <= %{version}
%endif
%if ! %{build_dc}
Obsoletes:      libpt%{_version}-plugins-dc <= %{version}
%endif

%description -n libpt%{_version}
This is a moderately large class library that was created many years
ago as a method to produce applications that run on both Microsoft
Windows and the X Window System.

%package -n libpt-devel
Summary:        Development files for %{name} (includes headers and scripts)
Group:          Development/Libraries/C and C++
Requires:       libpt%{_version} = %{version}
Conflicts:      pwlib-devel
# libpt2-devel was last used in openSUSE 11.3
Provides:       libpt2-devel = %{version}
Obsoletes:      libpt2-devel < %{version}

%description -n libpt-devel
This package includes header files and scripts needed for developers
using the %{name} library.

%if %{build_avc}

%package -n libpt%{_version}-plugins-avc

Summary:        AVC plugin for %{name}
Group:          System/Libraries
Requires:       libpt%{_version} = %{version}
Provides:       libpt2-video-plugin
# Package name that was last used in openSUSE 11.3
Provides:       libpt2-plugins-avc = %{version}
Obsoletes:      libpt2-plugins-avc < %{version}

%description -n libpt%{_version}-plugins-avc
This plugin enables AVC (firewire control for digital video cameras)
support in %{name}.
%endif

%if %{build_dc}

%package -n libpt%{_version}-plugins-dc

Summary:        DC plugin for %{name}
Group:          System/Libraries
Requires:       libpt%{_version} = %{version}
Provides:       libpt2-video-plugin
# Package name that was last used in openSUSE 11.3
Provides:       libpt2-plugins-dc = %{version}
Obsoletes:      libpt2-plugins-dc < %{version}

%description -n libpt%{_version}-plugins-dc
This plugin enables DC control (via firewire for digital video cameras)
for %{name}.
%endif

%if %{build_v4l}

%package -n libpt%{_version}-plugins-v4l

Summary:        V4L support for %{name}
Group:          System/Libraries
Requires:       libpt%{_version} = %{version}
Provides:       libpt2-video-plugin

%description -n libpt%{_version}-plugins-v4l
This plugin enables 'video for linux' (version 1) support (e.g. for USB
cameras) for %{name}.
%endif

%package -n libpt%{_version}-plugins-pulse

Summary:        Pulseaudio support for %{name}
Group:          System/Libraries
Requires:       libpt%{_version} = %{version}
# No idea about why this provides is here. Feel free to remove it if you think
# is the best thing to do... or to add an explanation about why it is useful.
Provides:       libpt2-audio-plugin
Supplements:    libpt2
Supplements:    packageand(libpt2:pulseaudio)

%description -n libpt%{_version}-plugins-pulse
This plugin enables pulseaudio support for %{name}.

%prep
%setup -q -n %{_name}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
export CXXFLAGS="%optflags -fvisibility-inlines-hidden"
#CXXFLAGS and CFLAGS are mixed up in the Makefiles..
export CFLAGS="%optflags -fvisibility-inlines-hidden"
%configure \
	--enable-oss \
	--enable-pulse \
%if %{build_v4l}
	--enable-v4l \
%endif
%if %{build_avc}
	--enable-avc \
%endif
        --enable-ipv6
make %{?_smp_mflags} V=1

%install
%makeinstall
rm -f %{buildroot}%{_libdir}/libpt_s.a

%post -n libpt%{_version} -p /sbin/ldconfig

%postun -n libpt%{_version} -p /sbin/ldconfig

%files -n libpt%{_version}
%defattr(-,root,root)
%doc mpl-1.0.htm History.txt
%{_libdir}/libpt.so.2*
# We explicitly list the plugins that are shipped by default to make sure we
# don't lose any without noticing it
%dir %{_libdir}/%{_name}-%{version}
%dir %{_libdir}/%{_name}-%{version}/devices
%dir %{_libdir}/%{_name}-%{version}/devices/sound
%dir %{_libdir}/%{_name}-%{version}/devices/videoinput
%{_libdir}/%{_name}-%{version}/devices/sound/alsa_pwplugin.so
%{_libdir}/%{_name}-%{version}/devices/sound/oss_pwplugin.so
%{_libdir}/%{_name}-%{version}/devices/videoinput/v4l2_pwplugin.so

%files -n libpt-devel
%defattr(0644,root,root,0755)
%doc ReadMe.txt ReadMe_QOS.txt
%{_datadir}/ptlib/
%attr(0755, root, root) %{_datadir}/ptlib/make/ptlib-config
%{_includedir}/ptbuildopts.h
%{_includedir}/ptlib.h
%{_includedir}/ptlib/
%{_includedir}/ptclib/
%{_bindir}/ptlib-config
%{_libdir}/libpt.so
%{_libdir}/pkgconfig/ptlib.pc

%if %{build_avc}

%files -n libpt%{_version}-plugins-avc
%defattr(-,root,root)
%{_libdir}/%{_name}-%{version}/devices/videoinput/avc_pwplugin.so
%endif

%if %{build_dc}

%files -n libpt%{_version}-plugins-dc
%defattr(-,root,root)
%{_libdir}/%{_name}-%{version}/devices/videoinput/dc_pwplugin.so
%endif

%if %{build_v4l}

%files -n libpt%{_version}-plugins-v4l
%defattr(-,root,root)
%{_libdir}/%{_name}-%{version}/devices/videoinput/v4l_pwplugin.so
%endif

%files -n libpt%{_version}-plugins-pulse
%defattr(-,root,root)
%{_libdir}/%{_name}-%{version}/devices/sound/pulse_pwplugin.so

%changelog
