#
# spec file for package blobAndConquer
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           blobAndConquer
Version:        1.11
Release:        0
Summary:        Blob Wars: Blob and Conquer - a 3rd person action game
License:        GPL-2.0+
Group:          Amusements/Games/3D/Shoot
Url:            http://sourceforge.net/projects/blobandconquer/
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-icons.tar
# PATCH-FIX-UPSTREAM for gcc 4.7
Patch0:         blobandconquer-gcc47.patch
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(SDL_ttf)
BuildRequires:  pkgconfig(sdl)

%description
With the apparent defeat of Galdov and the reclaiming of the Fire,
Time, Space and Reality Crystals the Blobs' battle was only just
beginning. Bob had rescued many Blobs and fought many battles,
but now he had an ever bigger task ahead of him. The Blobs'
homeworld is still littered with the alien forces and Bob once
again makes it his task to lead the counter attack. But even
without Galdov the aliens are still extremely well organised...

They're Ready. Will You Be?

%prep
%setup -q -a 1
%patch0
mv makefile Makefile

# Fix paths, add -lX11, remove docs install via files,
# remove png and install from tar
sed -i \
       -e 's|$(PREFIX)/games/|$(PREFIX)/bin/|' \
       -e 's|share/games/blobAndConquer|share/blobAndConquer|' \
       -e 's|-lz|-lz -lX11|' \
       -e 's|cp -pr $(DOCS)|#cp -pr $(DOCS)|' \
       -e 's|cp -p $(ICONS)$(PROG).png|#cp -p $(ICONS)$(PROG).png|' Makefile

# Fix Desktop
sed -i 's|0.7|1.0|; s|ArcadeGame;|ActionGame;ArcadeGame;|' \
         icons/blobAndConquer.desktop

%build
make %{?_smp_mflags} RELEASE=1

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/{applications,pixmaps}

# install icons
for i in 16 32 48 64 ; do
    install -Dm 0644 icons/%{name}-${i}.png \
            %{buildroot}/%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

%find_lang %{name}

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc doc
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}

%changelog
