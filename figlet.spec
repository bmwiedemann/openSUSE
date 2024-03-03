#
# spec file for package figlet
#
# Copyright (c) 2023 SUSE LLC
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


Name:           figlet
Version:        2.2.5
Release:        0
Summary:        Tool for Creating Cool ASCII-Art Signatures
License:        BSD-3-Clause
Group:          Productivity/Text/Utilities
URL:            http://www.figlet.org/
# Patched code is built by default.
# Use rpmbuild -D 'BUILD_ORIG 1' to build original code.
%if 0%{?BUILD_ORIG}
Source0:        ftp://ftp.figlet.org/pub/figlet/program/unix/%{name}-%{version}.tar.gz
Source999:      %{name}-%{version}-patched.tar.bz2
%else
# WARNING: This is not a comment, but a real command to repack source:
#%(sh %{_sourcedir}/figlet-licpatch.sh %{_sourcedir})
Source0:        %{name}-%{version}-patched.tar.bz2
Source999:      ftp://ftp.figlet.org/pub/figlet/program/unix/%{name}-%{version}.tar.gz
%endif
Source1:        ftp://ftp.figlet.org/pub/figlet/fonts/contributed.tar.gz
Source2:        ftp://ftp.figlet.org/pub/figlet/fonts/international.tar.gz
Source3:        ftp://ftp.figlet.org/pub/figlet/fonts/ours.tar.gz
Source100:      figlet-licpatch.sh
# PATCH-FIX-OPENSUSE figlet-config.patch -- Fix installation directories
Patch0:         figlet-config.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes

%description
FIGlet can create characters in many different styles and can kern and
"smush" these characters together in various ways. FIGlet output is
generally reminiscent of the sort of "signatures" many people like to
put at the end of e-mail and UseNet messages.

%prep
%setup -q -a 1 -a 2 -a 3
cd contributed
tar -zxf Obanner-canon.tgz
rm Obanner-canon.tgz
tar -zxf Obanner.tgz
rm Obanner.tgz
cd ..
cd international
tar -zxf cjkfonts.tar.gz
rm cjkfonts.tar.gz
cd ..
%patch -P 0

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
%make_install

# For inclusion in documentation
mv contributed/bdffonts/bdf2flf.pl .
mv international/febrew .

cp -a contributed %{buildroot}%{_datadir}/figlet/
cp -a international %{buildroot}%{_datadir}/figlet/
cp -a ours %{buildroot}%{_datadir}/figlet/

%fdupes -s %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES FAQ README figfont.txt
%license LICENSE
%doc bdf2flf.pl febrew
%{_bindir}/chkfont
%{_bindir}/figlet
%{_bindir}/figlist
%{_bindir}/showfigfonts
%{_datadir}/figlet/
%doc %{_mandir}/man6/chkfont.6%{ext_man}
%doc %{_mandir}/man6/figlet.6%{ext_man}
%doc %{_mandir}/man6/figlist.6%{ext_man}
%doc %{_mandir}/man6/showfigfonts.6%{ext_man}

%changelog
