#
# spec file for package perl-Path-FindDev
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


Name:           perl-Path-FindDev
Version:        0.5.3
Release:        0
%define cpan_name Path-FindDev
Summary:        Find a development path somewhere in an upper hierarchy
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Path-FindDev/
Source0:        https://cpan.metacpan.org/authors/id/K/KE/KENTNL/%{cpan_name}-v%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Tiny) >= 0.010
BuildRequires:  perl(Path::IsDev) >= 0.2.2
BuildRequires:  perl(Path::IsDev::Object)
BuildRequires:  perl(Path::Tiny) >= 0.054
BuildRequires:  perl(Sub::Exporter)
Requires:       perl(Class::Tiny) >= 0.010
Requires:       perl(Path::IsDev) >= 0.2.2
Requires:       perl(Path::IsDev::Object)
Requires:       perl(Path::Tiny) >= 0.054
Requires:       perl(Sub::Exporter)
Recommends:     perl(Path::Tiny) >= 0.058
%{perl_requires}

%description
This package is mostly a glue layer around 'Path::IsDev' with a few
directory walking tricks.

    use Path::FindDev qw( find_dev );

    if ( my $root = find_dev('/some/path/to/something/somewhere')) {
        print "development root = $root";
    } else {
        print "No development root :(";
    }

%prep
%setup -q -n %{cpan_name}-v%{version}

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
%doc Changes README
%license LICENSE

%changelog
