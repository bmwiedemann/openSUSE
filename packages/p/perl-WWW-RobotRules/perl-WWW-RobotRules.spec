#
# spec file for package perl-WWW-RobotRules
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name WWW-RobotRules
Name:           perl-WWW-RobotRules
Version:        6.30.0
Release:        0
# 6.03 -> normalize -> 6.30.0
%define cpan_version 6.03
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Database of robots.txt-derived permissions
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(URI) >= 1.100
Requires:       perl(URI) >= 1.100
Provides:       perl(WWW::RobotRules) = %{version}
Provides:       perl(WWW::RobotRules::AnyDBM_File) = %{version}
Provides:       perl(WWW::RobotRules::DB_File) = %{version}
Provides:       perl(WWW::RobotRules::InCore) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module parses _/robots.txt_ files as specified in at
https://www.robotstxt.org/robotstxt.html. Webmasters can use the
_/robots.txt_ file to forbid conforming robots from accessing parts of
their web site.

The parsed files are kept in a 'WWW::RobotRules' object, and this object
provides methods to check if access to a given URL is prohibited. The same
'WWW::RobotRules' object can be used for one or more parsed _/robots.txt_
files on any number of hosts.

The following methods are provided:

* $rules = WWW::RobotRules->new($robot_name)

This is the constructor for WWW::RobotRules objects. The first argument
given to new() is the name of the robot.

* $rules->parse($robot_txt_url, $content, $fresh_until)

The parse() method takes as arguments the URL that was used to retrieve the
_/robots.txt_ file, and the contents of the file.

* $rules->allowed($uri)

Returns TRUE if this robot is allowed to retrieve this URL.

* $rules->agent([$name])

Get/set the agent name. NOTE: Changing the agent name will clear the
_robots.txt_ rules and expire times out of the cache.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes
%license LICENSE

%changelog
