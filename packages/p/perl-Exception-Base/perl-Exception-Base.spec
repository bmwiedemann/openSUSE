#
# spec file for package perl-Exception-Base
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Exception-Base
Name:           perl-Exception-Base
Version:        0.2501
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Lightweight exceptions
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DE/DEXTER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
# PATCH-FIX-UPSTREAM deprecated smartmatch operator https://github.com/dex4er/perl-Exception-Base/issues/5
Patch0:         fix_perl538.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Unit::Lite) >= 0.12
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(Module::Build)
# MANUAL END

%description
This class implements a fully OO exception mechanism similar to
Exception::Class or Class::Throwable. It provides a simple interface
allowing programmers to declare exception classes. These classes can be
thrown and caught. Each uncaught exception prints full stack trace if the
default verbosity is increased for debugging purposes.

The features of 'Exception::Base':

  * fast implementation of the exception class

  * fully OO without closures and source code filtering

  * does not mess with '$SIG{__DIE__}' and '$SIG{__WARN__}'

  * no external run-time modules dependencies, requires core Perl modules only

  * the default behavior of exception class can be changed globally or just for
the thrown exception

  * matching the exception by class, message or other attributes

  * matching with string, regex or closure function

  * creating automatically the derived exception classes (perlfunc/use
interface)

  * easily expendable, see Exception::System class for example

  * prints just an error message or dumps full stack trace

  * can propagate (rethrow) an exception

  * can ignore some packages for stack trace output

  * some defaults (i.e. verbosity) can be different for different exceptions

%prep
%autosetup  -n %{cpan_name}-%{version} -p0

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples Incompatibilities README README.md
%license LICENSE

%changelog
