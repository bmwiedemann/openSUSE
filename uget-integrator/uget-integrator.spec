#
# spec file for package uget-integrator
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 Hillwood Yang <hillwood@opensuse.org>
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


Name:           uget-integrator
Version:        1.0.0
Release:        0
Summary:        Integration of the uGet Download Manager with Web browsers
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Utilities
Url:            https://github.com/ugetdm/uget-integrator
Source:         https://github.com/ugetdm/uget-integrator/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
Requires:       python3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Integration of the uGet Download Manager with Google Chrome,
Chromium, Opera, Vivaldi and Mozilla Firefox.

%package -n firefox-%{name}
Summary:        Integration of uGet with Firefox
Group:          Productivity/Networking/Web/Utilities
Supplements:    packageand(uget:MozillaFirefox)
Requires:       %{name} = %{version}-%{release}

%description -n firefox-%{name}
Integration of the uGet Download Manager with Mozilla Firefox.

%package -n chromium-%{name}
Summary:        Integration of uGet with Chromium
Group:          Productivity/Networking/Web/Utilities
Supplements:    packageand(uget:chromium)
Requires:       %{name} = %{version}-%{release}

%description -n chromium-%{name}
Integration of the uGet Download Manager with Chromium.

%package -n chrome-%{name}
Summary:        Integration of uGet with Chrome
Group:          Productivity/Networking/Web/Utilities
Supplements:    packageand(uget:google-chrome-stable)
Requires:       %{name} = %{version}-%{release}

%description -n chrome-%{name}
Integration of the uGet Download Manager with Chrome.

%package -n opera-%{name}
Summary:        Integration of uGet with Opera
Group:          Productivity/Networking/Web/Utilities
Supplements:    packageand(uget:opera)
Requires:       %{name} = %{version}-%{release}

%description -n opera-%{name}
Integration of the uGet Download Manager with Opera.

%prep
%setup -q -n %{name}-%{version}
sed -i 's|#!/usr/bin/env python3|#!/usr/bin/python3|g' bin/%{name}

%build
%cmake

%install
%cmake_install
install -Dm 0755 %{buildroot}/bin/uget-integrator %{buildroot}%{_bindir}/uget-integrator
install -Dm 0644 %{buildroot}/conf/com.ugetdm.chrome.json \
        %{buildroot}%{_sysconfdir}/chromium/native-messaging-hosts/com.ugetdm.chrome.json
install -Dm 0644 %{buildroot}/conf/com.ugetdm.chrome.json \
        %{buildroot}%{_sysconfdir}/opera/native-messaging-hosts/com.ugetdm.chrome.json
install -Dm 0644 %{buildroot}/conf/com.ugetdm.chrome.json \
        %{buildroot}%{_sysconfdir}/opt/chrome/native-messaging-hosts/com.ugetdm.chrome.json
install -Dm 0644 %{buildroot}/conf/com.ugetdm.firefox.json \
        %{buildroot}%{_libdir}/mozilla/native-messaging-hosts/com.ugetdm.firefox.json
rm -rf %{buildroot}/LICENSE \
       %{buildroot}/add_config.bat \
       %{buildroot}/bin \
       %{buildroot}/conf \
       %{buildroot}/icon.ico \
       %{buildroot}/remove_config.bat \
       %{buildroot}/uget-integrator \
       %{buildroot}/uget-integrator.bat \
       %{buildroot}/uget-integrator.nsi

%files
%defattr(-,root,root)
%doc README.md changelog
%license LICENSE copyright
%{_bindir}/uget-integrator

%files -n firefox-%{name}
%defattr(-,root,root)
%dir %{_libdir}/mozilla/
%{_libdir}/mozilla/native-messaging-hosts

%files -n chromium-%{name}
%defattr(-,root,root)
%dir %{_sysconfdir}/chromium
%config %{_sysconfdir}/chromium/native-messaging-hosts

%files -n chrome-%{name}
%defattr(-,root,root)
%dir %{_sysconfdir}/opt/chrome
%config %{_sysconfdir}/opt/chrome/native-messaging-hosts

%files -n opera-%{name}
%defattr(-,root,root)
%dir %{_sysconfdir}/opera
%config %{_sysconfdir}/opera/native-messaging-hosts

%changelog
