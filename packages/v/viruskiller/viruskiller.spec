#
# spec file for package viruskiller
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           viruskiller
Version:        1.03
Release:        0
Summary:        Arcade shoot 'em up game about virus invasion
License:        GPL-2.0+
Group:          Amusements/Games/3D/Shoot
Url:            https://web.archive.org/web/20110809092730/http://www.parallelrealities.co.uk/projects/virusKiller.php
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-icons.tar
# PATCH-FIX-OPENSUSE - viruskiller-icons_viruskiller.desktop.patch -- Change to right Desktop Entries
Patch0:         viruskiller-icons_viruskiller.desktop.patch
# PATCH-FIX-OPENSUSE bmwiedemann -- sort list of files in pak (boo#1041090)
Patch1:         reproducible.patch
%if 0%{?suse_version}
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(SDL_net)
BuildRequires:  pkgconfig(SDL_ttf)
BuildRequires:  pkgconfig(sdl)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Your computer has been invaded! Dozens of little viruses are pouring
in via security holes in Microsoft Internet Explorer, Microsoft Outlook,
Microsoft MSN Messenger and Microsoft Recycle Bin!! Using your trusty
mouse you must shoot the buggers before they can destroy your files!
Some will steal them from their home directories and take them back
to their security hole. Others will just eat them right there on
the spot! See how long you and your computer can survive the onslaught!

%prep
%setup -q -a 1
%patch0
%patch1 -p1

# SED-FIX-OPENSUSE -- Use normal pak, fix paths, , remove docs install via files,
# remove png and install from tar
sed -i -e 's|USEPAK ?= 0|USEPAK ?= 1|;
           s|$(PREFIX)/games|$(PREFIX)/bin|;
           s|$(PREFIX)/share/games|$(PREFIX)/share|;
           s|$(PREFIX)/share/doc|$(PREFIX)/share/doc/packages/|;
           s|$(PREFIX)/share/icons|$(PREFIX)/share/icons|;
           s|$(LIBS) $(OBJS)|$(OBJS) $(LIBS)|;
           s|$(LIBS) $(PAKOBJS)|$(PAKOBJS) $(LIBS)|;
           s|-lSDL_net|-lSDL_net -lz|;
           s|-o root -g games||' makefile

# SED-FIX-OPENSUSE -- Fix pak
sed -i -e 's|gzclose(pak)|gzclose((gzFile)pak)|;
           s|gzclose(fp)|gzclose((gzFile)fp)|' src/pak.cpp

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install

# install icons
for i in 16 22 32 48 64 ; do
    install -Dm 0644 icons/%{name}_${i}x${i}.png \
            %{buildroot}/%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
%endif

%files
%defattr(-,root,root,-)
%doc doc/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/%{name}

%changelog
