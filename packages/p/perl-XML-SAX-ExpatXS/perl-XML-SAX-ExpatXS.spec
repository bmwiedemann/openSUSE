#
# spec file for package perl-XML-SAX-ExpatXS
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


Name:           perl-XML-SAX-ExpatXS
%define cpan_name XML-SAX-ExpatXS
Summary:        Perl SAX 2 XS extension to Expat parser
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Version:        1.33
Release:        0
Url:            http://www.cpan.org/dist/XML-SAX-ExpatXS
Source0:        %{cpan_name}-%{version}.tar.gz
Patch:          %{cpan_name}-1.31-obs.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires:  perl(Module::Build)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(XML::SAX) >= 0.13
#BuildRequires:  perl(XML::SAX::ExpatXS)
%if 0%{?suse_version} > 1010
BuildRequires:  libexpat-devel
%else
BuildRequires:  expat
%endif
#
Requires:       expat
Requires:       perl(XML::SAX) >= 0.13

%description
XML::SAX::ExpatXS is a direct XS extension to Expat XML parser. It implements
 Perl SAX 2.1 interface. See http://perl-xml.sourceforge.net/perl-sax/ for
 Perl SAX API description. Any deviations from the Perl SAX 2.1 specification
 are considered as bugs.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch -p1

%build
perl Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS -Wall"
%{__make}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%post
perl -MXML::SAX -e "XML::SAX->add_parser(q(XML::SAX::ExpatXS))->save_parsers()"

%files -f %{name}.files
%defattr(-,root,root)
%doc Changes README

%changelog
