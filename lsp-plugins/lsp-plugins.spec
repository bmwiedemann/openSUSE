#
# spec file for package lsp-plugins
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           lsp-plugins
Version:        1.1.9
Release:        0
Summary:        Linux Studio Plugins Project
License:        LGPL-3.0-only AND Zlib
Group:          Productivity/Multimedia/Sound/Utilities
URL:            http://lsp-plug.in/
Source:         https://github.com/sadko4u/lsp-plugins/archive/lsp-plugins-%{version}.tar.gz
# PATCH-FIX-OPENSUSE lsp-plugins-verbose.patch aloisio@gmx.com -- print compiation flags
Patch0:         lsp-plugins-verbose.patch
BuildRequires:  gcc-c++
BuildRequires:  ladspa
BuildRequires:  ladspa-devel
BuildRequires:  php7-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(x11)
ExcludeArch:    ppc64 ppc64le

%description
LSP (Linux Studio Plugins) is a collection of open-source plugins
currently compatible with LADSPA, LV2 and LinuxVST formats.

The basic idea is to fill the lack of good and useful plugins under
the GNU/Linux platform.

%package        doc
Summary:        Linux Studio Plugins Documents
Group:          Documentation/HTML

%description    doc
Documents for Linux Studio Plugins Project

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1

%build
export PREFIX="%{_prefix}" DOC_PATH="%{_docdir}" LIB_PATH="%{_libdir}"
export CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
export PREFIX="%{_prefix}" DOC_PATH="%{_docdir}" LIB_PATH="%{_libdir}"
%make_install


%files
%license LICENSE.txt
%{_bindir}/%{name}-*
%{_libdir}/%{name}-jack-core-%{version}.so
%{_libdir}/ladspa/%{name}-ladspa.so
%{_libdir}/lv2/%{name}.lv2
# doesn't anything own this?
%dir %{_libdir}/vst
%{_libdir}/vst/%{name}-lxvst-%{version}

%files doc
%{_docdir}/%{name}

%changelog
