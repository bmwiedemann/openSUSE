#
# spec file for package lowdown
#
# Copyright (c) 2025 SUSE LLC
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


%global soname liblowdown2
#%%global version_string VERSION_1_1_0

Name:           lowdown
Version:        2.0.2
Release:        0
Summary:        Simple markdown translator
License:        ISC
#URL:            https://kristaps.bsd.lv/lowdown
URL:            https://github.com/kristapsdz/lowdown
#Source:         %%{name}-%%{version_string}.tar.gz
Source:         %{name}-%{version}.tar.gz
BuildRequires:  bmake
BuildRequires:  fdupes

%description
lowdown is a Markdown translator producing HTML5, roff documents in the ms and
man formats, LaTeX, gemini, OpenDocument, and terminal output.
The open source C source code has no dependencies. The tools are documented in
lowdown(1) and lowdown-diff(1), the language in lowdown(5),
and the library interface in lowdown(3).

lowdown is a fork of hoedown, although the parser and front-ends have changed
significantly.

%package -n %{soname}
Summary:        Simple markdown translator

%description -n %{soname}
lowdown is a fork of hoedown, although the parser and front-ends have changed
significantly.

%package devel
Summary:        Simple markdown translator
Requires:       %{soname} = %{version}

%description devel
lowdown is a fork of hoedown, although the parser and front-ends have changed
significantly.

%prep
#%%autosetup -p1 -n %%{name}-%%{version_string}
%autosetup -p1 -n %{name}-%{version}

%build
export CFLAGS="%{optflags}"
./configure PREFIX=%{_prefix} MANDIR=%{_mandir} LIBDIR=%{_libdir}
#%%make_build
bmake

%install
#%%make_install
bmake install DESTDIR=%{buildroot}
#%%make_install install_libs
bmake install DESTDIR=%{buildroot} install_libs
rm %{buildroot}%{_libdir}/*.a
chmod a+rx %{buildroot}%{_libdir}/liblowdown.so*
%fdupes -s %{buildroot}

%ldconfig_scriptlets -n %{soname}

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_datadir}/%{name}/

%files -n %{soname}
%{_libdir}/liblowdown.so.*

%files devel
%{_mandir}/man3/*
%{_libdir}/liblowdown.so
%{_libdir}/pkgconfig/lowdown.pc
%{_includedir}/*.h

%changelog
