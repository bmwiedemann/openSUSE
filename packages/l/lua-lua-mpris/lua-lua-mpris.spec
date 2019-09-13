#
# spec file for package lua-lua-mpris
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define flavor @BUILD_FLAVOR@
%define mod_name lua-mpris
%define mpv_lua_flavor lua51
Version:        0.0+git20190614.e4567e2
Release:        0
Summary:        MPRIS api for lua
License:        MIT
Group:          Development/Libraries/Other
Url:            https://github.com/antlarr/lua-mpris/
Source:         lua-mpris-%{version}.tar.xz
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-lua-dbus
BuildRequires:  pkgconfig(dbus-1)
Requires:       %{flavor}
Requires:       %{flavor}-lua-dbus
%if "%{flavor}" == "lua51"
Provides:       lua-%{mod_name} = %{version}
Obsoletes:      lua-%{mod_name} < %{version}
%endif
%if "%{flavor}" == ""
Name:           lua-%{mod_name}
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif

%description
MPRIS api for lua

%package -n mpv-plugin-mpris
Summary:        MPV plugin to add MPRIS support
Group:          Productivity/Multimedia/Video/Players
Requires:       %{mpv_lua_flavor}-lua-mpris
Requires:       mpv
Requires(post): mpv
Supplements:    mpv

%description -n mpv-plugin-mpris
mpv is a movie player based on MPlayer and mplayer2. It supports a wide variety
of video file formats, audio and video codecs, and subtitle types.

This package installs a lua plugin for mpv to add mpris support through a
dbus interface.

%prep
%setup -q -n lua-mpris-%{version}

%build

%install
mkdir -p %{buildroot}%{lua_noarchdir}/lua-mpris
cp -Ra applet.lua client.lua init.lua %{buildroot}%{lua_noarchdir}/lua-mpris/
%if "%{flavor}" == "lua51"
mkdir -p %{buildroot}%{_datadir}/mpv-plugin-mpris
cp mpv.lua %{buildroot}%{_datadir}/mpv-plugin-mpris/
%endif

%post -n mpv-plugin-mpris
if [ "$1" = 1 ] ; then
    mkdir -p %{_sysconfdir}/mpv/scripts/
    ln -s %{_datadir}/mpv-plugin-mpris/mpv.lua %{_sysconfdir}/mpv/scripts/mpris.lua
fi

%files
%license LICENSE
%{lua_noarchdir}/lua-mpris

# Only produce during one flavor to avoid duplicate binary.
%if "%{flavor}" == "lua51"
%files -n mpv-plugin-mpris
%defattr(-,root,root)
%license LICENSE
%{_datadir}/mpv-plugin-mpris
%ghost %config %{_sysconfdir}/mpv/scripts/mpris.lua
%ghost %dir %{_sysconfdir}/mpv/scripts
%endif

%changelog
