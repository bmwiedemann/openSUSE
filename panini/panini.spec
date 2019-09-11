#
# spec file for package panini
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           panini
Version:        0.73.0
Release:        0
Summary:        A tool for creating perspective views from panoramic and wide angle images
License:        GPL-3.0-only
Group:          Productivity/Graphics/Viewers
URL:            https://github.com/lazarus-pkgs/panini
Source:         https://github.com/lazarus-pkgs/panini/archive/v%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(zlib)

%description
Visual tool for creating perspective views from panoramic and wide angle photographs.

%prep
%setup -q

%build
# use qmake macro is present (fedora)
%{?qmake_qt5}%{?!qmake_qt5:qmake-qt5} PREFIX=%{buildroot}%{_prefix}/
make %{?_smp_mflags}

%install
%make_install

%files
%license LICENSE
%doc README.md USAGE.md
%{_bindir}/panini
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/panini.appdata.xml

%changelog
