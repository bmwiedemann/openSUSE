#
# spec file for package feh
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


Name:           feh
Version:        3.10.3
Release:        0
Summary:        X11 image viewer
License:        LGPL-2.0-or-later AND MIT
URL:            https://feh.finalrewind.org/
Source:         https://feh.finalrewind.org/%{name}-%{version}.tar.bz2
Source1:        https://feh.finalrewind.org/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
Source3:        jpegexiforient.c
Source4:        https://git.finalrewind.org/zsh/plain/etc/completions/_feh
Source99:       feh-rpmlintrc
# PATCH-FIX-OPENSUSE feh-makefile_optflags.patch https://github.com/derf/feh/issues/71 pascal.bleser@opensuse.org -- pass OPTFLAGS to make instead of hard-coded -O2 -g
Patch1:         feh-makefile_optflags.patch
# PATCH-FIX-UPSTREAM https://github.com/derf/feh/pull/337
Patch6:         feh-makefile_app.patch

Patch7:         feh-add_jxl_support.patch
BuildRequires:  curl-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xt)
Requires:       imlib2-loaders
# Needs only the binaries from it. (boo#1080592)
Requires:       libjpeg-turbo
Requires(post): desktop-file-utils
Requires(post): hicolor-icon-theme
Requires(postun): desktop-file-utils
Requires(postun): hicolor-icon-theme

%description
feh is an X11 image viewer aimed mostly at console users. It does not
have a fancy GUI, but simply displays images. It is controlled via
commandline arguments and configurable key/mouse actions. feh has
multiple file modes using a slideshow or multiple windows. It
supports the creation of montages as index prints with many
user-configurable options.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
ZSH completion script for %{name} 3.

%prep
%autosetup -p1
cp %{SOURCE3} .

%build
%make_build \
    PREFIX="%{_prefix}" \
    curl=1 \
    help=1 \
    xinerama=1 \
    debug=0 \
    exif=1 \
    app=1 \
    inotify=1 \
    OPTFLAGS="%{optflags} -Wall -Wextra"

gcc %{optflags} -fwhole-program jpegexiforient.c -o jpegexiforient

%install
%make_install \
    PREFIX="%{_prefix}" \
    cam=1 app=1 examples=0

rm -rf "%{buildroot}%{_datadir}/doc"

install -D -m0755 jpegexiforient %{buildroot}%{_bindir}/jpegexiforient

install -Dm0644 %{SOURCE4} %{buildroot}/%{_datadir}/zsh/site-functions/_%{name}

%files
%license COPYING
%doc AUTHORS ChangeLog README.md TODO
%{_bindir}/feh
%{_bindir}/jpegexiforient
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/feh.1%{?ext_man}

%files zsh-completion
%{_datadir}/zsh

%changelog
