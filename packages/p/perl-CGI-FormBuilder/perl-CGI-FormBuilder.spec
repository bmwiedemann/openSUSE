#
# spec file for package perl-CGI-FormBuilder
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-CGI-FormBuilder
Version:        3.10
Release:        0
%define cpan_name CGI-FormBuilder
Summary:        Easily generate and process stateful forms
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/CGI-FormBuilder/
Source0:        http://www.cpan.org/authors/id/B/BI/BIGPRESH/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CGI)
Requires:       perl(CGI)
Recommends:     perl(CGI::FastTemplate) >= 1.09
Recommends:     perl(CGI::SSI) >= 0.92
Recommends:     perl(CGI::Session) >= 3.95
Recommends:     perl(HTML::Template) >= 2.06
Recommends:     perl(Template) >= 2.08
Recommends:     perl(Text::Template) >= 1.43
%{perl_requires}

%description
The goal of CGI::FormBuilder (FormBuilder) is to provide an easy
way for you to generate and process entire CGI form-based
applications. Its main features are:

Field Abstraction
  Viewing fields as entities (instead of just params), where the
  HTML representation, CGI values, validation, and so on are
  properties of each field.

DWIMmery
  Lots of built-in "intelligence" (such as automatic field typing),
  giving you about a 4:1 ratio of the code it generates versus what
  you have to write.

Built-in Validation
  Full-blown regex validation for fields, even including
  JavaScript code generation.

Template Support
 Pluggable support for external template engines,
  such as HTML::Template, Text::Template, Template Toolkit,
  and CGI::FastTemplate.

Plus, the native HTML generated is valid XHTML 1.0 Transitional.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
