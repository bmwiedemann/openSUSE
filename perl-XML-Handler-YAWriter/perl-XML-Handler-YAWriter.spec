#
# spec file for package perl-XML-Handler-YAWriter
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-XML-Handler-YAWriter
Version:        0.23
Release:        0
%define cpan_name XML-Handler-YAWriter
Summary:        Yet another Perl SAX XML Writer
License:        GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/XML-Handler-YAWriter/
Source:         http://www.cpan.org/authors/id/K/KR/KRAEHE/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(XML::Parser::PerlSAX) >= 0.06
#BuildRequires: perl(XML::Handler::YAWriter)
Requires:       perl(XML::Parser::PerlSAX) >= 0.06
%{perl_requires}

%description
YAWriter implements Yet Another XML::Handler::Writer. The reasons for this
one are that I needed a flexible escaping technique, and want some kind of
pretty printing. If an instance of YAWriter is created without any options,
the default behavior is to produce an array of strings containing the XML
in :

  @{$ya->{Strings}}

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc action.xml cdatain.xml Changes directory.xml edifact03.dtd linux.1.xml nullin.xml README xmlpretty

%changelog
