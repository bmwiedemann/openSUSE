#
# spec file for package lsp-plugins
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%ifarch %arm aarch64
%define _lto_cflags %{nil}
%endif
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects

Name:           lsp-plugins
Version:        1.2.4
Release:        0
Summary:        Linux Studio Plugins Project (Stand-alone)
License:        LGPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://lsp-plug.in/
Source0:        https://github.com/sadko4u/lsp-plugins/releases/download/%{version}/%{name}-src-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ladspa
BuildRequires:  ladspa-devel
%if 0%{?suse_version} >= 1550
BuildRequires:  php8
%else
BuildRequires:  php7
%endif
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
Requires:       %{name}-common = %{version}

%description
LSP (Linux Studio Plugins) is a collection of open-source plugins
currently compatible with LADSPA, LV2 and LinuxVST formats.

The basic idea is to fill the lack of good and useful plugins under
the GNU/Linux platform.

%package        common
Summary:        Linux Studio Plugins (Common files)
Group:          Productivity/Multimedia/Sound/Utilities

%description    common
Common files for lsp-plugins.

%package        doc
Summary:        Linux Studio Plugins Documents
Group:          Documentation/HTML
BuildArch:      noarch

%description    doc
Documents for Linux Studio Plugins Project

%package -n     lv2-%{name}
Summary:        Linux Studio Plugins Documents (LV2)
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       %{name}-common = %{version}

%description -n lv2-%{name}
LSP (Linux Studio Plugins) is a collection of open-source plugins
currently compatible with LADSPA, LV2 and LinuxVST formats.

The basic idea is to fill the lack of good and useful plugins under
the GNU/Linux platform.

This is the LV2 version of the plugins.

%package -n     vst-%{name}
Summary:        Linux Studio Plugins Documents (VST)
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       %{name}-common = %{version}

%description -n vst-%{name}
LSP (Linux Studio Plugins) is a collection of open-source plugins
currently compatible with LADSPA, LV2 and LinuxVST formats.

The basic idea is to fill the lack of good and useful plugins under
the GNU/Linux platform.

This is the VST version of the plugins.

%package -n     ladspa-%{name}
Summary:        Linux Studio Plugins Documents (LADSPA)
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       %{name}-common = %{version}

%description -n ladspa-%{name}
LSP (Linux Studio Plugins) is a collection of open-source plugins
currently compatible with LADSPA, LV2 and LinuxVST formats.

The basic idea is to fill the lack of good and useful plugins under
the GNU/Linux platform.

This is the LADSPA version of the plugins.

%package devel
Summary:        Linux Studio Plugins Development files
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       %{name}-common = %{version}

%description devel

Development files for Linux Studio Plugins

%prep
%setup -qn %{name}
%autopatch -p1

%build
#export PREFIX="%{_prefix}" DOC_PATH="%{_docdir}" LIB_PATH="%{_libdir}"
export CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"
make config PREFIX="%{_prefix}" LIBDIR="%{_libdir}" SHAREDDIR=%{_datadir} FEATURES='lv2 vst2 doc jack ladspa xdg'
%make_build

%install
#export PREFIX="%{_prefix}" DOC_PATH="%{_docdir}" LIB_PATH="%{_libdir}"
%make_install

mkdir -p %{buildroot}/%{_docdir}
mv %{buildroot}/%{_datadir}/doc/%{name} %{buildroot}/%{_docdir}/

%fdupes -s %{buildroot}%{_libdir}

%files
%{_bindir}/%{name}-*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/liblsp*
%dir %{_datadir}/desktop-directories
%dir %{_sysconfdir}/xdg
%dir %{_sysconfdir}/xdg/menus
%dir %{_sysconfdir}/xdg/menus/applications-merged
%{_datadir}/applications/*.desktop
%{_datadir}/desktop-directories/*
%exclude %{_datadir}/icons/hicolor/*
%config %{_sysconfdir}/xdg/menus/applications-merged/lsp-plugins.menu

%files common
%license COPYING COPYING.LESSER
%{_libdir}/liblsp-*.so

%files devel
%{_libdir}/pkgconfig/*.pc
%{_libdir}/liblsp-*.a
%dir %{_includedir}/lsp-plug.in
%dir %{_includedir}/lsp-plug.in/r3d
%dir %{_includedir}/lsp-plug.in/r3d/glx
%{_includedir}/lsp-plug.in/r3d/glx/*.h

%files -n ladspa-%{name}
%{_libdir}/ladspa/%{name}-ladspa-%{version}.so

%files -n lv2-%{name}
%dir %{_libdir}/lv2
%{_libdir}/lv2/%{name}.lv2

%files -n vst-%{name}
%dir %{_libdir}/vst
%{_libdir}/vst/%{name}

%files doc
%{_docdir}/%{name}

%changelog
