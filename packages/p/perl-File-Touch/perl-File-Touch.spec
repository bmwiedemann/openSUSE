#
# spec file for package perl-File-Touch
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


Name:           perl-File-Touch
Version:        0.11
Release:        0
%define cpan_name File-Touch
Summary:        Update File Access and Modification Times, Optionally Creating Files If Needed
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/File-Touch/
Source0:        http://www.cpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
%{perl_requires}

%description
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
%doc Changes LICENSE README

%changelog
