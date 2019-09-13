#
# spec file for package perl-Math-ConvexHull-MonotoneChain
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Math-ConvexHull-MonotoneChain
Version:        0.01
Release:        0
%define cpan_name Math-ConvexHull-MonotoneChain
Summary:        Andrew's monotone chain algorithm for finding a convex hull in 2D
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Math-ConvexHull-MonotoneChain/
Source:         http://www.cpan.org/authors/id/S/SM/SMUELLER/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Test::More) >= 0.88
%{perl_requires}

%description
This is somewhat experimental still.

This (XS) module optionally exports a single function 'convex_hull' which
calculates the convex hull of the input points and returns it. The
algorithm is 'O(n log n)' due to having to sort the input list, but should
be somewhat faster than a plain Graham's scan (also 'O(n log n)') in
practice since it avoids polar coordinates.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes

%changelog
