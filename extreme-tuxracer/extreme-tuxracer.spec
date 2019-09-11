#
# spec file for package extreme-tuxracer
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


%define oname   etr
Name:           extreme-tuxracer
Version:        0.7.5
Release:        0
Summary:        Racing game featuring Tux the Linux Penguin
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Race
Url:            http://sourceforge.net/projects/extremetuxracer/
Source:         http://downloads.sourceforge.net/extremetuxracer/%{oname}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  sfml2-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
Requires:       %{name}-data = %{version}
%if 0%{?suse_version} < 1330
Requires(post): update-desktop-files
Requires(postun): update-desktop-files
%endif

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
make %{?_smp_mflags}

%install
%make_install
%fdupes -s %{buildroot}%{_prefix}

# Already included by the doc macro
rm -fr %{buildroot}%{_datadir}/doc

%if 0%{?suse_version} < 1330
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%doc AUTHORS NEWS doc/code doc/courses_events doc/guide doc/score_algorithm
%license COPYING
%{_bindir}/%{oname}
%{_datadir}/pixmaps/%{oname}.png
%{_datadir}/pixmaps/%{oname}.svg
%{_datadir}/applications/%{oname}.desktop
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{oname}.appdata.xml

%files data
%{_datadir}/%{oname}/

%changelog
