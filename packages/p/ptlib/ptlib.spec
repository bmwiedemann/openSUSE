#
# spec file for package libpt2
#
# Copyright (c) 2022 SUSE LLC
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

Name:           ptlib
Version:        2.18.8
Release:        0
# FIXME: when upgrading, check if the dc plugin builds with the current version of libdc1394. - Last check: 2.10.9 / 3.12.2012
%define _version 2_18_8
Summary:        Portable Windows Library from Equivalence Pty. Ltd. version 2
License:        MPL-1.0
Group:          Development/Libraries/C and C++
#Git-Clone:     https://git.code.sf.net/p/opalvoip/ptlib
URL:            https://sf.net/projects/opalvoip/
Source:         https://downloads.sf.net/opalvoip/%{name}-%{version}.tar.bz2
# PATCH-MISSING-TAG libpt2-fix-avc-plugin.patch jeffm@suse.com -- Fix build for avc-plugin. 
Patch1:         libpt2-fix-avc-plugin.patch 
# PATCH-FIX-UPSTREAM libpt2-aarch64.patch schwab@suse.de -- Add support for aarch64
Patch2:         libpt2-aarch64.patch
Patch3:         libpt2-ppc64le.patch
# PATCH-FIX-UPSTREAM missing-decls.patch -- Fix missing declarations
Patch7:         missing-decls.patch
Patch10:        libpt2-gnu-make-4.3.patch
Patch11:        libpt2-move.patch
Patch12:        pttypes.patch
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
BuildRequires:  openldap2-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libpulse)

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

%package devel
Summary:        Development files for %{name} (includes headers and scripts)
Group:          Development/Libraries/C and C++
Requires:       libpt%{_version} = %{version}
Conflicts:      pwlib-devel
# libpt2-devel was last used in openSUSE 11.3; libpt-devel was last used in 15.x
Provides:       libpt2-devel = %{version}-%{release}
Obsoletes:      libpt2-devel < %{version}-%{release}
Provides:       libpt-devel = %{version}-%{release}
Obsoletes:      libpt-devel < %{version}-%{release}

%description devel
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
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch7 -p1
%if %{pkg_vcmp make >= 4.3}
%patch10 -p1
%endif
%patch11 -p1
%patch12 -p1

%build
export CXXFLAGS="%optflags -fvisibility-inlines-hidden"
#CXXFLAGS and CFLAGS are mixed up in the Makefiles..
export CFLAGS="%optflags -fvisibility-inlines-hidden"
%configure \
	--enable-oss \
	--enable-pulse \
%if %{build_avc}
	--enable-avc \
%endif
        --enable-ipv6 --enable-cpp17
%make_build CPU="" OS="" DSYMUTIL=/bin/true

%install
%make_install CPU="" OS=""
rm -f %{buildroot}%{_libdir}/libpt_s.a

%post -n libpt%{_version} -p /sbin/ldconfig

%postun -n libpt%{_version} -p /sbin/ldconfig

%files -n libpt%{_version}
%doc mpl-1.0.htm History.txt
%{_libdir}/libpt.so.2*
# We explicitly list the plugins that are shipped by default to make sure we
# don't lose any without noticing it
%dir %{_libdir}/%{name}-%{version}
%dir %{_libdir}/%{name}-%{version}/device
%dir %{_libdir}/%{name}-%{version}/device/sound
%dir %{_libdir}/%{name}-%{version}/device/videoinput
%{_libdir}/%{name}-%{version}/device/sound/alsa_ptplugin.so
%{_libdir}/%{name}-%{version}/device/sound/oss_ptplugin.so
%{_libdir}/%{name}-%{version}/device/videoinput/v4l2_ptplugin.so

%files devel
%doc ReadMe.txt
%{_datadir}/ptlib/
%{_includedir}/pt*
%{_libdir}/libpt.so
%{_libdir}/pkgconfig/ptlib.pc

%if %{build_avc}

%files -n libpt%{_version}-plugins-avc
%{_libdir}/%{name}-%{version}/device/videoinput/avc_ptplugin.so
%endif

%if %{build_dc}

%files -n libpt%{_version}-plugins-dc
%{_libdir}/%{name}-%{version}/device/videoinput/dc_ptplugin.so
%endif

%files -n libpt%{_version}-plugins-pulse
%{_libdir}/%{name}-%{version}/device/sound/pulse_ptplugin.so

%changelog
