#
# spec file for package gnu-unifont-bitmap-fonts
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


%define	fontdir     %{_fontsdir}/uni
Name:           gnu-unifont-bitmap-fonts
Version:        14.0.04
Release:        0
Summary:        The GNU Unicode Bitmap Font
License:        GPL-2.0-or-later AND OFL-1.1
Group:          System/X11/Fonts
URL:            https://unifoundry.com/unifont/index.html
Source0:        https://ftp.gnu.org/gnu/unifont/unifont-%{version}/unifont-%{version}.pcf.gz
Source1:        https://ftp.gnu.org/gnu/unifont/unifont-%{version}/unifont-%{version}.pcf.gz.sig
Source2:        http://unifoundry.com/LICENSE.txt
Source3:        http://unifoundry.com/1A09227B1F435A33_public.asc#/%{name}.keyring
BuildRequires:  fontpackages-devel
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
The GNU Unifont by Roman Czyborra is a free bitmap font that
covers the Unicode Basic Multilingual Plane (BMP), using an
intermediate bitmapped font format.

%prep
cp %{SOURCE2} COPYING

%build

%install
install -Dm 444 -t %{buildroot}%{fontdir} %{SOURCE0}

%reconfigure_fonts_scriptlets

%files
%license COPYING
%{fontdir}

%changelog
