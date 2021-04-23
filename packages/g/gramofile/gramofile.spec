#
# spec file for package gramofile
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gramofile
Version:        1.6
Release:        0
Summary:        Digitize Audio Records
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Editors and Convertors
#BuildRequires:  fftw3-devel
Url:            http://www.opensourcepartners.nl/~costar/gramofile/
Source0:        http://www.opensourcepartners.nl/~costar/gramofile/gramofile-%{version}.tar.gz
Source1:        gramofile.1
Patch1:         gramofile-1.6-makefiles.dif
Patch2:         gramofile-codecleanup.dif
Patch3:         20-no-busy-wait-after-rec.dpatch
Patch4:         90_report_recording_errors.dpatch
Patch5:         20-overflow-fixes.dpatch
Patch6:         20-shell-quoting.dpatch
Patch7:         20-via-kludge.dpatch
Patch8:         20-warning-fixes.dpatch
Patch9:         30-basename-fix.dpatch
Patch10:        40-fast-swap-and-buffer.dpatch
Patch11:        50-cmf3.dpatch
Patch12:        60-bplay_in_gramo.dpatch
Patch13:        70-endian-fixes.dpatch
Patch14:        80_fix_wav_length.dpatch
Patch15:        91_rename_cdrecord_wodim.dpatch
BuildRequires:  ncurses-devel
Provides:       gramofil = %{version}-%{release}
Obsoletes:      gramofil < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Gramofile is a program to digitize audio records. Through the
application of several filters, it is possible to accomplish a
significant reduction of disturbances like ticks and scratches. Data is
saved in WAV format, making it easy to record on CD with programs like
cdrecord or xcdroast.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8
%patch9
%patch10
# Disable for now, needs to be ported to fftw3
#%%patch11
%patch12
%patch13
%patch14
%patch15

%build
make %{?_smp_mflags} CC="gcc"

%install
make CC="gcc" DESTDIR=%{buildroot} docdir=%{_docdir}/%{name} install
install -Dm644 %{SOURCE1} %{buildroot}%{_mandir}/man1/gramofile.1

%files
%defattr(-,root,root)
%{_bindir}/bplay_gramo
%{_bindir}/brec_gramo
%{_bindir}/gramofile
%{_mandir}/man1/gramofile.1*
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/ChangeLog
%{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/README
%{_docdir}/%{name}/Signproc.txt
%{_docdir}/%{name}/TODO
%{_docdir}/%{name}/Tracksplit2.txt
%{_docdir}/%{name}/Tracksplit.txt

%changelog
