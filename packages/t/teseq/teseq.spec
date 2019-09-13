#
# spec file for package teseq
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


Name:           teseq
Version:        1.1.1
Release:        0
Summary:        A tool for control characters and terminal control sequences
License:        GPL-3.0+
Group:          Productivity/Text/Utilities
Url:            http://www.gnu.org/software/teseq
Source:         ftp://ftp.gnu.org/pub/gnu/teseq/%{name}-%{version}.tar.xz
Source2:        ftp://ftp.gnu.org/pub/gnu/teseq/%{name}-%{version}.tar.xz.sig
Source3:        http://savannah.gnu.org/project/memberlist-gpgkeys.php?group=%{name}&download=1#/%{name}.keyring
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  pkg-config >= 0.9.0
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{?suse_version} == 1110
BuildRequires:  xz
%endif

%description
Teseq is a tool for analyzing files that contain control characters and
terminal control sequences, by printing these control sequences and their
meanings in readable English. It is intended to be useful for debugging
terminal emulators, and programs that make heavy use of advanced terminal
features such as cursor movement, coloring, and other effects.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%defattr(-,root,root)
%doc COPYING AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/%{name}.info.gz

%changelog
