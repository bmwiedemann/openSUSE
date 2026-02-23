#
# spec file for package nekobox
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           nekobox
Version: 5.10.19
Release:        0%{?autorelease}
Summary:        Qt based cross-platform GUI proxy configuration manager (backend: sing-box)
License:        GPL-3.0-only
URL:            https://github.com/qr243vbi/nekobox
Source0: https://github.com/qr243vbi/nekobox/releases/download/%{version}/nekobox-unified-source-%{version}.tar.xz
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  golang >= 1.24
BuildRequires:  pkgconfig
BuildRequires:  sed
BuildRequires:  thrift
BuildRequires:  (libboost-devel or boost-devel)
BuildRequires:  (libthrift-devel or thrift-devel)
BuildRequires:  (ninja or ninja-build)
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Linguist)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  ccache
BuildRequires:  gcc-c++
Provides:       nekoray
Conflicts:      nekoray

Requires:       nekobox-core
%if 0%{?suse_version}
Requires:       google-noto-coloremoji-fonts
Requires:       google-noto-sans-fonts
%endif


%define core nekobox_core

%package -n nekobox-core
Summary:        %{summary}
Provides:  sing-box
Conflicts: sing-box

%description
%{summary}.

%description -n nekobox-core
%{summary}.

%prep
%autosetup -p1 -n nekobox-unified-source-%{version}

%{?!%__builddir:%define __builddir %__cmake_builddir}
%{?!%__cmake_builddir:%define __cmake_builddir build}

%build

(
DEST=$PWD/build
SKIP_UPDATER=y
GOFLAGS='-mod=vendor %{?gobuildflags}'
VERSION_SINGBOX="$(cat SingBox.Version)"
. script/build_go.sh
)

%if %{undefined optflags}
%define optflags -O2 -g -m64 -fmessage-length=0 -D_FORTIFY_SOURCE=2 -fstack-protector -funwind-tables -fasynchronous-unwind-tables
%endif

(
%cmake -GNinja "-DSKIP_UPDATE_BUTTON=ON" "-DNKR_DEFAULT_VERSION=%{version}"
)
ninja -C "$(realpath %__builddir)" -v -j %{_smp_build_ncpus}


%install
install -Dm755 $PWD/build/%{core} %{buildroot}%{_libexecdir}/%{name}/%{core}
DESTDIR="%{buildroot}" ninja -C "$(realpath %__builddir)" -v  install
chrpath -d                  %{buildroot}%{_libexecdir}/%{name}/%{name}

%files
%attr(0755, -, -) %{_bindir}/%{name}
%attr(0755, -, -) %{_libexecdir}/%{name}/%{name}
%dir %{_libexecdir}/%{name}/public
%attr(0644, -, -) %{_libexecdir}/%{name}/public/*.*
%attr(0644, -, -) %{_datadir}/icons/hicolor/256x256/apps/nekobox.png
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/256x256
%dir %{_datadir}/icons/hicolor/256x256/apps
%attr(0644, -, -) %{_datadir}/applications/%{name}.desktop
%license LICENSE

%files -n nekobox-core
%attr(0755, -, -) %{_bindir}/sing-box
%dir %{_libexecdir}/%{name}
%attr(0755, -, -) %{_libexecdir}/%{name}/%{core}

%changelog

