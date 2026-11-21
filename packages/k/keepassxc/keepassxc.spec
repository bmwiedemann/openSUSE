#
# spec file for package keepassxc
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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



%if 0%{?suse_version}
%bcond_without keepassxc_cr_recovery
%else
%bcond_with    keepassxc_cr_recovery
%endif

Name:           keepassxc
Version:        2.8.0
Release:        0
Summary:        Qt6-based Password Manager
License:        GPL-2.0-only OR GPL-3.0-only
Group:          Productivity/Security
URL:            https://keepassxc.org/
Source0:        https://github.com/keepassxreboot/keepassxc/releases/download/%{version}/keepassxc-%{version}-src.tar.xz
Source1:        https://github.com/keepassxreboot/keepassxc/releases/download/%{version}/keepassxc-%{version}-src.tar.xz.sig
Source2:        https://keepassxc.org/keepassxc_master_signing_key.asc#/%{name}.keyring
Source3:        vendor.tar.zst
Source98:       debian.tar.xz
Source99:       keepassxc.dsc
BuildRequires:  cmake >= 3.16
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  readline-devel
BuildRequires:  cmake(Qt6Concurrent) >= 6.2.4
BuildRequires:  cmake(Qt6Core) >= 6.2.4
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(libkeyutils)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib) >= 1.2.0
%if 0%{?suse_version}
BuildRequires:  rubygem(%{rb_default_ruby_abi}:asciidoctor)
%else
BuildRequires:  rubygem(asciidoctor)
%endif
# C++20 is required
%if 0%{?suse_version} && 0%{?suse_version} < 1600
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif
%if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(botan-3)
%else
BuildRequires:  pkgconfig(botan-2) >= 2.19.1
%endif
%if %{with keepassxc_cr_recovery}
BuildRequires:  golang(API) >= 1.25
BuildRequires:  golang-packaging
BuildRequires:  zstd
%endif
Requires:       hicolor-icon-theme
# Wayland Auto-Type and Quick Unlock go through D-Bus portals and polkit
Recommends:     polkit
Recommends:     xdg-desktop-portal
%if 0%{?suse_version}
Recommends:     %{name}-lang
%endif
# boo#1148406. Last version in factory 2.0.3-2.7
Provides:       keepassx = 2.0.4
Obsoletes:      keepassx < 2.0.4

%description
KeePassXC is a cross-platform community fork of KeePassX, a password manager
that stores credentials in an encrypted database locked with a master
password, key file or hardware key. It supports browser integration, passkeys,
SSH agent, the Secret Service API, TOTP, and Auto-Type on both X11 and
Wayland.

%if 0%{?suse_version}
%lang_package
%endif

%prep
%autosetup -p1

%if %{with keepassxc_cr_recovery}
tar -C utils/keepassxc-cr-recovery -xf %{SOURCE3}
%endif

%build
%if %{with keepassxc_cr_recovery}
# build before %%cmake, which changes into the build directory on SUSE
pushd utils/keepassxc-cr-recovery
go build -buildmode=pie -mod=vendor
popd
%endif

%if 0%{?suse_version} && 0%{?suse_version} < 1600
export CC=gcc-13
export CXX=g++-13
%endif
%cmake \
  -DKEEPASSXC_BUILD_TYPE=Release \
  -DKPXC_FEATURE_UPDATES=OFF
%cmake_build

%install
%cmake_install

%if %{with keepassxc_cr_recovery}
install -D -m 0755 utils/keepassxc-cr-recovery/keepassxc-cr-recovery %{buildroot}%{_bindir}/keepassxc-cr-recovery
%endif

%fdupes %{buildroot}%{_prefix}

%check
# gh#keepassxreboot/keepassxc#667
export LANG=en_US.UTF-8
export QT_QPA_PLATFORM=offscreen
%ctest --exclude-regex 'test(cli|gui)'

%files
%license COPYING LICENSE*
%doc CHANGELOG.md README.md
%if %{with keepassxc_cr_recovery}
%{_bindir}/keepassxc-cr-recovery
%endif
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_bindir}/%{name}-proxy
%{_datadir}/%{name}/
%if 0%{?suse_version}
%exclude %{_datadir}/%{name}/translations
%endif
%{_datadir}/applications/org.keepassxc.KeePassXC.desktop
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.keepassxc.KeePassXC.appdata.xml
%{_datadir}/icons/hicolor/*/*/*%{name}*
%{_datadir}/mime/packages/%{name}.xml
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/org.keepassxc.KeePassXC.policy
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-cli.1*

%if 0%{?suse_version}
%files lang
%{_datadir}/%{name}/translations
%endif

%changelog
