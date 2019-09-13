#
# spec file for package perl-MouseX-SimpleConfig
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-MouseX-SimpleConfig
Version:        0.11
Release:        0
%define cpan_name MouseX-SimpleConfig
Summary:        A Mouse role for setting attributes from a simple configfile
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MouseX-SimpleConfig/
Source:         http://www.cpan.org/authors/id/M/MJ/MJGARDNER/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Config::Any) >= 0.13
BuildRequires:  perl(Mouse) >= 0.35
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(MouseX::ConfigFromFile) >= 0.02
BuildRequires:  perl(Path::Class::File)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Config::Any) >= 0.13
Requires:       perl(Mouse) >= 0.35
Requires:       perl(Mouse::Role)
Requires:       perl(MouseX::ConfigFromFile) >= 0.02
%{perl_requires}

%description
This role loads simple configfiles to set object attributes. It is based on
the abstract role MouseX::ConfigFromFile, and uses Config::Any to load your
configfile. Config::Any will in turn support any of a variety of different
config formats, detected by the file extension. See Config::Any for more
details about supported formats.

Like all MouseX::ConfigFromFile -derived configfile loaders, this module is
automatically supported by the MouseX::Getopt role as well, which allows
specifying '-configfile' on the commandline.

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
%doc Changes LICENSE perlcritic.rc README weaver.ini

%changelog
