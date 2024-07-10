#
# spec file for package lilv
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


%bcond_with     docs
%define sover 0
%define sordversion %(pkg-config --modversion sord-0)
%define serdversion %(pkg-config --modversion serd-0)
Name:           lilv
Version:        0.24.20
Release:        0
Summary:        C library to make use of LV2 plugins
License:        ISC
Group:          Development/Libraries/C and C++
URL:            https://drobilla.net/software/lilv.html
Source0:        https://download.drobilla.net/lilv-%{version}.tar.xz
Source99:       lilv-rpmlintrc
Source98:       baselibs.conf
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  meson
BuildRequires:  pkgconfig
%if %{with docs}
BuildRequires:  python3-Sphinx
BuildRequires:  python3-sphinx_lv2_theme
%endif
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  pkgconfig(lv2) >= 1.8.0
BuildRequires:  pkgconfig(serd-0) >= 0.30.0
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(sord-0) >= 0.13
BuildRequires:  pkgconfig(sratom-0) >= 0.6.10
# lilv 0.22 require new API of sord 0.13
# Since sord sover unchanged from 0.12, explicitly require here.
Requires(pre):  liblilv-0-%{sover} = %{version}

%description
Lilv is a C library to make use of LV2 plugins in applications.

%package        -n liblilv-0-%{sover}
Summary:        C library to make use of LV2 plugins
# NOTE: This is the only way to ensure that the correct version of sord and serd is installed.
# See boo#1158728
Group:          System/Libraries
Requires:       libserd-0-0 = %{serdversion}
Requires:       libsord-0-0 = %{sordversion}

%description    -n liblilv-0-%{sover}
Lilv is a C library to make use of LV2 plugins in applications.

%package        -n liblilv-0-devel
Summary:        Development files for liblilv
Group:          Development/Libraries/C and C++
Requires:       liblilv-0-%{sover} = %{version}

%description    -n liblilv-0-devel
Lilv is a C library to make use of LV2 plugins in applications.
This subpackage contains the development files for liblilv.

%package        -n python3-lilv
Summary:        Python 3 bindings for lilv
Group:          Development/Libraries/Python
Requires:       liblilv-0-%{sover} = %{version}

%description    -n python3-lilv
Lilv is a C library to make use of LV2 plugins in applications.
This subpackage contains the Python 3 bindings for lilv.

%prep
%setup -q
echo %{sordversion}

%build
%meson -Ddocs=disabled

%meson_build

%install
%meson_install
# Fix E: filelist-forbidden-bashcomp-userdirs /etc/bash_completion.d/lilv
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
mv %{buildroot}%{_sysconfdir}/bash_completion.d/lilv %{buildroot}%{_datadir}/bash-completion/completions/
rmdir %{buildroot}%{_sysconfdir}/bash_completion.d

%post -n liblilv-0-%{sover} -p /sbin/ldconfig
%postun -n liblilv-0-%{sover} -p /sbin/ldconfig

%files
%attr(0755,-,-) %{_bindir}/lv2bench
%attr(0755,-,-) %{_bindir}/lv2info
%attr(0755,-,-) %{_bindir}/lv2ls
%attr(0755,-,-) %{_bindir}/lv2apply
%doc AUTHORS NEWS README.md
%{_mandir}/man1/lv2bench.1%{?ext_man}
%{_mandir}/man1/lv2info.1%{?ext_man}
%{_mandir}/man1/lv2ls.1%{?ext_man}
%{_mandir}/man1/lv2apply.1%{?ext_man}
%{_datadir}/bash-completion/completions/%{name}

%files -n liblilv-0-%{sover}
%license COPYING
%{_libdir}/liblilv-0.so.%{sover}*

%files -n liblilv-0-devel
%{_libdir}/pkgconfig/lilv-0.pc
%{_libdir}/liblilv-0.so
%{_includedir}/lilv-0/
%if %{with docs}
%{_defaultdocdir}/lilv-0/
%{_mandir}/man3/*
%endif

%files -n python3-lilv
%{python_sitelib}/lilv.py
%pycache_only %{python_sitelib}/__pycache__/lilv.*.pyc

%changelog
