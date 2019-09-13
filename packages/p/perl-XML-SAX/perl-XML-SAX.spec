#
# spec file for package perl-XML-SAX
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           perl-XML-SAX
Version:        1.02
Release:        0
%define cpan_name XML-SAX
Summary:        Simple API for XML
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/XML-SAX
Source0:        https://cpan.metacpan.org/authors/id/G/GR/GRANTM/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         perl-XML-SAX-0.96-utf8.diff
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(XML::NamespaceSupport) >= 0.03
BuildRequires:  perl(XML::SAX::Base) >= 1.05
Requires:       perl(XML::NamespaceSupport) >= 0.03
Requires:       perl(XML::SAX::Base) >= 1.05
%{perl_requires}

%description
XML::SAX is a SAX parser access API for Perl. It includes classes and APIs
required for implementing SAX drivers, along with a factory class for
returning any SAX parser installed on the user's system.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
# MANUAL
touch %{buildroot}%{perl_vendorlib}/XML/SAX/ParserDetails.ini
echo "%ghost %{perl_vendorlib}/XML/SAX/ParserDetails.ini" >> perl-XML-SAX.files
# MANUAL/
%perl_process_packlist
%perl_gen_filelist

# MANUAL BEGIN
%post
perl -MXML::SAX -e "XML::SAX->add_parser(q(XML::SAX::PurePerl))->save_parsers()"
# MANUAL END

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
