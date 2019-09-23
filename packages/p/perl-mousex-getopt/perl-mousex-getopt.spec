#
# spec file for package perl-mousex-getopt
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


Name:           perl-mousex-getopt
Version:        0.37
Release:        0
%define cpan_name MouseX-Getopt
Summary:        A Mouse role for processing command line options
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source:         https://cpan.metacpan.org/authors/id/G/GF/GFUJI/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(Getopt::Long) >= 2.37
BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.091
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Mouse) >= 0.64
BuildRequires:  perl(Mouse::Meta::Attribute)
BuildRequires:  perl(Mouse::Meta::Class)
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Mouse::Util::TypeConstraints)
BuildRequires:  perl(MouseX::ConfigFromFile)
BuildRequires:  perl(MouseX::SimpleConfig)
BuildRequires:  perl(Test::Exception) >= 0.21
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Mouse)
BuildRequires:  perl(Test::Warn) >= 0.21
Requires:       perl(Getopt::Long) >= 2.37
Requires:       perl(Getopt::Long::Descriptive) >= 0.091
Requires:       perl(Mouse) >= 0.64
Requires:       perl(Mouse::Meta::Attribute)
Requires:       perl(Mouse::Role)
Requires:       perl(Mouse::Util::TypeConstraints)
# PATCH-FIX-UPSTREAM https://github.com/gfx/mousex-getopt/commit/91da15eed08ede5d7486ccc3eec9b70ae493d627
Patch1:         91da15eed08ede5d7486ccc3eec9b70ae493d627.patch
%{perl_requires}

%description
A Mouse role which provides an alternate constructor for creating objects
using parameters passed in from the command line.

%prep
%setup -q -n %{cpan_name}-%{version}
%autopatch -p1

%build
%{__perl} Build.PL --installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0 
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes cpanfile LICENSE minil.toml README.md

%changelog
