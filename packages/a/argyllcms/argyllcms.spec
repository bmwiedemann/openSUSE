#
# spec file for package argyllcms
#
# Copyright (c) 2022 SUSE LLC
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


%define tarname Argyll

Name:           argyllcms
Version:        2.3.1
Release:        0
Summary:        ICC compatible color management system
License:        AGPL-3.0-only AND GPL-2.0-or-later AND MIT
Group:          System/X11/Utilities
URL:            https://www.argyllcms.com/
Source0:        https://www.argyllcms.com/%{tarname}_V%{version}_src.zip
Source1:        19-color.fdi
Source2:        color-device-file.policy
Source3:        ajam-2.5.2-1.3.3.tgz
Patch1:         ajam-include.patch
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  unzip
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zlib)
#needed for ajam
BuildRequires:  bison
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(udev)
Requires:       udev
# FIXME: The application dlopens libcolordcompat.so, which does not
# exists in openSUSE colord package. We should use Suggests
# or Recommends here, and change its name in the source code
# to not read file from colord-devel.

%description
The Argyll color management system supports accurate ICC profile creation for
scanners, CMYK printers, film recorders and calibration and profiling of
displays.

Spectral sample data is supported, allowing a selection of illuminants observer
types, and paper fluorescent whitener additive compensation. Profiles can also
incorporate source specific gamut mappings for perceptual and saturation
intents. Gamut mapping and profile linking uses the CIECAM02 appearance model,
a unique gamut mapping algorithm, and a wide selection of rendering intents. It
also includes code for the fastest portable 8 bit raster color conversion
engine available anywhere, as well as support for fast, fully accurate 16 bit
conversion. Device color gamuts can also be viewed and compared using a VRML
viewer.

%package doc
Summary:        Argyll CMS documentation
# Does not really make sense without Argyll CMS itself
Group:          System/X11/Utilities
Requires:       %{name} = %{version}

%description doc
The Argyll color management system supports accurate ICC profile creation for
scanners, CMYK printers, film recorders and calibration and profiling of
displays.

This package contains the Argyll color management system documentation.

%prep
%setup -q -n %{tarname}_V%{version} -a3
cd ajam-2.5.2-1.3.3
%patch1 -p1 -b .include
cd ..

# remove unused source code
rm -fr usb/{*.inf,*.rtf,*.inf,*.cat,*.vcproj,*.sys,*.dsw,*.sln,*.dsp,*template*,WinCo*,winsub*,*kext*,KDRIVER_LICENSE,README_MSVC.txt,msvc,*.cmd,bin,driver,binfiles.*}
rm -fr zlib tiff png ccast/axTLS/*.c

%build
%define _lto_cflags %{nil}
cd ajam-2.5.2-1.3.3
make CFLAGS="-std=gnu89 %{optflags}"
ln -s $PWD/bin.unix/jam ../jam
cd ..

echo "CCFLAGS += -std=gnu89 %{optflags} -fno-strict-aliasing ;" >> Jamtop
# Evil hack to get --as-needed working. The build system unfortunately lists all
# the shared libraries by default on the command line _before_ the object to be built...
echo "STDLIBS += -ldl -lrt -lX11 -lXext -lXxf86vm -lXinerama -lXrandr -lXau -lXdmcp -lXss -ltiff -ljpeg ;" >> Jamtop

./jam  -fJambase %{?_smp_mflags}

%install
./jam -q -fJambase install

rm bin/License.txt
mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{_datadir}/color/argyll/ref
install -m 0755 -D bin/* %{buildroot}/%{_bindir}
install -m 0644 -D ref/*  %{buildroot}/%{_datadir}/color/argyll/ref
rm -f %{buildroot}/%{_datadir}/color/argyll/License.txt

# ensure timestamp in shipped files is not changing for each rebuild (boo#916158)
TIMESTAMP=$(LC_ALL=C date --date=@${SOURCE_DATE_EPOCH} +%c)

sed -i -e 's/^CREATED .*/CREATED "$TIMESTAMP"/g' %{buildroot}%{_datadir}/color/argyll/ref/RefMediumGamut.gam

install -d -m 0755 %{buildroot}%{_udevrulesdir}
install -p -m 0644 usb/55-Argyll.rules \
        %{buildroot}%{_udevrulesdir}
chmod a-x *.txt
find doc -type f -exec chmod a-x {} \;

%files
%doc *.txt
%{_bindir}/*
%dir %{_datadir}/color
%{_datadir}/color/argyll
%{_udevrulesdir}/55-Argyll.rules

%files doc
%doc doc/*.html doc/*.jpg doc/*.txt

%changelog
