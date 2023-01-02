#
# spec file for package remind
#
# Copyright (c) 2023 SUSE LLC
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


Name:           remind
Version:        4.2.2
Release:        0
%define tar_version 04.02.02
Summary:        A sophisticated calendar and alarm program
License:        GPL-2.0-only
Group:          Productivity/Office/Organizers
URL:            https://dianne.skoll.ca/projects/remind/
Source0:        %{name}-%{tar_version}.tar.gz
Source100:      %{name}-rpmlintrc
BuildRequires:  perl
BuildRequires:  perl-Cairo
BuildRequires:  perl-Getopt-Long-Descriptive
BuildRequires:  perl-JSON-MaybeXS
BuildRequires:  perl-Pango

Requires:       perl
Requires:       perl-Cairo
Requires:       perl-Getopt-Long-Descriptive
Requires:       perl-JSON-Any
Requires:       perl-Pango
Requires:       tcllib

%description
Remind is a sophisticated calendar and alarm program.
It includes the following features:

* A sophisticated scripting language and intelligent
  handling of exceptions and holidays.
* Plain-text, PostScript and HTML output.
* Timed reminders and pop-up alarms.
* A friendly graphical front-end for people who don't
  want to learn the scripting language.
* Facilities for both the Gregorian and Hebrew calendars.
* Support for 12 different languages.

%prep
%setup -q -n %{name}-%{tar_version}

%build
CFLAGS="%{optflags}" ./configure --disable-perl-build-artifacts --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

##%%check
##make test

%files
%defattr(-,root,root,-)
%doc %{_mandir}/man1/rem.1%{ext_man}
%doc %{_mandir}/man1/rem2html.1%{ext_man}
%doc %{_mandir}/man1/rem2ps.1%{ext_man}
%doc %{_mandir}/man1/rem2pdf.1%{ext_man}
%doc %{_mandir}/man1/remind.1%{ext_man}
%doc %{_mandir}/man1/tkremind.1%{ext_man}
%doc %{_mandir}/man3/Remind::PDF.3pm%{ext_man}
%doc %{_mandir}/man3/Remind::PDF::Entry.3pm%{ext_man}

%{_bindir}/rem
%attr(0755,root,root) %{_bindir}/rem2html
%attr(0755,root,root) %{_bindir}/rem2pdf
%attr(0755,root,root) %{_bindir}/rem2ps
%attr(0755,root,root) %{_bindir}/remind
%attr(0755,root,root) %{_bindir}/tkremind
%attr(0755,root,root) %{perl_vendorlib}/Remind/

%dir /usr/share/remind/
%dir /usr/share/remind/holidays
%dir /usr/share/remind/lang
%dir /usr/share/remind/site
/usr/share/remind/ansitext.rem
/usr/share/remind/seasons.rem
/usr/share/remind/holidays/ca.rem
/usr/share/remind/holidays/fr.rem
/usr/share/remind/holidays/jewish.rem
/usr/share/remind/holidays/us.rem
/usr/share/remind/lang/auto.rem
%lang(da) /usr/share/remind/lang/da.rem
%lang(de) /usr/share/remind/lang/de.rem
%lang(en) /usr/share/remind/lang/en.rem
%lang(es) /usr/share/remind/lang/es.rem
%lang(fi) /usr/share/remind/lang/fi.rem
%lang(fr) /usr/share/remind/lang/fr.rem
%lang(is) /usr/share/remind/lang/is.rem
%lang(it) /usr/share/remind/lang/it.rem
%lang(nl) /usr/share/remind/lang/nl.rem
%lang(no) /usr/share/remind/lang/no.rem
%lang(pl) /usr/share/remind/lang/pl.rem
%lang(pt) /usr/share/remind/lang/pt.rem
%lang(ro) /usr/share/remind/lang/ro.rem
/usr/share/remind/site/README

%changelog
