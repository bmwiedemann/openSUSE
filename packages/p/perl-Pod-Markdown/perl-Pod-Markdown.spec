#
# spec file for package perl-Pod-Markdown
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


Name:           perl-Pod-Markdown
Version:        3.300
Release:        0
%define cpan_name Pod-Markdown
Summary:        Convert POD to Markdown
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RW/RWSTAUNER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Pod::Simple) >= 3.27
BuildRequires:  perl(Pod::Simple::Methody)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(parent)
Requires:       perl(Pod::Simple) >= 3.27
Requires:       perl(Pod::Simple::Methody)
Requires:       perl(URI::Escape)
Requires:       perl(parent)
Recommends:     perl(HTML::Entities)
%{perl_requires}

%description
This module uses Pod::Simple to convert POD to Markdown.

Literal characters in Pod that are special in Markdown (like *asterisks*)
are backslash-escaped when appropriate.

By default 'markdown' and 'html' formatted regions are accepted. Regions of
'markdown' will be passed through unchanged. Regions of 'html' will be
placed inside a '<div>' tag so that markdown characters won't be processed.
Regions of ':markdown' or ':html' will be processed as POD and included. To
change which regions are accepted use the Pod::Simple API:

  my $parser = Pod::Markdown->new;
  $parser->unaccept_targets(qw( markdown html ));

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
