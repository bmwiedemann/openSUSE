#
# spec file for package LiE
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


Name:           LiE
Version:        2.2.2
Release:        0
# See URL for Licensing, source contains no License file, hence appropriate COPYRIGHT file has been manually added
Summary:        A Computer algebra package for Lie group computations
License:        LGPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://young.sp2mi.univ-poitiers.fr/~marc/LiE/
Source0:        http://young.sp2mi.univ-poitiers.fr/~marc/LiE/conLiE.tar.gz
Source1:        COPYING
Source2:        %{name}-rpmlintrc
Patch1:         LiE-2.2.2-date-time.patch
# PATCH-FIX-UPSTREAM bmwiedemann -- initialize memory (boo#1061220)
Patch2:         LiE-2.2.2-memory-init.patch
Patch3:         reproducible-noaslr.patch
BuildRequires:  bison
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  readline-devel
BuildRequires:  texlive-dvips
BuildRequires:  texlive-latex-bin
Recommends:     %{name}-doc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
LiE is a computer algebra system that is specialised in computations
involving (reductive) Lie groups and their representations.

%package doc
Summary:        A Computer algebra package for Lie group computations
Group:          Documentation/Other

%description doc
LiE is a computer algebra system that is specialised in computations
involving (reductive) Lie groups and their representations.

This packlage provides documentation for %{name}.

%prep
%autosetup -p1 -n %{name}

%build
# parallel build fails
make

%install
%make_install
cat << EOF >> lie-wrapper
#!/bin/bash
LD=%{_libdir}/%{name}
exec \$LD/lie initfile \$LD
EOF

dvipdf manual/manual.dvi manual.pdf

install -D -m0755 Lie.exe %{buildroot}%{_libdir}/%{name}/lie
install -D lie-wrapper %{buildroot}%{_bindir}/lie
chmod +x %{buildroot}%{_bindir}/lie
install -m0644 *.ind %{buildroot}%{_libdir}/%{name}/
install -m0644 INFO.* %{buildroot}%{_libdir}/%{name}/
mkdir -p %{buildroot}%{_docdir}/%{name}/
install -m0644 manual.pdf %{buildroot}%{_docdir}/%{name}/
install -m0644 %{SOURCE1} %{buildroot}%{_docdir}/%{name}/

%files
%defattr(-,root,root)
%doc README
%dir %{_docdir}/%{name}
%license %{_docdir}/%{name}/COPYING
%{_bindir}/lie
%{_libdir}/%{name}/
%exclude %{_docdir}/%{name}/manual.pdf

%files doc
%defattr(-,root,root)
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/manual.pdf

%changelog
