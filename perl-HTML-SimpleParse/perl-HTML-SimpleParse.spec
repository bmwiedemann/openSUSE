#
# spec file for package perl-HTML-SimpleParse
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           perl-HTML-SimpleParse
Version:        0.12
Release:        266
Provides:       HTML-SimpleParse
Conflicts:      perlmod
AutoReqProv:    on
Group:          Development/Libraries/Perl
License:        Artistic-1.0
Url:            http://search.cpan.org/perldoc?HTML::SimpleParse
Summary:        a bare-bones HTML parser
Source:         HTML-SimpleParse-%{version}.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

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
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc Changes README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/HTML
%{perl_vendorarch}/auto/HTML

%changelog
