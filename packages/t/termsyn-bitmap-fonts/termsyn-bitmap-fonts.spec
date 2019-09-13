#
# spec file for package termsyn-bitmap-fonts
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define fontname termsyn
Name:           termsyn-bitmap-fonts
Version:        1.8.7
Release:        0
Summary:        Clean, monospaced bitmap font based on Terminus and Tamsyn
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://sourceforge.net/projects/termsyn
Source:         http://downloads.sf.net/termsyn/termsyn-%{version}.tar.gz
BuildRequires:  fontpackages-devel
Provides:       termsyn-font
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Termsyn is a clean monospaced bitmap font based on Terminus
(http://terminus-font.sourceforge.net/) and
Tamsyn (http://www.fial.com/~scott/tamsyn-font/).

There are four sizes now: 6x11, 7x12, 6x13 and 7x14. There are iso8859-1 and
2 versions, version s with status "icons", consolefonts, and I started working
on iso10646-1 versions. All have bold too.

Each size has 12 fonts, for example:
termsyn6x11r.pcf (6x11 medium)
termsyn6x11b.pcf (6x11 bold)
termsyn6x11r2.pcf (6x11 medium iso8859-2)
termsyn6x11b2.pcf (6x11 bold iso8859-2)
termsyn6x11r.icons.pcf (6x11 medium with status icons)
termsyn6x11b.icons.pcf (6x11 bold with status icons)
termsyn6x11r.psfu (6x11 medium consolefont)
termsyn6x11b.psfu (6x11 bold consolefont)
termsyn6x11r2.psfu (6x11 medium iso8859-2 consolefont)
termsyn6x11b2.psfu (6x11 bold iso8859-2 consolefont)
termsynu6x11r.pcf (6x11 medium iso10646-1)
termsynu6x11b.pcf (6x11 bold iso10646-1)

You can use xfontsel or xlsfonts to get the full names.

%prep
%setup -q -n %{fontname}-%{version}

%define psfdir %{_datadir}/kbd/consolefonts

%build
gzip *.pcf

%install
mkdir -p %{buildroot}%{_miscfontsdir}/

for f in $(find ./ -name '*.pcf.gz') ; do
    install -m 0444 $f %{buildroot}%{_miscfontsdir}/
done

mkdir -p %{buildroot}%{psfdir}/

for f in $(find ./ -name '*.psfu') ; do
    install -m 0444 $f %{buildroot}%{psfdir}/
done

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc README*
%{_miscfontsdir}
%{psfdir}
%dir %{_datadir}/kbd

%changelog
