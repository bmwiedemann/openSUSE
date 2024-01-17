#
# spec file for package libsixel
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


%define _sover 1
Name:           libsixel
Version:        1.10.3
Release:        0
Summary:        SIXEL encoder/decoder
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/libsixel/libsixel
Source:         https://github.com/libsixel/libsixel/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         meson.patch
Patch1:         static-libs.patch
BuildRequires:  bash
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)

%description
A C encoder/decoder implementation for DEC SIXEL graphics.

%package -n libsixel%{_sover}
Summary:        SIXEL encoder/decoder
Group:          System/Libraries

%description -n libsixel%{_sover}
A C encoder/decoder implementation for DEC SIXEL graphics.

%package utils
Summary:        Utilities for the SIXEL encoder/decoder %{name}
Group:          Development/Libraries/C and C++
Requires:       libsixel%{_sover} = %{version}

%description utils
img2sixel and sixel2png utilities for libsixel, a C encoder/decoder implementation for DEC SIXEL graphics.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libsixel%{_sover} = %{version}

%description devel
Development files for %{name}, a C encoder/decoder implementation for DEC SIXEL graphics.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name}-utils = %{version}
Requires:       bash-completion
Supplements:    (%{name}-utils and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/Shells
Requires:       %{name}-utils = %{version}
Supplements:    (%{name}-utils and zsh)
BuildArch:      noarch

%description zsh-completion
ZSH command line completion support for %{name}.

%prep
%autosetup -v -p1

%build
%meson \
  -Dgdk-pixbuf2=enabled \
  -Dlibcurl=enabled \
  -Dtests=enabled \
%{nil}
%meson_build

%install
%meson_install

%post -n libsixel%{_sover} -p /sbin/ldconfig
%postun -n libsixel%{_sover} -p /sbin/ldconfig

%files -n libsixel%{_sover}
%{_libdir}/libsixel.so.%{_sover}{,.*}

%files utils
%{_bindir}/img2sixel
%{_bindir}/libsixel-config
%{_bindir}/sixel2png
%{_mandir}/man1/img2sixel.1%{?ext_man}
%{_mandir}/man1/sixel2png.1%{?ext_man}

%files devel
%{_includedir}/sixel.h
%{_libdir}/libsixel.so
%{_libdir}/pkgconfig/libsixel.pc

%files bash-completion
%{_datadir}/bash-completion/completions/img2sixel

%files zsh-completion
%{_datadir}/zsh/site-functions/_img2sixel

%changelog
