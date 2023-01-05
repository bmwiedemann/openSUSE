#
# spec file for package goverlay
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


Name:           goverlay
Version:        0.9.1
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
Requires:       Mesa-demo
Requires:       mangohud
Requires:       replay-sorcery
Requires:       vkbasalt
Requires:       vulkan-tools

%description
GOverlay is a graphical UI to manage Vulkan/OpenGL overlays.

%prep
%setup -q
%patch0 -p1

%build
# Manually set build flag as Leap 15.2 does not support %%{set_build_flags} macro unlike TW.
CFLAGS='-O2 -Wall -D_FORTIFY_SOURCE=2 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -Werror=return-type -flto=auto -g'
export CFLAGS
CXXFLAGS='-O2 -Wall -D_FORTIFY_SOURCE=2 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -Werror=return-type -flto=auto -g'
export CXXFLAGS
FFLAGS='-O2 -Wall -D_FORTIFY_SOURCE=2 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -Werror=return-type -flto=auto -g'
export FFLAGS
FCFLAGS='-O2 -Wall -D_FORTIFY_SOURCE=2 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -Werror=return-type -flto=auto -g'
export FCFLAGS
LDFLAGS=-flto=auto
export LDFLAGS

%make_build

%install
%make_install prefix=%{_prefix} libexecdir=/%{_lib}

# Desktop file validation fails in Leap
# https://github.com/benjamimgois/goverlay/issues/46
%if 0%{?sle_version} > 0 && 0%{?sle_version} <= 150200
%suse_update_desktop_file -r io.github.benjamimgois.%{name} Development Profiling
%endif

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
