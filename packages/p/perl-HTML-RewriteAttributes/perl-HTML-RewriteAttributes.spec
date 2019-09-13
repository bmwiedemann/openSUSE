#
# spec file for package perl-HTML-RewriteAttributes
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


Name:           perl-HTML-RewriteAttributes
Version:        0.05
Release:        0
%define cpan_name HTML-RewriteAttributes
Summary:        Concise Attribute Rewriting
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTML-RewriteAttributes/
Source0:        https://cpan.metacpan.org/authors/id/T/TS/TSIBLEY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(URI)
Requires:       perl(HTML::Entities)
Requires:       perl(HTML::Parser)
Requires:       perl(HTML::Tagset)
Requires:       perl(URI)
%{perl_requires}

%description
'HTML::RewriteAttributes' is designed for simple yet powerful HTML
attribute rewriting.

You simply specify a callback to run for each attribute and we do the rest
for you.

This module is designed to be subclassable to make handling special cases
eaiser. See the source for methods you can override.

%prep
%setup -q -n %{cpan_name}-%{version}
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

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
%doc Changes README

%changelog
