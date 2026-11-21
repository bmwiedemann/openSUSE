#
# spec file for package perl-ExtUtils-XSpp
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


%define cpan_name ExtUtils-XSpp
Name:           perl-ExtUtils-XSpp
Version:        0.190.0
Release:        0
# 0.19 -> normalize -> 0.190.0
%define cpan_version 0.19
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        XS for C++
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBARBON/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.07
BuildRequires:  perl(ExtUtils::Typemaps) >= 1
BuildRequires:  perl(Module::Build) >= 0.420
BuildRequires:  perl(Test::Base)
BuildRequires:  perl(Test::Differences)
Requires:       perl(ExtUtils::ParseXS) >= 3.07
Requires:       perl(ExtUtils::Typemaps) >= 1
Provides:       perl(ExtUtils::XSpp) = %{version}
Provides:       perl(ExtUtils::XSpp::Cmd)
Provides:       perl(ExtUtils::XSpp::Driver)
Provides:       perl(ExtUtils::XSpp::Exception)
Provides:       perl(ExtUtils::XSpp::Exception::code)
Provides:       perl(ExtUtils::XSpp::Exception::object)
Provides:       perl(ExtUtils::XSpp::Exception::perlcode)
Provides:       perl(ExtUtils::XSpp::Exception::simple)
Provides:       perl(ExtUtils::XSpp::Exception::stdmessage)
Provides:       perl(ExtUtils::XSpp::Exception::unknown)
Provides:       perl(ExtUtils::XSpp::Grammar)
Provides:       perl(ExtUtils::XSpp::Grammar::YappDriver) = 1.210.0
Provides:       perl(ExtUtils::XSpp::Lexer)
Provides:       perl(ExtUtils::XSpp::Node)
Provides:       perl(ExtUtils::XSpp::Node::Access)
Provides:       perl(ExtUtils::XSpp::Node::Argument)
Provides:       perl(ExtUtils::XSpp::Node::Class)
Provides:       perl(ExtUtils::XSpp::Node::Comment)
Provides:       perl(ExtUtils::XSpp::Node::Constructor)
Provides:       perl(ExtUtils::XSpp::Node::Destructor)
Provides:       perl(ExtUtils::XSpp::Node::Enum)
Provides:       perl(ExtUtils::XSpp::Node::EnumValue)
Provides:       perl(ExtUtils::XSpp::Node::File)
Provides:       perl(ExtUtils::XSpp::Node::Function)
Provides:       perl(ExtUtils::XSpp::Node::Member)
Provides:       perl(ExtUtils::XSpp::Node::Method)
Provides:       perl(ExtUtils::XSpp::Node::Module)
Provides:       perl(ExtUtils::XSpp::Node::Package)
Provides:       perl(ExtUtils::XSpp::Node::PercAny)
Provides:       perl(ExtUtils::XSpp::Node::Preprocessor)
Provides:       perl(ExtUtils::XSpp::Node::Raw)
Provides:       perl(ExtUtils::XSpp::Node::Type)
Provides:       perl(ExtUtils::XSpp::Parser)
Provides:       perl(ExtUtils::XSpp::Plugin::feature::default_xs_typemap)
Provides:       perl(ExtUtils::XSpp::Typemap)
Provides:       perl(ExtUtils::XSpp::Typemap::parsed)
Provides:       perl(ExtUtils::XSpp::Typemap::reference)
Provides:       perl(ExtUtils::XSpp::Typemap::simple)
Provides:       perl(ExtUtils::XSpp::Typemap::wrapper)
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
Requires:       gcc-c++
Provides:       xspp = %{version}
Obsoletes:      xspp < %{version}
# MANUAL END

%description
Anything that does not look like a XS++ directive or a class declaration is
passed verbatim to XS. If you want XS++ to ignore code that looks like a
XS++ directive or class declaration, simply surround it with a raw block
delimiter like this:

  %{
  XS++ won't interpret this
  %}

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL --installdirs=vendor optimize="%{optflags}"
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples README XSP.yp

%changelog
