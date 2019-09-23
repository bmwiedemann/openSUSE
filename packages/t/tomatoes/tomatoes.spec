#
# spec file for package tomatoes
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


Name:           tomatoes
Version:        1.55
Release:        0
Summary:        How many tomatoes can you smash in ten short minutes?
License:        Zlib
Group:          Amusements/Games/Action/Arcade
Url:            http://tomatoes.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/1.5/%{name}-linux-src-%{version}.tar.bz2
Source1:        http://downloads.sourceforge.net/%{name}/1.5/%{name}-linux-1.5.tar.bz2
Source2:        %{name}-rpmlintrc
Source3:        %{name}.desktop
Patch0:         reproducible.patch
BuildRequires:  Mesa-devel
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(sdl)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version}
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
%if 0%{?fedora_version}
BuildRequires:  desktop-file-utils
%endif

%description
I Have No Tomatoes is an extreme leisure time activity idea of which
culminates in the following question: How many tomatoes can you smash
in ten short minutes? If you have the time to spare, this game has the
vegetables just waiting to beeliminated!

%prep
%setup -q -a1
%patch0 -p1

cp -r tomatoes-1.5/* .

# SED-FIX-OPENSUSE -- Fix Flags
sed -i -e 's|-O3 -march=$(MARCH) -Wall||;
           s|-lGLU -s|-lGLU -lm|;
           s|-I./include|-I./include $(SDL_FLAGS)|;
           s|$(OBJS) $(LDFLAGS)|$(OBJS) $(LDFLAGS) $(LDLIBS)|;
           s|$(CC) $(CFLAGS)|$(CXX) $(CXXFLAGS)|' makefile

# SED-FIX-OPENSUSE -- Fix place config.dir
sed -i -e 's|string tmp = get_tomatoes_dir()|static string tmp = get_tomatoes_dir()|' src/config.cpp

# SED-FIX-OPENSUSE -- Fix hiscore
sed -i -e 's|string tmp;|static string tmp;|' src/hiscore.cpp

# Some docs have the DOS line ends
dos2unix README

%build
CXXFLAGS="%{optflags}" make  %{?_smp_mflags} \
        MPKDIR="%{_datadir}/%{name}/" \
        MUSICDIR="%{_datadir}/%{name}/music/" \
        CONFIGDIR="%{_sysconfdir}/%{name}/"

%install
# install executable
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}

# install files
mkdir -p %{buildroot}%{_datadir}/%{name}/music
install -Dm 0644 tomatoes.mpk %{buildroot}%{_datadir}/%{name}/
install -Dm 0644 music/* %{buildroot}%{_datadir}/%{name}/music/
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
install -Dm 0644 config.cfg %{buildroot}%{_sysconfdir}/%{name}/

# install icon
install -Dm 0644 icon.png %{buildroot}/%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

# install Desktop file
install -Dm 0644 %{S:3} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
        %suse_update_desktop_file %{name}
%endif
%if 0%{?fedora_version}
        desktop-file-validate '%{buildroot}/%{_datadir}/applications/%{name}.desktop'
%endif

%files
%defattr(-, root, root,-)
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}

%changelog
