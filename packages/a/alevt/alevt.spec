#
# spec file for package alevt
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           alevt
%{expand:%%global _prefix %(pkg-config --variable prefix x11 || echo /usr/X11R6)}
%if "%_prefix" == "/usr/X11R6"
%define _man_dir man
%else
%define _man_dir share/man
%endif
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
Url:            http://www.goron.de/~froese/
Summary:        Teletext and Videotext Decoder for the BTTV Driver
License:        GPL-2.0-or-later
Version:        1.6.2
Release:        0
Source0:        alevt-%version.tar.bz2
Source1:        alevt.desktop
Source2:        alevt.png
Patch2:         alevt-1.6.0-dvb-demux.patch
Patch4:         alevt-overflow2.diff
Patch5:         alevt-happy-abuild.diff
# PATCH-FIX-UPSTREAM pngtoico-libpng15.patch -- pgajdos@suse.com; build with libpng15; sent today to froese@gmx.de
# build against libpng14 should not be affected, otherwise please let me know
Patch6:         alevt-libpng15.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
AleVT is a teletext and videotext decoder and browser for the BTTV
driver (/dev/vbi) and the X Window System.  It features multiple
windows, a page cache, regexp searching, a built-in manual, and more.
There is also a program to get the time from teletext.

%prep
%setup -q
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
make OPT="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
echo "Using _prefix=%{_prefix} _man_dir=%{_man_dir}"
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}/bin $RPM_BUILD_ROOT%{_prefix}/%{_man_dir}/man1
make rpm-install USR_X11R6=%{_prefix} MAN=%{_man_dir}
%suse_update_desktop_file -i alevt AudioVideo TV

%files
%defattr(-,root,root)
%doc CHANGELOG COPYRIGHT README
%dir %{_prefix}/include/X11/pixmaps
/usr/share/applications/*.desktop
/usr/share/pixmaps/alevt.png
%{_prefix}/bin/alevt
%{_prefix}/bin/alevt-cap
%{_prefix}/bin/alevt-date
%{_prefix}/include/X11/pixmaps/mini-alevt.xpm
%doc %{_prefix}/%{_man_dir}/man1/alevt-cap.1.gz
%doc %{_prefix}/%{_man_dir}/man1/alevt-date.1.gz
%doc %{_prefix}/%{_man_dir}/man1/alevt.1x.gz

%changelog
