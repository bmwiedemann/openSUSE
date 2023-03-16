#
# spec file for package tuxcursors
#
# Copyright (c) 2023 SUSE LLC
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


Name:           tuxcursors
Version:        0.5
Release:        0
Summary:        Tux Cursors!
License:        GPL-2.0-only
Source:         tuxcursors-0.5.tar.bz2
Source1:        tuxcursors.sh
BuildRequires:  xcursorgen
BuildArch:      noarch

%description
A cursor set that has nice animated penguins.

%prep
%autosetup -n tuxcursors

%build
./build.sh

%install
mkdir -p %{buildroot}%{_datadir}/icons
cp -a tuxcursors %{buildroot}%{_datadir}/icons
install -m 755 -D %{SOURCE1} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE COPYING
%{_bindir}/tuxcursors
%{_datadir}/icons/tuxcursors

%changelog
