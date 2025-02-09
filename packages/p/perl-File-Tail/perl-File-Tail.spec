#
# spec file for package perl-File-Tail
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name File-Tail
Name:           perl-File-Tail
Version:        1.300.0
Release:        0
# 1.3 -> normalize -> 1.300.0
%define cpan_version 1.3
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl extension for reading from continously updated files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MG/MGRABNAR/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(File::Tail) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The primary purpose of File::Tail is reading and analysing log files while
they are being written, which is especialy usefull if you are monitoring
the logging process with a tool like Tobias Oetiker's MRTG.

The module tries very hard NOT to "busy-wait" on a file that has little
traffic. Any time it reads new data from the file, it counts the number of
new lines, and divides that number by the time that passed since data were
last written to the file before that. That is considered the average time
before new data will be written. When there is no new data to read,
'File::Tail' sleeps for that number of seconds. Thereafter, the waiting
time is recomputed dynamicaly. Note that 'File::Tail' never sleeps for more
than the number of seconds set by 'maxinterval'.

If the file does not get altered for a while, 'File::Tail' gets suspicious
and startschecking if the file was truncated, or moved and recreated. If
anything like that had happened, 'File::Tail' will quietly reopen the file,
and continue reading. The only way to affect what happens on reopen is by
setting the reset_tail parameter (see below). The effect of this is that
the scripts need not be aware when the logfiles were rotated, they will
just quietly work on.

Note that the sleep and time used are from Time::HiRes, so this module
should do the right thing even if the time to sleep is less than one
second.

The logwatch script (also included) demonstrates several ways of calling
the methods.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes logwatch README select_demo Tail.pm.debug

%changelog
