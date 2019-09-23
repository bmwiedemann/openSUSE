#
# spec file for package gifsicle
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gifsicle
Version:        1.91
Release:        0
Summary:        Creating and editing GIF images and animations
License:        GPL-2.0-only
Group:          Productivity/Graphics/Other
URL:            https://www.lcdf.org/gifsicle/
Source:         https://www.lcdf.org/gifsicle/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix_gifdiff_null_pointer_deref.patch
Patch0:         fix_gifdiff_null_pointer_deref.patch
Obsoletes:      ungifsicle < %{version}
Provides:       ungifsicle = %{version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  perl-Time-HiRes
%endif

%description
Gifsicle manipulates GIF image files on the
command line. It supports merging several GIFs
into a GIF animation; exploding an animation into
its component frames; changing individual frames
in an animation; turning interlacing on and off;
adding transparency; adding delays, disposals, and
looping to animations; adding or removing
comments; optimizing animations for space; and
changing images' colormaps, among other things.

The gifsicle package contains two other programs:
gifview, a lightweight GIF viewer for X, can show
animations as slideshows or in real time, and
gifdiff compares two GIFs for identical visual
appearance.

%prep
%setup -q
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install

%files
%license COPYING
%doc NEWS.md README.md
%{_bindir}/gifdiff
%{_bindir}/gifsicle
%{_bindir}/gifview
%{_mandir}/man1/gifdiff.1*
%{_mandir}/man1/gifsicle.1*
%{_mandir}/man1/gifview.1*

%changelog
