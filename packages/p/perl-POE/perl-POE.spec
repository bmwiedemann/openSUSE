#
# spec file for package perl-POE
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-POE
Version:        1.367
Release:        0
%define cpan_name POE
Summary:        Portable Multitasking and Networking Framework for Any Event Loop
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/POE/
Source0:        http://www.cpan.org/authors/id/R/RC/RCAPUTO/%{cpan_name}-%{version}.tar.gz
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
select(), IO::Poll, the Glib manpage, the Gtk manpage, the Tk manpage, the
Wx manpage, and the Gtk2 manpage. Many of these event loop interfaces were
written by others, with the help of POE::Test::Loops. They may be found on
the CPAN.

POE achieves its high degree of portability to different operating systems
and Perl versions by being written entirely in Perl. CPAN hosts optional XS
modules for POE if speed is more desirable than portability.

POE is designed in layers. Each layer builds atop the lower level ones.
Programs are free to use POE at any level of abstraction, and different
levels can be mixed and matched seamlessly within a single program.
Remember, though, that higher-level abstractions often require more
resources than lower-level ones. The conveniences they provide are not
free.

POE's bundled abstraction layers are the tip of a growing iceberg. the
Sprocket manpage, POE::Stage, and other CPAN distributions build upon this
work. You're encouraged to look around.

No matter how high you go, though, it all boils down to calls to
POE::Kernel. So your down-to-earth code can easily cooperate with
stratospheric systems.

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
%doc CHANGES examples HISTORY README TODO

%changelog
