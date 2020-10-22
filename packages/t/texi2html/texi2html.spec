#
# spec file for package texi2html
#
# Copyright (c) 2020 SUSE LLC
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


Name:           texi2html
Version:        5.0
Release:        0
Summary:        Tool for converting texinfo documents to HTML
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/Texinfo
URL:            http://www.nongnu.org/texi2html/
Source0:        http://download.savannah.nongnu.org/releases/texi2html/texi2html-%{version}.tar.bz2
Patch1:         texi2html-1.78.dif
Patch2:         texi2html-5584.patch
Patch3:         03_add_build-date_param.patch
BuildRequires:  perl
BuildRequires:  perl-Text-Unidecode
BuildRequires:  perl-gettext
BuildRequires:  perl-libintl-perl
BuildRequires:  perl(Unicode::EastAsianWidth)
Requires:       perl-Text-Unidecode
Requires:       perl-gettext
Requires:       perl-libintl-perl
Requires:       perl(Unicode::EastAsianWidth)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Conflicts:      texinfo < 5.0
# Split provides: texi2html was part of texinfo until openSUSE 13.2
Provides:       texinfo:/usr/bin/texi2html

%description
The basic purpose of texi2html is to convert Texinfo documents into HTML,
and other formats.  Configuration files written in perl provide fine degree
of control over the final output, allowing most every aspect of the final
output not specified in the Texinfo input file to be specified.

%lang_package

%prep
%setup -q
%patch1
%patch2 -p0 -b .random
%patch3 -p1

# Avoid regenerated translations.pl as this becomes broken
mkdir i18n
touch i18n/en.thl
touch translations.pl

%build
LANG=POSIX
LC_ALL=POSIX
export LANG LC_ALL
%configure \
  --enable-nls \
  --with-encode \
  --with-gnu-ld \
  --with-unidecode \
  --with-external-libintl-perl \
  --with-external-Unicode-EastAsianWidth

make %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}%{_datadir}/texinfo/
rm -rf %{buildroot}%{_datadir}/locale/*.us-ascii
rm -rf %{buildroot}%{_datadir}/%{name}/lib

%find_lang %name
%find_lang %{name}_document

%post
%install_info --info-dir=%{_infodir} %{_infodir}/texi2html.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/texi2html.info.gz

%files
%defattr(-,root,root)
%doc COPYING NEWS README doc/texi2html.html
%{_bindir}/texi2html
%{_infodir}/texi2html.info.gz
%{_mandir}/man1/texi2html.1.gz
%{_datadir}/texi2html

%files lang -f %name.lang -f %{name}_document.lang
%defattr(-,root,root)

%changelog
