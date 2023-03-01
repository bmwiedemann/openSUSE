#
# spec file for package sonic-pi
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2021 Fabio Pesari
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


Name:           sonic-pi
Version:        4.3.0
Release:        0
Summary:        Livecoding environment for musicians and schools
License:        MIT
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            https://sonic-pi.net/
Source0:        https://github.com/sonic-pi-net/sonic-pi/archive/refs/tags/v%{version}.tar.gz
Source1:        %{name}-mix-deps.tar.gz
Source2:        sonic-pi
Source3:        sonic-pi.desktop
Source9:        sonic-pi-rpmlintrc
Patch1:         ruby32.patch
Patch2:         qscintilla-detection.patch
BuildRequires:  Catch2-devel
BuildRequires:  PlatformFolders-devel
BuildRequires:  alsa-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake
BuildRequires:  crossguid-devel
BuildRequires:  curl
BuildRequires:  zip
BuildRequires:  unzip
BuildRequires:  elixir
BuildRequires:  elixir-hex
BuildRequires:  erlang-rebar3
BuildRequires:  esbuild
BuildRequires:  fdupes
BuildRequires:  flac-devel
BuildRequires:  gcc-c++
BuildRequires:  gl3w-devel
BuildRequires:  kissfft-devel
BuildRequires:  libaubio-devel
BuildRequires:  libffi-devel
BuildRequires:  libogg-devel
BuildRequires:  libopus-devel
BuildRequires:  libqt5-linguist
BuildRequires:  libuuid-devel
BuildRequires:  libvorbis-devel
BuildRequires:  pkgconfig
BuildRequires:  reproc-devel
BuildRequires:  rtmidi-devel
BuildRequires:  ruby-devel
BuildRequires:  sndio-devel
BuildRequires:  speex-devel
BuildRequires:  sqlite3-devel
BuildRequires:  qscintilla-qt5-devel
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WebEngineCore)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  update-desktop-files
# IMGUI
# BuildRequires:  fmt-devel
# BuildRequires:  libSDL2-devel
# Not compatible with Pipewire: calls directly jack client executable
Requires:       jack-example-tools
Requires:       lua
Requires:       ruby
Requires:       supercollider
Recommends:     supercollider-sc3-plugins
BuildRequires:  libopenssl-devel

%description
Sonic Pi is a new kind of musical instrument. Instead of strumming strings or whacking things with sticks - you write code - live.

%prep
%setup -q
%autopatch -p1
sed -i s/lrelease/lrelease-qt5/g app/linux-prebuild.sh app/gui/qt/rp-build-app
tar xf %{SOURCE1} -C app/server/beam/tau
cp -af %{SOURCE3} .

%build
cd app
export MIX_DEPS_PATH=$PWD/server/beam/tau/deps
export MIX_ENV=prod
export HEX_OFFLINE=1
# export HEX_HOME=/usr/lib/elixir/lib/hex/ebin

MIX_ESBUILD_PATH=%{_bindir}/esbuild MIX_REBAR3=%{_bindir}/rebar3 ./linux-build-all.sh -s -o
./linux-release.sh

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
find app/build/linux_dist/app/server/ruby/vendor/ -type f -name '*.rb' -exec chmod -x {} \;
cd app/build
mv linux_dist sonic-pi
cp -r sonic-pi %{buildroot}%{_libdir}
install -D -m 0755 %{SOURCE2} %{buildroot}%{_bindir}
install -D -m644 ../gui/qt/images/icon-smaller.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/sonic-pi.png
install -D -m644 %{SOURCE3} %{buildroot}%{_datadir}/applications/%{name}.desktop

%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}

%check
pushd app/server/beam/tau
    MIX_ESBUILD_PATH=%{_bindir}/esbuild MIX_REBAR3=%{_bindir}/rebar3 MIX_ENV=test TAU_ENV=test mix test
popd
pushd app/server/ruby
    rake test
popd

%files
%license LICENSE.md
%doc README.md CHANGELOG.md FAQ.md CONTRIBUTING.md CONTRIBUTORS.md SYNTH_DESIGN.md
%{_bindir}/%{name}
%{_libdir}/sonic-pi
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/sonic-pi.png

%changelog
