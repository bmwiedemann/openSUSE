#
# spec file for package perl-POE
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-POE
Version:        1.368
Release:        0
%define cpan_name POE
Summary:        Portable multitasking and networking framework for any event loop
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO) >= 1.24
BuildRequires:  perl(IO::Handle) >= 1.27
BuildRequires:  perl(IO::Pipely) >= 0.005
BuildRequires:  perl(IO::Tty) >= 1.08
BuildRequires:  perl(POE::Test::Loops) >= 1.360
BuildRequires:  perl(Storable) >= 2.16
Requires:       perl(IO) >= 1.24
Requires:       perl(IO::Handle) >= 1.27
Requires:       perl(IO::Pipely) >= 0.005
Requires:       perl(IO::Tty) >= 1.08
Requires:       perl(POE::Test::Loops) >= 1.360
Requires:       perl(Storable) >= 2.16
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  netcfg
# MANUAL END

%description
POE is a framework for cooperative, event driven multitasking and
networking in Perl. Other languages have similar frameworks. Python has
Twisted. TCL has "the event loop".

POE provides a unified interface for several other event loops, including
select(), IO::Poll, Glib, Gtk, Tk, Wx, and Gtk2. Many of these event loop
interfaces were written by others, with the help of POE::Test::Loops. They
may be found on the CPAN.

POE achieves its high degree of portability to different operating systems
and Perl versions by being written entirely in Perl. CPAN hosts optional XS
modules for POE if speed is more desirable than portability.

POE is designed in layers. Each layer builds atop the lower level ones.
Programs are free to use POE at any level of abstraction, and different
levels can be mixed and matched seamlessly within a single program.
Remember, though, that higher-level abstractions often require more
resources than lower-level ones. The conveniences they provide are not
free.

POE's bundled abstraction layers are the tip of a growing iceberg.
Sprocket, POE::Stage, and other CPAN distributions build upon this work.
You're encouraged to look around.

No matter how high you go, though, it all boils down to calls to
POE::Kernel. So your down-to-earth code can easily cooperate with
stratospheric systems.

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
%doc CHANGES examples HISTORY README TODO

%changelog
