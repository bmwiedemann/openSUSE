#
# spec file for package gnucash
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


%define __builder ninja

# Define used guile version
%if 0%{?suse_version} > 1500
%define guile_version 3.0
%else
%if 0%{?sle_version} >= 150200
%define guile_version 2.0
%endif
%endif

%if 0%{?suse_version} > 1600
%bcond_without python
%else
%bcond_with python
%endif

Name:           gnucash
Version:        5.10
Release:        0
Summary:        Personal Finance Manager
License:        SUSE-GPL-2.0-with-openssl-exception OR SUSE-GPL-3.0-with-openssl-exception
Group:          Productivity/Office/Finance
URL:            http://www.gnucash.org/
Source:         https://github.com/Gnucash/gnucash/releases/download/%{version}/%{name}-%{version}.tar.bz2
Source1:        %{name}-rpmlintrc
## Cpan-warning patch must always be applied.
# PATCH-FIX-UPSTREAM gnucash-cpan-warning.patch -- Add a warning about the danger of using gnc-fq-update to update the perl modules used by GnuCash.
Patch0:         gnucash-cpan-warning.patch
# PATCH-FIX-UPSTREAM gnucash-libm.patch gh#gnucash/gnucash#632 dimstar@opensuse.org -- Link libm: gnucash uses e.g. log10 without explicitly requesting libm
Patch1:         gnucash-libm.patch
Patch2:         gnucash-4.1-fix-gtest-path.patch
Patch3:         gnucash-icu.patch
Patch4:         gnucash-swig43.patch

BuildRequires:  cmake >= 3.14
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
%if 0%{?suse_version} == 1500
BuildRequires:  gcc13-PIE
BuildRequires:  gcc13-c++
%endif
BuildRequires:  gmock >= 1.8.0
BuildRequires:  gtest >= 1.8.0
BuildRequires:  guile-devel
BuildRequires:  libboost_date_time-devel-impl >= 1.67.0
BuildRequires:  libboost_filesystem-devel-impl >= 1.67.0
BuildRequires:  libboost_headers-devel-impl >= 1.67.0
BuildRequires:  libboost_locale-devel-impl >= 1.67.0
BuildRequires:  libboost_program_options-devel-impl >= 1.67.0
BuildRequires:  libboost_regex-devel-impl >= 1.67.0
BuildRequires:  libboost_system-devel-impl >= 1.67.0
BuildRequires:  libdbi-drivers-dbd-sqlite3
BuildRequires:  libicu-devel
BuildRequires:  makeinfo
BuildRequires:  ninja
BuildRequires:  pkgconfig
%if %{with python}
BuildRequires:  python3-devel >= 3.8
%endif
BuildRequires:  swig >= 3.0.12
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(aqbanking) >= 6.0.0
BuildRequires:  pkgconfig(dbi) >= 0.8.3
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.56.1
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.40
BuildRequires:  pkgconfig(gnome-keyring-1) >= 0.6
BuildRequires:  pkgconfig(gobject-2.0) >= 2.40
BuildRequires:  pkgconfig(gthread-2.0) >= 2.40
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.29
BuildRequires:  pkgconfig(gwenhywfar) >= 3.99.20
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(ktoblzcheck)
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(libofx) >= 0.9.0
BuildRequires:  pkgconfig(libsecret-1) >= 0.18
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.4
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
Recommends:     %{name}-docs
# For translation of currency names
Recommends:     iso-codes
%if %{with python}
Recommends:     python3-gnucash = %{version}
%endif
# Optional perl modules for online price retrieval
Recommends:     perl(Date::Manip)
Recommends:     yelp
Recommends:     perl(Finance::Quote)
BuildRequires:  pkgconfig(gwengui-gtk3)

%description
GnuCash is a personal finance manager. A check book-like register GUI
allows you to enter and track bank accounts, stocks, income, and even
currency trades.

Feature Highlights:

 * Double-Entry Accounting;
 * Stock/Bond/Mutual Fund Accounts;
 * Small-Business Accounting;
 * Reports, Graphs;
 * QIF/OFX/HBCI Import, Transaction Matching;
 * Scheduled Transactions;
 * Financial Calculations.

%if %{with python}
%package -n python3-gnucash
Summary:        Python bindings for GnuCash
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}

%description -n python3-gnucash
This package provides the Python 3 bindings for development of GnuCash,
a personal finance manager.
%endif

%package devel
Summary:        Development files for GnuCash
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This package provides all the necessary files for development of GnuCash,
a personal finance manager.

%lang_package

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%define _lto_cflags %{nil}
%define __builder ninja
%if 0%{?suse_version} == 1500
export CXX=g++-13
%endif
%cmake \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
    -DCMAKE_SKIP_RPATH=OFF \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
    -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
    -DGMOCK_ROOT=%{_includedir}/gmock \
    -DGTEST_ROOT=%{_includedir}/gtest \
%if %{with python}
    -DWITH_PYTHON=ON \
%else
    -DWITH_PYTHON=OFF \
%endif
    -DCOMPILE_GSCHEMAS=OFF \
    -DCMAKE_CXX_FLAGS=-Wno-error
%cmake_build

%install
%cmake_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_libdir}
%fdupes %{buildroot}%{_datadir}
# Remove MS-Windows-related files and auto-installed LICENSE file
rm %{buildroot}%{_docdir}/%{name}/LICENSE

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_bindir}/gnc-fq-*
%{_bindir}/finance-quote-wrapper
%{_bindir}/gnucash
%{_bindir}/gnucash-cli
%{_bindir}/gnucash-valgrind
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/gnucash.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/org.gnucash.*.xml
%{_datadir}/gnucash/
%{_datadir}/icons/hicolor/*/apps/gnucash-icon.png
%{_datadir}/icons/hicolor/scalable/apps/gnucash-icon.svg
%dir %{_datadir}/guile/site/%{guile_version}
%{_datadir}/guile/site/%{guile_version}/gnucash
%doc %{_docdir}/%{name}
%{_libdir}/*.so
%{_libdir}/gnucash
%dir %{_libdir}/guile/%{guile_version}/site-ccache
%{_libdir}/guile/%{guile_version}/site-ccache/gnucash
%{_mandir}/man?/*%{?ext_man}
%dir %{_sysconfdir}/gnucash
%config %{_sysconfdir}/gnucash/environment
%exclude %{_datadir}/gnucash/python

%if %{with python}
%files -n python3-gnucash
%{_datadir}/gnucash/python
%dir %{python3_sitearch}/gnucash
%{python3_sitearch}/gnucash
%endif

%files devel
%doc ChangeLog README
%{_includedir}/gnucash/

%files lang -f %{name}.lang

%changelog
