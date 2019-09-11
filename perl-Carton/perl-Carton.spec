#
# spec file for package perl-Carton
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Carton
Version:        1.0.28
Release:        0
%define cpan_name Carton
Summary:        Perl module dependency manager (aka Bundler for Perl)
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Carton/
Source0:        http://www.cpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-v%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(App::cpanminus) >= 1.703
BuildRequires:  perl(CPAN::Meta) >= 2.120921
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121000
BuildRequires:  perl(Class::Tiny) >= 1.001
BuildRequires:  perl(Getopt::Long) >= 2.39
BuildRequires:  perl(JSON) >= 2.53
BuildRequires:  perl(Module::CPANfile) >= 0.9031
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Metadata) >= 1.000003
BuildRequires:  perl(Module::Reader) >= 0.002
BuildRequires:  perl(Path::Tiny) >= 0.033
BuildRequires:  perl(Try::Tiny) >= 0.09
BuildRequires:  perl(parent) >= 0.223
BuildRequires:  perl(version) >= 0.77
Requires:       perl(App::cpanminus) >= 1.703
Requires:       perl(CPAN::Meta) >= 2.120921
Requires:       perl(CPAN::Meta::Requirements) >= 2.121000
Requires:       perl(Class::Tiny) >= 1.001
Requires:       perl(Getopt::Long) >= 2.39
Requires:       perl(JSON) >= 2.53
Requires:       perl(Module::CPANfile) >= 0.9031
Requires:       perl(Module::CoreList)
Requires:       perl(Module::Metadata) >= 1.000003
Requires:       perl(Module::Reader) >= 0.002
Requires:       perl(Path::Tiny) >= 0.033
Requires:       perl(Try::Tiny) >= 0.09
Requires:       perl(parent) >= 0.223
Recommends:     perl(App::FatPacker) >= 0.009018
Recommends:     perl(File::pushd)
%{perl_requires}

%description
carton is a command line tool to track the Perl module dependencies for
your Perl application. Dependencies are declared using cpanfile format, and
the managed dependencies are tracked in a _cpanfile.snapshot_ file, which
is meant to be version controlled, and the snapshot file allows other
developers of your application will have the exact same versions of the
modules.

For 'cpanfile' syntax, see cpanfile documentation.

%prep
%setup -q -n %{cpan_name}-v%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes LICENSE README

%changelog
