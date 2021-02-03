#
# spec file for package perl-HTML-Restrict
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


Name:           perl-HTML-Restrict
Version:        3.0.0
Release:        0
%define cpan_name HTML-Restrict
Summary:        Strip unwanted HTML tags and attributes
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{cpan_name}-v%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Moo) >= 1.002000
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Type::Tiny) >= 1.002001
BuildRequires:  perl(Types::Standard) >= 1.000001
BuildRequires:  perl(URI)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(version)
Requires:       perl(Data::Dump)
Requires:       perl(HTML::Entities)
Requires:       perl(HTML::Parser)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Moo) >= 1.002000
Requires:       perl(Sub::Quote)
Requires:       perl(Type::Tiny) >= 1.002001
Requires:       perl(Types::Standard) >= 1.000001
Requires:       perl(URI)
Requires:       perl(namespace::clean)
Requires:       perl(version)
%{perl_requires}

%description
This module uses HTML::Parser to strip HTML from text in a restrictive
manner. By default all HTML is restricted. You may alter the default
behaviour by supplying your own tag rules.

%prep
%setup -q -n %{cpan_name}-v%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes CONTRIBUTORS examples README.md
%license LICENSE

%changelog
