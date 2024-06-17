#
# spec file for package ddnet
#
# Copyright (c) 2024 SUSE LLC
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


Name:           ddnet
Version:        18.3
Release:        0
Summary:        DDraceNetwork, a cooperative racing mod of Teeworlds
License:        Apache-2.0 AND CC-BY-SA-3.0 AND Zlib AND MIT AND SUSE-Public-Domain
Group:          Amusements/Games/Action/Race
URL:            https://ddnet.org/
Source0:        https://github.com/ddnet/ddnet/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  appstream-glib
BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  glslang-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libminiupnpc-devel
BuildRequires:  pkgconfig
BuildRequires:  pnglite-devel
BuildRequires:  python3
BuildRequires:  rust
BuildRequires:  rust-std
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-data = %{version}-%{release}
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
BuildRequires:  gcc11
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc-c++
%endif

%description
DDraceNetwork (DDNet) is an actively maintained version of DDRace,
a Teeworlds modification with a unique cooperative gameplay.
Help each other play through custom maps with up to 64 players,
compete against the best in international tournaments, design your
own maps, or run your own server.

%package        data
Summary:        Data files for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    data
Data files for DDraceNetwork (DDNet).

%package        server
Summary:        Standalone server for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    server
Standalone server for DDraceNetwork (DDNet).

%prep
%setup -qa1

mkdir cargo-home
cat >cargo-home/config <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source."https://github.com/selaux/android-ndk-rs"]
git = "https://github.com/selaux/android-ndk-rs"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = './vendor'
EOF

%build
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
export CC="gcc-11"
export CXX="g++-11"
%endif
export CARGO_HOME=`pwd`/cargo-home/
mkdir -p build && cd build
# NOTE that %%cmake macro breaks linking.
cmake .. \
    -DCMAKE_BUILD_TYPE=Release  \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DPREFER_BUNDLED_LIBS=OFF \
    -DAUTOUPDATE=OFF \
    -DANTIBOT=ON \
    -DUPNP=ON \
    -DSTEAM=OFF \
    -DVIDEORECORDER=OFF

# Fix for "error: failed to run custom build command for `link-cplusplus v1.0.6` - error occurred: Failed to find tool. Is `c++` installed?"
%make_build \
     OPTFLAGS="%{optflags} -std=gnu++17"

%install
export CARGO_HOME=`pwd`/cargo-home/
%cmake_install
install -Dp -m 0644 man/DDNet.6 %{buildroot}%{_mandir}/man6/DDNet.6
install -Dp -m 0644 man/DDNet-Server.6 %{buildroot}%{_mandir}/man6/DDNet-Server.6

%fdupes %{buildroot}%{_datadir}

%files
%license license.txt
%doc README.md
%{_mandir}/man6/DDNet.6%{?ext_man}
%{_bindir}/DDNet
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files data
%{_datadir}/%{name}/

%files server
%{_mandir}/man6/DDNet-Server.6%{?ext_man}
%{_bindir}/DDNet-Server
%{_datadir}/icons/hicolor/*/apps/%{name}-server.png

%changelog
