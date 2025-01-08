#
# spec file for package libuser
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


%define         sover 1
Name:           libuser
Version:        0.64
Release:        0
Summary:        A user and group account administration library
License:        LGPL-2.0-or-later
URL:            https://pagure.io/libuser
Source0:        %{url}/archive/%{name}-%{version}/%{name}-%{name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  gettext-tools
BuildRequires:  gtkdoc
BuildRequires:  libtool
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} >= 1600
BuildRequires:  selinux-policy-devel
%else
BuildRequires:  libselinux-devel
%endif
%if 0%{?suse_version} == 1600
BuildRequires:  selinux-policy-targeted
%endif
BuildRequires:  sgmltool
BuildRequires:  pkgconfig(audit)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(ldap)
BuildRequires:  pkgconfig(libsasl2)
%if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(pam)
%else
BuildRequires:  pam-devel
%endif
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(python3)

%description
The libuser library implements a standardized interface for manipulating and
administering user and group accounts.  The library uses pluggable back-ends to
interface to its data sources.

Sample applications modeled after those included with the shadow password suite
are included.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
Requires:       %{name}%{sover} = %{version}

%description devel
%{summary}.

%package -n python3-%{name}
Summary:        Python library for %{name}
Requires:       %{name}%{sover} = %{version}

%description -n python3-%{name}
%{summary}.

%package -n %{name}%{sover}
Summary:        Library files for %{name}

%description -n %{name}%{sover}
%{summary}.

%package docs
Summary:        HTML Documentation for %{name}
BuildArch:      noarch

%description docs
%{summary}.

%lang_package

%prep
%autosetup -n %{name}-%{name}-%{version}

%build
./autogen.sh
%configure \
  --with-selinux \
  --with-ldap \
  --with-audit \
  --with-sasl \
  --with-python \
  --enable-gtk-doc
%make_build

%install
%make_install
%find_lang %{name}
find %{buildroot} -type f \( -name '*.a' -o -name '*.la' \) -delete

%if 0%{?suse_version} != 1600
# Leap16.0 doesn't have openldap-server and with python313 the crypt module is missing
%check
%make_build check
%endif

%ldconfig_scriptlets -n %{name}%{sover}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/lchfn
%{_bindir}/lchsh
%{_sbindir}/lchage
%{_sbindir}/lgroupadd
%{_sbindir}/lgroupdel
%{_sbindir}/lgroupmod
%{_sbindir}/lid
%{_sbindir}/lnewusers
%{_sbindir}/lpasswd
%{_sbindir}/luseradd
%{_sbindir}/luserdel
%{_sbindir}/lusermod
%config %{_sysconfdir}/%{name}.conf
%{_mandir}/man?/lchage.?%{?ext_man}
%{_mandir}/man?/lchfn.?%{?ext_man}
%{_mandir}/man?/lchsh.?%{?ext_man}
%{_mandir}/man?/lgroupadd.?%{?ext_man}
%{_mandir}/man?/lgroupdel.?%{?ext_man}
%{_mandir}/man?/lgroupmod.?%{?ext_man}
%{_mandir}/man?/lid.?%{?ext_man}
%{_mandir}/man?/lnewusers.?%{?ext_man}
%{_mandir}/man?/lpasswd.?%{?ext_man}
%{_mandir}/man?/luseradd.?%{?ext_man}
%{_mandir}/man?/luserdel.?%{?ext_man}
%{_mandir}/man?/lusermod.?%{?ext_man}
%{_mandir}/man?/libuser.conf.?%{?ext_man}

%files -n %{name}%{sover}
%{_libdir}/%{name}.so.%{sover}
%{_libdir}/%{name}.so.%{sover}.*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%files -n python3-%{name}
%{python_sitearch}/%{name}.so

%files docs
%{_datadir}/gtk-doc/html/%{name}

%files lang -f %{name}.lang

%changelog
