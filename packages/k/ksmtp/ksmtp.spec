#
# spec file for package ksmtp
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


%bcond_without lang
Name:           ksmtp
Version:        19.08.2
Release:        0
Summary:        Job-based library to send email through an SMTP server
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules >= 1.0.0
BuildRequires:  kcoreaddons-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Network) >= 5.7.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.7.0
Recommends:     %{name}-lang

%description
KSMTP is a job based library to send email through an SMTP server.

%package -n libKPimSMTP5
Summary:        Job-based library to send email through an SMTP server
Group:          System/GUI/KDE
Requires:       %{name}
Recommends:     %{name}-lang = %{version}

%description -n libKPimSMTP5
KSMTP is a job based library to send email through an SMTP server. This
package contains the KSMTP library itself.

%package devel
Summary:        Development files for KSMTP
Group:          Development/Libraries/KDE
Requires:       kcoreaddons-devel
Requires:       ki18n-devel
Requires:       kio-devel
Requires:       kmime-devel
Requires:       libKPimSMTP5 = %{version}

%description devel
This package contains all necessary include files and libraries needed
to build programs that use the KSMTP library.

%lang_package

%prep
%setup -q

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --with-qt --all-name
  %endif

%post -n libKPimSMTP5 -p /sbin/ldconfig
%postun -n libKPimSMTP5 -p /sbin/ldconfig

%files -n libKPimSMTP5
%license COPYING.LIB
%{_kf5_libdir}/libKPimSMTP.so.*

%files
%license COPYING.LIB
%{_kf5_debugdir}/ksmtp.categories

%files devel
%license COPYING.LIB
%{_includedir}/KPim/
%{_kf5_cmakedir}/KPimSMTP/
%{_kf5_libdir}/libKPimSMTP.so
%{_kf5_mkspecsdir}/qt_KSMTP.pri

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING.LIB
%endif

%changelog
