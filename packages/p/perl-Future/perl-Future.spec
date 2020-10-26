#
# spec file for package perl-Future
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Future
Version:        0.46
Release:        0
%define cpan_name Future
Summary:        Represent an operation awaiting completion
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp) >= 1.25
BuildRequires:  perl(Module::Build) >= 0.400400
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Identity)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Refcount)
Requires:       perl(Carp) >= 1.25
%{perl_requires}

%description
A 'Future' object represents an operation that is currently in progress, or
has recently completed. It can be used in a variety of ways to manage the
flow of control, and data, through an asynchronous program.

Some futures represent a single operation and are explicitly marked as
ready by calling the 'done' or 'fail' methods. These are called "leaf"
futures here, and are returned by the 'new' constructor.

Other futures represent a collection of sub-tasks, and are implicitly
marked as ready depending on the readiness of their component futures as
required. These are called "convergent" futures here as they converge
control and data-flow back into one place. These are the ones returned by
the various 'wait_*' and 'need_*' constructors.

It is intended that library functions that perform asynchronous operations
would use future objects to represent outstanding operations, and allow
their calling programs to control or wait for these operations to complete.
The implementation and the user of such an interface would typically make
use of different methods on the class. The methods below are documented in
two sections; those of interest to each side of the interface.

It should be noted however, that this module does not in any way provide an
actual mechanism for performing this asynchronous activity; it merely
provides a way to create objects that can be used for control and data flow
around those operations. It allows such code to be written in a neater,
forward-reading manner, and simplifies many common patterns that are often
involved in such situations.

See also Future::Utils which contains useful loop-constructing functions,
to run a future-returning function repeatedly in a loop.

Unless otherwise noted, the following methods require at least version
_0.08_.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
