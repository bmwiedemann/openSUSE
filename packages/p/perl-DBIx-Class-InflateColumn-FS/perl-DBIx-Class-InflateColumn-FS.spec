#
# spec file for package perl-DBIx-Class-InflateColumn-FS
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


Name:           perl-DBIx-Class-InflateColumn-FS
Version:        0.01007
Release:        0
%define cpan_name DBIx-Class-InflateColumn-FS
Summary:        Inflate/deflate columns to Path::Class::File objects
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/DBIx-Class-InflateColumn-FS/
Source:         http://www.cpan.org/authors/id/M/MM/MMIMS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBD::SQLite) >= 1.12
BuildRequires:  perl(DBICx::TestDatabase)
BuildRequires:  perl(DBIx::Class) >= 0.08
BuildRequires:  perl(DBIx::Class::UUIDColumns) >= 0.02005
BuildRequires:  perl(Module::Install)
BuildRequires:  perl(Path::Class)
Requires:       perl(DBD::SQLite) >= 1.12
Requires:       perl(DBICx::TestDatabase)
Requires:       perl(DBIx::Class) >= 0.08
Requires:       perl(DBIx::Class::UUIDColumns) >= 0.02005
Requires:       perl(Path::Class)
%{perl_requires}

%description
Provides inflation to a Path::Class::File object allowing file system
storage of BLOBS.

The storage path is specified with 'fs_column_path'. Each file receives a
unique name, so the storage for all FS columns can share the same path.

Within the path specified by 'fs_column_path', files are stored in
sub-directories based on the first 2 characters of the unique file names.
Up to 256 sub-directories will be created, as needed. Override
'_fs_column_dirs' in a derived class to change this behavior.

'fs_new_on_update' will create a new file name if the file has been
updated.

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
%doc Changes README

%changelog
