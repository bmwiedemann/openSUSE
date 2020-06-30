#
# spec file for package perl-File-Map
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


Name:           perl-File-Map
Version:        0.67
Release:        0
%define cpan_name File-Map
Summary:        Memory mapping made simple and safe
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.280000
BuildRequires:  perl(PerlIO::Layers)
BuildRequires:  perl(Sub::Exporter::Progressive) >= 0.001005
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Warnings) >= 0.005
Requires:       perl(PerlIO::Layers)
Requires:       perl(Sub::Exporter::Progressive) >= 0.001005
%{perl_requires}

%description
File::Map maps files or anonymous memory into perl variables.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor optimize="%{optflags}"
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples metamerge.yml README
%license LICENSE

%changelog
