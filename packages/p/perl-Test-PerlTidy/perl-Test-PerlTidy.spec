#
# spec file for package perl-Test-PerlTidy
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Test-PerlTidy
Name:           perl-Test-PerlTidy
Version:        20230226
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Check that all your files are tidy
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.280000
BuildRequires:  perl(Path::Tiny) >= 0.100
BuildRequires:  perl(Perl::Tidy) >= 20220613
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(parent)
Requires:       perl(Path::Tiny) >= 0.100
Requires:       perl(Perl::Tidy) >= 20220613
Requires:       perl(Text::Diff)
Requires:       perl(parent)
%{perl_requires}

%description
This test submodule runs perltidy on files and reports errors if any
of the files differ after having been tidied. It does not permanently
modify the files being tested.

By default, perltidy will be run on files under the current directory
and its subdirectories with extensions matching: .pm .pl .PL .t.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
