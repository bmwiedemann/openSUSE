#
# spec file for package myman
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


%define realver 2009-10-30

Name:           myman
Version:        0.7.0+cvs20091030
Release:        0
Summary:        Text based Pacman clone
License:        MIT
Group:          Amusements/Games/Action/Arcade
URL:            http://myman.sourceforge.net/
Source:         http://downloads.sourceforge.net/myman/myman-cvs/%{name}-cvs-%{realver}/%{name}-wip-%{realver}.tar.gz
BuildRequires:  groff-full
BuildRequires:  pkgconfig(ncursesw)

%description
MyMan is a video game for color and monochrome text
terminals in the genre of Namco's Pac-Man.
It includes many maze variations and several tile
and sprite sets, ranging from large ASCII art through
large pseudo-bitmap Unicode or CP437 graphics to
single characters.

%prep
%setup -q -n %{name}-wip-%{realver}

%build
echo %{version} > VERSION
export date=$(date -u -r ChangeLog -I) # for boo#1047218
%configure \
  --with-ncursesw
export CFLAGS="%{optflags}"
export NCURSESWLIBS=$(pkg-config --libs ncursesw)
export NCURSESWCFLAGS=$(pkg-config --cflags ncursesw)
make %{?_smp_mflags}

%install
%make_install
mv -f %{buildroot}%{_mandir}/man6/%{name}-%{version}* %{buildroot}%{_mandir}/man6/%{name}.6
# remove uneeded files
rm -rf %{buildroot}%{_datadir}/doc/%{name}-%{version}
rm -f %{buildroot}%{_bindir}/%{name}-%{version}
rm -f %{buildroot}%{_bindir}/%{name}.command
rm -f %{buildroot}%{_mandir}/man6/%{name}.command.6*

%files
%doc AUTHORS ChangeLog NEWS README THANKS
%license LICENSE COPYRIGHT
%{_bindir}/%{name}
%{_datadir}/%{name}-%{version}
%{_mandir}/man6/%{name}.6%{?ext_man}

%changelog
