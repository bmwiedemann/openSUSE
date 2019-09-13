#
# spec file for package perl-Dist-CheckConflicts
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


Name:           perl-Dist-CheckConflicts
Version:        0.11
Release:        0
%define cpan_name Dist-CheckConflicts
Summary:        declare version conflicts for your dist
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Dist-CheckConflicts/
Source:         http://www.cpan.org/authors/id/D/DO/DOY/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Runtime) >= 0.009
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Module::Runtime) >= 0.009
%{perl_requires}

%description
One shortcoming of the CPAN clients that currently exist is that they have
no way of specifying conflicting downstream dependencies of modules. This
module attempts to work around this issue by allowing you to specify
conflicting versions of modules separately, and deal with them after the
module is done installing.

For instance, say you have a module 'Foo', and some other module 'Bar' uses
'Foo'. If 'Foo' were to change its API in a non-backwards-compatible way,
this would cause 'Bar' to break until it is updated to use the new API.
'Foo' can't just depend on the fixed version of 'Bar', because this will
cause a circular dependency (because 'Bar' is already depending on 'Foo'),
and this doesn't express intent properly anyway - 'Foo' doesn't use 'Bar'
at all. The ideal solution would be for there to be a way to specify
conflicting versions of modules in a way that would let CPAN clients update
conflicting modules automatically after an existing module is upgraded, but
until that happens, this module will allow users to do this manually.

This module accepts a hash of options passed to its 'use' statement, with
these keys being valid:

* -conflicts

  A hashref of conflict specifications, where keys are module names, and
  values are the last broken version - any version greater than the
  specified version should work.

* -also

  Additional modules to get conflicts from (potentially recursively). This
  should generally be a list of modules which use Dist::CheckConflicts,
  which correspond to the dists that your dist depends on. (In an ideal
  world, this would be intuited directly from your dependency list, but the
  dependency list isn't available outside of build time).

* -dist

  The name of the distribution, to make the error message from
  check_conflicts more user-friendly.

The methods listed below are exported by this module into the module that
uses it, so you should call these methods on your module, not
Dist::CheckConflicts.

As an example, this command line can be used to update your modules, after
installing the 'Foo' dist (assuming that 'Foo::Conflicts' is the module in
the 'Foo' dist which uses Dist::CheckConflicts):

    perl -MFoo::Conflicts -e'print "$_\n"
        for map { $_->{package} } Foo::Conflicts->calculate_conflicts' | cpanm

As an added bonus, loading your conflicts module will provide warnings at
runtime if conflicting modules are detected (regardless of whether they are
loaded before or afterwards).

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
%doc Changes LICENSE README

%changelog
