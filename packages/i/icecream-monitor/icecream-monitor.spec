#
# spec file for package icecream-monitor
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           icecream-monitor
Version:        3.2.0
Release:        0
Summary:        Monitor Program for the icecream Compile Farm
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/icecc/icemon
Source0:        icemon-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  docbook2x
BuildRequires:  hicolor-icon-theme
BuildRequires:  lzo-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xsltproc
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(icecc)

%description
icecream is the next generation distcc. This package provides a monitor
program.

%prep
%setup -q -n icemon-%{version}

%build
%cmake
%make_jobs

%install
%cmake_install
%suse_update_desktop_file icemon Development Building

%files
%{_bindir}/icemon
%{_datadir}/applications/icemon.desktop
%{_datadir}/icons/hicolor/*/apps/icemon.*
%{_mandir}/man1/icemon.*

%changelog
