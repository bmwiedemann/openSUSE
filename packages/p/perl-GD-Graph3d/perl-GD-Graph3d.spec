#
# spec file for package perl-GD-Graph3d
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-GD-Graph3d
BuildRequires:  perl-GD
BuildRequires:  perl-GDGraph
BuildRequires:  perl-GDTextUtil
BuildRequires:  perl-macros
Version:        0.63
Release:        0
Requires:       perl-GD
Requires:       perl-GDGraph
Requires:       perl-GDTextUtil
Provides:       perl-GDGraph3d
Obsoletes:      perl-GDGraph3d
Url:            http://cpan.org/modules/by-module/GD/
Summary:        3d extension for perl-GDGraph
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Source:         GD-Graph3d-%{version}.tar.gz
Patch:          GD-Graph3d-trim_miter.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
This is the GD::Graph3d extensions module. It provides 3D graphs for
the GD::Graph module by Martien Verbruggen, which in turn generates
graph using Lincoln Stein's GD.pm.

%prep
%setup -n GD-Graph3d-%{version}
%patch -p1

%build
perl Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS -Wall"
make %{?_smp_mflags}
make test

%install
rm -rf $RPM_BUILD_ROOT
%perl_make_install
%perl_process_packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc %{_mandir}/man?/*
%{perl_vendorarch}/auto/GD
%{perl_vendorlib}/GD
%{perl_vendorlib}/GD/Graph3d.pm

%changelog
