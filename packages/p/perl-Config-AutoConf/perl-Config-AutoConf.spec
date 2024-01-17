#
# spec file for package perl-Config-AutoConf
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


%define cpan_name Config-AutoConf
Name:           perl-Config-AutoConf
Version:        0.320
Release:        0
Summary:        Module to implement some of AutoConf macros in pure perl
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AM/AMBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.23
BuildRequires:  perl(Test::More) >= 0.9
Requires:       perl(Capture::Tiny)
Recommends:     perl(ExtUtils::CBuilder) >= 0.280220
Recommends:     perl(File::Slurper)
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
%autosetup  -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md testTc852_
%license ARTISTIC-1.0 GPL-1 LICENSE

%changelog
