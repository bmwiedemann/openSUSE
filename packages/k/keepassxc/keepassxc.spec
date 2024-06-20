#
# spec file for package keepassxc
#
# Copyright (c) 2022 SUSE LLC
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


%if 0%{?suse_version} || 0%{?fedora_version} >= 33
%bcond_without cmake_macros
%else
%bcond_with    cmake_macros
%endif

%if 0%{?suse_version}
%bcond_without keepassxc_cr_recovery
%else
%bcond_with    keepassxc_cr_recovery
%endif

Name:           keepassxc
Version:        2.7.9
Release:        0
Summary:        Qt5-based Password Manager
License:        GPL-2.0-only OR GPL-3.0-only
Group:          Productivity/Security
URL:            https://www.keepassxc.org/
Source0:        https://github.com/keepassxreboot/keepassxc/releases/download/%{version}/keepassxc-%{version}-src.tar.xz
Source1:        https://github.com/keepassxreboot/keepassxc/releases/download/%{version}/keepassxc-%{version}-src.tar.xz.sig
Source2:        https://keepassxc.org/keepassxc_master_signing_key.asc#/%{name}.keyring
Source3:        vendor.tar.zst
#Source96:       _service
#Source97:       _constraints
Source98:       debian.tar.xz
Source99:       keepassxc.dsc
BuildRequires:  cmake >= 3.1.0
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
%if 0%{?suse_version}
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig(minizip)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:asciidoctor)
%else
BuildRequires:  minizip-compat-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  rubygem(asciidoctor)
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(botan-2) >= 2.11.0
BuildRequires:  pkgconfig(libargon2)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib) >= 1.2.0
BuildRequires:  readline-devel

%if %{with keepassxc_cr_recovery}
BuildRequires:  golang(API)
BuildRequires:  golang-packaging
BuildRequires:  zstd
%endif

%if 0%{?suse_version}
BuildRequires:  update-desktop-files
Requires(post): update-desktop-files
Requires(postun): update-desktop-files
%endif
Requires:       hicolor-icon-theme
Requires(post): hicolor-icon-theme
Requires(post): shared-mime-info
Requires(postun): hicolor-icon-theme
Requires(postun): shared-mime-info
Recommends:     %{name}-lang
# boo#1148406. Last version in factory 2.0.3-2.7
Provides:       keepassx = 2.0.4
Obsoletes:      keepassx < 2.0.4


%description
A password manager or safe which manages your passwords. Databases
are locked with a master key/password or a key disk. The databases
are encrypted using AES and Twofish.

%if 0%{?suse_version}
%lang_package
%endif

%prep
%autosetup -p1

%if %{with keepassxc_cr_recovery}
pushd utils/keepassxc-cr-recovery
tar xf %{SOURCE3}
popd
%endif

%build
%cmake \
  -DKEEPASSXC_BUILD_TYPE="Release" \
  -DWITH_XC_UPDATECHECK=OFF        \
  -DWITH_XC_ALL=ON

%if %{with cmake_macros}
%cmake_build
%else
%make_build
%endif

%if %{with keepassxc_cr_recovery}
pushd ../utils/keepassxc-cr-recovery
go build -buildmode=pie -mod=vendor
popd
%endif

%install
%if %{with cmake_macros}
%cmake_install
%else
%make_install
%endif

%if %{with keepassxc_cr_recovery}
install -D -m 0755 utils/keepassxc-cr-recovery/keepassxc-cr-recovery %{buildroot}%{_bindir}/keepassxc-cr-recovery
%endif

for i in $(find %{buildroot} -type f -name \*.svgz) ; do
  j="${i%z}"
  gunzip < $i > $j
done
%if 0%{?suse_version}
%fdupes -s %{buildroot}/%{_prefix}

%check
# gh#keepassxreboot/keepassxc#667
export LANG=en_US.UTF-8
%ctest -- -E 'test(cli|gui)'
%endif

%if 0%{?suse_version}
# on newer distros it is handled via file trigger
%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif
%else
%post
touch --no-create %{_datadir}/icons/hicolor >/dev/null 2>/dev/null || :

%postun
update-desktop-database >/dev/null 2>/dev/null || :
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor >/dev/null 2>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor >/dev/null 2>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor >/dev/null 2>/dev/null || :
%endif

%files
%license COPYING LICENSE*
%doc CHANGELOG.md README.md
%doc docs/*
%if %{with keepassxc_cr_recovery}
%{_bindir}/keepassxc-cr-recovery
%endif
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_bindir}/%{name}-proxy
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/docs/
%{_datadir}/%{name}/icons/
%{_datadir}/%{name}/wordlists/
%{_datadir}/applications/org.keepassxc.KeePassXC.desktop
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.keepassxc.KeePassXC.appdata.xml
%{_datadir}/icons/hicolor/*/*/*%{name}*
%{_datadir}/mime/packages/%{name}.xml
%dir %{_libdir}/%{name}
%{_libdir}/keepassxc/libkeepassxc-autotype-xcb.so
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-cli.1*

%if 0%{?suse_version}
%files lang
%endif
%{_datadir}/%{name}/translations

%changelog
