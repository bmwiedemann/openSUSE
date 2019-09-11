#
# spec file for package openarena
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


# The binaries filenames postfix defining:
%ifarch %ix86
%define postfix i386
%else
%ifarch armv6l armv6hl
%define postfix armv6l
%else
%ifarch armv7l armv7hl
%define postfix armv7l
%else
%define postfix %{_target_cpu}
%endif
%endif
%endif
Name:           openarena
Version:        0.8.8
Release:        0
Summary:        Open Arena game engine
License:        GPL-2.0+
Group:          Amusements/Games/Action/Shoot
Url:            http://openarena.ws/
Source0:        http://files.poulsander.com/~poul19/public_files/oa/dev088/%{name}-engine-source-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.svg
Source99:       %{name}.changes
# PATCH-FIX-UPSTREAM to prevent stack.
Patch0:         openarena-0.8.8-stack.patch
# PATCH-FIX-UPSTREAM fix build with newer gcc
Patch1:         fix-compile-gcc5.patch
Patch2:         q_platform_aarch64_support.diff
BuildRequires:  Mesa-devel
BuildRequires:  SDL-devel
BuildRequires:  autoconf >= 2.60
BuildRequires:  libvorbis-devel
BuildRequires:  openal-soft-devel
BuildRequires:  update-desktop-files
Requires:       openarena-data = %{version}
Recommends:     openarena-doc = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
OpenArena is an open-source content package for Quake III Arena
licensed under the GPL, effectively creating a free stand-alone game.

%prep
%setup -q -n %{name}-engine-source-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p0
# FIX usage of __DATE__
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE99}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
sed -i "s/__DATE__/$DATE/g" code/qcommon/common.c code/sys/sys_main.c

%build
# START of configuration of building ----------------
export CFLAGS="%{optflags}" # C flags for compiler
export USE_OPENAL=1            # We want openAL
export USE_OPENAL_DLOPEN=1     # Next we want to bind openAL on runtime.
                               # SDL sound will be used if openAL is not installed
export USE_CODEC_VORBIS=1      # We want vorbis support
export BUILD_STANDALONE=1      # Open Arena is a standalone game
export DEFAULT_BASEDIR=%{_datadir}/games/openarena  # Where is directory with openarena-data
# END of configuration of building -----------------------------
make %{?_smp_mflags} V=1

%install
make copyfiles COPYDIR=%{buildroot}/%{_libexecdir}/%{name}  # Where will come compiled engine files
mkdir -p %{buildroot}/%{_bindir}
install -dm755 %{buildroot}/%{_libexecdir}/%{name}
install -m 755 build/release-linux*/o*%{postfix} %{buildroot}/%{_libexecdir}/%{name}
ln -sf %{_libexecdir}/%{name}/openarena.%{postfix} %{buildroot}%{_bindir}/%{name}
ln -sf %{_libexecdir}/%{name}/oa_ded.%{postfix} %{buildroot}%{_bindir}/%{name}-ded
# Icon, it is simple official icon
install -D -m 644 %{SOURCE2} %{buildroot}/%{_datadir}/pixmaps/%{name}.svg
# Desktop entry
install -D -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file %{name}

%files
%defattr(-,root,root)
%{_libexecdir}/%{name}
%{_bindir}/openarena*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg

%changelog
