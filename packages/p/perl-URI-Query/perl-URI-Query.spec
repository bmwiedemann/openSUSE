#
# spec file for package perl-URI-Query
#
# Copyright (c) 2021 SUSE LLC
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


Name:           perl-URI-Query
Version:        0.16
Release:        0
%define cpan_name URI-Query
Summary:        Class providing URI query string manipulation
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GAVINC/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Clone)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(YAML)
BuildRequires:  perl(parent)
Requires:       perl(Clone)
Requires:       perl(URI::Escape)
Requires:       perl(parent)
%{perl_requires}

%description
URI::Query provides simple URI query string manipulation, allowing you to
create and manipulate URI query strings from GET and POST requests in web
applications. This is primarily useful for creating links where you wish to
preserve some subset of the parameters to the current request, and
potentially add or replace others. Given a query string this is doable with
regexes, of course, but making sure you get the anchoring and escaping
right is tedious and error-prone - this module is simpler.

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
%doc ChangeLog README TODO
%license LICENSE

%changelog
