#
# spec file for package perl-JSON
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


Name:           perl-JSON
Version:        4.02
Release:        0
%define cpan_name JSON
Summary:        JSON (JavaScript Object Notation) encoder/decoder
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
Recommends:     perl(JSON::XS) >= 2.34
%{perl_requires}

%description
This module is a thin wrapper for JSON::XS-compatible modules with a few
additional features. All the backend modules convert a Perl data structure
to a JSON text and vice versa. This module uses JSON::XS by default, and
when JSON::XS is not available, falls back on JSON::PP, which is in the
Perl core since 5.14. If JSON::PP is not available either, this module then
falls back on JSON::backportPP (which is actually JSON::PP in a different
.pm file) bundled in the same distribution as this module. You can also
explicitly specify to use Cpanel::JSON::XS, a fork of JSON::XS by Reini
Urban.

All these backend modules have slight incompatibilities between them,
including extra features that other modules don't support, but as long as
you use only common features (most important ones are described below),
migration from backend to backend should be reasonably easy. For details,
see each backend module you use.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes README

%changelog
