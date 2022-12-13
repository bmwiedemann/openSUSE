#
# spec file for package perl-Mojo-IOLoop-ReadWriteProcess
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Mojo-IOLoop-ReadWriteProcess
Name:           perl-Mojo-IOLoop-ReadWriteProcess
Version:        0.33
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Execute external programs or internal code blocks as separate process
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SZ/SZARATE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IPC::SharedMem)
BuildRequires:  perl(Module::Build) >= 0.400500
BuildRequires:  perl(Mojolicious)
BuildRequires:  perl(Test::Exception)
Requires:       perl(IPC::SharedMem)
Requires:       perl(Mojolicious)
%{perl_requires}

%description
Mojo::IOLoop::ReadWriteProcess is yet another process manager.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes codecov.yml minil.toml README.md
%license LICENSE

%changelog
