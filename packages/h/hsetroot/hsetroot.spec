#
# spec file for package hsetroot
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           hsetroot
Version:        1.0.5
Release:        0
Summary:        Advanced wallpaper tool for X
License:        GPL-2.0
Group:          System/X11/Utilities
Url:            https://github.com/himdel/hsetroot
Source:         https://github.com/himdel/hsetroot/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        hsetroot.1
Patch0:         add_destdir_support.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  freetype2-devel
BuildRequires:  imlib2-devel
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-devel
Requires:       imlib2-filters
Requires:       imlib2-loaders

%description
hsetroot is a tool which allows you to compose wallpapers ("root pixmaps") for
X. It has a lot of options like rendering gradients, solids, images but it also
allows you to perform manipulations on those things, or chain them together.
You could use one standard background image for isntance, and using tint to
make it fit your current theme. And yes, of course it is compatible with
semi-translucent applications like aterm and xchat :)

At this time, hsetroot can render: gradients (multi-color with variable
distance), solids (rectangles) and images (centered, tiled, fullscreen, or
maximum aspect). It supports the following manipulations: tinting (overlaying a
color mask), blurring, sharpening, flipping (horizontally, diagonally,
vertically) it also allows you to adjust brightness, contrast and gamma-level.
hsetroot also supports alpha-channels when rendering things.

%prep
%setup -q
%patch0 -p1

%build
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot}%{_bindir} install
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/hsetroot.1


%files
%{_bindir}/%{name}
%{_bindir}/hsr-outputs
%{_mandir}/man1/%{name}.1%{ext_man}
%doc README.md

%changelog
