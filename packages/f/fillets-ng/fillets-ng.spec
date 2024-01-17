#
# spec file for package fillets-ng
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


Name:           fillets-ng
Version:        1.0.1
Release:        0
Summary:        Fish Fillets - Next Generation
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
Url:            http://fillets.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/fillets/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         %{name}-0.9.3-datadir.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  fribidi-devel
BuildRequires:  gcc-c++
BuildRequires:  lua51-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
Requires:       %{name}-data = %{version}

%description
Fish Fillets is strictly a puzzle game. The goal in each of the 70
levels is always the same: find a safe way out. The fish utter witty
remarks about their surroundings and the various inhabitants of their
underwater realm quarrel among themselves or comment on the efforts of
your fish. The whole game is accompanied by quiet, comforting music.

%prep
%setup -q
%patch0

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
install -D -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%suse_update_desktop_file -i %{name}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%doc %{_mandir}/man6/*
%{_bindir}/fillets
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
