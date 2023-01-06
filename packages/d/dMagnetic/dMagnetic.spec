#
# spec file for package dMagnetic
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


Name:           dMagnetic
Version:        0.34
Release:        0
Summary:        An interpreter for Magnetic Scrolls games
License:        BSD-2-Clause
Group:          Amusements/Games/Other
URL:            http://dettus.net/dMagnetic/
Source0:        http://dettus.net/dMagnetic/dMagnetic_%{version}.tar.bz2

%description
An interpreter for games produced by the studio Magnetic Scrolls. It
can be used to play "The Pawn", "The Guild of Thieves", "Jinxter",
"Fish!", "Myth", "Corruption" and "Wonderland".

%prep
%setup -q -n dMagnetic_%{VERSION}

%build
make all

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man6
mkdir -p %{buildroot}%{_mandir}/man5
mkdir -p %{buildroot}%{_datadir}/dMagnetic
install -m 755 dMagnetic %{buildroot}%{_bindir}/dMagnetic
install -m 644 dMagnetic.6 %{buildroot}%{_mandir}/man6/dMagnetic.6
install -m 644 dMagneticini.5 %{buildroot}%{_mandir}/man5/dMagneticini.5
install -m 644 dMagnetic.ini %{buildroot}%{_datadir}/dMagnetic/dMagnetic.ini

%files
%{_bindir}/dMagnetic
%{_mandir}/man6/dMagnetic.6%{?ext_man}
%{_mandir}/man5/dMagneticini.5%{?ext_man}
%{_datadir}/dMagnetic/
%doc README.txt
%license LICENSE.txt

%changelog
