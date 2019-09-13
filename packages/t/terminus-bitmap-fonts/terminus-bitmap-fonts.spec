#
# spec file for package terminus-bitmap-fonts
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define fontname terminus-font

Name:           terminus-bitmap-fonts
Version:        4.48
Release:        0
Summary:        Readable Fixed Width Fonts for X11 and the Linux Console
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            http://terminus-font.sf.net/
Source:         https://sf.net/projects/terminus-font/files/terminus-font-%{version}/terminus-font-%{version}.tar.gz
BuildRequires:  bdftopcf
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  python3-devel >= 3.5
%reconfigure_fonts_prereq
Provides:       terminus-font
Provides:       locale(ru;bg)
BuildArch:      noarch

%description
Terminus Font is a geometric sans-serif font designed for long (8 and
more hours per day) work with computers. Version 4.03 contains 538
characters, covering code pages ISO8859-1/2/5/9/15/16,
Windows-1250/1251/1252/1254, IBM-437/852/855/866, KOI8-R/U/E/F,
Bulgarian-MIK, Paratype-PT154/PT254 and Macintosh-Ukrainian, and also
the vt100 and xterm pseudographic characters.

The sizes and styles present are 8x14-normal, 8x14-bold,
8x14-EGA/VGA-bold, 8x16-normal, 8x16-bold, 8x16-EGA/VGA-bold,
10x20-normal, 10x20-bold, 12x24-normal, 12x24-bold and 14x28-normal
(which's weight is actually between normal and bold).

%prep
%setup -q -n %{fontname}-%{version}
dos2unix OFL.TXT
%define psfdir %{_datadir}/kbd/consolefonts

%build
chmod +x ./configure
# not autoconf
./configure --prefix=%{_prefix}
make -e x11dir=%{_miscfontsdir} psfdir=%{psfdir}

%install
make -e DESTDIR=%{buildroot}  x11dir=%{_miscfontsdir} psfdir=%{psfdir} install
rm -f %{buildroot}%{_miscfontsdir}/fonts.dir
pushd %{buildroot}%{psfdir}
    rename .psf.gz .psfu.gz *.psf.gz
popd
#
# Was once a patch, now a command here. Author and exact reason unknown,
# but recompression does not look all that bad -j.eng.
#
find "%buildroot" -type f "(" -name "*.pcf.gz" -o -name "*.psfu.gz" ")" \
	-exec gzip -dv "{}" "+"
find "%buildroot" -type f "(" -name "*.pcf.gz" -o -name "*.psfu.gz" ")" \
	-exec gzip -9v "{}" "+"

%reconfigure_fonts_scriptlets

%files
%license OFL.TXT
%doc README*
%{_miscfontsdir}
%{psfdir}
%dir %{_datadir}/kbd

%changelog
