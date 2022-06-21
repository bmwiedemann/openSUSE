#
# spec file for package perl-Chart
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Chart
Name:           perl-Chart
Version:        2.402.3
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Series of charting modules
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LI/LICHTKIND/%{cpan_name}-v%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp) >= 1.35
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(GD) >= 2
BuildRequires:  perl(Test::More) >= 1.3
BuildRequires:  perl(Test::Warn) >= 0.30
Requires:       perl(Carp) >= 1.35
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
%autosetup  -n %{cpan_name}-v%{version}

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
%doc Changes CONTRIBUTING doc Documentation.pdf README TODO
%license LICENSE

%changelog
