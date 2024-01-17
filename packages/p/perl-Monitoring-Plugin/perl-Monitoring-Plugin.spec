#
# spec file for package perl-Monitoring-Plugin
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


Name:           perl-Monitoring-Plugin
Version:        0.40
Release:        0
%define         cpan_name Monitoring-Plugin
Summary:        Family of Perl modules to streamline writing Nagios compatible plugins
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Monitoring-Plugin/
Source0:        %{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(Params::Validate)
Requires:       perl-base
Requires:       perl(Class::Accessor)
Requires:       perl(Config::Tiny)
Requires:       perl(Params::Validate)
%if 0%{?suse_version}
BuildRequires:  perl-macros
BuildRequires:  perl(Math::Calc::Units)
%if 0%{?suse_version} > 1320
BuildRequires:  perl(Module::Install)
%endif
Requires:       perl(Math::Calc::Units)
%endif
%{perl_requires}

%description
Monitoring::Plugin and its associated Monitoring::Plugin::* modules are a
family of perl modules to streamline writing Monitoring plugins. The main
end user modules are Monitoring::Plugin, providing an object-oriented
interface to the entire Monitoring::Plugin::* collection, and
Monitoring::Plugin::Functions, providing a simpler functional interface to
a useful subset of the available functionality.

The purpose of the collection is to make it as simple as possible for
developers to create plugins that conform the Monitoring Plugin guidelines
(https://www.monitoring-plugins.org/doc/guidelines.html).

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

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
%doc Changes notes README

%changelog
