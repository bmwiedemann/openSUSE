#
# spec file for package perl-constant-boolean
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           perl-constant-boolean
Version:        0.02
Release:        0
%define cpan_name constant-boolean
Summary:        Define TRUE and FALSE constants.
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/constant-boolean/
Source:         http://www.cpan.org/authors/id/D/DE/DEXTER/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Symbol::Util) >= 0.02
#BuildRequires: perl(File::Slurp)
#BuildRequires: perl(Readonly)
#BuildRequires: perl(Test::CheckChanges)
#BuildRequires: perl(Test::Distribution)
#BuildRequires: perl(Test::Kwalitee)
#BuildRequires: perl(Test::Perl::Critic)
#BuildRequires: perl(Test::Signature)
#BuildRequires: perl(Test::Spelling)
Requires:       perl(Symbol::Util) >= 0.02
%{perl_requires}

%description
Defines 'TRUE' and 'FALSE' constants in caller's namespace. You could use
simple values like empty string or zero for false, or any non-empty and
non-zero string value as true, but the 'TRUE' and 'FALSE' constants are
more descriptive.

It is virtually the same as:

  # double "not" operator is used for converting scalar to boolean value
  use constant TRUE => !! 1;
  use constant FALSE => !! '';

The constants exported by 'constant::boolean' are not reported by the
Test::Pod::Coverage manpage, so it is more convenient to use this module
than to define 'TRUE' and 'FALSE' constants by yourself.

The constants can be removed from class API with 'no constant::boolean'
pragma or some universal tool like the namespace::clean manpage.

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
%doc Changes LICENSE README xt

%changelog
