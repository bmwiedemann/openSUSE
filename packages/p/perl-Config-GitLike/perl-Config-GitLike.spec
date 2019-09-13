#
# spec file for package perl-Config-GitLike
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Config-GitLike
Version:        1.17
Release:        0
%define cpan_name Config-GitLike
Summary:        Git-Compatible Config File Parsing
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Config-GitLike/
Source0:        https://cpan.metacpan.org/authors/id/A/AL/ALEXMV/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::Types::MooseLike)
BuildRequires:  perl(Test::Exception)
Requires:       perl(Moo)
Requires:       perl(MooX::Types::MooseLike)
%{perl_requires}

%description
This module handles interaction with configuration files of the style used
by the version control system Git. It can both parse and modify these
files, as well as create entirely new ones.

You only need to know a few things about the configuration format in order
to use this module. First, a configuration file is made up of key/value
pairs. Every key must be contained in a section. Sections can have
subsections, but they don't have to. For the purposes of setting and
getting configuration variables, we join the section name, subsection name,
and variable name together with dots to get a key name that looks like
"section.subsection.variable". These are the strings that you'll be passing
in to 'key' arguments.

Configuration files inherit from each other. By default, 'Config::GitLike'
loads data from a system-wide configuration file, a per-user configuration
file, and a per-directory configuration file, but by subclassing and
overriding methods you can obtain any combination of configuration files.
By default, configuration files that don't exist are just skipped.

See
http://www.kernel.org/pub/software/scm/git/docs/git-config.html#_configurat
ion_file for details on the syntax of git configuration files. We won't
waste pixels on the nitty gritty here.

While the behavior of a couple of this module's methods differ slightly
from the 'git config' equivalents, this module can read any config file
written by git. The converse is usually true, but only if you don't take
advantage of this module's increased permissiveness when it comes to key
names. (See DIFFERENCES FROM GIT-CONFIG for details.)

This is an object-oriented module using Moo. All subroutines are object
method calls.

A few methods have parameters that are always used for the same purpose:

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
%doc Changes

%changelog
