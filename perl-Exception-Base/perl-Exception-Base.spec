#
# spec file for package perl-Exception-Base
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


Name:           perl-Exception-Base
Version:        0.2501
Release:        0
%define cpan_name Exception-Base
Summary:        Lightweight exceptions
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Exception-Base/
Source0:        http://www.cpan.org/authors/id/D/DE/DEXTER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Unit::Lite) >= 0.12
%{perl_requires}

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
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples Incompatibilities LICENSE README README.md

%changelog
