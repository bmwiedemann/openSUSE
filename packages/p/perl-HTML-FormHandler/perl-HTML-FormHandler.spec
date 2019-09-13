#
# spec file for package perl-HTML-FormHandler
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


Name:           perl-HTML-FormHandler
Version:        0.40068
Release:        0
%define cpan_name HTML-FormHandler
Summary:        HTML forms using Moose
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTML-FormHandler/
Source0:        https://cpan.metacpan.org/authors/id/G/GS/GSHANK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Load) >= 0.06
BuildRequires:  perl(Crypt::Blowfish)
BuildRequires:  perl(Crypt::CBC)
BuildRequires:  perl(Data::Clone)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(Email::Valid)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::TreeBuilder) >= 3.23
BuildRequires:  perl(JSON::MaybeXS) >= 1.003003
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Moose) >= 2.1403
BuildRequires:  perl(MooseX::Getopt) >= 0.16
BuildRequires:  perl(MooseX::Types) >= 0.20
BuildRequires:  perl(MooseX::Types::Common)
BuildRequires:  perl(MooseX::Types::LoadableClass) >= 0.006
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Memory::Cycle) >= 1.04
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(aliased)
BuildRequires:  perl(namespace::autoclean) >= 0.09
Requires:       perl(Class::Load) >= 0.06
Requires:       perl(Crypt::Blowfish)
Requires:       perl(Crypt::CBC)
Requires:       perl(Data::Clone)
Requires:       perl(DateTime)
Requires:       perl(DateTime::Format::Strptime)
Requires:       perl(Email::Valid)
Requires:       perl(File::ShareDir)
Requires:       perl(HTML::Entities)
Requires:       perl(HTML::TreeBuilder) >= 3.23
Requires:       perl(JSON::MaybeXS) >= 1.003003
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Moose) >= 2.1403
Requires:       perl(MooseX::Getopt) >= 0.16
Requires:       perl(MooseX::Types) >= 0.20
Requires:       perl(MooseX::Types::Common)
Requires:       perl(MooseX::Types::LoadableClass) >= 0.006
Requires:       perl(Sub::Exporter)
Requires:       perl(Sub::Name)
Requires:       perl(Try::Tiny)
Requires:       perl(aliased)
Requires:       perl(namespace::autoclean) >= 0.09
%{perl_requires}

%description
*** Although documentation in this file provides some overview, it is
mainly intended for API documentation. See HTML::FormHandler::Manual::Intro
for an introduction, with links to other documentation.

HTML::FormHandler maintains a clean separation between form construction
and form rendering. It allows you to define your forms and fields in a
number of flexible ways. Although it provides renderers for HTML, you can
define custom renderers for any kind of presentation.

HTML::FormHandler allows you to define form fields and validators. It can
be used for both database and non-database forms, and will automatically
update or create rows in a database. It can be used to process structured
data that doesn't come from an HTML form.

One of its goals is to keep the controller/application program interface as
simple as possible, and to minimize the duplication of code. In most cases,
interfacing your controller to your form is only a few lines of code.

With FormHandler you shouldn't have to spend hours trying to figure out how
to make a simple HTML change that would take one minute by hand. Because
you _can_ do it by hand. Or you can automate HTML generation as much as you
want, with template widgets or pure Perl rendering classes, and stay
completely in control of what, where, and how much is done automatically.
You can define custom renderers and display your rendered forms however you
want.

You can split the pieces of your forms up into logical parts and compose
complete forms from FormHandler classes, roles, fields, collections of
validations, transformations and Moose type constraints. You can write
custom methods to process forms, add any attribute you like, and use Moose
method modifiers. FormHandler forms are Perl classes, so there's a lot of
flexibility in what you can do.

HTML::FormHandler provides rendering through roles which are applied to
form and field classes (although there's no reason you couldn't write a
renderer as an external object either). There are currently two flavors:
all-in-one solutions like HTML::FormHandler::Render::Simple and
HTML::FormHandler::Render::Table that contain methods for rendering field
widget classes, and the HTML::FormHandler::Widget roles, which are more
atomic roles which are automatically applied to fields and form. See
HTML::FormHandler::Manual::Rendering for more details. (And you can easily
use hand-built forms - FormHandler doesn't care.)

The typical application for FormHandler would be in a Catalyst,
DBIx::Class, Template Toolkit web application, but use is not limited to
that. FormHandler can be used in any Perl application.

More Formhandler documentation and a tutorial can be found in the manual at
HTML::FormHandler::Manual.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes README README.md TODO util
%license LICENSE

%changelog
