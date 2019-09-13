#
# spec file for package perl-Tk
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Tk
Version:        804.034
Release:        0
Summary:        Perl Tk
License:        (GPL-1.0+ or Artistic-1.0) and Zlib
Group:          Development/Libraries/Perl
Url:            http://cpan.org/modules/by-module/Tk/
Source:         http://www.cpan.org/modules/by-module/Tk/Tk-%{version}.tar.gz
Patch1:         Tk-804.029-macro.diff
Patch2:         Tk-804.029-null.diff
Patch3:         Tk-804.029-refcnt.diff
Patch4:         Tk-804.029-event.diff
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  xkeyboard-config
BuildRequires:  xorg-x11
BuildRequires:  xorg-x11-Xnest
BuildRequires:  xorg-x11-Xvfb
BuildRequires:  xorg-x11-devel
BuildRequires:  xorg-x11-fonts
BuildRequires:  xorg-x11-fonts-100dpi
BuildRequires:  xorg-x11-fonts-scalable
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
%ifnarch s390 s390x
BuildRequires:  xorg-x11-server
%endif

%description
Perl Tk is an enhancement for Perl. It combines the well structured
graphical library Tk with the powerful scripting language Perl.

%package devel
Summary:        Perl Tk
Group:          Development/Libraries/Perl
Requires:       %{name} = %{version}

%description devel
Perl Tk is an enhancement for Perl. It combines the well structured
graphical library Tk with the powerful scripting language Perl.

%prep
%setup -q -n Tk-%{version}
%patch1
%patch2
%patch3
%patch4

%build
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
#disable test that require Test
mv t/browseentry-grabtest.t t/browseentry-grabtest.tt
mv t/browseentry2.t t/browseentry2.tt
mv t/entry.t t/entry.tt
mv t/listbox.t t/listbox.tt
# disable test that seems to fail at random
mv t/fileevent2.t t/fileevent2.tt
perl Makefile.PL XFT=1
make %{?_smp_mflags} CFLAGS="%{optflags} -Wall -fpic"

%check
Xvfb :95 -screen 0 1280x1024x24 & #430569
trap "kill $!" EXIT
sleep 5
DISPLAY=:95 make test %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install_vendor
%perl_process_packlist
rm -f %{buildroot}/%{perl_vendorarch}/fix_4_os2.pl

%files
%defattr(-,root,root)
%doc COPYING Change.log Changes Funcs.doc INSTALL PPM-HowTo README* ToDo VERSIONS
%{_mandir}/man?/*
%{_bindir}/*
%{perl_vendorarch}/Tie
%{perl_vendorarch}/Tk
%{perl_vendorarch}/Tk.*
%{perl_vendorarch}/auto/Tk
%exclude %{perl_vendorarch}/Tk/pTk
%exclude %{perl_vendorarch}/Tk/*.h

%files devel
%defattr(-,root,root)
%{perl_vendorarch}/Tk/pTk
%{perl_vendorarch}/Tk/*.h

%changelog
