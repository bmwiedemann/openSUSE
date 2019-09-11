#
# spec file for package perl-GraphViz
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


Name:           perl-GraphViz
Version:        2.24
Release:        0
%define cpan_name GraphViz
Summary:        Interface to AT&T's GraphViz. Deprecated. See GraphViz2
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/GraphViz/
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/%{cpan_name}-%{version}.tgz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Which) >= 1.09
BuildRequires:  perl(IPC::Run) >= 0.6
BuildRequires:  perl(LWP::Simple) >= 6
BuildRequires:  perl(Parse::RecDescent) >= 1.965001
BuildRequires:  perl(Test::More) >= 1.001002
BuildRequires:  perl(Test::Pod) >= 1.48
BuildRequires:  perl(XML::Twig) >= 3.52
BuildRequires:  perl(XML::XPath) >= 1.13
Requires:       perl(File::Which) >= 1.09
Requires:       perl(IPC::Run) >= 0.6
Requires:       perl(LWP::Simple) >= 6
Requires:       perl(Parse::RecDescent) >= 1.965001
Requires:       perl(XML::Twig) >= 3.52
Requires:       perl(XML::XPath) >= 1.13
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  graphviz
# graphviz-gnome is required so that dot -Tpng works.
Requires:       cairo
Requires:       graphviz
Requires:       graphviz-gnome
Requires:       pango
# MANUAL END

%description
This module provides an interface to layout and image generation of
directed and undirected graphs in a variety of formats (PostScript, PNG,
etc.) using the "dot", "neato", "twopi", "circo" and "fdp" programs from
the Graphviz project (http://www.graphviz.org/ or
http://www.research.att.com/sw/tools/graphviz/).

GraphViz is deprecated in favour of GraphViz2.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
# MANUAL BEGIN
sed -i -e s,/usr/local/bin/perl,/usr/bin/perl, examples/*.pl
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
%doc Changes examples README
%license LICENSE

%changelog
