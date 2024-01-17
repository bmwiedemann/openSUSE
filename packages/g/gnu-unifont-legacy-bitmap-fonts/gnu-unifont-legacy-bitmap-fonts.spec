#
# spec file for package gnu-unifont-legacy-bitmap-fonts
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define	fontdir     %{_fontsdir}/uni

Name:           gnu-unifont-legacy-bitmap-fonts
Version:        20080123
Release:        0
Summary:        The GNU Unicode Bitmap Font
License:        GPL-2.0+
Group:          System/X11/Fonts
Url:            http://en.wikipedia.org/wiki/Gnu_unifont
Source0:        gnu-unifont-%{version}.tar.bz2
Source1:        gpl-2.0.txt
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Provides:       gnu-unifont = %{version}
Obsoletes:      gnu-unifont <= 20080123
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The GNU Unifont by Roman Czyborra is a free bitmap font that
covers the Unicode Basic Multilingual Plane (BMP), using an
intermediate bitmapped font format.

This package provides an old version of GNU unifont just for
compatibility reasons.

%prep
# gnu-unifont-20080123/
%setup -q -n gnu-unifont-%{version}
# Explicitly overwrite COPYING with gpl-2.0.txt to avoid
# "incorrect-fsf-address" warning
cp %{SOURCE1} COPYING

%build
gzip --best *.pcf

%install
mkdir -p %{buildroot}%{fontdir}
install -m 444 *.pcf.gz %{buildroot}%{fontdir}

%clean

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc COPYING
%{fontdir}

%changelog
