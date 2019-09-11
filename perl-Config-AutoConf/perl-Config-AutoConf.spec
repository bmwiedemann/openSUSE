#
# spec file for package perl-Config-AutoConf
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


Name:           perl-Config-AutoConf
Version:        0.317
Release:        0
%define cpan_name Config-AutoConf
Summary:        Module to Implement Some of Autoconf Macros in Pure Perl
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Config-AutoConf/
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.23
BuildRequires:  perl(Test::More) >= 0.9
Requires:       perl(Capture::Tiny)
Recommends:     perl(ExtUtils::CBuilder) >= 0.280220
Recommends:     perl(File::Slurp::Tiny)
%{perl_requires}

%description
Config::AutoConf is intended to provide the same opportunities to Perl
developers as at http://www.gnu.org/software/autoconf/ does for Shell
developers.

As Perl is the second most deployed language (mind: every Unix comes with
Perl, several mini-computers have Perl and even lot's of Windows machines
run Perl software - which requires deployed Perl there, too), this gives
wider support than Shell based probes.

The API is leaned against GNU Autoconf, but we try to make the API
(especially optional arguments) more Perl'ish than m4 abilities allow to
the original.

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
%doc Changes GPL-1 README.md
%license ARTISTIC-1.0 LICENSE

%changelog
