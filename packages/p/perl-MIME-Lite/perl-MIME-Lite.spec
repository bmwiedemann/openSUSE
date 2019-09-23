#
# spec file for package perl-MIME-Lite
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-MIME-Lite
Version:        3.030
Release:        0
%define cpan_name MIME-Lite
Summary:        low-calorie MIME generator
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MIME-Lite/
Source:         http://www.cpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Email::Date::Format) >= 1.000
#BuildRequires: perl(ExtUtils::TBone)
#BuildRequires: perl(Mail::Address)
#BuildRequires: perl(MIME::Lite)
#BuildRequires: perl(MIME::Types) >= 1.28
#BuildRequires: perl(Utils)
Requires:       perl(Email::Date::Format) >= 1.000
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
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

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
%doc COPYING examples INSTALLING LICENSE README

%changelog
