#
# spec file for package perl-Web-Scraper
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


%define cpan_name Web-Scraper
Name:           perl-Web-Scraper
Version:        0.38
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Web Scraping Toolkit using HTML and CSS Selectors or XPath expressions
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Selector::XPath) >= 0.03
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(HTML::TreeBuilder) >= 3.23
BuildRequires:  perl(HTML::TreeBuilder::XPath) >= 0.08
BuildRequires:  perl(LWP) >= 5.827
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(Test::Base)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(URI)
BuildRequires:  perl(XML::XPathEngine) >= 0.08
BuildRequires:  perl(YAML)
Requires:       perl(HTML::Entities)
Requires:       perl(HTML::Selector::XPath) >= 0.03
Requires:       perl(HTML::Tagset)
Requires:       perl(HTML::TreeBuilder) >= 3.23
Requires:       perl(HTML::TreeBuilder::XPath) >= 0.08
Requires:       perl(LWP) >= 5.827
Requires:       perl(UNIVERSAL::require)
Requires:       perl(URI)
Requires:       perl(XML::XPathEngine) >= 0.08
Requires:       perl(YAML)
%{perl_requires}

%description
Web::Scraper is a web scraper toolkit, inspired by Ruby's equivalent
Scrapi. It provides a DSL-ish interface for traversing HTML documents and
returning a neatly arranged Perl data structure.

The _scraper_ and _process_ blocks provide a method to define what segments
of a document to extract. It understands HTML and CSS Selectors as well as
XPath expressions.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
