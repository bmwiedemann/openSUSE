#
# spec file for package perl-MouseX-ConfigFromFile
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


Name:           perl-MouseX-ConfigFromFile
Version:        0.05
Release:        0
%define cpan_name MouseX-ConfigFromFile
Summary:        An abstract Mouse role for setting attributes from a configfile
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MouseX-ConfigFromFile/
Source:         http://www.cpan.org/authors/id/M/MA/MASAKI/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Mouse) >= 0.39
BuildRequires:  perl(MouseX::Types::Path::Class) >= 0.06
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(Mouse) >= 0.39
Requires:       perl(MouseX::Types::Path::Class) >= 0.06
%{perl_requires}

%description
This is an abstract role which provides an alternate constructor for
creating objects using parameters passed in from a configuration file. The
actual implementation of reading the configuration file is left to concrete
subroles.

It declares an attribute 'configfile' and a class method 'new_with_config',
and requires that concrete roles derived from it implement the class method
'get_config_from_file'.

Attributes specified directly as arguments to 'new_with_config' supercede
those in the configfile.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
export PERL5LIB=.
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
%doc Changes README README.mkdn

%changelog
