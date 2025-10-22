#
# spec file for package perl-Parallel-ForkManager
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name Parallel-ForkManager
Name:           perl-Parallel-ForkManager
Version:        2.40.0
Release:        0
# 2.04 -> normalize -> 2.40.0
%define cpan_version 2.04
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Simple parallel processing fork manager
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moo) >= 1.1
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Warn)
Requires:       perl(Moo) >= 1.1
Requires:       perl(Moo::Role)
Provides:       perl(Parallel::ForkManager) = %{version}
Provides:       perl(Parallel::ForkManager::Child) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module is intended for use in operations that can be done in parallel
where the number of processes to be forked off should be limited. Typical
use is a downloader which will be retrieving hundreds/thousands of files.

The code for a downloader would look something like this:

  use LWP::Simple;
  use Parallel::ForkManager;

  ...

  my @links=(
    ["http://www.foo.bar/rulez.data","rulez_data.txt"],
    ["http://new.host/more_data.doc","more_data.doc"],
    ...
  );

  ...

  # Max 30 processes for parallel download
  my $pm = Parallel::ForkManager->new(30);

  LINKS:
  foreach my $linkarray (@links) {
    $pm->start and next LINKS; # do the fork

    my ($link, $fn) = @$linkarray;
    warn "Cannot get $fn from $link"
      if getstore($link, $fn) != RC_OK;

    $pm->finish; # do the exit in the child process
  }
  $pm->wait_all_children;

First you need to instantiate the ForkManager with the "new" constructor.
You must specify the maximum number of processes to be created. If you
specify 0, then NO fork will be done; this is good for debugging purposes.

Next, use $pm->start to do the fork. $pm returns 0 for the child process,
and child pid for the parent process (see also perlfunc/fork). The "and
next" skips the internal loop in the parent process. NOTE: $pm->start dies
if the fork fails.

$pm->finish terminates the child process (assuming a fork was done in the
"start").

NOTE: You cannot use $pm->start if you are already in the child process. If
you want to manage another set of subprocesses in the child process, you
must instantiate another Parallel::ForkManager object!

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTORS doap.xml examples README.mkdn SECURITY.md

%changelog
