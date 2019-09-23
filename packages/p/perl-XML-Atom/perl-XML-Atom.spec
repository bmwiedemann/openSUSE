#
# spec file for package perl-XML-Atom
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


Name:           perl-XML-Atom
Version:        0.42
Release:        0
%define cpan_name XML-Atom
Summary:        Atom feed and API implementation
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/XML-Atom/
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
# Patch-Fix-UPSTREAM https://github.com/miyagawa/xml-atom/issues/12
Patch1:         d2c045a8ca0d0ca147b04bc9e7c70b27db8cc4e1.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(URI)
BuildRequires:  perl(XML::LibXML) >= 1.69
BuildRequires:  perl(XML::XPath)
Requires:       perl(Class::Data::Inheritable)
Requires:       perl(DateTime)
Requires:       perl(DateTime::TimeZone)
Requires:       perl(Digest::SHA1)
Requires:       perl(LWP::UserAgent)
Requires:       perl(URI)
Requires:       perl(XML::LibXML) >= 1.69
Requires:       perl(XML::XPath)
%{perl_requires}

%description
Atom is a syndication, API, and archiving format for weblogs and other
data. _XML::Atom_ implements the feed format as well as a client for the
API.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch1 -p1

%build
%{__perl} Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
