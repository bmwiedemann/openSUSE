#
# spec file for package blktrace
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{!?_without_docs: %global with_docs 1}
Name:           blktrace
Version:        1.2.0+git.20180516
Release:        0
Summary:        Block IO tracer
License:        GPL-2.0
Group:          Development/Tools/Other
Url:            http://git.kernel.dk/?p=blktrace.git;a=summary
Source0:        %{name}-%{version}.tar.xz
Patch0:         blkparse-track-smallest-sequence-read-per-device.patch
BuildRequires:  gcc
BuildRequires:  libaio-devel
# Required for older releases
BuildRequires:  xz
%if 0%{?with_docs}
BuildRequires:  texlive
BuildRequires:  texlive-latex
%if 0%{?suse_version} > 1220
BuildRequires:  texlive-amsfonts
BuildRequires:  texlive-cm
BuildRequires:  texlive-cm-super
BuildRequires:  texlive-dvipdfm
BuildRequires:  texlive-dvipdfmx
BuildRequires:  texlive-pdftex
BuildRequires:  tex(multirow.sty)
BuildRequires:  tex(placeins.sty)
%endif
%else
BuildRequires:  te_latex
BuildRequires:  tetex
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
blktrace is a block layer IO tracing mechanism which provides detailed
information about request queue operations up to user space. This is
valuable for diagnosing and fixing performance or application problems
relating to block layer io.

%prep
%setup -q
%patch0 -p1

%build
make CFLAGS="%{optflags}" all %{?with_docs: docs} -j1

%install
make DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir} install
# move blktrace to /bin (bug #300186)
mkdir -p %{buildroot}/bin
mv %{buildroot}%{_bindir}/{blktrace,blkparse,btrace} \
    %{buildroot}/bin

%files
%defattr(-,root,root)
%doc README %{?with_docs: doc/blktrace.pdf btreplay/doc/btreplay.pdf btt/doc/btt.pdf}
/bin/blktrace
/bin/blkparse
/bin/btrace
%{_bindir}/blkrawverify
%{_bindir}/bno_plot.py
%{_bindir}/btt
%{_bindir}/btrecord
%{_bindir}/btreplay
%{_bindir}/verify_blkparse
%{_bindir}/blkiomon
%{_bindir}/iowatcher
%{_mandir}/man1/blkparse.1*
%{_mandir}/man1/blkrawverify.1*
%{_mandir}/man1/bno_plot.1*
%{_mandir}/man1/btt.1*
%{_mandir}/man1/iowatcher.1*
%{_mandir}/man1/verify_blkparse.1*
%{_mandir}/man8/blktrace.8*
%{_mandir}/man8/btrace.8*
%{_mandir}/man8/btrecord.8*
%{_mandir}/man8/btreplay.8*
%{_mandir}/man8/blkiomon.8*

%changelog
