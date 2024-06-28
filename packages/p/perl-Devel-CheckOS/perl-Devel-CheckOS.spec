#
# spec file for package perl-Devel-CheckOS
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Devel-CheckOS
Name:           perl-Devel-CheckOS
Version:        2.40.0
Release:        0
# 2.04 -> normalize -> 2.40.0
%define cpan_version 2.04
#Upstream: SUSE-Public-Domain
License:        Artistic-1.0 OR GPL-2.0-only
Summary:        Check what OS we're running on
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:  perl(File::Find::Rule) >= 0.28
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warnings)
Requires:       perl(File::Find::Rule) >= 0.28
Requires:       perl(File::Temp) >= 0.19
Requires:       perl(Test::More) >= 0.88
Requires:       perl(Test::Warnings)
Provides:       perl(Devel::AssertOS) = 1.21
Provides:       perl(Devel::AssertOS::AIX) = 1.2
Provides:       perl(Devel::AssertOS::Alias::MacOS) = 1.0
Provides:       perl(Devel::AssertOS::Amiga) = 1.2
Provides:       perl(Devel::AssertOS::Android) = 1.2
Provides:       perl(Devel::AssertOS::Apple) = 1.3
Provides:       perl(Devel::AssertOS::BSDOS) = 1.2
Provides:       perl(Devel::AssertOS::BeOS) = 1.4
Provides:       perl(Devel::AssertOS::Bitrig) = 1.0
Provides:       perl(Devel::AssertOS::Cygwin) = 1.3
Provides:       perl(Devel::AssertOS::DEC) = 1.4
Provides:       perl(Devel::AssertOS::DGUX) = 1.2
Provides:       perl(Devel::AssertOS::DragonflyBSD) = 1.2
Provides:       perl(Devel::AssertOS::Dynix) = 1.2
Provides:       perl(Devel::AssertOS::EBCDIC) = 1.0
Provides:       perl(Devel::AssertOS::FreeBSD) = 1.2
Provides:       perl(Devel::AssertOS::GNUkFreeBSD) = 1.1
Provides:       perl(Devel::AssertOS::HPUX) = 1.2
Provides:       perl(Devel::AssertOS::HWCapabilities::Int32) = 1.0
Provides:       perl(Devel::AssertOS::HWCapabilities::Int64) = 1.0
Provides:       perl(Devel::AssertOS::Haiku) = 1.1
Provides:       perl(Devel::AssertOS::Hurd) = 1.0
Provides:       perl(Devel::AssertOS::Interix) = 1.2
Provides:       perl(Devel::AssertOS::Irix) = 1.2
Provides:       perl(Devel::AssertOS::Linux) = 1.3
Provides:       perl(Devel::AssertOS::Linux::Alma) = 1.0.0
Provides:       perl(Devel::AssertOS::Linux::Alpine) = 1.100.0
Provides:       perl(Devel::AssertOS::Linux::Arch) = 1.0.0
Provides:       perl(Devel::AssertOS::Linux::Centos) = 1.0.0
Provides:       perl(Devel::AssertOS::Linux::Debian) = 1.2
Provides:       perl(Devel::AssertOS::Linux::Devuan) = 1.100.0
Provides:       perl(Devel::AssertOS::Linux::Elementary) = 1.100.0
Provides:       perl(Devel::AssertOS::Linux::Fedora) = 1.0.0
Provides:       perl(Devel::AssertOS::Linux::Gentoo) = 1.0.0
Provides:       perl(Devel::AssertOS::Linux::NixOS) = 1.0.0
Provides:       perl(Devel::AssertOS::Linux::OpenSUSE) = 1.0.0
Provides:       perl(Devel::AssertOS::Linux::Oracle) = 1.0.0
Provides:       perl(Devel::AssertOS::Linux::PopOS) = 1.0.0
Provides:       perl(Devel::AssertOS::Linux::RHEL) = 1.0.0
Provides:       perl(Devel::AssertOS::Linux::Raspbian) = 1.100.0
Provides:       perl(Devel::AssertOS::Linux::RealDebian) = 1.100.0
Provides:       perl(Devel::AssertOS::Linux::Redhat) = 1.0.0
Provides:       perl(Devel::AssertOS::Linux::Rocky) = 1.0.0
Provides:       perl(Devel::AssertOS::Linux::SLES) = 1.0.0
Provides:       perl(Devel::AssertOS::Linux::SUSE) = 1.0.0
Provides:       perl(Devel::AssertOS::Linux::Slackware) = 1.0.0
Provides:       perl(Devel::AssertOS::Linux::Ubuntu) = 1.200.0
Provides:       perl(Devel::AssertOS::Linux::UnknownDebianLike) = 1.0
Provides:       perl(Devel::AssertOS::Linux::v2_6) = 1.3
Provides:       perl(Devel::AssertOS::MPEiX) = 1.2
Provides:       perl(Devel::AssertOS::MSDOS) = 1.2
Provides:       perl(Devel::AssertOS::MSWin32) = 1.3
Provides:       perl(Devel::AssertOS::MSYS) = 1.0
Provides:       perl(Devel::AssertOS::MacOSX) = 1.3
Provides:       perl(Devel::AssertOS::MacOSX::v10_0) = 1.0
Provides:       perl(Devel::AssertOS::MacOSX::v10_1) = 1.0
Provides:       perl(Devel::AssertOS::MacOSX::v10_10) = 1.0
Provides:       perl(Devel::AssertOS::MacOSX::v10_11) = 1.0
Provides:       perl(Devel::AssertOS::MacOSX::v10_12) = 1.0
Provides:       perl(Devel::AssertOS::MacOSX::v10_13) = 1.0
Provides:       perl(Devel::AssertOS::MacOSX::v10_14) = 1.0
Provides:       perl(Devel::AssertOS::MacOSX::v10_15) = 1.0
Provides:       perl(Devel::AssertOS::MacOSX::v10_2) = 1.0
Provides:       perl(Devel::AssertOS::MacOSX::v10_3) = 1.0
Provides:       perl(Devel::AssertOS::MacOSX::v10_4) = 1.4
Provides:       perl(Devel::AssertOS::MacOSX::v10_5) = 1.0
Provides:       perl(Devel::AssertOS::MacOSX::v10_6) = 1.0
Provides:       perl(Devel::AssertOS::MacOSX::v10_7) = 1.0
Provides:       perl(Devel::AssertOS::MacOSX::v10_8) = 1.0
Provides:       perl(Devel::AssertOS::MacOSX::v10_9) = 1.0
Provides:       perl(Devel::AssertOS::MacOSX::v11) = 1.0
Provides:       perl(Devel::AssertOS::MacOSX::v12) = 1.0
Provides:       perl(Devel::AssertOS::MacOSX::v13) = 1.0
Provides:       perl(Devel::AssertOS::MacOSX::v14) = 1.0.0
Provides:       perl(Devel::AssertOS::MacOSclassic) = 1.2
Provides:       perl(Devel::AssertOS::MachTen) = 1.2
Provides:       perl(Devel::AssertOS::MicrosoftWindows) = 1.4
Provides:       perl(Devel::AssertOS::MidnightBSD) = 1.1
Provides:       perl(Devel::AssertOS::Minix) = 1.0
Provides:       perl(Devel::AssertOS::MirOSBSD) = 1.2
Provides:       perl(Devel::AssertOS::NeXT) = 1.2
Provides:       perl(Devel::AssertOS::NetBSD) = 1.2
Provides:       perl(Devel::AssertOS::Netware) = 1.2
Provides:       perl(Devel::AssertOS::OS2) = 1.1
Provides:       perl(Devel::AssertOS::OS390) = 1.2
Provides:       perl(Devel::AssertOS::OS400) = 1.2
Provides:       perl(Devel::AssertOS::OSF) = 1.2
Provides:       perl(Devel::AssertOS::OSFeatures::POSIXShellRedirection) = 1.4
Provides:       perl(Devel::AssertOS::OSFeatures::Systemd) = 1.0
Provides:       perl(Devel::AssertOS::OpenBSD) = 1.2
Provides:       perl(Devel::AssertOS::POSIXBC) = 1.2
Provides:       perl(Devel::AssertOS::QNX) = 1.2
Provides:       perl(Devel::AssertOS::QNX::Neutrino) = 1.1
Provides:       perl(Devel::AssertOS::QNX::v4) = 1.1
Provides:       perl(Devel::AssertOS::RISCOS) = 1.2
Provides:       perl(Devel::AssertOS::Realtime) = 1.2
Provides:       perl(Devel::AssertOS::SCO) = 1.2
Provides:       perl(Devel::AssertOS::Solaris) = 1.2
Provides:       perl(Devel::AssertOS::Sun) = 1.3
Provides:       perl(Devel::AssertOS::SunOS) = 1.2
Provides:       perl(Devel::AssertOS::SysVr4) = 1.2
Provides:       perl(Devel::AssertOS::SysVr5) = 1.2
Provides:       perl(Devel::AssertOS::Unicos) = 1.2
Provides:       perl(Devel::AssertOS::Unix) = 1.6
Provides:       perl(Devel::AssertOS::VMESA) = 1.2
Provides:       perl(Devel::AssertOS::VMS) = 1.2
Provides:       perl(Devel::AssertOS::VOS) = 1.2
Provides:       perl(Devel::AssertOS::iOS) = 1.0
Provides:       perl(Devel::CheckOS) = %{version}
Provides:       perl(Devel::CheckOS::Helpers::LinuxOSrelease) = 1.0.0
%undefine       __perllib_provides
%{perl_requires}

%description
A learned sage once wrote on IRC:

   $^O is stupid and ugly, it wears its pants as a hat

Devel::CheckOS provides a more friendly interface to $^O, and also lets you
check for various OS "families" such as "Unix", which includes things like
Linux, Solaris, AIX etc.

It spares perl the embarrassment of wearing its pants on its head by
covering them with a splendid Fedora.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc CHANGELOG README TODO
%license ARTISTIC.txt GPL2.txt

%changelog
