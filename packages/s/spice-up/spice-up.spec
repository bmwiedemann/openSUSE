#
# spec file for package spice-up
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           spice-up
Version:        1.8.2
Release:        0
Summary:        Desktop presentation application
License:        GPL-3.0-only
Group:          Productivity/Office/Other
URL:            https://github.com/Philip-Scott/Spice-up
Source:         https://github.com/Philip-Scott/Spice-up/archive/%{version}.tar.gz#/Spice-up-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  vala >= 0.40.4
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libsoup-2.4)
Recommends:     %{name}-lang

%description
Spice-up is a desktop presentation application
based upon SpiceOfDesign's presentation concept.

%lang_package

%prep
%setup -q -n Spice-up-%{version}

%build
%cmake \
    -DGSETTINGS_COMPILE=OFF

# remove smp_mflags to avoid compilation errors
make -j1 V=1

%install
%cmake_install
%find_lang com.github.philip-scott.spice-up %{name}.lang
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc README.md
%{_bindir}/com.github.philip-scott.spice-up
%{_datadir}/applications/com.github.philip-scott.spice-up.desktop
%{_datadir}/com.github.philip-scott.spice-up/
%{_datadir}/glib-2.0/schemas/com.github.philip-scott.spice-up.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.??g
%{_datadir}/metainfo/com.github.philip-scott.spice-up.appdata.xml
%{_datadir}/mime/packages/com.github.philip-scott.spice-up.mime.xml

%files lang -f %{name}.lang

%changelog
