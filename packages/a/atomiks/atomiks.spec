#
# spec file for package atomiks
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Mateusz Viste
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


Name:           atomiks
Version:        1.0.4.1
Release:        0
Summary:        A faithful remake of, and a tribute to, Atomix, a classic puzzle game
License:        GPL-3.0+
Group:          Amusements/Games/Logic
Url:            http://atomiks.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
BuildRequires:  dos2unix
BuildRequires:  libmikmod-devel
BuildRequires:  libpng-devel
BuildRequires:  upx
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(sdl2)

%description
Atomiks is a faithful remake of, and a tribute to, Atomix, a classic puzzle game
created by Softtouch & RoSt and published in 1990 by the Thalion Software company.
Atomiks is free software, and shares no code with the original Atomix game.

%prep
%setup -q

# SED-FIX-OPENSUSE -- add editor
sed -i -e 's|all: atomiks|all: atomiks editor|' Makefile

# Some docs have the DOS line ends
dos2unix *.txt

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
# install executable
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm 0755 editor %{buildroot}%{_bindir}/%{name}-editor

# install icon
install -Dm 0644 %{name}.png %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%doc *.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-editor
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/

%changelog
