#
# spec file for package perl-Capture-Tiny
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


Name:           perl-Capture-Tiny
Version:        0.48
Release:        0
%define cpan_name Capture-Tiny
Summary:        Capture STDOUT and STDERR from Perl, XS or external programs
License:        Apache-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Capture-Tiny/
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Capture::Tiny provides a simple, portable way to capture almost anything
sent to STDOUT or STDERR, regardless of whether it comes from Perl, from XS
code or from an external program. Optionally, output can be teed so that it
is captured while being passed through to the original filehandles. Yes, it
even works on Windows (usually). Stop guessing which of a dozen capturing
modules to use in any particular situation and just use this one.

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
%doc Changes CONTRIBUTING.mkdn examples README Todo
%license LICENSE

%changelog
