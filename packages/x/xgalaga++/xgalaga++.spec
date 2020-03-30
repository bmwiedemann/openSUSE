#
# spec file for package xgalaga++
#
# Copyright (c) 2020 SUSE LLC
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


Name:           xgalaga++
Version:        0.9
Release:        0
Summary:        Classic single screen vertical shoot em up
License:        GPL-2.0-only
URL:            http://marc.mongenet.ch/OSS/XGalaga/
Source0:        http://marc.mongenet.ch/OSS/XGalaga/%{name}_%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
# PATCH-FIX-UPSTREAM -- TODO
Patch0:         reproducible.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xpm)
%if 0%{?suse_version}
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif

%description
XGalaga++ is a classic vertical scrolling shoot em up.
It requires no X Window extension and its window is freely resizable.
It is inspired by XGalaga, but rewritten from scratch,
except for the graphics.

%prep
%setup -q
%patch0 -p1

# Adjust Highscore
sed -i -e 's|/usr/local|/usr/|' \
    -i -e 's|HIGH_SCORES_FILE=/var|#HIGH_SCORES_FILE=/var|' \
    -i -e 's|#HIGH_SCORES_FILE=.xgalaga++|HIGH_SCORES_FILE=.xgalaga++|' Makefile

%build
%make_build CXXFLAGS="%{optflags}" all

%install
# install executable
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}

# install man
install -Dm 0644 %{name}.6x %{buildroot}%{_mandir}/man6/%{name}.6x

# install icon
install -Dm 0644 %{SOURCE2} %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

# install Desktop file
install -Dm 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
%endif

%files
%doc README
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6x%{ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/

%changelog
