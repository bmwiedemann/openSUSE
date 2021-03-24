#
# spec file for package perl-File-Touch
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name File-Touch
Name:           perl-File-Touch
Version:        0.12
Release:        0
Summary:        Update file access and modification times, optionally creating files if needed
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Time::HiRes) >= 1.9764
Requires:       perl(Time::HiRes) >= 1.9764
%{perl_requires}

%description
This module provides both a functional and OO interface for changing the
file access and modification times on files. It can optionally create the
file for you, if it doesn't exist.

*Note*: you should specify a minimum version of 0.12, as per the SYNOPSIS,
as that fixed an issue that affected systems that have sub-second
granularity on those file times.

Here's a list of arguments that can be used with the object-oriented
contruction:

* atime_only => [0|1]

If nonzero, change only the access time of files. Default is zero.

* mtime_only => [0|1]

If nonzero, change only the modification time of files. Default is zero.

* no_create => [0|1]

If nonzero, do not create new files. Default is zero.

* reference => $reference_file

If defined, use timestamps from this file instead of current time. The
timestamps are read from the reference file when the object is created, not
when '<-'touch>> is invoked. Default is undefined.

* time => $time

If defined, then this value will be used for both access time and
modification time, whichever of those are set. This time is overridden by
the 'atime' and 'mtime' arguments, if you use them.

* atime => $time

If defined, use this time (in epoch seconds) instead of current time for
access time.

* mtime => $time

If defined, use this time (in epoch seconds) instead of current time for
modification time.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
