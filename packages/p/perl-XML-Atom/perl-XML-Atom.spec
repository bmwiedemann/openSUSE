#
# spec file for package perl-XML-Atom
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name XML-Atom
Name:           perl-XML-Atom
Version:        0.43
Release:        0
Summary:        Atom feed and API implementation
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(URI)
BuildRequires:  perl(XML::LibXML) >= 2.0202
BuildRequires:  perl(XML::XPath) >= 1.20
Requires:       perl(Class::Data::Inheritable)
Requires:       perl(DateTime)
Requires:       perl(DateTime::TimeZone)
Requires:       perl(Digest::SHA)
Requires:       perl(LWP::UserAgent)
Requires:       perl(URI)
Requires:       perl(XML::LibXML) >= 2.0202
Requires:       perl(XML::XPath) >= 1.20
%{perl_requires}

%description
Atom is a syndication, API, and archiving format for weblogs and other
data. _XML::Atom_ implements the feed format as well as a client for the
API.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
