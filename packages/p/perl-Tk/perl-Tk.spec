#
# spec file for package perl-Tk
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


%define cpan_name Tk
Name:           perl-Tk
Version:        804.036
Release:        0
#Upstream: SUSE-Public-Domain
License:        (Artistic-1.0 OR GPL-1.0-or-later) AND Zlib
Summary:        Tk - a Graphical User Interface Toolkit
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         Tk-804.029-event.diff
Patch1:         Tk-804.029-macro.diff
Patch2:         Tk-804.029-null.diff
Patch3:         Tk-804.029-refcnt.diff
Patch4:         Tk-804.036-fix-strlen-vs-int-pointer-confusion.patch
# PATCH-FIX-UPSTREAM fix gcc14 build error https://github.com/eserte/perl-tk/issues/98
Patch5:         Tk-804-config-C99.diff
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  liberation-fonts
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  xkeyboard-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xt)
%if 0%{?suse_version} >= 01550
BuildRequires:  xvfb-run
BuildRequires:  perl(Devel::Leak)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
%endif
BuildRequires:  xorg-x11-Xnest
BuildRequires:  xorg-x11-Xvfb
BuildRequires:  xorg-x11-fonts
BuildRequires:  xorg-x11-fonts-100dpi
BuildRequires:  xorg-x11-fonts-scalable
BuildRequires:  zlib-devel
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
%ifnarch s390 s390x
BuildRequires:  xorg-x11-server
%endif
# MANUAL END

%description
This a re-port of a perl interface to Tk8.4.
C code is derived from Tcl/Tk8.4.5.
It also includes all the C code parts of Tix8.1.4 from SourceForge.
The perl code corresponding to Tix's Tcl code is not fully implemented.

Perl API is essentially the same as Tk800 series Tk800.025 but has not
been verified as compliant. There ARE differences see pod/804delta.pod.

%prep
%autosetup  -n %{cpan_name}-%{version} -p0

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644
# MANUAL BEGIN
find . -type f -name "Tcl-pTk" -print0 | xargs -0 chmod +x
find . -type f -name "mkVFunc" -print0 | xargs -0 chmod +x
# MANUAL END

%build
# Work around boo#1225909, see the bug for more details
%global optflags %{optflags} -fpermissive

find -name "*.orig" -exec rm {} \;
for file in `find -type f` ; do
  grep -q "%{_prefix}/local/bin/perl" $file && \
      sed -i -e "s@%{_prefix}/local/bin/perl@%{_bindir}/perl@g" "$file"
  grep -q "%{_prefix}/local/bin/nperl" $file && \
      sed -i -e "s@%{_prefix}/local/bin/nperl@%{_bindir}/nperl@g" "$file"
  grep -q "#!\s*/bin/perl" $file && \
      sed -i -e "s@/bin/perl@%{_bindir}/perl@g" "$file"
  grep -q "#!\s*/tools/local/perl" $file && \
      sed -i -e "s@/tools/local/perl@%{_bindir}/perl@g" "$file"
  grep -q "%{_prefix}/local/bin/new/perl" $file && \
      sed -i -e "s@%{_prefix}/local/bin/new/perl@%{_bindir}/perl@g" "$file"
done
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" XFT=1
make %{?_smp_mflags} CFLAGS="%{optflags} -Wall -fpic"

%check
%if 0%{?suse_version} >= 01550
xvfb-run -a make test  %{?_smp_mflags} V=1
%else
Xvfb :95 -screen 0 1280x1024x24 & #430569
trap "kill $!" EXIT
sleep 5
DISPLAY=:95 make test %{?_smp_mflags}
%endif

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Change.log Changes examples Funcs.doc PPM-HowTo README README.linux ToDo VERSIONS
%license COPYING
%exclude %{perl_vendorarch}/Tk/pTk
%exclude %{perl_vendorarch}/Tk/*.h

%package devel
Summary:        Development files for perl-Tk
Requires:       %{name} = %{version}

%description devel
Development files for Tk - a graphical user interface toolkit for Perl

%files devel
%{perl_vendorarch}/Tk/pTk
%{perl_vendorarch}/Tk/*.h

%changelog
