#
# spec file for package perl-HTML-FormHandler
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


%define cpan_name HTML-FormHandler
Name:           perl-HTML-FormHandler
Version:        0.400.680
Release:        0
# 0.40068 -> normalize -> 0.400.680
%define cpan_version 0.40068
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        HTML forms using Moose
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GS/GSHANK/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Load) >= 0.60
BuildRequires:  perl(Crypt::Blowfish)
BuildRequires:  perl(Crypt::CBC)
BuildRequires:  perl(Data::Clone)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(Email::Valid)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install) >= 0.60
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::TreeBuilder) >= 3.230
BuildRequires:  perl(JSON::MaybeXS) >= 1.3.3
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Moose) >= 2.140.300
BuildRequires:  perl(MooseX::Getopt) >= 0.160
BuildRequires:  perl(MooseX::Types) >= 0.200
BuildRequires:  perl(MooseX::Types::Common)
BuildRequires:  perl(MooseX::Types::LoadableClass) >= 0.6
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Memory::Cycle) >= 1.40
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(aliased)
BuildRequires:  perl(namespace::autoclean) >= 0.90
Requires:       perl(Class::Load) >= 0.60
Requires:       perl(Crypt::Blowfish)
Requires:       perl(Crypt::CBC)
Requires:       perl(Data::Clone)
Requires:       perl(DateTime)
Requires:       perl(DateTime::Format::Strptime)
Requires:       perl(Email::Valid)
Requires:       perl(File::ShareDir)
Requires:       perl(HTML::Entities)
Requires:       perl(HTML::TreeBuilder) >= 3.230
Requires:       perl(JSON::MaybeXS) >= 1.3.3
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Moose) >= 2.140.300
Requires:       perl(MooseX::Getopt) >= 0.160
Requires:       perl(MooseX::Types) >= 0.200
Requires:       perl(MooseX::Types::Common)
Requires:       perl(MooseX::Types::LoadableClass) >= 0.6
Requires:       perl(Sub::Exporter)
Requires:       perl(Sub::Name)
Requires:       perl(Try::Tiny)
Requires:       perl(aliased)
Requires:       perl(namespace::autoclean) >= 0.90
Provides:       perl(HTML::FormHandler) = %{version}
Provides:       perl(HTML::FormHandler::Base) = %{version}
Provides:       perl(HTML::FormHandler::Blocks) = %{version}
Provides:       perl(HTML::FormHandler::BuildFields) = %{version}
Provides:       perl(HTML::FormHandler::BuildPages) = %{version}
Provides:       perl(HTML::FormHandler::Field) = %{version}
Provides:       perl(HTML::FormHandler::Field::AddElement) = %{version}
Provides:       perl(HTML::FormHandler::Field::BoolSelect) = %{version}
Provides:       perl(HTML::FormHandler::Field::Boolean) = %{version}
Provides:       perl(HTML::FormHandler::Field::Button) = %{version}
Provides:       perl(HTML::FormHandler::Field::Captcha) = %{version}
Provides:       perl(HTML::FormHandler::Field::Checkbox) = %{version}
Provides:       perl(HTML::FormHandler::Field::Compound) = %{version}
Provides:       perl(HTML::FormHandler::Field::Date) = %{version}
Provides:       perl(HTML::FormHandler::Field::DateMDY) = %{version}
Provides:       perl(HTML::FormHandler::Field::DateTime) = %{version}
Provides:       perl(HTML::FormHandler::Field::Display) = %{version}
Provides:       perl(HTML::FormHandler::Field::Duration) = %{version}
Provides:       perl(HTML::FormHandler::Field::Email) = %{version}
Provides:       perl(HTML::FormHandler::Field::File) = %{version}
Provides:       perl(HTML::FormHandler::Field::Float) = %{version}
Provides:       perl(HTML::FormHandler::Field::Hidden) = %{version}
Provides:       perl(HTML::FormHandler::Field::Hour) = %{version}
Provides:       perl(HTML::FormHandler::Field::IntRange) = %{version}
Provides:       perl(HTML::FormHandler::Field::Integer) = %{version}
Provides:       perl(HTML::FormHandler::Field::Minute) = %{version}
Provides:       perl(HTML::FormHandler::Field::Money) = %{version}
Provides:       perl(HTML::FormHandler::Field::Month) = %{version}
Provides:       perl(HTML::FormHandler::Field::MonthDay) = %{version}
Provides:       perl(HTML::FormHandler::Field::MonthName) = %{version}
Provides:       perl(HTML::FormHandler::Field::Multiple) = %{version}
Provides:       perl(HTML::FormHandler::Field::Nested) = %{version}
Provides:       perl(HTML::FormHandler::Field::NoValue) = %{version}
Provides:       perl(HTML::FormHandler::Field::NonEditable) = %{version}
Provides:       perl(HTML::FormHandler::Field::Password) = %{version}
Provides:       perl(HTML::FormHandler::Field::PasswordConf) = %{version}
Provides:       perl(HTML::FormHandler::Field::PosInteger) = %{version}
Provides:       perl(HTML::FormHandler::Field::PrimaryKey) = %{version}
Provides:       perl(HTML::FormHandler::Field::Repeatable) = %{version}
Provides:       perl(HTML::FormHandler::Field::RequestToken) = %{version}
Provides:       perl(HTML::FormHandler::Field::Reset) = %{version}
Provides:       perl(HTML::FormHandler::Field::Result) = %{version}
Provides:       perl(HTML::FormHandler::Field::RmElement) = %{version}
Provides:       perl(HTML::FormHandler::Field::Role::RequestToken) = %{version}
Provides:       perl(HTML::FormHandler::Field::Second) = %{version}
Provides:       perl(HTML::FormHandler::Field::Select) = %{version}
Provides:       perl(HTML::FormHandler::Field::SelectCSV) = %{version}
Provides:       perl(HTML::FormHandler::Field::Submit) = %{version}
Provides:       perl(HTML::FormHandler::Field::Text) = %{version}
Provides:       perl(HTML::FormHandler::Field::TextArea) = %{version}
Provides:       perl(HTML::FormHandler::Field::TextCSV) = %{version}
Provides:       perl(HTML::FormHandler::Field::Upload) = %{version}
Provides:       perl(HTML::FormHandler::Field::Weekday) = %{version}
Provides:       perl(HTML::FormHandler::Field::Year) = %{version}
Provides:       perl(HTML::FormHandler::Fields) = %{version}
Provides:       perl(HTML::FormHandler::Foo) = %{version}
Provides:       perl(HTML::FormHandler::I18N) = %{version}
Provides:       perl(HTML::FormHandler::I18N::ar_kw) = %{version}
Provides:       perl(HTML::FormHandler::I18N::bg_bg) = %{version}
Provides:       perl(HTML::FormHandler::I18N::ca_es) = %{version}
Provides:       perl(HTML::FormHandler::I18N::cs_cz) = %{version}
Provides:       perl(HTML::FormHandler::I18N::de_de) = %{version}
Provides:       perl(HTML::FormHandler::I18N::en_us) = %{version}
Provides:       perl(HTML::FormHandler::I18N::es_es) = %{version}
Provides:       perl(HTML::FormHandler::I18N::hu_hu) = %{version}
Provides:       perl(HTML::FormHandler::I18N::it_it) = %{version}
Provides:       perl(HTML::FormHandler::I18N::ja_jp) = %{version}
Provides:       perl(HTML::FormHandler::I18N::pt_br) = %{version}
Provides:       perl(HTML::FormHandler::I18N::ru_ru) = %{version}
Provides:       perl(HTML::FormHandler::I18N::sv_se) = %{version}
Provides:       perl(HTML::FormHandler::I18N::tr_tr) = %{version}
Provides:       perl(HTML::FormHandler::I18N::ua_ua) = %{version}
Provides:       perl(HTML::FormHandler::InitResult) = %{version}
Provides:       perl(HTML::FormHandler::Merge) = %{version}
Provides:       perl(HTML::FormHandler::Model) = %{version}
Provides:       perl(HTML::FormHandler::Model::Object) = %{version}
Provides:       perl(HTML::FormHandler::Moose) = %{version}
Provides:       perl(HTML::FormHandler::Moose::Role) = %{version}
Provides:       perl(HTML::FormHandler::Page) = %{version}
Provides:       perl(HTML::FormHandler::Page::Simple) = %{version}
Provides:       perl(HTML::FormHandler::Pages) = %{version}
Provides:       perl(HTML::FormHandler::Render::RepeatableJs) = %{version}
Provides:       perl(HTML::FormHandler::Render::Simple) = %{version}
Provides:       perl(HTML::FormHandler::Render::Table) = %{version}
Provides:       perl(HTML::FormHandler::Render::Util) = %{version}
Provides:       perl(HTML::FormHandler::Render::WithTT) = %{version}
Provides:       perl(HTML::FormHandler::Result) = %{version}
Provides:       perl(HTML::FormHandler::Result::Role) = %{version}
Provides:       perl(HTML::FormHandler::Test) = %{version}
Provides:       perl(HTML::FormHandler::TraitFor::Captcha) = %{version}
Provides:       perl(HTML::FormHandler::TraitFor::I18N) = %{version}
Provides:       perl(HTML::FormHandler::TraitFor::Types) = %{version}
Provides:       perl(HTML::FormHandler::Traits) = %{version}
Provides:       perl(HTML::FormHandler::Types) = %{version}
Provides:       perl(HTML::FormHandler::Validate) = %{version}
Provides:       perl(HTML::FormHandler::Widget::ApplyRole) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Block) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Block::Bootstrap) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::Button) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::ButtonTag) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::Captcha) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::Checkbox) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::CheckboxGroup) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::Compound) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::Hidden) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::HorizCheckboxGroup) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::NoRender) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::Password) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::RadioGroup) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::Repeatable) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::Reset) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::Role::HTMLAttributes) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::Role::SelectedOption) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::Select) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::Span) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::Submit) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::Text) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::Textarea) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Field::Upload) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Form::Role::HTMLAttributes) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Form::Simple) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Form::Table) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Theme::Bootstrap) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Theme::Bootstrap3) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Theme::BootstrapFormMessages) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Wrapper::Base) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Wrapper::Bootstrap) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Wrapper::Bootstrap3) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Wrapper::Fieldset) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Wrapper::None) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Wrapper::Simple) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Wrapper::SimpleInline) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Wrapper::Table) = %{version}
Provides:       perl(HTML::FormHandler::Widget::Wrapper::TableInline) = %{version}
Provides:       perl(HTML::FormHandler::Wizard) = %{version}
%undefine       __perllib_provides
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
%doc Changes README README.md TODO util
%license LICENSE

%changelog
