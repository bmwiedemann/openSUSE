#
# spec file for package chromium-bsu
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


Name:           chromium-bsu
Version:        0.9.16.1
Release:        0
Summary:        Vertical Scrolling Space Shooter Game
License:        ClArtistic AND MIT
Group:          Amusements/Games/Action/Shoot
Url:            http://sourceforge.net/projects/chromium-bsu/
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# hiscore patch
Patch0:         %{name}-0.9.15.1-src_HiScore.cpp.patch
BuildRequires:  dejavu-fonts
BuildRequires:  gcc-c++
BuildRequires:  libGLC-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(freealut)
BuildRequires:  pkgconfig(sdl2)
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif

%description
Chromium B.S.U. is a fast paced, arcade-style, top-scrolling space shooter.

You are captain of the cargo ship Chromium B.S.U., responsible for
delivering supplies to our troops on the front line. Your ship has
a small fleet of robotic fighters which you control from the relative
safety of the Chromium vessel.

%prep
%setup -q
%patch0

%build
%configure --docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}/%{name}-%{version}/data/doc/Makefile*
rm -f %{buildroot}/%{name}-%{version}/data/doc/images/Makefile*

mkdir -p %{buildroot}%{_localstatedir}/games/
touch %{buildroot}%{_localstatedir}/games/%{name}.highscore

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS NEWS README
%license COPYING data/wav/license.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_docdir}/%{name}
%dir %{_localstatedir}/games/
%config(noreplace) %attr(664,games,games) %{_localstatedir}/games/%{name}.highscore

%changelog
