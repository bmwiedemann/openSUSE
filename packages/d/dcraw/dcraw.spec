#
# spec file for package dcraw
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           dcraw
Version:        9.27.0
Release:        0
Summary:        Raw Digital Photo Decoding
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Convertors
Url:            http://www.cybercom.net/~dcoffin/dcraw/
#*** NOTE: run "sh update_dcraw" to update to latest version of the following sources ("wget", "rcs" and "lynx" packages are required for the update).
Source0:        http://www.cybercom.net/~dcoffin/dcraw/archive/%{name}-%{version}.tar.gz
Source1:        README
# http://www.cybercom.net/~dcoffin/dcraw/.badpixels
Source2:        badpixels
Source3:        http://www.cybercom.net/~dcoffin/dcraw/clean_crw.c
Source4:        http://www.cybercom.net/~dcoffin/dcraw/fuji_green.c
Source5:        http://www.cybercom.net/~dcoffin/dcraw/fujiturn.c
Source6:        http://www.cybercom.net/~dcoffin/dcraw/parse.c
Source7:        http://www.cybercom.net/~dcoffin/dcraw/rawphoto.c
#***
Source100:      README.openSUSE
Source101:      update_dcraw
# PATCH-FIX-OPENSUSE fuji_green.c_fix_gcc_warnings.patch asterios.dramis@gmail.com -- Fix gcc implicit declaration warning
Patch0:         fuji_green.c_fix_gcc_warnings.patch
BuildRequires:  gettext-runtime
BuildRequires:  libjpeg-devel
BuildRequires:  liblcms2-devel
Recommends:     %{name}-lang = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Command line tools for raw digital photo decoding and processing.

%lang_package

%prep
%setup -q -n %{name}
cp -a %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} .
%patch0

%build
export CFLAGS="%{optflags} -fno-strict-aliasing -fstack-protector-all"

for file in *.c ; do
  LDFLAGS=
  OTHERFLAGS=
  if test $file = dcraw.c ; then
    LDFLAGS="-lm -ljpeg -llcms2 -DLOCALEDIR=\""%{_datadir}/locale"\""
  fi
  if test $file = fuji_green.c ; then
    LDFLAGS="-lm"
  fi
  gcc $CFLAGS $OTHERFLAGS -o ${file%.c} $file $LDFLAGS -DNO_JASPER
done
# Compile with -D_16BIT to rotate 48-bit PPM images
gcc $CFLAGS -D_16BIT -o fujiturn16 fujiturn.c

# Build language catalogs
for catsrc in dcraw_*.po ; do
  lang="${catsrc%.po}"
  lang="${lang#dcraw_}"
  msgfmt -o "dcraw_${lang}.mo" "$catsrc"
done

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -d -m 0755 %{buildroot}%{_mandir}/man1

install -pm 0755 dcraw %{buildroot}%{_bindir}/
install -pm 0644 dcraw.1 %{buildroot}%{_mandir}/man1/

install -pm 0755 clean_crw %{buildroot}%{_bindir}/
install -pm 0755 fuji_green %{buildroot}%{_bindir}/
install -pm 0755 fujiturn %{buildroot}%{_bindir}/
install -pm 0755 fujiturn16 %{buildroot}%{_bindir}/
install -pm 0755 parse %{buildroot}%{_bindir}/dcparse

# Install language catalogs
for catalog in dcraw_*.mo ; do
  lang="${catalog%.mo}"
  lang="${lang#dcraw_}"
  install -d -m 0755 "%{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES"
  install -pm 0644 "$catalog" "%{buildroot}%{_datadir}/locale/${lang}/LC_MESSAGES/dcraw.mo"
done

# Install localized manpages
for manpage in dcraw_*.1 ; do
  lang="${manpage%.1}"
  lang="${lang#dcraw_}"
  install -d -m 0755 "%{buildroot}%{_mandir}/${lang}/man1"
  install -pm 0644 "${manpage}" "%{buildroot}%{_mandir}/${lang}/man1/dcraw.1"
done

# Documentation
cp -a %{SOURCE1} %{SOURCE2} %{SOURCE7} %{SOURCE100} .
mv badpixels .badpixels

%find_lang %{name} --with-man

%files
%defattr(-,root,root,-)
%doc .badpixels README README.openSUSE rawphoto.c
%{_bindir}/clean_crw
%{_bindir}/dcparse
%{_bindir}/dcraw
%{_bindir}/fuji_green
%{_bindir}/fujiturn
%{_bindir}/fujiturn16
%{_mandir}/man1/dcraw.1%{ext_man}

%files lang -f %{name}.lang
%defattr(-,root,root,-)
%dir %{_mandir}/ca
%dir %{_mandir}/ca/man1
%dir %{_mandir}/cs
%dir %{_mandir}/cs/man1
%dir %{_mandir}/da
%dir %{_mandir}/da/man1
%dir %{_mandir}/eo
%dir %{_mandir}/eo/man1
%dir %{_mandir}/hu
%dir %{_mandir}/hu/man1
%dir %{_mandir}/pl
%dir %{_mandir}/pl/man1
%dir %{_mandir}/pt
%dir %{_mandir}/pt/man1
%dir %{_mandir}/ro
%dir %{_mandir}/ro/man1
%dir %{_mandir}/sv
%dir %{_mandir}/sv/man1
%dir %{_mandir}/zh_CN
%dir %{_mandir}/zh_CN/man1
%dir %{_mandir}/zh_TW
%dir %{_mandir}/zh_TW/man1

%changelog
