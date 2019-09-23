#
# spec file for package perl-Mojo-IOLoop-ReadWriteProcess
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


Name:           perl-Mojo-IOLoop-ReadWriteProcess
Version:        0.23
Release:        0
%define cpan_name Mojo-IOLoop-ReadWriteProcess
Summary:        Execute external programs or internal code blocks as separate process
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Mojo-IOLoop-ReadWriteProcess/
Source0:        https://cpan.metacpan.org/authors/id/M/MU/MUDLER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.400500
BuildRequires:  perl(Mojolicious) >= 7.24
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(Mojolicious) >= 7.24
%{perl_requires}

%description
Mojo::IOLoop::ReadWriteProcess is yet another process manager.

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
%doc Changes codecov.yml minil.toml README.md
%license LICENSE

%changelog
