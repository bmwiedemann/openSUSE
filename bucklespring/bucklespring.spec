#
# spec file for package bucklespring
#
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


Name:           bucklespring
Version:        1.4.0
Release:        0
Summary:        Nostalgia keyboard sound emulator
License:        GPL-2.0-only
Group:          Amusements/Toys/Other
URL:            https://github.com/zevv/bucklespring
#Git-Clone:     https://github.com/zevv/bucklespring.git
Source:         https://github.com/zevv/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alure)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)

%description
This project emulates the sound of an old faithful IBM Model-M space
saver bucklespring keyboard while typing on a notebook/pc.

%prep
%setup -q

%build
export CFLAGS='%{optflags}'
make PATH_AUDIO=%{_datadir}/bucklespring/wav/ %{?_smp_mflags}

%install
install -Dm 0755 buckle %{buildroot}/%{_bindir}/buckle
install -d %{buildroot}/%{_datadir}/%{name}/wav
install -m 0644 wav/* %{buildroot}/%{_datadir}/%{name}/wav
%fdupes -s %{buildroot}/%{_datadir}/%{name}/wav

%files
%license LICENSE
%doc README.md
%{_bindir}/buckle
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/wav

%changelog
