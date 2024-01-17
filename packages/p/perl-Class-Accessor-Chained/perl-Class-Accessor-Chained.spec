#
# spec file for package perl-Class-Accessor-Chained
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


Name:           perl-Class-Accessor-Chained
%define cpan_name %( echo %{name} | %{__sed} -e 's,perl-,,' )
Summary:        Make chained accessors
Version:        0.01
Release:        1
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-Accessor-Chained
Source:         %{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Class::Accessor)
Requires:       perl(Class::Accessor)

Provides:       %{cpan_name}
Provides:       %{cpan_name}-Fast
Obsoletes:      %{cpan_name}-Fast

#-------------------------------------------------------------------------------

%description
#-------------------------------------------------------------------------------
A chained accessor is one that always returns the object when called with
parameters (to set), and the value of the field when called with no arguments.

This module subclasses Class::Accessor in order to provide the same
mk_accessors interface.

  Authors:	Richard Clamp <richardc@unixbeard.net>
-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
%prep
#-------------------------------------------------------------------------------
%setup -q -n %{cpan_name}-%{version}

#-------------------------------------------------------------------------------

%build
#-------------------------------------------------------------------------------
perl Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS -Wall"
%{__make}

%check
%{__make} test

#-------------------------------------------------------------------------------

%install
#-------------------------------------------------------------------------------
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

#-------------------------------------------------------------------------------

%clean
#-------------------------------------------------------------------------------
%{__rm} -rf $RPM_BUILD_ROOT

#-------------------------------------------------------------------------------

%files -f %{name}.files
#-------------------------------------------------------------------------------
# normally you only need to check for doc files
%defattr(0644,root,root,0755)
%doc Changes README

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
%changelog
