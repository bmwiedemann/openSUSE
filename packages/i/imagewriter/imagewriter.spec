#
# spec file for package imagewriter
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

%if 0%{?rhel_version} == 600
     %define dist el6
     %define breq qt-devel
     %define backend hal-devel
     %define qmake /usr/bin/qmake-qt4
     %define lrelease /usr/bin/lrelease-qt4
     %define definedbackend USEHAL
%endif

%if 0%{?fedora}
    %define breq qt4-devel
    %define backend udisks2
    %define qmake /usr/bin/qmake-qt4
    %define lrelease /usr/bin/lrelease-qt4
    %define definedbackend USEUDISKS2
%endif

%if 0%{?mandriva_version}
    %define breq libqt4-devel
    %define backend hal-devel
    %define qmake /usr/lib/qt4/bin/qmake
    %define lrelease /usr/lib/qt4/bin/lrelease
    %define definedbackend USEHAL
%endif

%if 0%{?suse_version}
    %define breq pkgconfig(Qt5DBus) pkgconfig(Qt5Gui) pkgconfig(Qt5Widgets) update-desktop-files
    %define qmake /usr/bin/qmake-qt5
    %define lrelease /usr/bin/lrelease-qt5
%endif

%if 0%{?suse_version} <= 1130
    %define backend hal-devel
    %define definedbackend USEHAL
%endif

%if 0%{?suse_version} == 1140 || 0%{?suse_version} == 1210
    %define backend udisks
    %define definedbackend USEUDISKS
%endif

%if 0%{?suse_version} >= 1220
    %define backend udisks2
    %define definedbackend USEUDISKS2
%endif

Name:           imagewriter
Version:        1.10.1432200249.1d253d9
Release:        0
Summary:        Utility for writing disk images to USB keys
License:        GPL-2.0-only
Group:          Hardware/Other
URL:            https://github.com/openSUSE/imagewriter
Source0:        imagewriter-%{version}.tar.xz
Patch0:         0001-remove-include-sys-sysctl.h.patch
BuildRequires:  %{backend}
BuildRequires:  %{breq}
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  xz
Requires:       xdg-utils

%description
A graphical utility for writing raw disk images & hybrid ISOs to USB keys.

%prep
%autosetup -p1

%build
# Create qmake cache file for building and use optflags.
cat > .qmake.cache <<EOF
PREFIX=%{_prefix}
QMAKE_CXXFLAGS_RELEASE += "%{optflags} -DKIOSKHACK"
DEFINES=%{definedbackend}
EOF
%qmake
make %{?_smp_mflags}

%install
make %{?_smp_mflags} INSTALL_ROOT=%{buildroot} install
%if 0%{?suse_version}
    %suse_update_desktop_file imagewriter
%endif

%if 0%{?suse_version} >= 1140
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/imagewriter
%{_datadir}/applications/imagewriter.desktop
%{_datadir}/icons/hicolor/*/apps/imagewriter.*
%if 0%{?mandriva_version}
%{_mandir}/man1/imagewriter.1.*
%else
%{_mandir}/man1/imagewriter.1%{?ext_man}
%endif

%changelog
