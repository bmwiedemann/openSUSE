#
# spec file for package xwallpaper
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2022 Tomasz Hołubowicz <alternateved@pm.me>
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


Name:           xwallpaper
Version:        0.7.4
Release:        0
Summary:        Wallpaper setting utility for X
License:        ISC
Group:          System/X11/Utilities
URL:            https://github.com/stoeckmann/xwallpaper
Source:         https://github.com/stoeckmann/xwallpaper/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:  libpixman-1-0-devel
BuildRequires:  pkgconfig
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(xpm)

%description
The xwallpaper utility allows you to set image files as your X wallpaper. JPEG, PNG, and XPM file formats are supported, all of them being configurable and therefore no fixed dependencies.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/X11/Utilities
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh shell completion for %{name}

%prep
%setup -q

%build
%configure \
        --with-seccomp \
        --with-randr \
        --with-jpeg \
        --with-png \
        --with-xpm

%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/xwallpaper
%{_mandir}/man1/xwallpaper.1%{?ext_man}

%files zsh-completion
%{_datadir}/zsh
%{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_xwallpaper

%changelog
