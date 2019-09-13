#
# spec file for package meterbridge
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           meterbridge
BuildRequires:  SDL_image-devel
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  jack-devel
BuildRequires:  update-desktop-files
Summary:        A Meterbridge for the JACK Audio System
Version:        0.9.2
Release:        0
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Visualization
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://plugin.org.uk/meterbridge/
Source:         %{name}-%{version}.tar.bz2
Source1:        meterbridge.desktop
Source2:        meterbridge.png
Patch:          meterbridge-gcc4-fix.diff
Patch1:         meterbridge-makefile-fix.diff

%description
Meterbridge is a JACK (JACK Audio Connection Kit) client for
visualizing audio signals.



Authors:
--------
    Steve Harris <steve@plugin.org.uk>

%prep
%setup -q
%patch
%patch1

%build
# This package failed when testing with -Wl,-as-needed being default.
# So we disable it here, if you want to retest, just delete this comment and the line below.
export SUSE_ASNEEDED=0
%{?suse_update_config:%{suse_update_config -f}}
autoreconf --force --install
export CFLAGS="%optflags -fgnu89-inline"
%configure
make

%install
[ "$RPM_BUILD_ROOT" != "/" -a -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
%suse_update_desktop_file -i meterbridge AudioVideo Music
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps

%clean
[ "$RPM_BUILD_ROOT" != "/" -a -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/%{name}
%if %suse_version > 820
%{_datadir}/applications/*.desktop
%endif
%{_datadir}/pixmaps/*.png

%changelog
