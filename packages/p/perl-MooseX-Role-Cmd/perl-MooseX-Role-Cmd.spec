#
# spec file for package perl-MooseX-Role-Cmd
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


Name:           perl-MooseX-Role-Cmd
Version:        0.10
Release:        0
%define cpan_name MooseX-Role-Cmd
Summary:        Wrap system command binaries the Moose way
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Role-Cmd/
Source0:        https://cpan.metacpan.org/authors/id/E/ED/EDENC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IPC::Cmd) >= 0.42
BuildRequires:  perl(Moose) >= 0.6
BuildRequires:  perl(Test::Exception)
Requires:       perl(IPC::Cmd) >= 0.42
Requires:       perl(Moose) >= 0.6
%{perl_requires}

%description
MooseX::Role::Cmd is a Moose role intended to ease the task of building
command-line wrapper modules. It automatically maps Moose objects into
command strings which are passed to IPC::Cmd.

%prep
%setup -q -n %{cpan_name}-%{version}
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

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

%changelog
