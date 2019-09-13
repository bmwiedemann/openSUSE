#
# spec file for package dvgt
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


Name:           dvgt
Version:        3.51L3
Release:        0
Summary:        A DVI Previewer
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Utilities
Source:         dvgt-3.51L3.tar.bz2
Patch0:         dvgt-3.51L3.dif
BuildRequires:  texlive-bin-devel
BuildRequires:  texlive-devel
BuildRequires:  texlive-latex
BuildRequires:  texlive-tex
Requires:       texlive

%description
Dvgt is a DVI previewer for console, terminals, and graphical terminals
like Tektronics or the good old XTerm. dvgt tries to fit the conditions
of the DVI files, therefore output on text terminals is not legible.

%prep
%setup -q
%patch0

%build
RPM_OPT_FLAGS="-std=gnu89 %{optflags} -fno-strict-aliasing -funsigned-char"
#RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wno-uninitialized -Wno-unused -pipe"
RPM_OPT_FLAGS="%{optflags} -Wno-unused -pipe"
export RPM_OPT_FLAGS
pushd src
   make -f Makefile.linux %{?_smp_mflags}
popd
pushd doc
   make %{?_smp_mflags}

%install
cd src
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install    -m 755 dvgt   %{buildroot}%{_bindir}/
install -c -m 644 dvgt.1 %{buildroot}%{_mandir}/man1/
cd ../doc
mkdir -p %{buildroot}%{_docdir}/dvgt
install -c -m 644 sysguide.dvi  %{buildroot}%{_docdir}/dvgt/
install -c -m 644 userguide.dvi %{buildroot}%{_docdir}/dvgt/
cd ../
install -c -m 644 README        %{buildroot}%{_docdir}/dvgt/
install -c -m 644 README.Linux  %{buildroot}%{_docdir}/dvgt/
install -c -m 644 README-3.51l2 %{buildroot}%{_docdir}/dvgt/
install -c -m 644 README.SUSE   %{buildroot}%{_docdir}/dvgt/

%files
%{_bindir}/dvgt
%{_mandir}/man1/dvgt.1%{ext_man}
%dir %{_docdir}/dvgt
%{_docdir}/dvgt/sysguide.dvi
%{_docdir}/dvgt/userguide.dvi
%{_docdir}/dvgt/README
%{_docdir}/dvgt/README.Linux
%{_docdir}/dvgt/README-3.51l2
%{_docdir}/dvgt/README.SUSE

%changelog
