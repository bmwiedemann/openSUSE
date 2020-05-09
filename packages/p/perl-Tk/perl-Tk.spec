#
# spec file for package perl-Tk
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Tk
Version:        804.035
Release:        0
%define cpan_name Tk
Summary:        Graphical user interface toolkit for Perl
License:        (GPL-1.0-or-later OR Artistic-1.0) AND Zlib
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/Tk
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
# MANUAL BEGIN
Patch1:         Tk-804.029-macro.diff
Patch2:         Tk-804.029-null.diff
Patch3:         Tk-804.029-refcnt.diff
Patch4:         Tk-804.029-event.diff
# MANUAL END
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
# MANUAL BEGIN
BuildRequires:  libX11-devel
BuildRequires:  libXft-devel
BuildRequires:  liberation-fonts
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  xkeyboard-config
%if 0%{?suse_version} >= 01550
BuildRequires:  xvfb-run
BuildRequires:  perl(Devel::Leak)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
%endif
BuildRequires:  xorg-x11
BuildRequires:  xorg-x11-Xnest
BuildRequires:  xorg-x11-Xvfb
BuildRequires:  xorg-x11-devel
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
%{perl_requires}

%description
Tk - a graphical user interface toolkit for Perl

%package devel
Summary:        Development files for perl-Tk
Group:          Development/Libraries/Perl
Requires:       %{name} = %{version}

%description devel
Development files for Tk - a graphical user interface toolkit for Perl

%prep
%setup -q -n %{cpan_name}-%{version}
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644
find . -type f -name "Tcl-pTk" -print0 | xargs -0 chmod +x
find . -type f -name "mkVFunc" -print0 | xargs -0 chmod +x

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
make DESTDIR=%{buildroot} install_vendor
%perl_process_packlist
rm -f %{buildroot}/%{perl_vendorarch}/fix_4_os2.pl
find %{buildroot} -type f -name '*.bs' -size 0 -delete

%files
%defattr(-,root,root,755)
%license COPYING pTk/*license*
%doc Changes Change.log Funcs.doc PPM-HowTo README README.linux ToDo demos/widget VERSIONS
%doc blib/man1/widget.1
%{_mandir}/man?/*
%{_bindir}/p*
%{_bindir}/tkjpeg
%{_bindir}/gedi
%{_bindir}/widget
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
