#
# spec file for package perl-SVN-Simple
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-SVN-Simple
Url:            http://search.cpan.org/~clkao/
BuildRequires:  perl-macros
BuildRequires:  subversion-perl
Requires:       subversion-perl
Summary:        A simple interface to subversion's editor interface
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Version:        0.28
Release:        0
Source:         http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/SVN-Simple-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
SVN::Simple::Edit wraps the subversion delta editor with a perl
friendly interface and then you could easily drive it for describing
changes to a tree. A common usage is to wrap the commit editor, so you
could make commits to a subversion repository easily.



Authors:
--------
    Chia-liang Kao <clkao at clkao dot org>

%prep
%setup -n SVN-Simple-%{version}

%build
perl Makefile.PL
%{__make} %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist

%clean
[ "${RPM_BUILD_ROOT}" != "/" -a -d ${RPM_BUILD_ROOT} ] && rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-, root, root)
%dir %{perl_vendorlib}/SVN
%dir %{perl_vendorlib}/SVN/Simple
%{perl_vendorlib}/SVN/Simple/*.pm
%dir %{perl_vendorarch}/auto/SVN/Simple
%dir %{perl_vendorarch}/auto/SVN/Simple/Edit
%{_mandir}/man3/SVN::Simple::Edit*.3pm.gz

%changelog
