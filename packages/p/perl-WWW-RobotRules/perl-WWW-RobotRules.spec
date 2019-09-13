#
# spec file for package perl-WWW-RobotRules
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-WWW-RobotRules
Version:        6.02
Release:        0
%define cpan_name WWW-RobotRules
Summary:        database of robots.txt-derived permissions
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/WWW-RobotRules/
Source:         http://www.cpan.org/authors/id/G/GA/GAAS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(URI) >= 1.10
#BuildRequires: perl(WWW::RobotRules)
#BuildRequires: perl(WWW::RobotRules::AnyDBM_File)
Requires:       perl(URI) >= 1.10
%{perl_requires}

%description
This module parses _/robots.txt_ files as specified in "A Standard for
Robot Exclusion", at <http://www.robotstxt.org/wc/norobots.html> Webmasters
can use the _/robots.txt_ file to forbid conforming robots from accessing
parts of their web site.

The parsed files are kept in a WWW::RobotRules object, and this object
provides methods to check if access to a given URL is prohibited. The same
WWW::RobotRules object can be used for one or more parsed _/robots.txt_
files on any number of hosts.

The following methods are provided:

* $rules = WWW::RobotRules->new($robot_name)

  This is the constructor for WWW::RobotRules objects. The first argument
  given to new() is the name of the robot.

* $rules->parse($robot_txt_url, $content, $fresh_until)

  The parse() method takes as arguments the URL that was used to retrieve
  the _/robots.txt_ file, and the contents of the file.

* $rules->allowed($uri)

  Returns TRUE if this robot is allowed to retrieve this URL.

* $rules->agent([$name])

  Get/set the agent name. NOTE: Changing the agent name will clear the
  robots.txt rules and expire times out of the cache.

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
%doc Changes README

%changelog
