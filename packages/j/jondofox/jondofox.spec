#
# spec file for package jondofox
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


Name:           jondofox
Version:        2.15.0
Release:        0
Summary:        Secure Firefox profile for anonymous web browsing
License:        GPL-3.0+
Group:          Productivity/Networking/Security
Url:            https://anonymous-proxy-servers.net/en/jondofox.html
Source0:        https://anonymous-proxy-servers.net/en/downloads/jondofox-en_all.deb
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRequires:  dos2unix
BuildRequires:  xz
Requires:       firefox
Recommends:     jondo
Recommends:     tor
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
JonDoFox is a profile for the Mozilla Firefox web browser or
Firefox ESR (recommended), particularly optimized for anonymous
and secure web surfing. For anonymous surfing you need an
IP changer proxy too. We recommend our proxy tool JonDo.

By default JonDoFox uses restrictive settings for security reasons.
Time by time a website does not work like expected. You may have
a look at our online help for JonDoFox to learn how to deal with
restrictions.

This package contains an secure browser profil for anonymous web browsing.


Adjust when needed than user JonDoFox and rename profile to use JonDoFox name

mv ~/.mozilla/firefox/profile ~/.mozilla/firefox/JonDoFox

sed -i 's|Path=profile|Path=JonDoFox|' ~/.mozilla/firefox/profiles.ini

%prep
%setup -q -T -c
ar p %{S:0} data.tar.xz | tar Jx

# Convert to unix line end
find -name "*.js" -print0 -or -name "*.cfg" -print0 -or -name "*.manifest" -print0 -or -name "*.rdf" -print0 -or -name "*.txt" -print0 | xargs -0 dos2unix

%build

%install
# install executable
mkdir -p %{buildroot}%{_bindir}
for f in %{name}-install %{name}-start ; do
    install -Dm 0755 usr/bin/"$f" %{buildroot}%{_bindir}
done

# install icons
mkdir -p %{buildroot}%{_datadir}/{icons,pixmaps}
cp -r usr/share/icons/{crystalsvg,oxygen} %{buildroot}%{_datadir}/icons
install -Dm 0644 usr/share/pixmaps/%{name}*.png %{buildroot}%{_datadir}/pixmaps

# install Desktop file
mkdir -p %{buildroot}%{_datadir}/applications
install -Dm 0644 usr/share/applications/%{name}.desktop %{buildroot}%{_datadir}/applications

# install directories
cp -r usr/share/%{name} %{buildroot}%{_datadir}

%if 0%{?suse_version}
    %suse_update_desktop_file -r %{name} Network WebBrowser
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%doc usr/share/doc/jondofox-en
%{_bindir}/%{name}-*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/crystalsvg/
%{_datadir}/icons/oxygen/
%{_datadir}/pixmaps/%{name}*.png
%{_datadir}/%{name}

%changelog
