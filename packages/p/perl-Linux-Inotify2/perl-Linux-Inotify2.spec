#
# spec file for package perl-Linux-Inotify2
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


%define cpan_name Linux-Inotify2
Name:           perl-Linux-Inotify2
Version:        2.300.0
Release:        0
# 2.3 -> normalize -> 2.300.0
%define cpan_version 2.3
#Upstream: CHECK(Artistic-1.0 or GPL-1.0-or-later)
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Scalable directory/file change notification
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(common::sense)
Requires:       perl(common::sense)
Provides:       perl(Linux::Inotify2) = %{version}
Provides:       perl(Linux::Inotify2::Event)
Provides:       perl(Linux::Inotify2::Watch)
%undefine       __perllib_provides
%{perl_requires}

%description
This module implements an interface to the Linux 2.6.13 and later Inotify
file/directory change notification system.

It has a number of advantages over the Linux::Inotify module:

   - it is portable (Linux::Inotify only works on x86)
   - the equivalent of fullname works correctly
   - it is better documented
   - it has callback-style interface, which is better suited for
     integration.

As for the inotify API itself - it is a very tricky, and somewhat
unreliable API. For a good overview of the challenges you might run into,
see this LWN article: https://lwn.net/Articles/605128/.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license COPYING

%changelog
