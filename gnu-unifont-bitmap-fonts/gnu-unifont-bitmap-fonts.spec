#
# spec file for package gnu-unifont-bitmap-fonts
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


%define	fontdir     %{_fontsdir}/uni
Name:           gnu-unifont-bitmap-fonts
Version:        12.1.03
Release:        0
Summary:        The GNU Unicode Bitmap Font
License:        GPL-2.0-or-later
Group:          System/X11/Fonts
URL:            http://unifoundry.com/unifont.html
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
:

%install
mkdir -p %{buildroot}%{fontdir}
install -m 444 -D %{SOURCE0} %{buildroot}%{fontdir}

%reconfigure_fonts_scriptlets

%files
%license COPYING
%{fontdir}

%changelog
