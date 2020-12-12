#
# spec file for package fetchmsttfonts
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020 B1 Systems GmbH
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


Name:           fetchmsttfonts
Version:        12.0
Release:        0
Summary:        Helper package to download Microsoft Core fonts for the Web
License:        GPL-2.0-or-later
Group:          System/X11/Fonts
URL:            https://corefonts.sourceforge.net/
Source0:        fetchmsttfonts.sh.in
Source1:        COPYING
Source4:        corefonts.sha512
#these stop the patch from pulling in the package
#Provides:       pullin-msttf-fonts = 11.1
#Obsoletes:      pullin-msttf-fonts <= 11.1
Requires:       cabextract
Requires:       coreutils
Requires:       curl
Requires:       fonts-config
Requires:       mktemp
Requires:       w3m
BuildArch:      noarch

%description
This package contains a helper script that downloads and installs
a number of TrueType fonts collectively known as corefonts, or the
Core fonts for the Web. Originally made available my Micosoft under
a non-free End-user licence agreement (EULA), they continue to be
distributed subject to the same licence terms. The user is shown
a copy of the licence text upon execution.

The Core fonts for the Web include: Arial, Arial Black, Andale Mono,
Monotype, Courier New, Comic Sans MS, Georgia, Impact, Times New
Roman, Trebuchet MS, Verdana, Webdings.

%prep
cp %{SOURCE0} .
cp %{SOURCE1} .
cp %{SOURCE4} .

%build
sed \
	-e 's,__VERSION__,%version,' \
	-e 's,__RELEASE__,%release,' \
	-e 's,__NAME__,%name,' \
	fetchmsttfonts.sh.in > fetchmsttfonts.sh

%install
%suse_install_update_script fetchmsttfonts.sh
%{nil}
#
mkdir -p %buildroot/var/adm/update-messages
touch %buildroot/var/adm/update-messages/%name-%version-%release-1
mkdir -p %buildroot/usr/share/doc/corefonts
touch %buildroot/usr/share/doc/corefonts/EULA.html
mkdir -p %buildroot/usr/share/fonts/truetype
for f in webdings.ttf verdanaz.ttf verdana.ttf verdanai.ttf verdanab.ttf trebuc.ttf trebucit.ttf trebucbi.ttf trebucbd.ttf times.ttf timesi.ttf timesbi.ttf timesbd.ttf impact.ttf georgiaz.ttf georgia.ttf georgiai.ttf georgiab.ttf cour.ttf couri.ttf courbi.ttf courbd.ttf comic.ttf comicbd.ttf ariblk.ttf arial.ttf ariali.ttf arialbi.ttf arialbd.ttf andalemo.ttf;
do
	touch %buildroot/usr/share/fonts/truetype/$f
done
mkdir -p %{buildroot}/usr/share/%{name}
mv corefonts.sha512 %{buildroot}/usr/share/%{name}

%postun -p /usr/sbin/fonts-config

%files
%license COPYING
/var/adm/update-scripts/*
%dir /usr/share/doc/corefonts
%dir /usr/share/fonts/truetype
%ghost /var/adm/update-messages/%name-%version-%release-1
# so we can get rid of them by rpm -e fetchmsttfonts
%ghost /usr/share/doc/corefonts/EULA.html
%ghost /usr/share/fonts/truetype/webdings.ttf
%ghost /usr/share/fonts/truetype/verdanaz.ttf
%ghost /usr/share/fonts/truetype/verdana.ttf
%ghost /usr/share/fonts/truetype/verdanai.ttf
%ghost /usr/share/fonts/truetype/verdanab.ttf
%ghost /usr/share/fonts/truetype/trebuc.ttf
%ghost /usr/share/fonts/truetype/trebucit.ttf
%ghost /usr/share/fonts/truetype/trebucbi.ttf
%ghost /usr/share/fonts/truetype/trebucbd.ttf
%ghost /usr/share/fonts/truetype/times.ttf
%ghost /usr/share/fonts/truetype/timesi.ttf
%ghost /usr/share/fonts/truetype/timesbi.ttf
%ghost /usr/share/fonts/truetype/timesbd.ttf
%ghost /usr/share/fonts/truetype/impact.ttf
%ghost /usr/share/fonts/truetype/georgiaz.ttf
%ghost /usr/share/fonts/truetype/georgia.ttf
%ghost /usr/share/fonts/truetype/georgiai.ttf
%ghost /usr/share/fonts/truetype/georgiab.ttf
%ghost /usr/share/fonts/truetype/cour.ttf
%ghost /usr/share/fonts/truetype/couri.ttf
%ghost /usr/share/fonts/truetype/courbi.ttf
%ghost /usr/share/fonts/truetype/courbd.ttf
%ghost /usr/share/fonts/truetype/comic.ttf
%ghost /usr/share/fonts/truetype/comicbd.ttf
%ghost /usr/share/fonts/truetype/ariblk.ttf
%ghost /usr/share/fonts/truetype/arial.ttf
%ghost /usr/share/fonts/truetype/ariali.ttf
%ghost /usr/share/fonts/truetype/arialbi.ttf
%ghost /usr/share/fonts/truetype/arialbd.ttf
%ghost /usr/share/fonts/truetype/andalemo.ttf
/usr/share/%{name}

%changelog
