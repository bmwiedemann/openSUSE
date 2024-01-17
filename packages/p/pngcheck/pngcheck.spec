#
# spec file for package pngcheck
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


Name:           pngcheck
Version:        3.0.3
Release:        0
Summary:        PNG file format checker
License:        GPL-2.0-or-later AND HPND
Group:          Productivity/Graphics/Other
URL:            http://www.libpng.org/pub/png/apps/pngcheck.html
Source:         http://www.libpng.org/pub/png/src/pngcheck-%{version}.tar.gz
Patch0:         fixbuild.diff
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
pngcheck verifies the integrity of PNG, JNG and MNG files (by checking the
internal 32-bit CRCs or checksums) and optionally dumps almost all of the
chunk-level information in the image in human-readable form. For example, it
can be used to print the basic stats about an image (dimensions, bit depth,
etc.); to list the color and transparency info in its palette; or to extract
the embedded text annotations. All PNG and JNG chunks are supported, plus
almost all MNG chunks (everything but PAST, DISC, tERm, DROP, DBYK, and
ORDR). This is a command-line program with batch capabilities (e.g.,
``pngcheck *.png'').

%prep
%setup -q
%patch0 -p1

%build
make %{?_smp_mflags} -f Makefile.unx

%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}/
install -m 755 pngsplit %{buildroot}%{_bindir}/
install -m 755 png-fix-IDAT-windowsize %{buildroot}%{_bindir}/
install -m 755 -d %{buildroot}%{_mandir}/man1/
install -m 0644 pngcheck.1 %{buildroot}%{_mandir}/man1/

%files
%defattr(-,root,root)
%doc CHANGELOG README gpl/COPYING
%{_bindir}/*
%{_mandir}/man1/%{name}.1.gz

%changelog
