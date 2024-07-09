#
# spec file for package extreme-tuxracer
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


%define oname   etr
Name:           extreme-tuxracer
Version:        0.8.4
Release:        0
Summary:        Racing game featuring Tux the Linux Penguin
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Race
URL:            https://sourceforge.net/projects/extremetuxracer/
Source:         https://downloads.sourceforge.net/extremetuxracer/%{oname}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  sfml2-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
Requires:       %{name}-data = %{version}

%description
Extreme Tux Racer is a racing game featuring Tux
the Linux Penguin. Extreme Tux Racer continues in the tracks
of Tux Racer and its forks.

%package data
Summary:        Data files for %{name}
Group:          Amusements/Games/3D/Race
BuildArch:      noarch

%description data
This package contains the data files for %{name}.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure
%make_build

%install
%make_install
%fdupes -s %{buildroot}%{_prefix}

# Already included by the doc macro
rm -fr %{buildroot}%{_datadir}/doc

%files
%doc AUTHORS NEWS doc/code doc/courses_events doc/guide doc/score_algorithm
%license COPYING
%{_bindir}/%{oname}
%{_datadir}/pixmaps/%{oname}.png
%{_datadir}/pixmaps/%{oname}.svg
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.metainfo.xml

%files data
%{_datadir}/%{oname}/

%changelog
