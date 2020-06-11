#
# spec file for package fs-uae
#
# Copyright (c) 2020 SUSE LLC
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


Name:           fs-uae
Version:        3.0.5
Release:        0
Summary:        Amiga emulator with on-screen GUI and online play support
License:        GPL-2.0-or-later
Group:          System/Emulators/Other
URL:            https://fs-uae.net/
Source0:        https://fs-uae.net/stable/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  zip
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(libmpeg2)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)

%description
FS-UAE is an Amiga emulator based on UAE/WinUAE, with a focus on
emulating games.

Features include emulation of Amiga 500, 1200, 4000, CD32
and CDTV, perfectly smooth scrolling on 50Hz displays, support
for floppy images in ADF and IPF formats, CD-ROM images in ISO
or BIN/CUE format, mounting directories on a machine as Amiga
hard drives, support for Picasso 96 drivers for high-color and
high-resolution Workbench displays, and more.

A unique feature is support for cross-platform online play.
Amiga games can be played against (or with) other users over
a network.

The emulator uses the Amiga emulation code from the
WinUAE project and requires a moderately fast computer with
accelerated graphics (OpenGL) to work. A game pad or joystick is
recommended, but not required (FS-UAE can emulate a joystick
using the cursor keys and right Ctrl/Alt keys).

%prep
%setup -q

%build
%if 0%{?sle_version} == 150000
export CFLAGS="%optflags -fPIC"
export CXXFLAGS="%optflags -fPIC"
%endif
%configure \
%ifarch %arm aarch64
  --disable-jit
%else
  --enable-jit
%endif
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}
rm -rf %{buildroot}/%{_datadir}/doc
%fdupes %{buildroot}%{_datadir}

%files -f %{name}.lang
%doc ChangeLog README
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-device-helper
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/mime/packages/%{name}.xml

%changelog
