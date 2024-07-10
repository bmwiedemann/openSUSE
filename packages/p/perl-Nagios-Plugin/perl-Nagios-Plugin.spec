#
# spec file for package perl-Nagios-Plugin
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


%define         cpan_name Nagios-Plugin

Name:           perl-%cpan_name
Version:        0.36
Release:        0
Summary:        A family of perl modules to streamline writing Nagios plugins
License:        Artistic-1.0 or GPL-2.0+
Group:          Development/Languages/Perl
Url:            http://search.cpan.org/perldoc?Nagios%3A%3APlugin
Source:         %cpan_name-%{version}.tar.gz
Patch0:         perl522.patch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(Math::Calc::Units)
BuildRequires:  perl(Params::Validate)
Requires:       perl(Class::Accessor)
Requires:       perl(Config::Tiny)
Requires:       perl(Math::Calc::Units)
Requires:       perl(Params::Validate)
Provides:       %cpan_name = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%perl_requires

%description
Nagios::Plugin and its associated Nagios::Plugin::* modules are a family of
perl modules to streamline writing Nagios plugins. The main end user modules
are Nagios::Plugin, providing an object-oriented interface to the entire
Nagios::Plugin::* collection, and Nagios::Plugin::Functions, providing a
simpler functional interface to a useful subset of the available functionality.

The purpose of the collection is to make it as simple as possible for
developers to create plugins that conform the Nagios Plugin guidelines
(http://nagiosplug.sourceforge.net/developer-guidelines.html).

%prep
%autosetup -p2 -n %cpan_name-%{version}

%build
perl Makefile.PL OPTIMIZE="%{optflags} -Wall"
make %{?_smp_mflags}

%if 0%{?suse_version} >= 1010
%check
make test
%endif

%install
%perl_make_install
%perl_process_packlist

%files
%defattr(-,root,root)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Nagios
%{perl_vendorarch}/auto/Nagios

%changelog
