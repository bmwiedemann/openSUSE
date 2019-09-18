#
# spec file for package os-autoinst
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


Name:           os-autoinst
Version:        4.5.1568227729.687c4ca8
Release:        0
Summary:        OS-level test automation
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
Url:            https://github.com/os-autoinst/os-autoinst
Source0:        %{name}-%{version}.tar.xz
# Force OBS to resolve choices on opencv-devel
#!BuildIgnore: opencv3-devel
%{perl_requires}
%define build_requires autoconf automake gcc-c++ libtool pkgconfig(opencv) pkg-config perl(Module::CPANfile) pkgconfig(fftw3) pkgconfig(libpng) pkgconfig(sndfile) pkgconfig(theoraenc) make
%define requires perl(B::Deparse) perl(Mojolicious) >= 7.92, perl(Mojo::IOLoop::ReadWriteProcess) >= 0.23, perl(Carp::Always) perl(Data::Dump) perl(Data::Dumper) perl(Crypt::DES) perl(JSON) perl(autodie) perl(Class::Accessor::Fast) perl(Exception::Class) perl(File::Touch) perl(File::Which) perl(IPC::Run::Debug) perl(Net::DBus) perl(Net::SNMP) perl(Net::IP) perl(IPC::System::Simple) perl(Net::SSH2) perl(XML::LibXML) perl(XML::SemanticDiff) perl(JSON::XS) perl(List::MoreUtils) perl(Mojo::IOLoop::ReadWriteProcess) perl(Socket::MsgHdr) perl(Cpanel::JSON::XS) perl(IO::Scalar) perl(Try::Tiny) perl-base
%define requires_not_needed_in_tests qemu >= 2.0.0, /usr/bin/qemu-img, git-core optipng
# all requirements needed by the tests, do not require on this in the package
# itself or any sub-packages
%define test_requires %build_requires %requires perl(Perl::Tidy) perl(Test::Compile) perl(Test::Exception) perl(Test::Output) perl(Test::Fatal) perl(Test::Warnings) perl(Pod::Coverage) perl(Test::Pod) perl(Test::MockModule) perl(Test::MockObject) perl(Devel::Cover) perl(Test::Mock::Time) qemu-tools
%define devel_requires %test_requires %requires_not_needed_in_tests
BuildRequires:  %test_requires
Requires:       %requires
Recommends:     tesseract-ocr
Recommends:     /usr/bin/xkbcomp /usr/bin/Xvnc dumponlyconsole
Requires(pre):  %{_bindir}/getent
Requires(pre):  %{_sbindir}/useradd
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The OS-autoinst project aims at providing a means to run fully
automated tests. Especially to run tests of basic and low-level
operating system components such as bootloader, kernel, installer
and upgrade, which can not easily and safely be tested with other
automated testing frameworks. However, it can just as well be used
to test firefox and openoffice operation on top of a newly
installed OS.

%package devel
Summary:        Development package pulling in all build+test dependencies
Group:          Development/Tools/Other
Requires:       %devel_requires

%description devel
Development package pulling in all build+test dependencies.

%package openvswitch
Summary:        Openvswitch support for os-autoinst
Group:          Development/Tools/Other
Requires:       openvswitch
Requires:       openvswitch-switch
Requires:       os-autoinst

%description openvswitch
This package contains openvswitch support for os-autoinst.

%prep
%setup -q
sed -e 's,/bin/env python,/bin/python,' -i crop.py
# Replace version number from git to what's reported by the package
sed  -i 's/ my $thisversion = qx{git.*rev-parse HEAD}.*;/ my $thisversion = "%{version}";/' isotovideo

%build
mkdir -p m4
autoreconf -f -i
%configure --docdir=%{_docdir}/%{name}
make INSTALLDIRS=vendor %{?_smp_mflags}

%install
%make_install INSTALLDIRS=vendor
# only internal stuff
rm %{buildroot}/usr/lib/os-autoinst/tools/{tidy,check_coverage,absolutize}
rm -r %{buildroot}/usr/lib/os-autoinst/tools/lib/perlcritic
#
ls -lR %buildroot
find %{buildroot} -type f -name .packlist -print0 | xargs -0 --no-run-if-empty rm -f
find %{buildroot} -depth -type d -and -not -name distri -print0 | xargs -0 --no-run-if-empty rmdir 2>/dev/null || true
%perl_gen_filelist
#
# service symlink
mkdir -p %{buildroot}%{_sbindir}
ln -s ../sbin/service %{buildroot}%{_sbindir}/rcos-autoinst-openvswitch
#
# we need the stale symlinks to point to git
export NO_BRP_STALE_LINK_ERROR=yes

%check
# disable code quality checks - not worth the time for package builds
sed '/perlcritic/d' -i Makefile
sed '/Perl::Critic/d' -i cpanfile
sed '/tidy/d' -i Makefile
rm tools/lib/perlcritic/Perl/Critic/Policy/*.pm

# don't require qemu within OBS
for i in 18-qemu-options 18-backend-qemu 99-full-stack; do
    cp t/05-pod.t t/${i}.t
done

# should work offline
for p in $(cpanfile-dump); do rpm -q --whatprovides "perl($p)"; done
make check VERBOSE=1

%pre openvswitch
%service_add_pre os-autoinst-openvswitch.service

%post openvswitch
%service_add_post os-autoinst-openvswitch.service

%preun openvswitch
%service_del_preun os-autoinst-openvswitch.service

%postun openvswitch
%service_del_postun os-autoinst-openvswitch.service

%files -f %{name}.files
%defattr(-,root,root)
%{_docdir}/os-autoinst
%dir %{_libexecdir}/os-autoinst
%{_libexecdir}/os-autoinst/videoencoder
%{_libexecdir}/os-autoinst/basetest.pm
#
%{_libexecdir}/os-autoinst/dmidata
#
%{_libexecdir}/os-autoinst/bmwqemu.pm
%{_libexecdir}/os-autoinst/commands.pm
%{_libexecdir}/os-autoinst/distribution.pm
%{_libexecdir}/os-autoinst/testapi.pm
%{_libexecdir}/os-autoinst/mmapi.pm
%{_libexecdir}/os-autoinst/lockapi.pm
%{_libexecdir}/os-autoinst/cv.pm
%{_libexecdir}/os-autoinst/ocr.pm
%{_libexecdir}/os-autoinst/needle.pm
%{_libexecdir}/os-autoinst/osutils.pm
%{_libexecdir}/os-autoinst/myjsonrpc.pm
%{_libexecdir}/os-autoinst/backend
%{_libexecdir}/os-autoinst/OpenQA
%{_libexecdir}/os-autoinst/consoles
%dir %{_libexecdir}/os-autoinst/tools
%{_libexecdir}/os-autoinst/tools/preparepool
%{_libexecdir}/os-autoinst/autotest.pm
%{_libexecdir}/os-autoinst/crop.py

%files openvswitch
%defattr(-,root,root)
%{_libexecdir}/os-autoinst/os-autoinst-openvswitch
/usr/lib/systemd/system/os-autoinst-openvswitch.service
%config /etc/dbus-1/system.d/org.opensuse.os_autoinst.switch.conf
%{_sbindir}/rcos-autoinst-openvswitch

%files devel

%changelog
