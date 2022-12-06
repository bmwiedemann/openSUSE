#
# spec file for package urlscan
#
# Copyright (c) 2022 SUSE LLC
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


%define python_flavor python3
Name:           urlscan
Version:        0.9.10
Release:        0
Summary:        An other URL extractor/viewer
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            https://github.com/firecat53/urlscan
Source0:        https://github.com/firecat53/urlscan/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        muttrc
BuildRequires:  fdupes
BuildRequires:  python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  sed
Requires:       python3
Requires:       python3-base
Requires:       python3-urwid
BuildArch:      noarch

%description
The urlscan utility displays URLs found in an email message with
the respective context. Selecting an URL uses the Python webbrowser
module to determine which browser to open. It also supports
quoted-printable and base64 encoding.

%prep
%setup -q

%build
%python3_build

%install
%python3_install
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
if test -e %{buildroot}%{_datadir}/doc/%{name}*
then
   rm -vf %{buildroot}%{_datadir}/doc/%{name}*/COPYING
   mv %{buildroot}%{_datadir}/doc/%{name}*/* \
      %{buildroot}%{_defaultdocdir}/%{name}/
fi
rm -rf %{buildroot}%{_datadir}/doc/%{name}*
install -m 0644 %{SOURCE1} %{buildroot}%{_defaultdocdir}/%{name}
chmod 755 %{buildroot}%{python_sitelib}/%{name}/__main__*
sed -ri '1 { s@(/usr/bin/)env *@\1@ }' %{buildroot}%{python_sitelib}/%{name}/__main__*
%fdupes %{buildroot}

%files
%license COPYING
%{_bindir}/%{name}
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-py*.egg-info
%{_mandir}/man1/%{name}.1%{?ext_man}
%dir %{_defaultdocdir}/%{name}/
%doc %{_defaultdocdir}/%{name}/muttrc
%doc %{_defaultdocdir}/%{name}/README.md

%changelog
