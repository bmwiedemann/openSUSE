#
# spec file for package goverlay
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


Name:           goverlay
Version:        1.1.1
Release:        0
Summary:        Graphical UI to help manage overlays
License:        GPL-3.0-or-later
URL:            https://github.com/benjamimgois/goverlay
Source0:        https://github.com/benjamimgois/goverlay/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE goverlay-enable-debuginfo-generation.patch andythe_great@pm.me -- Enable generate debuginfo
Patch0:         goverlay-enable-debuginfo-generation.patch
BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  lazarus
BuildRequires:  libQt5Pas-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-3.0)
ExclusiveArch:  x86_64 aarch64
Requires:       mangohud
Recommends:     Mesa-demo
Recommends:     vkbasalt
Recommends:     vulkan-tools
%if 0%{?suse_version} > 1500
BuildRequires:  lazarus-lcl-qt6
%endif

%description
GOverlay is a graphical UI to manage Vulkan/OpenGL overlays.

%prep
%autosetup -p1
chmod -x LICENSE README.md

%build
%{set_build_flags}
%make_build

%install
%make_install prefix=%{_prefix} libexecdir=/%{_lib}
%suse_update_desktop_file -r io.github.benjamimgois.%{name} Development Profiling
%{__strip} %{buildroot}/usr/lib64/goverlay

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.benjamimgois.%{name}.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/metainfo/io.github.benjamimgois.%{name}.metainfo.xml

%changelog
