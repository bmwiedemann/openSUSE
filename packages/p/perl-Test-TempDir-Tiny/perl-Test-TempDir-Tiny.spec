#
# spec file for package perl-Test-TempDir-Tiny
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           perl-Test-TempDir-Tiny
Version:        0.018
Release:        0
%define cpan_name Test-TempDir-Tiny
Summary:        Temporary directories that stick around when tests fail
License:        Apache-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-TempDir-Tiny/
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Path) >= 2.070000
BuildRequires:  perl(File::Temp) >= 0.2308
Requires:       perl(File::Path) >= 2.070000
Requires:       perl(File::Temp) >= 0.2308
%{perl_requires}

%description
This module works with Test::More to create temporary directories that
stick around if tests fail.

It is loosely based on Test::TempDir, but with less complexity, greater
portability and zero non-core dependencies. (Capture::Tiny is recommended
for testing.)

The tempdir and in_tempdir functions are exported by default.

If the current directory is writable, the root for directories will be
_./tmp_. Otherwise, a File::Temp directory will be created wherever
temporary directories are stored for your system.

Every _*.t_ file gets its own subdirectory under the root based on the test
filename, but with slashes and periods replaced with underscores. For
example, _t/foo.t_ would get a test-file-specific subdirectory
_./tmp/t_foo_t/_. Directories created by tempdir get put in that directory.
This makes it very easy to find files later if tests fail.

The test-file-specific name is consistent from run-to-run. If an old
directory already exists, it will be removed.

When the test file exits, if all tests passed, then the test-file-specific
directory is recursively removed.

If a test failed and the root directory is _./tmp_, the test-file-specific
directory sticks around for inspection. (But if the root is a File::Temp
directory, it is always discarded).

If nothing is left in _./tmp_ (i.e. no other test file failed), then
_./tmp_ is cleaned up as well (unless it's a symlink).

This module attempts to avoid race conditions due to parallel testing. In
extreme cases, the test-file-specific subdirectory might be created as a
regular File::Temp directory rather than in _./tmp_. In such a case, a
warning will be issued.

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
%doc Changes CONTRIBUTING.mkdn README
%license LICENSE

%changelog
