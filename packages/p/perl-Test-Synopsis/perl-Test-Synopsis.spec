#
# spec file for package perl-Test-Synopsis
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


Name:           perl-Test-Synopsis
Version:        0.16
Release:        0
%define cpan_name Test-Synopsis
Summary:        Test your SYNOPSIS code
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/Z/ZO/ZOFFIX/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Pod::Simple) >= 3.09
BuildRequires:  perl(Test::Builder) >= 0.34
BuildRequires:  perl(parent)
Requires:       perl(Pod::Simple) >= 3.09
Requires:       perl(parent)
%{perl_requires}

%description
Test::Synopsis is an (author) test module to find .pm or .pod files under
your _lib_ directory and then make sure the example snippet code in your
_SYNOPSIS_ section passes the perl compile check.

Note that this module only checks the perl syntax (by wrapping the code
with 'sub') and doesn't actually run the code, *UNLESS* that code is a
'BEGIN {}' block or a 'use' statement.

Suppose you have the following POD in your module.

  =head1 NAME

  Awesome::Template - My awesome template

  =head1 SYNOPSIS

    use Awesome::Template;

    my $template = Awesome::Template->new;
    $tempalte->render("template.at");

  =head1 DESCRIPTION

An user of your module would try copy-paste this synopsis code and find
that this code doesn't compile because there's a typo in your variable name
_$tempalte_. Test::Synopsis will catch that error before you ship it.

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
%doc Changes README README.md
%license LICENSE

%changelog
