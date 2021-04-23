#
# spec file for package perl-DBIx-Class-UUIDColumns
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-DBIx-Class-UUIDColumns
Version:        0.02006
Release:        0
%define cpan_name DBIx-Class-UUIDColumns
Summary:        Implicit uuid columns
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/DBIx-Class-UUIDColumns/
Source:         http://www.cpan.org/authors/id/A/AB/ABRAXXA/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor::Grouped)
BuildRequires:  perl(DBD::SQLite) >= 1.11
BuildRequires:  perl(DBIx::Class) >= 0.07005
BuildRequires:  perl(Module::Install)
Requires:       perl(Class::Accessor::Grouped)
Requires:       perl(DBIx::Class) >= 0.07005
Recommends:     perl(APR::UUID)
Recommends:     perl(Data::Uniqid)
Recommends:     perl(Data::UUID)
Recommends:     perl(UUID)
Recommends:     perl(UUID::Random)
Recommends:     perl(Win32API::GUID)
Recommends:     perl(Win32::Guidgen)
%{perl_requires}
# MANUAL
BuildRequires:  perl(Data::UUID)
Requires:       perl(Data::UUID)

%description
This the DBIx::Class manpage component resembles the behaviour of the
Class::DBI::UUID manpage, to make some columns implicitly created as uuid.

When loaded, 'UUIDColumns' will search for a suitable uuid generation
module from the following list of supported modules:

  Data::UUID
  APR::UUID*
  UUID
  Win32::Guidgen
  Win32API::GUID

If no supporting module can be found, an exception will be thrown.

*APR::UUID will not be loaded under OpenBSD due to an as yet unidentified
XS issue.

If you would like to use a specific module, you can set the /uuid_class
manpage:

  __PACKAGE__->uuid_class('::Data::UUID');
  __PACKAGE__->uuid_class('MyUUIDGenerator');

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
