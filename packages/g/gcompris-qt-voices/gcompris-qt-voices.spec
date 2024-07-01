#
# spec file for package gcompris-qt-voices
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


Name:           gcompris-qt-voices
Version:        4.1~20240524
Release:        0
Summary:        Voice files for gcompris-qt
License:        GPL-2.0-or-later AND GPL-3.0-or-later AND CC-BY-SA-1.0+ AND GFDL-1.1-or-later AND SUSE-Public-Domain AND SUSE-Free-Art-1.3
Group:          Amusements/Teaching/Other
URL:            https://gcompris.net
Source:         gcompris-qt-voices.tar.xz
Source2:        fetch_voices.sh
Source3:        LICENSE
Requires:       gcompris-qt = 4.1
Provides:       gcompris-voices = 4.1
Provides:       locale(gcompris:en)
BuildArch:      noarch

%description
This is the voice data package for %{name}. This a full bundle for
when you do not want to use the automatic online feature.

This allow you to play %{name} activities in different languages.

%prep

%build

%install
cp %{_sourcedir}/LICENSE .
mkdir -p %{buildroot}%{_datadir}/KDE/gcompris-qt
tar -C %{buildroot}%{_datadir}/KDE/gcompris-qt -xJf %{SOURCE0}

%files
%defattr(-,root,root)
%dir %{_datadir}/KDE/
%dir %{_datadir}/KDE/gcompris-qt/
%dir %{_datadir}/KDE/gcompris-qt/data2
%dir %{_datadir}/KDE/gcompris-qt/data2/voices-ogg
%{_datadir}/KDE/gcompris-qt/data2/voices-ogg/Contents
%{_datadir}/KDE/gcompris-qt/data2/voices-ogg/*.rcc
%license LICENSE

%changelog
