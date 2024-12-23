#
# spec file for package lsp-plugins
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


%ifarch %arm aarch64
%define _lto_cflags %{nil}
%endif
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects

Name:           lsp-plugins
Version:        1.2.20
Release:        0
Summary:        Linux Studio Plugins Project (Stand-alone)
License:        LGPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://lsp-plug.in/
Source0:        https://github.com/sadko4u/lsp-plugins/releases/download/%{version}/%{name}-src-%{version}.tar.gz
Patch0:         lsp-dsp-lib-Fixed-invalid-label.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ladspa
BuildRequires:  ladspa-devel
BuildRequires:  php8
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
Requires:       %{name}-common = %{version}

%description
LSP (Linux Studio Plugins) is a collection of open-source plugins
currently compatible with LADSPA, LV2, CLAP and LinuxVST formats.

The basic idea is to fill the lack of good and useful plugins under
the GNU/Linux platform.

%package        common
Summary:        Linux Studio Plugins (Common files)
Group:          Productivity/Multimedia/Sound/Utilities

%description    common
Common files for lsp-plugins.

%package        doc
Summary:        Linux Studio Plugins Documentation
Group:          Documentation/HTML
BuildArch:      noarch

%description    doc
Documentation for Linux Studio Plugins Project

%package -n     lv2-%{name}
Summary:        Linux Studio Plugins (LV2)
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       %{name}-common = %{version}

%description -n lv2-%{name}
LSP (Linux Studio Plugins) is a collection of open-source plugins
currently compatible with LADSPA, LV2, CLAP and LinuxVST formats.

The basic idea is to fill the lack of good and useful plugins under
the GNU/Linux platform.

This is the LV2 version of the plugins.

%package -n     vst-%{name}
Summary:        Linux Studio Plugins (VST)
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       %{name}-common = %{version}

%description -n vst-%{name}
LSP (Linux Studio Plugins) is a collection of open-source plugins
currently compatible with LADSPA, LV2, CLAP and LinuxVST formats.

The basic idea is to fill the lack of good and useful plugins under
the GNU/Linux platform.

This is the VST version of the plugins.

%package -n     ladspa-%{name}
Summary:        Linux Studio Plugins (LADSPA)
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       %{name}-common = %{version}

%description -n ladspa-%{name}
LSP (Linux Studio Plugins) is a collection of open-source plugins
currently compatible with LADSPA, LV2, CLAP and LinuxVST formats.

The basic idea is to fill the lack of good and useful plugins under
the GNU/Linux platform.

This is the LADSPA version of the plugins.

%package -n    clap-%{name}
Summary:        Linux Studio Plugins (CLAP)
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       %{name}-common = %{version}

%description -n clap-%{name}
LSP (Linux Studio Plugins) is a collection of open-source plugins
currently compatible with LADSPA, LV2, CLAP and LinuxVST formats.

The basic idea is to fill the lack of good and useful plugins under
the GNU/Linux platform.

This is the CLAP version of the plugins.

%package -n     vst3-%{name}
Summary:        Linux Studio Plugins (VST3)
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       %{name}-common = %{version}

%description -n vst3-%{name}
LSP (Linux Studio Plugins) is a collection of open-source plugins
currently compatible with LADSPA, LV2, CLAP and LinuxVST formats.

The basic idea is to fill the lack of good and useful plugins under
the GNU/Linux platform.

This is the VST3 version of the plugins.

%package -n     gstreamer-%{name}
Summary:        Linux Studio Plugins (GStreamer)
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       %{name}-common = %{version}

%description -n gstreamer-%{name}
LSP (Linux Studio Plugins) is a collection of open-source plugins
currently compatible with LADSPA, LV2, CLAP and LinuxVST formats.

The basic idea is to fill the lack of good and useful plugins under
the GNU/Linux platform.

This is the GStreamer version of the plugins.

%package devel
Summary:        Linux Studio Plugins Development files
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       %{name}-common = %{version}

%description devel

Development files for Linux Studio Plugins

%prep
%setup -q -n %{name}
%patch -P 0 -p1 -d modules/lsp-dsp-lib

%build
export CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"
make config PREFIX="%{_prefix}" LIBDIR="%{_libdir}" SHAREDDIR=%{_datadir} FEATURES='vst3 lv2 vst2 clap doc jack ladspa xdg gst ui'
%make_build

%install
%make_install

mkdir -p %{buildroot}/%{_docdir}
mv %{buildroot}/%{_datadir}/doc/%{name} %{buildroot}/%{_docdir}/

%fdupes -s %{buildroot}%{_libdir}

%post common -p /sbin/ldconfig
%postun common -p /sbin/ldconfig

%files
%{_bindir}/%{name}-*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/liblsp-plugins-jack*.so
%dir %{_datadir}/desktop-directories
%dir %{_sysconfdir}/xdg
%dir %{_sysconfdir}/xdg/menus
%dir %{_sysconfdir}/xdg/menus/applications-merged
%{_datadir}/applications/*.desktop
%{_datadir}/desktop-directories/*
%exclude %{_datadir}/icons/hicolor/*
%config %{_sysconfdir}/xdg/menus/applications-merged/lsp-plugins.menu

%files common
%license COPYING COPYING.LESSER modules/lsp-plugins-shared/LICENSE_OFL.txt
%{_libdir}/liblsp-r3d-glx-lib*.so

%files devel
%{_libdir}/pkgconfig/*.pc
%{_libdir}/liblsp-*.a

%files -n ladspa-%{name}
%{_libdir}/ladspa/%{name}-ladspa.so

%files -n lv2-%{name}
%dir %{_libdir}/lv2
%{_libdir}/lv2/%{name}.lv2

%files -n vst-%{name}
%dir %{_libdir}/vst
%{_libdir}/vst/%{name}.vst

%files -n clap-%{name}
%dir %{_libdir}/clap
%{_libdir}/clap/*

%files -n vst3-%{name}
%dir %{_libdir}/vst3
%{_libdir}/vst3/*

%files -n gstreamer-%{name}
%dir %{_libdir}/gstreamer-1.0
%{_libdir}/gstreamer-1.0/*
%{_libdir}/%{name}/liblsp-plugins-gstreamer*.so

%files doc
%{_docdir}/%{name}

%changelog
