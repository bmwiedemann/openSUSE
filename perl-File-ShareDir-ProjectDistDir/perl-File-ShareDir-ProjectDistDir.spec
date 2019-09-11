#
# spec file for package perl-File-ShareDir-ProjectDistDir
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


Name:           perl-File-ShareDir-ProjectDistDir
Version:        1.000009
Release:        0
%define cpan_name File-ShareDir-ProjectDistDir
Summary:        Simple set-and-forget using of a '/share' directory in your projects root
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/File-ShareDir-ProjectDistDir/
Source0:        https://cpan.metacpan.org/authors/id/K/KE/KENTNL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(Path::FindDev)
BuildRequires:  perl(Path::IsDev)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Sub::Exporter)
Requires:       perl(File::ShareDir)
Requires:       perl(Path::FindDev)
Requires:       perl(Path::IsDev)
Requires:       perl(Path::Tiny)
Requires:       perl(Sub::Exporter)
Recommends:     perl(Path::Tiny) >= 0.058
%{perl_requires}

%description
Simple set-and-forget using of a '/share' directory in your projects root

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
%doc Changes README
%license LICENSE

%changelog
