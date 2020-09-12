#
# spec file for package wizznic
#
# Copyright (c) 2020 SUSE LLC
# Copyright Vincent Petry <PVince81@yahoo.fr>
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


Name:           wizznic
Version:        1.1
Release:        0
Summary:        Implementation of the arcade classic Puzznic
License:        GPL-3.0-only
Group:          Amusements/Games/Board/Puzzle
URL:            http://wizznic.org/
Source0:        https://github.com/DusteDdk/Wizznic/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(sdl)

%description
Wizznic is a brick-matching puzzle-game, an improved version of Puzznic.
The challenge is to clear each level of bricks by moving the bricks next
to each other, this sounds a lot easier than it is.
The bricks are heavy, so you can only push them, not lift them up.

%prep
%setup -q -n Wizznic-%{version}

# Correct Permissions
sed -i 's|chmod -R 755|#chmod -R 755|' Makefile.linux

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" DATADIR="%{_datadir}/%{name}/" -f Makefile.linux

%install
make install DESTDIR=%{buildroot} BINDIR=%{_bindir}/ DATADIR=%{_datadir}/%{name}/ -f Makefile.linux

# install icon
install -Dm 0644 data/wmicon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%doc doc
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
%{_datadir}/man/man6/wizznic.6.gz

%changelog
