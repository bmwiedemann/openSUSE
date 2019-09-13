#
# spec file for package perl-HTML-Format
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


%define cpan_name HTML-Format
Name:           perl-HTML-Format
Version:        2.12
Release:        0
Summary:        Base class for HTML formatters
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTML-Format/
Source0:        http://www.cpan.org/authors/id/N/NI/NIGELM/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(Font::Metrics::Courier)
BuildRequires:  perl(Font::Metrics::CourierBold)
BuildRequires:  perl(Font::Metrics::CourierBoldOblique)
BuildRequires:  perl(Font::Metrics::CourierOblique)
BuildRequires:  perl(Font::Metrics::Helvetica)
BuildRequires:  perl(Font::Metrics::HelveticaBold)
BuildRequires:  perl(Font::Metrics::HelveticaBoldOblique)
BuildRequires:  perl(Font::Metrics::HelveticaOblique)
BuildRequires:  perl(Font::Metrics::TimesBold)
BuildRequires:  perl(Font::Metrics::TimesBoldItalic)
BuildRequires:  perl(Font::Metrics::TimesItalic)
BuildRequires:  perl(Font::Metrics::TimesRoman)
BuildRequires:  perl(HTML::Element) >= 3.15
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(Module::Build) >= 0.360100
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::NoTabs)
BuildRequires:  perl(parent)
Requires:       perl(Font::Metrics::Courier)
Requires:       perl(Font::Metrics::CourierBold)
Requires:       perl(Font::Metrics::CourierBoldOblique)
Requires:       perl(Font::Metrics::CourierOblique)
Requires:       perl(Font::Metrics::Helvetica)
Requires:       perl(Font::Metrics::HelveticaBold)
Requires:       perl(Font::Metrics::HelveticaBoldOblique)
Requires:       perl(Font::Metrics::HelveticaOblique)
Requires:       perl(Font::Metrics::TimesBold)
Requires:       perl(Font::Metrics::TimesBoldItalic)
Requires:       perl(Font::Metrics::TimesItalic)
Requires:       perl(Font::Metrics::TimesRoman)
Requires:       perl(HTML::Element) >= 3.15
Requires:       perl(HTML::TreeBuilder)
Requires:       perl(parent)
BuildArch:      noarch
%{perl_requires}

%description
Base class for HTML formatters

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%license LICENSE
%doc Changes README

%changelog
