#
# spec file for package 0ad-data
#
# Copyright (c) 2025 SUSE LLC
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


Name:           0ad-data
Version:        0.27.0
Release:        0
Summary:        The Data Files for 0 AD
# When openSUSE supports full spdx 2.2, replace GPL-3.0+ with (GPL-3.0+ with Font-exception-2.0)
License:        CC-BY-SA-3.0 AND LPPL-1.3c+ AND GPL-3.0-or-later
Group:          Amusements/Games/Strategy/Real Time
URL:            https://play0ad.com/
# SF tarball is currently broken. Upstreamed notified and confirmed. Lets use their site for now.
Source:         https://releases.wildfiregames.com/0ad-%{version}-unix-data.tar.xz
BuildRequires:  dejavu-fonts
BuildRequires:  fdupes
BuildRequires:  gnu-free-fonts
Requires:       dejavu-fonts
Requires:       gnu-free-fonts
BuildArch:      noarch

%description
0 A.D. (pronounced "zero ey-dee") is a free, open-source, cross-platform real-time
strategy (RTS) game of ancient warfare. In short, it is a historically-based
war/economy game that allows players to relive or rewrite the history of Western
civilizations, focusing on the years between 500 B.C. and 500 A.D. The project is
highly ambitious, involving state-of-the-art 3D graphics, detailed artwork, sound,
and a flexible and powerful custom-built game engine.

The game has been in development by Wildfire Games (WFG), a group of volunteer,
hobbyist game developers, since 2001. The code and data are available under the GPL
license, and the art, sound and documentation are available under CC-BY-SA.

%prep
%setup -q -n 0ad-%{version}

%build

%install
mkdir -p %{buildroot}%{_datadir}
mv binaries/data %{buildroot}%{_datadir}/0ad
mkdir -p %{buildroot}%{_datadir}/0ad/l10n

# Replace fonts with system provided ones
cd %{buildroot}%{_datadir}/0ad/tools/fontbuilder/fonts
for font in {Free,Deja}*.ttf; do
    rm "$font"
    ln -s %{_datadir}/fonts/truetype/"$font" "$font"
done

%fdupes %{buildroot}%{_datadir}/0ad

%files
%defattr(-,root,root)
%{_datadir}/0ad

%changelog
