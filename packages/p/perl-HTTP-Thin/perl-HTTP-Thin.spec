#
# spec file for package perl-HTTP-Thin
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


%define cpan_name HTTP-Thin
Name:           perl-HTTP-Thin
Version:        0.6.0
Release:        0
# 0.006 -> normalize -> 0.6.0
%define cpan_version 0.006
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Thin Wrapper around HTTP::Tiny to play nice with HTTP::Message
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERIGRIN/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(Hash::MultiValue)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(parent)
Requires:       perl(Class::Method::Modifiers)
Requires:       perl(HTTP::Response)
Requires:       perl(HTTP::Tiny)
Requires:       perl(Hash::MultiValue)
Requires:       perl(Safe::Isa)
Requires:       perl(parent)
Provides:       perl(HTTP::Thin) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
WARNING: This module is untested beyond the very basics. The implementation
is simple enough that it shouldn't do evil things but, yeah it's still not
approved for use by small children.

'HTTP::Thin' is a thin wrapper around HTTP::Tiny adding the ability to pass
in HTTP::Request objects and get back HTTP::Response objects. The
maintainers of HTTP::Tiny, justifiably, don't want to have to maintain
compatibility but many other projects already consume the HTTP::Message
objects. This is just glue code doing what it does best.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc CHANGES README
%license LICENSE

%changelog
