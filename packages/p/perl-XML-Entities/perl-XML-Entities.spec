# vim: set sw=3 ts=3 noet:
#
# spec file for package perl-XML-Entities
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-XML-Entities
Version:        1.0002
Release:        0
Summary:        Perl Module to decode Strings with XML Entities
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Source:         http://search.cpan.org/CPAN/authors/id/S/SI/SIXTEASE/XML-Entities-%{version}.tar.gz
Patch1:         perl-XML-Entities-local_files.patch
Source10:       http://www.w3.org/2003/entities/iso9573-2003doc/overview.html
Source11:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isobox.ent
Source12:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isocyr1.ent
Source13:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isocyr2.ent
Source14:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isodia.ent
Source15:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isolat1.ent
Source16:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isolat2.ent
Source17:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isonum.ent
Source18:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isopub.ent
Source19:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isoamsa.ent
Source20:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isoamsb.ent
Source21:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isoamsc.ent
Source22:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isoamsn.ent
Source23:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isoamso.ent
Source24:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isoamsr.ent
Source25:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isogrk1.ent
Source26:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isogrk2.ent
Source27:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isogrk3.ent
Source28:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isogrk4.ent
Source29:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isomfrk.ent
Source30:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isomopf.ent
Source31:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isomscr.ent
Source32:       http://www.w3.org/2003/entities/iso9573-2003doc/../iso9573-2003/isotech.ent
Url:            http://search.cpan.org/dist/XML-Entities/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl-libwww-perl
BuildRequires:  perl-macros

%description
This module deals with decoding of strings with XML character entities.

%prep
%setup -q -n "XML-Entities"
%__sed -i '/^auto_install/d' Makefile.PL
%__cp bin/download-entities.pl bin/download-entities.pl.orig
%patch1

%__cp -v "%{SOURCE10}" .
%__grep -E 'href.*=.*/.*\.ent.*Entity Declarations' "%{SOURCE10}" | cut -f2 -d\" \
| while read ent; do
	 ent="${ent##*/}"
	 test -f "${RPM_SOURCE_DIR}/${ent}" || { echo "missing source \"${ent}\"" >&2; exit 1; }
	 %__cp -v "${RPM_SOURCE_DIR}/${ent}" "${ent}"
done

%build
%__perl Makefile.PL PREFIX="%{_prefix}"
%__make %{?jobs:-j%{jobs}}

%install
%perl_make_install
%perl_process_packlist

%__install -m0755 bin/download-entities.pl.orig "%{buildroot}%{_bindir}/download-entities.pl"

%clean
%__rm -rf "%{buildroot}"

%files
%defattr(-,root,root)
%doc Changes README
%exclude %{_bindir}/download-entities.pl
%exclude %{_mandir}/man1/download-entities.pl.1%{ext_man}
%dir %{perl_vendorlib}/XML
%{perl_vendorlib}/XML/Entities.pm
%{perl_vendorlib}/XML/Entities
%dir %{perl_vendorarch}/auto/XML
%{perl_vendorarch}/auto/XML/Entities/
%doc %{perl_man3dir}/XML::Entities*.%{perl_man3ext}%{ext_man}
%exclude %{perl_man3dir}/download-entities.pl.%{perl_man3ext}%{ext_man}

%changelog
