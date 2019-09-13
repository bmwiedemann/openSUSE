#
# spec file for package perl-Time-Duration
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Time-Duration
Version:        1.210000
Release:        0
%define cpan_version 1.21
Provides:       perl(Time::Duration) = 1.210000
%define cpan_name Time-Duration
Summary:        Rounded or exact English expression of durations
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module provides functions for expressing durations in rounded or exact
terms.

In the first example in the Synopsis, using duration($interval_seconds):

If the 'time() - $start_time' is 3 seconds, this prints "Runtime: *3
seconds*.". If it's 0 seconds, it's "Runtime: *0 seconds*.". If it's 1
second, it's "Runtime: *1 second*.". If it's 125 seconds, you get "Runtime:
*2 minutes and 5 seconds*.". If it's 3820 seconds (which is exactly 1h, 3m,
40s), you get it rounded to fit within two expressed units: "Runtime: *1
hour and 4 minutes*.". Using duration_exact instead would return "Runtime:
*1 hour, 3 minutes, and 40 seconds*".

In the second example in the Synopsis, using ago($interval_seconds):

If the $age is 3 seconds, this prints "_file_ was modified *3 seconds
ago*". If it's 0 seconds, it's "_file_ was modified *just now*", as a
special case. If it's 1 second, it's "from *1 second ago*". If it's 125
seconds, you get "_file_ was modified *2 minutes and 5 seconds ago*". If
it's 3820 seconds (which is exactly 1h, 3m, 40s), you get it rounded to fit
within two expressed units: "_file_ was modified *1 hour and 4 minutes
ago*". Using ago_exact instead would return "_file_ was modified *1 hour, 3
minutes, and 40 seconds ago*". And if the file's modtime is, surprisingly,
three seconds into the future, $age is -3, and you'll get the equally and
appropriately surprising "_file_ was modified *3 seconds from now*."

%prep
%setup -q -n %{cpan_name}-%{cpan_version}

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
%doc Changes README
%license LICENSE

%changelog
