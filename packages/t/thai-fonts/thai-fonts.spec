#
# spec file for package thai-fonts
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           thai-fonts
Version:        0.6.1
Release:        0
Summary:        A Collection of Thai TrueType Fonts
License:        LPPL-1.3c AND GPL-2.0-only WITH Font-exception-2.0
Group:          System/X11/Fonts
Url:            ftp://linux.thai.net/pub/thailinux/software/fonts-tlwg/
Source0:        ftp://linux.thai.net/pub/thailinux/software/fonts-tlwg/fonts-tlwg-%{version}.tar.xz
BuildRequires:  fontpackages-devel
Patch0:         build.patch
BuildRequires:  fontconfig
BuildRequires:  fontforge
BuildRequires:  xz
%reconfigure_fonts_prereq
Provides:       locale(th)
Obsoletes:      fonts-thai < 0.4.16
Provides:       fonts-thai = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The Thai TrueType fonts included here are Norasi and Garuda from the
National Font project.

%prep
%setup -q -n fonts-tlwg-%{version}
%patch0 -p1

%build
%configure --with-ttfdir=%{_ttfontsdir}
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f %{buildroot}%{_ttfontsdir}/encodings.dir
rm -f %{buildroot}%{_ttfontsdir}/fonts.*
mkdir -p %{buildroot}%{_fontsconfavaildir}
mv %{buildroot}/etc/fonts/conf.avail/*.conf %{buildroot}%{_fontsconfavaildir}
rm -r %{buildroot}/etc

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc AUTHORS COPYING NEWS README ChangeLog
%{_ttfontsdir}
%files_fontsconf_availdir
%files_fontsconf_file 64-01-tlwg-kinnari.conf
%files_fontsconf_file 64-02-tlwg-norasi.conf
%files_fontsconf_file 64-11-tlwg-waree.conf
%files_fontsconf_file 64-12-tlwg-loma.conf
%files_fontsconf_file 64-13-tlwg-garuda.conf
%files_fontsconf_file 64-14-tlwg-umpush.conf
%files_fontsconf_file 64-15-laksaman.conf
%files_fontsconf_file 64-21-tlwg-typo.conf
%files_fontsconf_file 64-22-tlwg-typist.conf
%files_fontsconf_file 64-23-tlwg-mono.conf
%files_fontsconf_file 89-tlwg-garuda-synthetic.conf
%files_fontsconf_file 89-tlwg-kinnari-synthetic.conf
%files_fontsconf_file 89-tlwg-loma-synthetic.conf
%files_fontsconf_file 89-tlwg-umpush-synthetic.conf
%files_fontsconf_file 89-tlwg-waree-synthetic.conf
%files_fontsconf_file 89-tlwg-laksaman-synthetic.conf

%changelog
