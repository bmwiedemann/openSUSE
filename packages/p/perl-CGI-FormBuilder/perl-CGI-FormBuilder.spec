#
# spec file for package perl-CGI-FormBuilder
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


%define cpan_name CGI-FormBuilder
Name:           perl-CGI-FormBuilder
Version:        3.200.0
Release:        0
# 3.20 -> normalize -> 3.200.0
%define cpan_version 3.20
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Easily generate and process stateful forms
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BIGPRESH/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CGI)
Requires:       perl(CGI)
Provides:       perl(CGI::FormBuilder) = %{version}
Provides:       perl(CGI::FormBuilder::Field) = %{version}
Provides:       perl(CGI::FormBuilder::Field::button) = %{version}
Provides:       perl(CGI::FormBuilder::Field::checkbox) = %{version}
Provides:       perl(CGI::FormBuilder::Field::date) = %{version}
Provides:       perl(CGI::FormBuilder::Field::datetime) = %{version}
Provides:       perl(CGI::FormBuilder::Field::datetime_local) = %{version}
Provides:       perl(CGI::FormBuilder::Field::email) = %{version}
Provides:       perl(CGI::FormBuilder::Field::file) = %{version}
Provides:       perl(CGI::FormBuilder::Field::hidden) = %{version}
Provides:       perl(CGI::FormBuilder::Field::image) = %{version}
Provides:       perl(CGI::FormBuilder::Field::number) = %{version}
Provides:       perl(CGI::FormBuilder::Field::password) = %{version}
Provides:       perl(CGI::FormBuilder::Field::radio) = %{version}
Provides:       perl(CGI::FormBuilder::Field::select) = %{version}
Provides:       perl(CGI::FormBuilder::Field::static) = %{version}
Provides:       perl(CGI::FormBuilder::Field::submit) = %{version}
Provides:       perl(CGI::FormBuilder::Field::text) = %{version}
Provides:       perl(CGI::FormBuilder::Field::textarea) = %{version}
Provides:       perl(CGI::FormBuilder::Field::time) = %{version}
Provides:       perl(CGI::FormBuilder::Field::url) = %{version}
Provides:       perl(CGI::FormBuilder::Messages) = %{version}
Provides:       perl(CGI::FormBuilder::Messages::base) = %{version}
Provides:       perl(CGI::FormBuilder::Messages::default) = %{version}
Provides:       perl(CGI::FormBuilder::Messages::locale) = %{version}
Provides:       perl(CGI::FormBuilder::Multi) = %{version}
Provides:       perl(CGI::FormBuilder::Source) = %{version}
Provides:       perl(CGI::FormBuilder::Source::File) = %{version}
Provides:       perl(CGI::FormBuilder::Template) = %{version}
Provides:       perl(CGI::FormBuilder::Template::Builtin) = %{version}
Provides:       perl(CGI::FormBuilder::Template::CGI_SSI) = %{version}
Provides:       perl(CGI::FormBuilder::Template::Div) = %{version}
Provides:       perl(CGI::FormBuilder::Template::Fast) = %{version}
Provides:       perl(CGI::FormBuilder::Template::HTML) = %{version}
Provides:       perl(CGI::FormBuilder::Template::TT2) = %{version}
Provides:       perl(CGI::FormBuilder::Template::Text) = %{version}
Provides:       perl(CGI::FormBuilder::Test) = %{version}
Provides:       perl(CGI::FormBuilder::Util) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
Recommends:     perl(CGI::FastTemplate) >= 1.09
Recommends:     perl(CGI::SSI) >= 0.92
Recommends:     perl(CGI::Session) >= 3.95
Recommends:     perl(HTML::Template) >= 2.06
Recommends:     perl(Template) >= 2.08
Recommends:     perl(Text::Template) >= 1.43
# MANUAL END

%description
If this is your first time using *FormBuilder*, you should check out the
website for tutorials and examples at http://formbuilder.org.

You should also consider joining the google group at
http://groups.google.com/group/perl-formbuilder. There are some pretty
smart people on the list that can help you out.

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
%doc Changes README

%changelog
