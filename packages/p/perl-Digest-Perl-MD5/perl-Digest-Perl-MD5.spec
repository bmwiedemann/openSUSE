#
# spec file for package perl-Digest-Perl-MD5
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Digest-Perl-MD5
Name:           perl-Digest-Perl-MD5
Version:        1.900.0
Release:        0
# 1.9 -> normalize -> 1.900.0
%define cpan_version 1.9
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl Implementation of Rivest's MD5 algorithm
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DE/DELTA/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Digest::Perl::MD5) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This modules has the same interface as the much faster 'Digest::MD5'. So
you can easily exchange them, e.g.

	BEGIN {
	  eval {
	    require Digest::MD5;
	    import Digest::MD5 'md5_hex'
	  };
	  if ($@) { # ups, no Digest::MD5
	    require Digest::Perl::MD5;
	    import Digest::Perl::MD5 'md5_hex'
	  }
	}

If the 'Digest::MD5' module is available it is used and if not you take
'Digest::Perl::MD5'.

You can also install the Perl part of Digest::MD5 together with
Digest::Perl::MD5 and use Digest::MD5 as normal, it falls back to
Digest::Perl::MD5 if it cannot load its object files.

For a detailed Documentation see the 'Digest::MD5' module.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CHANGES rand.f

%changelog
