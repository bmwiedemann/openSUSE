#
# spec file for package perl-HTML-Form
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name HTML-Form
Name:           perl-HTML-Form
Version:        6.11
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Class that represents an HTML form element
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SI/SIMBABQUE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(HTTP::Request) >= 6
BuildRequires:  perl(HTTP::Request::Common) >= 6.03
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(URI) >= 1.10
BuildRequires:  perl(parent)
Requires:       perl(HTML::TokeParser)
Requires:       perl(HTTP::Request) >= 6
Requires:       perl(HTTP::Request::Common) >= 6.03
Requires:       perl(Test::More) >= 0.96
Requires:       perl(URI) >= 1.10
Requires:       perl(parent)
%{perl_requires}

%description
Objects of the 'HTML::Form' class represents a single HTML '<form> ...
</form>' instance. A form consists of a sequence of inputs that usually
have names, and which can take on various values. The state of a form can
be tweaked and it can then be asked to provide HTTP::Request objects that
can be passed to the request() method of LWP::UserAgent.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes
%license LICENSE

%changelog
