#
# spec file for package perl-HTML-Tidy
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


Name:           perl-HTML-Tidy
Version:        1.60
Release:        0
%define cpan_name HTML-Tidy
Summary:        (X)HTML validation in a Perl object
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTML-Tidy/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(Test::More) >= 0.98
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  libtidyp-devel
BuildRequires:  perl(Alien::Tidyp)
Requires:       perl(LWP::Simple)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Test::Exception)
# MANUAL END

%description
'HTML::Tidy' is an HTML checker in a handy dandy object. It's meant as a
replacement for HTML::Lint. If you're currently an HTML::Lint user looking
to migrate, see the section Converting from HTML::Lint.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README.markdown

%changelog
