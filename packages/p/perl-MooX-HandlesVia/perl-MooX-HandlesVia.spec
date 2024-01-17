#
# spec file for package perl-MooX-HandlesVia
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-MooX-HandlesVia
Version:        0.001009
Release:        0
%define cpan_name MooX-HandlesVia
Summary:        NativeTrait-like behavior for Moo
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Data::Perl) >= 0.002006
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 1.003000
BuildRequires:  perl(MooX::Types::MooseLike::Base) >= 0.23
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
Requires:       perl(Class::Method::Modifiers)
Requires:       perl(Data::Perl) >= 0.002006
Requires:       perl(Module::Runtime)
Requires:       perl(Moo) >= 1.003000
Requires:       perl(Role::Tiny)
%{perl_requires}

%description
MooX::HandlesVia is an extension of Moo's 'handles' attribute
functionality. It provides a means of proxying functionality from an
external class to the given atttribute. This is most commonly used as a way
to emulate 'Native Trait' behavior that has become commonplace in Moose
code, for which there was no Moo alternative.

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
%doc Changes README.mkdn TODO
%license LICENSE

%changelog
