#
# spec file for package perl-HTML-SimpleParse
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


Name:           perl-HTML-SimpleParse
Version:        0.12
Release:        0
Provides:       HTML-SimpleParse
Conflicts:      perlmod
Url:            http://search.cpan.org/perldoc?HTML::SimpleParse
Summary:        a bare-bones HTML parser
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Source:         HTML-SimpleParse-%{version}.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros
BuildArch:      noarch

%description
This is the HTML::SimpleParse module.  It is a bare-bones HTML parser,
similar to HTML::Parser, but with a couple important distinctions:

First, HTML::Parser knows which tags can contain other tags, which
start tags have corresponding end tags, which tags can exist only in
the <HEAD> portion of the document, and so forth.  HTML::SimpleParse
does not know any of these things.  It just finds tags and text in the
HTML you give it, it does not care about the specific content of these
tags (though it does distiguish between different _types_ of tags, such
as comments, starting tags like <b>, ending tags like </b>, and so on).

Second, HTML::SimpleParse does not create a hierarchical tree of HTML
content, but rather a simple linear list.  It does not pay any
attention to balancing start tags with corresponding end tags, or which
pairs of tags are inside other pairs of tags.

Because of these characteristics, you can make a very effective HTML
filter by sub-classing HTML::SimpleParse.



Authors:
--------
    Ken Williams <ken@forum.swarthmore.edu>

%prep 
%setup -n HTML-SimpleParse-%{version}

%build
perl Makefile.PL
make %{?_smp_mflags} all
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-, root, root)
%doc Changes README

%changelog
