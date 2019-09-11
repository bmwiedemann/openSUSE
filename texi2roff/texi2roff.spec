#
# spec file for package texi2roff
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           texi2roff
Version:        2.0
Release:        0
Summary:        Tool for converting texinfo documents to HTML
License:        SUSE-Permissive-Modify-By-Patch
Group:          Productivity/Publishing/Texinfo
Url:            http://www.nongnu.org/texi2html/
Source0:        http://mirrors.ctan.org/support/texi2roff/texi2roff-2.0.tar.gz
Source1:        http://mirrors.ctan.org/support/texi2roff/texi2roff.patch.gz
Patch1:         texi2roff-2.0.dif
Patch2:         texi2roff-2.0-gcc4.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Conflicts:      texinfo < 5.0
# Split provides: until openSUSE 13.2, texi2roff was part of the texinfo package
Provides:       texinfo:/usr/bin/texi2roff

%description
Tex­i2roff trans­lates tex­info doc­u­ments to nroff/troff (it does not deal
with Plain TeX or LaTeX sources). While the conversion is not complete, it
provides a solid basis for translating most texinfo documentation.

%prep
%setup -q 
zcat %{S:1} | patch --fuzz=%{_default_patch_fuzz} --suffix=.Bader
%patch1 -p0
%patch2 -p1

%build
RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -std=c89 -D_GNU_SOURCE"
rm -f texi2roff
make %{?_smp_mflags}

%install
doc=%{_defaultdocdir}/texi2roff
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}${doc}
install -m 755 texi2roff     %{buildroot}%{_bindir}/
install -m 755 texi2index    %{buildroot}%{_bindir}/
install -m 644 texi2roff.1   %{buildroot}%{_mandir}/man1/
ln -sf texi2roff.1           %{buildroot}%{_mandir}/man1/texi2index.1

%files
%defattr(-,root,root)
%doc Readme copyright
%{_bindir}/texi2roff
%{_bindir}/texi2index
%{_mandir}/man1/texi2roff.1.gz
%{_mandir}/man1/texi2index.1.gz

%changelog
