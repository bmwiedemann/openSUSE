#
# spec file for package perl-GraphViz
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name GraphViz
Name:           perl-GraphViz
Version:        2.26
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Interface to AT&T's GraphViz. Deprecated. See GraphViz2
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Which) >= 1.09
BuildRequires:  perl(IPC::Run) >= 0.6
BuildRequires:  perl(LWP::Simple) >= 6
BuildRequires:  perl(Parse::RecDescent) >= 1.965001
BuildRequires:  perl(Test::More) >= 1.001002
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
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644
# MANUAL BEGIN
sed -i -e s,/usr/local/bin/perl,/usr/bin/perl, examples/*.pl
# MANUAL END

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
%doc Changes examples README
%license LICENSE

%changelog
