#
# spec file for package google-caladea-fonts
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuremberg, Germany.
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


Name:           google-caladea-fonts
Version:        1.002
Release:        0
Summary:        Sans-serif Font Metrics-compatible with Cambria
# License as per: https://chromium.googlesource.com/chromiumos/overlays/chromiumos-overlay/+/cd597de7c7079edb302effde8acfecf5a65dc73d/media-fonts/crosextrafonts/crosextrafonts-20130214.ebuild
License:        Apache-2.0
Group:          System/X11/Fonts
# FIXME: This is likely not the best upstream URL. However, this font
#   is currently not available through Google Fonts.
Url:            https://commondatastorage.googleapis.com/chromeos-localmirror/distfiles/
Source:         https://commondatastorage.googleapis.com/chromeos-localmirror/distfiles/crosextrafonts-20130214.tar.gz
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Workhorse serif font that is designed to be a metrics-compatible drop-in 
replacement for Cambria.
Contains Regular, Bold, Italic, and Bold Italic version.

Designed by Huerta Típografica for Google.

%prep
%setup -c %{name}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
# by default install command uses 755 umask
install -m 644 crosextrafonts-20130214/*.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%dir %{_ttfontsdir}
%{_ttfontsdir}/*

%changelog
