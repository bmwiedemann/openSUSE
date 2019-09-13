#
# spec file for package perl-Chart
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Chart
Version:        2.4.10
Release:        0
%define cpan_name Chart
Summary:        Series of Charting Modules
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Chart/
Source0:        http://www.cpan.org/authors/id/C/CH/CHARTGRP/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(GD) >= 2
Requires:       perl(GD) >= 2
%{perl_requires}

%description
These man-pages give you the most important information about Chart. There
is also a complete documentation (Documentation.pdf) within the Chart
package. Look at it to get more information. This module is an attempt to
build a general purpose graphing module that is easily modified and
expanded. I borrowed most of the API from Martien Verbruggen's GIFgraph
module. I liked most of GIFgraph, but I thought it was to difficult to
modify, and it was missing a few things that I needed, most notably
legends. So I decided to write a new module from scratch, and I've designed
it from the bottom up to be easy to modify. Like GIFgraph, Chart uses
Lincoln Stein's GD module for all of its graphics primitives calls.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

rm -f pm_to_blib

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
%doc doc Documentation.pdf README TODO

%changelog
