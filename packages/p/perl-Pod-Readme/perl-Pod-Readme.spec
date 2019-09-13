#
# spec file for package perl-Pod-Readme
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


Name:           perl-Pod-Readme
Version:        1.2.3
Release:        0
%define cpan_name Pod-Readme
Summary:        Intelligently generate a README file from POD
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRWO/%{cpan_name}-v%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Changes) >= 0.30
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(Getopt::Long::Descriptive)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::HandlesVia)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Pod::Simple::Text)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Kit)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Tiny) >= 1.000000
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(CPAN::Changes) >= 0.30
Requires:       perl(CPAN::Meta)
Requires:       perl(Class::Method::Modifiers)
Requires:       perl(File::Slurp)
Requires:       perl(Getopt::Long::Descriptive)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Module::CoreList)
Requires:       perl(Moo)
Requires:       perl(Moo::Role)
Requires:       perl(MooX::HandlesVia)
Requires:       perl(Path::Tiny)
Requires:       perl(Pod::Simple)
Requires:       perl(Role::Tiny)
Requires:       perl(Try::Tiny)
Requires:       perl(Type::Tiny) >= 1.000000
Requires:       perl(Types::Standard)
Requires:       perl(namespace::autoclean)
Recommends:     perl(Pod::Markdown)
Recommends:     perl(Pod::Markdown::Github)
Recommends:     perl(Pod::Simple::HTML)
Recommends:     perl(Pod::Simple::LaTeX)
Recommends:     perl(Pod::Simple::RTF)
Recommends:     perl(Pod::Simple::Text)
Recommends:     perl(Pod::Simple::XHTML)
Recommends:     perl(Type::Tiny::XS)
%{perl_requires}

%description
This module filters POD to generate a _README_ file, by using POD commands
to specify which parts are included or excluded from the _README_ file.

%prep
%setup -q -n %{cpan_name}-v%{version}
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

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
%doc Changes
%license LICENSE

%changelog
