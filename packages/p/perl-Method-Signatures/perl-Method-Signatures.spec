#
# spec file for package perl-Method-Signatures
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


Name:           perl-Method-Signatures
Version:        20170211
Release:        0
%define cpan_name Method-Signatures
Summary:        Method and Function Declarations with Signatures and No Source Filter
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Method-Signatures/
Source0:        http://www.cpan.org/authors/id/B/BA/BAREFOOT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Any::Moose) >= 0.11
BuildRequires:  perl(Const::Fast) >= 0.006
BuildRequires:  perl(Devel::Declare) >= 0.006002
BuildRequires:  perl(Devel::Declare::MethodInstaller::Simple) >= 0.006002
BuildRequires:  perl(Lexical::SealRequireHints) >= 0.008
BuildRequires:  perl(Module::Build) >= 0.310000
BuildRequires:  perl(Mouse) >= 0.64
BuildRequires:  perl(PPI) >= 1.203
BuildRequires:  perl(Sub::Name) >= 0.03
BuildRequires:  perl(Test::Builder) >= 0.82
BuildRequires:  perl(Test::Exception) >= 0.290000
BuildRequires:  perl(Test::More) >= 0.82
BuildRequires:  perl(Test::Warn) >= 0.10
Requires:       perl(Any::Moose) >= 0.11
Requires:       perl(Const::Fast) >= 0.006
Requires:       perl(Devel::Declare) >= 0.006002
Requires:       perl(Devel::Declare::MethodInstaller::Simple) >= 0.006002
Requires:       perl(Lexical::SealRequireHints) >= 0.008
Requires:       perl(Mouse) >= 0.64
Requires:       perl(PPI) >= 1.203
Requires:       perl(Sub::Name) >= 0.03
Recommends:     perl(Data::Alias) >= 1.08
Recommends:     perl(Moose) >= 0.96
%{perl_requires}

%description
Provides two new keywords, 'func' and 'method', so that you can write
subroutines with signatures instead of having to spell out 'my $self =
shift; my($thing) = @_'

'func' is like 'sub' but takes a signature where the prototype would
normally go. This takes the place of 'my($foo, $bar) = @_' and does a whole
lot more.

'method' is like 'func' but specifically for making methods. It will
automatically provide the invocant as '$self' (by default). No more 'my
$self = shift'.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes examples LICENSE README

%changelog
