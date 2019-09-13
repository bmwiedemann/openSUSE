#
# spec file for package perl-BSD-Resource
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


Name:           perl-BSD-Resource
Version:        1.2911
Release:        0
#Upstream:  This module free software; you can redistribute it and/or modify it under the terms of the Artistic License 2.0 or GNU Lesser General Public License 2.0. For more details, see the full text of the licenses at <http://www.perlfoundation.org/artistic_license_2_0>, and <http://www.gnu.org/licenses/gpl-2.0.html>.
%define cpan_name BSD-Resource
Summary:        BSD process resource limit and priority functions
License:        Artistic-2.0 or LGPL-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/BSD-Resource/
Source0:        https://cpan.metacpan.org/authors/id/J/JH/JHI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
BSD process resource limit and priority functions

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
%doc ChangeLog README
%license LICENSE

%changelog
