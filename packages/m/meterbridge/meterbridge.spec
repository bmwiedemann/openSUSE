#
# spec file for package meterbridge
#
# Copyright (c) 2021 SUSE LLC
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


Name:           meterbridge
Version:        0.9.3
Release:        0
Summary:        A Meterbridge for the JACK Audio System
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Visualization
URL:            http://plugin.org.uk/meterbridge
Source:         %{url}/meterbridge-%{version}.tar.gz
Source1:        meterbridge.desktop
Source2:        meterbridge.png
Patch0:         meterbridge-gcc4-fix.diff
Patch1:         meterbridge-makefile-fix.diff
Patch2:         https://gitweb.gentoo.org/repo/gentoo.git/plain/media-sound/meterbridge/files/meterbridge-0.9.3-setrgba.patch
Patch3:         https://gitweb.gentoo.org/repo/gentoo.git/plain/media-sound/meterbridge/files/meterbridge-0.9.3-asneeded.patch
BuildRequires:  SDL_image-devel
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  jack-devel
BuildRequires:  update-desktop-files

%description
Meterbridge is a JACK (JACK Audio Connection Kit) client for
visualizing audio signals.

%prep
%autosetup -p1

%build
autoreconf --force --install
%configure
%make_build

%install
%make_install
%suse_update_desktop_file -i meterbridge AudioVideo Music
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp %{SOURCE2} %{buildroot}%{_datadir}/pixmaps

%files
%license COPYING
%doc AUTHORS ChangeLog
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
