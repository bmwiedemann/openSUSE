#
# spec file for package perl-Linux-Inotify2
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


Name:           perl-Linux-Inotify2
Version:        2.1
Release:        0
%define cpan_name Linux-Inotify2
Summary:        Scalable directory/file change notification
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(common::sense)
Requires:       perl(common::sense)
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
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
%license COPYING

%changelog
