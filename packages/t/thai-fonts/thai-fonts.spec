#
# spec file for package thai-fonts
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


Name:           thai-fonts
Version:        0.7.3
Release:        0
Summary:        A Collection of Thai OpenType Fonts
License:        GPL-2.0-only WITH Font-exception-2.0 AND LPPL-1.3c
Group:          System/X11/Fonts
URL:            https://linux.thai.net/projects/fonts-tlwg
Source0:        https://linux.thai.net/pub/thailinux/software/fonts-tlwg/fonts-tlwg-%{version}.tar.xz
BuildRequires:  fontpackages-devel
Patch0:         build.patch
BuildRequires:  fontconfig
BuildRequires:  fontforge >= 20190801
BuildRequires:  xz
%reconfigure_fonts_prereq
Provides:       locale(th)
Obsoletes:      fonts-thai < 0.4.16
Provides:       fonts-thai = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Fonts-TLWG is a collection of Thai scalable fonts. It provides
fonts that conform to existing standards and recommendations, so that it
can be a reference implementation.

The fonts included are Garuda, Kinnari, Laksaman, Loma, Norasi, Purisa,
Sawasdee, TlwgMono, TlwgTypewriter, TlwgTypo, Umpush and Waree.

%prep
%autosetup -n fonts-tlwg-%{version} -p1

%build
%configure --with-ttfdir=%{_ttfontsdir}
%make_build

%install
%make_install
rm -f %{buildroot}%{_ttfontsdir}/encodings.dir
rm -f %{buildroot}%{_ttfontsdir}/fonts.*
mkdir -p %{buildroot}%{_fontsconfavaildir}
mv %{buildroot}%{_datadir}/fontconfig/conf.avail/*.conf %{buildroot}%{_fontsconfavaildir}

%reconfigure_fonts_scriptlets

%files
%doc AUTHORS COPYING NEWS README ChangeLog
%files_fontsconf_availdir
%{_fontsdir}/opentype/
%files_fontsconf_availdir
%files_fontsconf_file 64-01-tlwg-kinnari.conf
%files_fontsconf_file 64-02-tlwg-norasi.conf
%files_fontsconf_file 64-10-tlwg-loma.conf
%files_fontsconf_file 64-11-tlwg-waree.conf
%files_fontsconf_file 64-13-tlwg-garuda.conf
%files_fontsconf_file 64-14-tlwg-umpush.conf
%files_fontsconf_file 64-15-laksaman.conf
%files_fontsconf_file 64-21-tlwg-typo.conf
%files_fontsconf_file 64-22-tlwg-typist.conf
%files_fontsconf_file 64-23-tlwg-mono.conf
%files_fontsconf_file 89-tlwg-garuda-synthetic.conf
%files_fontsconf_file 89-tlwg-kinnari-synthetic.conf
%files_fontsconf_file 89-tlwg-umpush-synthetic.conf
%files_fontsconf_file 89-tlwg-laksaman-synthetic.conf

%changelog
