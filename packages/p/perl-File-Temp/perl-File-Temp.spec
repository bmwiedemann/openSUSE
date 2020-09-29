#
# spec file for package perl-File-Temp
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           perl-File-Temp
Version:        0.2310
Release:        0
%define cpan_name File-Temp
Summary:        Return name and handle of a temporary file safely
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Path) >= 2.060000
BuildRequires:  perl(parent) >= 0.221
Requires:       perl(File::Path) >= 2.060000
Requires:       perl(parent) >= 0.221
%{perl_requires}

%description
'File::Temp' can be used to create and open temporary files in a safe way.
There is both a function interface and an object-oriented interface. The
File::Temp constructor or the tempfile() function can be used to return the
name and the open filehandle of a temporary file. The tempdir() function
can be used to create a temporary directory.

The security aspect of temporary file creation is emphasized such that a
filehandle and filename are returned together. This helps guarantee that a
race condition can not occur where the temporary file is created by another
process between checking for the existence of the file and its opening.
Additional security levels are provided to check, for example, that the
sticky bit is set on world writable directories. See "safe_level" for more
information.

For compatibility with popular C library functions, Perl implementations of
the mkstemp() family of functions are provided. These are, mkstemp(),
mkstemps(), mkdtemp() and mktemp().

Additionally, implementations of the standard POSIX tmpnam() and tmpfile()
functions are provided if required.

Implementations of mktemp(), tmpnam(), and tempnam() are provided, but
should be used with caution since they return only a filename that was
valid when function was called, so cannot guarantee that the file will not
exist by the time the caller opens the filename.

Filehandles returned by these functions support the seekable methods.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
