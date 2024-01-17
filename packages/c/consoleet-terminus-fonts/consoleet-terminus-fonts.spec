#
# spec file for package consoleet-terminus-fonts
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


Name:           consoleet-terminus-fonts
Version:        4.49.1
Release:        0
Summary:        Vector/OTF versions of the Terminus bitmap fonts
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://inai.de/projects/consoleet/
Source:         https://inai.de/files/consoleet/consoleet-terminus-4.49.1.tar.zst
Source2:        https://inai.de/files/consoleet/consoleet-terminus-4.49.1.tar.zst.asc
Source3:        40-terminus-alias.conf
BuildRequires:  fontpackages-devel
BuildRequires:  zstd
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
The Terminus bitmap fonts, provided in OpenType vector format.
Both original (jagged-edge) and smooth-edge variants are provided.

%prep
%setup -Tcq
tar --use=zstd --strip-components=1 -xf %SOURCE0

%build

%install
mkdir -p "%buildroot/%_ttfontsdir" "%buildroot/%_sysconfdir/fonts/conf.d" "%buildroot/%_datadir/fontconfig/conf.avail"
cp -av *.otf "%buildroot/%_ttfontsdir/"
# If ax86's variant is not installed, this alias will take effect
cp -av "%_sourcedir/40-terminus-alias.conf" "%buildroot/%_datadir/fontconfig/conf.avail"
ln -s "%_datadir/fontconfig/conf.avail/40-terminus-alias.conf" "%buildroot/%_sysconfdir/fonts/conf.d/"

%reconfigure_fonts_scriptlets

%files
%license OFL.txt
%dir %_sysconfdir/fonts
%dir %_sysconfdir/fonts/conf.d
%config %_sysconfdir/fonts/conf.d/*.conf
%_ttfontsdir/
%_datadir/fontconfig/

%changelog
