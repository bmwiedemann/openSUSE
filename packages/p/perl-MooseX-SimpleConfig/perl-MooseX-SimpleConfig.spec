#
# spec file for package perl-MooseX-SimpleConfig
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


Name:           perl-MooseX-SimpleConfig
Version:        0.11
Release:        0
%define cpan_name MooseX-SimpleConfig
Summary:        A Moose role for setting attributes from a simple configuration file
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-SimpleConfig/
Source:         http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Config::Any) >= 0.13
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::ConfigFromFile)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Config::Any) >= 0.13
Requires:       perl(Moose::Role)
Requires:       perl(MooseX::ConfigFromFile)
%{perl_requires}

%description
This role loads simple files to set object attributes. It is based on the
abstract role the MooseX::ConfigFromFile manpage, and uses the Config::Any
manpage to load your configuration file. the Config::Any manpage will in
turn support any of a variety of different config formats, detected by the
file extension. See the Config::Any manpage for more details about
supported formats.

To pass additional arguments to the Config::Any manpage you must provide a
'config_any_args()' method, for example:

  sub config_any_args {
    return {
      driver_args => { General => { '-InterPolateVars' => 1 } }
    };
  }

Like all the MooseX::ConfigFromFile manpage -derived file loaders, this
module is automatically supported by the the MooseX::Getopt manpage role as
well, which allows specifying '-configfile' on the command line.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING LICENSE README

%changelog
