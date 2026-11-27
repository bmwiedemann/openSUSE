#
# spec file for package linux-entra-sso
#
# Copyright (c) 2026 SUSE LLC and contributors
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

# Firefox's native messaging directory is architecture-specific, but the host
# contains no compiled code or debuginfo.
%global debug_package %{nil}

Name:           linux-entra-sso
Version:        1.13.0
Release:        0
Summary:        Entra ID SSO via Himmelblau or Microsoft Identity Broker
License:        MPL-2.0
URL:            https://github.com/siemens/linux-entra-sso
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  python3
Requires:       python3
Requires:       python3-gobject
Requires:       python3-pydbus
# Himmelblau provides an alternative and conflicting (same file) implementation
Conflicts:      himmelblau-sso

%description
Local native messaging host for the Firefox/Chromium/Chrome extension to
implement Entra ID SSO Conditional Access, connecting to the Identity Broker
via D-Bus. Supports the open source Himmelblau stack or the Microsoft stack.

The browser extension must be installed separately.

%prep
%autosetup

%build
# Only the native Python host is packaged

%install
%make_install \
    prefix=%{_prefix} \
    libexecdir=%{_libexecdir} \
    python3_bin=%{_bindir}/python3 \
    firefox_nm_dir=%{_libdir}/mozilla/native-messaging-hosts \
    chrome_nm_dir=%{_sysconfdir}/opt/chrome/native-messaging-hosts \
    chrome_ext_dir=%{_datadir}/google-chrome/extensions \
    chromium_nm_dir=%{_sysconfdir}/chromium/native-messaging-hosts \
    RELEASE_TAG=v%{version}

%check
%{_bindir}/python3 -m py_compile linux-entra-sso.py

%files
%license LICENSES/MPL-2.0.txt
%doc README.md
%{_libexecdir}/%{name}/
%dir %{_libdir}/mozilla
%dir %{_libdir}/mozilla/native-messaging-hosts
%{_libdir}/mozilla/native-messaging-hosts/linux_entra_sso.json
%dir %{_sysconfdir}/chromium
%dir %{_sysconfdir}/chromium/native-messaging-hosts
%config(noreplace) %{_sysconfdir}/chromium/native-messaging-hosts/linux_entra_sso.json
%dir %{_sysconfdir}/opt/chrome
%dir %{_sysconfdir}/opt/chrome/native-messaging-hosts
%config(noreplace) %{_sysconfdir}/opt/chrome/native-messaging-hosts/linux_entra_sso.json
%dir %{_datadir}/google-chrome
%dir %{_datadir}/google-chrome/extensions
%{_datadir}/google-chrome/extensions/jlnfnnolkbjieggibinobhkjdfbpcohn.json

%changelog
