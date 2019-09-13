#
# spec file for package perl-HTML-Scrubber
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-HTML-Scrubber
Version:        0.15
Release:        0
%define cpan_name HTML-Scrubber
Summary:        Perl extension for scrubbing/sanitizing html
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTML-Scrubber/
Source0:        http://www.cpan.org/authors/id/N/NI/NIGELM/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser) >= 3.47
BuildRequires:  perl(Module::Build) >= 0.280000
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::NoTabs)
Requires:       perl(HTML::Entities)
Requires:       perl(HTML::Parser) >= 3.47
%{perl_requires}

%description
If you want to "scrub" or "sanitize" html input in a reliable and flexible
fashion, then this module is for you.

I wasn't satisfied with HTML::Sanitizer because it is based on
HTML::TreeBuilder, so I thought I'd write something similar that works
directly with HTML::Parser.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README

%changelog
