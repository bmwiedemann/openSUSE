#
# spec file for package perl-MIME-Lite
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name MIME-Lite
Name:           perl-MIME-Lite
Version:        3.38.0
Release:        0
# 3.038 -> normalize -> 3.38.0
%define cpan_version 3.038
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Low-calorie MIME generator
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Email::Date::Format) >= 1.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Email::Date::Format) >= 1.0
Provides:       perl(MIME::Lite) = %{version}
Provides:       perl(MIME::Lite::IO_Handle) = %{version}
Provides:       perl(MIME::Lite::IO_Scalar) = %{version}
Provides:       perl(MIME::Lite::IO_ScalarArray) = %{version}
Provides:       perl(MIME::Lite::SMTP) = %{version}
%undefine       __perllib_provides
Recommends:     perl(MIME::Types) >= 1.280
Recommends:     perl(Mail::Address) >= 1.620
%{perl_requires}

%description
In the never-ending quest for great taste with fewer calories, we proudly
present: _MIME::Lite_.

MIME::Lite is intended as a simple, standalone module for generating (not
parsing!) MIME messages... specifically, it allows you to output a simple,
decent single- or multi-part message with text or binary attachments. It
does not require that you have the Mail:: or MIME:: modules installed, but
will work with them if they are.

You can specify each message part as either the literal data itself (in a
scalar or array), or as a string which can be given to open() to get a
readable filehandle (e.g., "<filename" or "somecommand|").

You don't need to worry about encoding your message data: this module will
do that for you. It handles the 5 standard MIME encodings.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes examples README
%license LICENSE

%changelog
