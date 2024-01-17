#
# spec file for package perl-Net-AMQP
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Net-AMQP
Version:        0.06
Release:        0
%define cpan_name Net-AMQP
Summary:        Advanced Message Queue Protocol (de)serialization and representation
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-AMQP/
Source0:        http://www.cpan.org/authors/id/C/CH/CHIPS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
# 32 bit is broken: https://rt.cpan.org/Public/Bug/Display.html?id=87816
ExcludeArch:    i586 armv7l ppc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(Module::Build) >= 0.400000
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(XML::LibXML)
Requires:       perl(Class::Accessor)
Requires:       perl(Class::Data::Inheritable)
Requires:       perl(XML::LibXML)
%{perl_requires}

%description
This module implements the frame (de)serialization and representation of
the Advanced Message Queue Protocol (http://www.amqp.org/). It is to be
used in conjunction with client or server software that does the actual
TCP/IP communication.

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
%doc CHANGES eg LICENSE README spec

%changelog
