#
# spec file for package perl-Math-ConvexHull
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


Name:           perl-Math-ConvexHull
Version:        1.04
Release:        0
%define cpan_name Math-ConvexHull
Summary:        Calculate convex hulls using Graham's scan (n*log(n))
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Math-ConvexHull/
Source:         http://www.cpan.org/authors/id/S/SM/SMUELLER/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
'Math::ConvexHull' is a simple module that calculates convex hulls from a
set of points in 2D space. It is a straightforward implementation of the
algorithm known as Graham's scan which, with complexity of O(n*log(n)), is
the fastest known method of finding the convex hull of an arbitrary set of
points. There are some methods of eliminating points that cannot be part of
the convex hull. These may or may not be implemented in a future version.

The implementation cannot deal with duplicate points. Therefore, points
which are very, very close (think floating point close) to the previous
point are dropped since version 1.02 of the module. However, if you pass in
randomly ordered data which contains duplicate points, this safety measure
might not help you. In that case, you will have to remove duplicates
yourself.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes README

%changelog
