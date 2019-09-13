#
# spec file for package fetchmsttfonts
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           fetchmsttfonts
Summary:        Helper package to run the fetchmsttfonts script
License:        GPL-2.0+
Group:          System/X11/Fonts
Version:        11.4
Release:        0
Source0:        fetchmsttfonts.sh.in
Source1:        COPYING
Source2:        corefonts.md5
Source3:        corefonts.sha1
Source4:        corefonts.sha512
#these stop the patch from pulling in the package
#Provides:       pullin-msttf-fonts = 11.1
#Obsoletes:      pullin-msttf-fonts <= 11.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       awk
Requires:       cabextract
Requires:       coreutils
Requires:       curl
Requires:       fonts-config
Requires:       mktemp
Requires:       w3m
BuildArch:      noarch

%description
This package contains the fetchmsttfonts helper script, which on
running retrieves and unpacks the freely available MS Truetype fonts.



Authors:
--------
    Marcus Meissner <meissner@suse.de>
    Stefan Dirsch <sndirsch@suse.de>

%prep
cp %{SOURCE0} .
cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .
cp %{SOURCE4} .

%build
sed \
	-e 's,__VERSION__,%version,' \
	-e 's,__RELEASE__,%release,' \
	-e 's,__NAME__,%name,' \
	-e 's,__DOCDIR__,%{_docdir},' \
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

%clean
rm -rf $RPM_BUILD_ROOT

%postun -p /usr/sbin/fonts-config

%files
%defattr(-, root, root)
%doc COPYING
%doc corefonts.{md5,sha1,sha512}
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

%changelog
