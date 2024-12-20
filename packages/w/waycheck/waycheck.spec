#
# spec file for package waycheck
#
# Copyright (c) Neal Gompa
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


%global qt6_minver 6.5

Name:           waycheck
Version:        1.5.0
Release:        0
Summary:        GUI that displays protocols implemented by a Wayland compositor

License:        Apache-2.0
URL:            https://gitlab.freedesktop.org/serebit/waycheck
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  meson
%if 0%{?suse_version} && 0%{?suse_version} < 1600
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  pkgconfig(Qt6Core) >= %{qt6_minver}
BuildRequires:  pkgconfig(Qt6Gui) >= %{qt6_minver}
BuildRequires:  pkgconfig(Qt6WaylandClient) >= %{qt6_minver}
BuildRequires:  pkgconfig(Qt6Widgets) >= %{qt6_minver}
BuildRequires:  pkgconfig(wayland-client)

Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
%autosetup -n %{name}-v%{version}


%build
%if 0%{?suse_version} && 0%{?suse_version} < 1600
export CC=gcc-11
export CXX=g++-11
%endif
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE.txt
%doc README.md
%{_bindir}/waycheck
%{_datadir}/applications/dev.serebit.Waycheck.desktop
%{_datadir}/metainfo/dev.serebit.Waycheck.metainfo.xml
%{_datadir}/icons/hicolor/

%changelog
