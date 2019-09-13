#
# spec file for package perl-HTML-Parser
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


Name:           perl-HTML-Parser
Version:        3.72
Release:        0
%define cpan_name HTML-Parser
Summary:        HTML parser class
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTML-Parser/
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTML::Tagset) >= 3
Requires:       perl(HTML::Tagset) >= 3
Recommends:     perl(HTTP::Headers)
%{perl_requires}

%description
Objects of the 'HTML::Parser' class will recognize markup and separate it
from plain text (alias data content) in HTML documents. As different kinds
of markup and text are recognized, the corresponding event handlers are
invoked.

'HTML::Parser' is not a generic SGML parser. We have tried to make it able
to deal with the HTML that is actually "out there", and it normally parses
as closely as possible to the way the popular web browsers do it instead of
strictly following one of the many HTML specifications from W3C. Where
there is disagreement, there is often an option that you can enable to get
the official behaviour.

The document to be parsed may be supplied in arbitrary chunks. This makes
on-the-fly parsing as documents are received from the network possible.

If event driven parsing does not feel right for your application, you might
want to use 'HTML::PullParser'. This is an 'HTML::Parser' subclass that
allows a more conventional program structure.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes mkhctype mkpfunc README TODO

%changelog
