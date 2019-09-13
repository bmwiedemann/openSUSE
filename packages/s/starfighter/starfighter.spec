#
# spec file for package starfighter
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


Name:           starfighter
Version:        1.7
Release:        0
Summary:        Liberate the universe from the evil company WEAPCO
License:        GPL-3.0+
Group:          Amusements/Games/Action/Arcade
Url:            http://starfighter.nongnu.org/
Source0:        http://download.savannah.gnu.org/releases/%{name}/%{version}/%{name}-%{version}-src.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-icons.tar
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(sdl)
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif

%description
Project: Starfighter is an old school 2D shoot 'em up. In the game you take on
the role of a rebel pilot called Chris, who is attempting to overthrow a
military corporation called Weapco. Weapco has seized control of the known
universe and currently rules it with an iron fist. Chris can no longer stand
back and watch as millions of people suffer and die. He steals an experimental
craft known as "Firefly" and begins his mission to fight his way to Sol,
freeing key systems along the way. The game opens with Chris attempting to
escape a Weapco patrol that has intercepted him.

%prep
%setup -q -a 1 -n %{name}-%{version}-src

# Some docs have the DOS line ends
dos2unix README.txt

%build
%configure
make %{?_smp_mflags}

%install
%make_install

# install icons
for i in 16 32 48 64 72 96 128 ; do
    install -Dm 0644 icons/%{name}_${i}x${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

# remove duplicate docs
rm -fr %{buildroot}%{_datadir}/doc/%{name}

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%doc docs/* COPYING LICENSES README.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
