#
# spec file for package jondo
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           jondo
Version:        00.20.001
Release:        0
Summary:        Proxy client for the anonymous proxy system JonDonym
License:        BSD-3-Clause
Group:          Productivity/Networking/Web/Proxy
Url:            https://anonymous-proxy-servers.net/
Source0:        https://anonymous-proxy-servers.net/downloads/jondo_linux.tar.bz2
Source1:        %{name}.sh
# PATCH-FIX-UPSTREAM - jondo-desktop_jondo.desktop.patch -- Add Exec
Patch0:         %{name}-desktop_jondo.desktop.patch
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  update-desktop-files
Requires:       jre >= 1.6.0
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
JonDo is the local proxy client for JonDonym anonymous webservice.
JonDonym (the name is derived from John Doe and Anonymous) protects your
privacy on the Internet and makes truely anonymous using of webservices
possible. You may use JonDo like a proxy for different web applications.
For anonymous web surfing we hardly recommend Firefox or Iceweasel
together with the JonDoFox profile.

%prep
%autosetup -p0 -n %{name}_linux

%build

%install
# install wrappers
install -Dm 0755 %{S:1} %{buildroot}%{_bindir}/%{name}

# install man
install -Dm 0644 man1/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# install files
mkdir -p %{buildroot}%{_datadir}/%{name}
install -Dm 0644 JAP.jar %{buildroot}%{_javadir}/JAP.jar

# install icons
for i in 16 22 32 48 64 128 ; do
    install -Dm 0644 icons/%{name}-${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

# install Desktop file
install -Dm 0644 desktop/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%suse_update_desktop_file -r %{name} Utility Security

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/
%{_javadir}/JAP.jar

%changelog
