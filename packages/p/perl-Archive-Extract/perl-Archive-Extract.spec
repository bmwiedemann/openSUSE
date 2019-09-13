#
# spec file for package perl-Archive-Extract
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


Name:           perl-Archive-Extract
Version:        0.80
Release:        0
%define cpan_name Archive-Extract
Summary:        Generic Archive Extracting Mechanism
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Archive-Extract/
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IPC::Cmd) >= 0.64
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Module::Load::Conditional) >= 0.66
BuildRequires:  perl(Params::Check) >= 0.07
Requires:       perl(IPC::Cmd) >= 0.64
Requires:       perl(Locale::Maketext::Simple)
Requires:       perl(Module::Load::Conditional) >= 0.66
Requires:       perl(Params::Check) >= 0.07
%{perl_requires}

%description
Archive::Extract is a generic archive extraction mechanism.

It allows you to extract any archive file of the type .tar, .tar.gz, .gz,
.Z, tar.bz2, .tbz, .bz2, .zip, .xz,, .txz, .tar.xz or .lzma without having
to worry how it does so, or use different interfaces for each type by using
either perl modules, or commandline tools on your system.

See the 'HOW IT WORKS' section further down for details.

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
%doc CHANGES README

%changelog
