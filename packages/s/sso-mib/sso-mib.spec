#
# spec file for package libjwt
#
# Copyright (c) 2026 SUSE LLC
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

%global soversion 0

Name:           sso-mib
Version:        0.7.0
Release:        1%{?dist}
Summary:        Tools and library for Single-Sign-On with CA for Entra via Himmelblau

License:        LGPL-2.1-only AND GPL-2.0-only AND MIT
URL:            https://github.com/siemens/sso-mib
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.53
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libjwt)
BuildRequires:  pkgconfig(uuid)

%description
Applications can link with this library to get Entra Conditional Access tokens
for authentication and Single-Sign-On from the Himmelblau stack.

%package -n libsso-mib%{soversion}
Summary:        Shared library for SSO with Entra via Himmelblau
License:        LGPL-2.1-only

%description -n libsso-mib%{soversion}
Applications can link with this library to get Entra Conditional Access tokens
for authentication and Single-Sign-On from the Himmelblau stack.

This package contains the shared library.

%package -n libsso-mib-devel
Summary:        Development files for libsso-mib
License:        LGPL-2.1-only
Requires:       libsso-mib%{soversion}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(gio-2.0)
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(uuid)

%description -n libsso-mib-devel
Applications can link with this library to get Entra Conditional Access tokens
for authentication and Single-Sign-On from the Himmelblau stack.

This package contains the development files for the shared library.

%package -n sso-mib-tool
Summary:        Command line tool for SSO with Entra via Himmelblau
License:        GPL-2.0-only

%description -n sso-mib-tool
Applications can link with this library to get Entra Conditional Access tokens
for authentication and Single-Sign-On from the Himmelblau stack.

This package contains command line tools that use the shared library.

%package -n sso-mib-gch-smtp-o365
Summary:        Git credential helper for SMTP on O365 via Himmelblau
License:        MIT
Enhances:       git

%description -n sso-mib-gch-smtp-o365
Applications can link with this library to get Entra Conditional Access tokens
for authentication and Single-Sign-On from the Himmelblau stack.

This package contains a git send-email credential helper to authenticate SMTP
on O365.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

# Install bash completion for sso-mib-tool
install -Dpm0644 debian/sso-mib-tool.bash-completion \
    %{buildroot}%{_datadir}/bash-completion/completions/sso-mib-tool

%check
%meson_test

%if 0%{?suse_version}
%ldconfig_scriptlets -n libsso-mib%{soversion}
%endif

%files -n libsso-mib%{soversion}
%license LICENSES/LGPL-2.1-only.txt
%doc README.md
%{_libdir}/libsso-mib.so.%{soversion}
%{_libdir}/libsso-mib.so.%{version}

%files -n libsso-mib-devel
%license LICENSES/LGPL-2.1-only.txt
%{_includedir}/sso-mib/
%{_libdir}/libsso-mib.so
%{_libdir}/pkgconfig/sso-mib.pc

%files -n sso-mib-tool
%license LICENSES/GPL-2.0-only.txt
%{_bindir}/sso-mib-tool
%{_datadir}/bash-completion/completions/sso-mib-tool

%files -n sso-mib-gch-smtp-o365
%license LICENSES/MIT.txt
%{_bindir}/sso-mib-gch-smtp-o365

%changelog
