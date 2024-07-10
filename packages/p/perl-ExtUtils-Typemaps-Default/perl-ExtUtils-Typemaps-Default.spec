#
# spec file for package perl-ExtUtils-Typemaps-Default
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


Name:           perl-ExtUtils-Typemaps-Default
Version:        1.05
Release:        0
%define cpan_name ExtUtils-Typemaps-Default
Summary:        A set of useful typemaps
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/ExtUtils-Typemaps-Default/
Source:         http://www.cpan.org/authors/id/S/SM/SMUELLER/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::Typemaps) >= 3.18_03
BuildRequires:  perl(Module::Build)
Requires:       perl(ExtUtils::Typemaps) >= 3.18_03
%{perl_requires}

%description
'ExtUtils::Typemaps::Default' is an 'ExtUtils::Typemaps' subclass that
provides a set of default mappings (in addition to what perl itself
provides). These default mappings are currently defined as the combination
of the mappings provided by the following typemap classes which are
provided in this distribution:

the ExtUtils::Typemaps::ObjectMap manpage, the ExtUtils::Typemaps::STL
manpage, the ExtUtils::Typemaps::Basic manpage

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
%doc Changes

%changelog
