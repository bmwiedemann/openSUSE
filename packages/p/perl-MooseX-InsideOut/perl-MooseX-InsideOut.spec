#
# spec file for package perl-MooseX-InsideOut
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-MooseX-InsideOut
Version:        0.106
Release:        0
%define cpan_name MooseX-InsideOut
Summary:        inside-out objects with Moose
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-InsideOut/
Source:         http://www.cpan.org/authors/id/D/DO/DOY/MooseX-InsideOut-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::MOP) >= 0.80
BuildRequires:  perl(Hash::Util::FieldHash::Compat)
BuildRequires:  perl(Moose) >= 0.94
BuildRequires:  perl(namespace::clean) >= 0.11
Requires:       perl(Class::MOP) >= 0.80
Requires:       perl(Hash::Util::FieldHash::Compat)
Requires:       perl(Moose) >= 0.94
Requires:       perl(namespace::clean) >= 0.11
%{perl_requires}

%description
MooseX::InsideOut provides metaroles for inside-out objects. That is, it
sets up attribute slot storage somewhere other than inside '$self'. This
means that you can extend non-Moose classes, whose internals you either
don't want to care about or aren't hash-based.

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
%defattr(644,root,root,755)
%doc Changes LICENSE README

%changelog
