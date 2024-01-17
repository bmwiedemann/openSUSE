#
# spec file for package perl-HTML-TokeParser-Simple
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


Name:           perl-HTML-TokeParser-Simple
Version:        3.16
Release:        0
%define cpan_name HTML-TokeParser-Simple
Summary:        Easy to use C<HTML::TokeParser> interface
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTML-TokeParser-Simple/
Source:         http://www.cpan.org/authors/id/O/OV/OVID/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTML::Parser) >= 3.25
BuildRequires:  perl(HTML::TokeParser) >= 2.24
BuildRequires:  perl(Module::Build) >= 0.40
BuildRequires:  perl(Sub::Override)
#BuildRequires: perl(HTML::Entities)
#BuildRequires: perl(HTML::TokeParser::Simple::Token)
#BuildRequires: perl(HTML::TokeParser::Simple::Token::Comment)
#BuildRequires: perl(HTML::TokeParser::Simple::Token::Declaration)
#BuildRequires: perl(HTML::TokeParser::Simple::Token::ProcessInstruction)
#BuildRequires: perl(HTML::TokeParser::Simple::Token::Tag)
#BuildRequires: perl(HTML::TokeParser::Simple::Token::Tag::End)
#BuildRequires: perl(HTML::TokeParser::Simple::Token::Tag::Start)
#BuildRequires: perl(HTML::TokeParser::Simple::Token::Text)
Requires:       perl(HTML::Parser) >= 3.25
Requires:       perl(HTML::TokeParser) >= 2.24
Requires:       perl(Sub::Override)
%{perl_requires}

%description
'HTML::TokeParser' is an excellent module that's often used for parsing
HTML. However, the tokens returned are not exactly intuitive to parse:

 ["S",  $tag, $attr, $attrseq, $text]
 ["E",  $tag, $text]
 ["T",  $text, $is_data]
 ["C",  $text]
 ["D",  $text]
 ["PI", $token0, $text]

To simplify this, 'HTML::TokeParser::Simple' allows the user ask more
intuitive (read: more self-documenting) questions about the tokens
returned.

You can also rebuild some tags on the fly. Frequently, the attributes
associated with start tags need to be altered, added to, or deleted. This
functionality is built in.

Since this is a subclass of 'HTML::TokeParser', all 'HTML::TokeParser'
methods are available. To truly appreciate the power of this module, please
read the documentation for 'HTML::TokeParser' and 'HTML::Parser'.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README xt

%changelog
