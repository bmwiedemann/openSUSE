#
# spec file for package sidplayfp
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2023-2024, Martin Hauke <mardnh@gmx.de>
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


Name:           sidplayfp
Version:        2.8.0
Release:        0
Summary:        SID chip music module player
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Players
#Git-Clone:     https://github.com/libsidplayfp/sidplayfp.git
URL:            https://sourceforge.net/projects/sidplay-residfp/
Source0:        https://sourceforge.net/projects/sidplay-residfp/files/sidplayfp/2.8/sidplayfp-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libsidplayfp)
BuildRequires:  pkgconfig(libstilview)

%description
A player for playing SID music modules originally created on the Commodore 64
and compatibles.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%check

%files
%license COPYING
%doc AUTHORS README TODO
%{_bindir}/sidplayfp
%{_bindir}/stilview
%{_mandir}/man1/sidplayfp.1%{?ext_man}
%{_mandir}/man1/stilview.1%{?ext_man}
%{_mandir}/man5/sidplayfp.ini.5%{?ext_man}

%changelog
