#
# spec file for package urlscan
#
# Copyright (c) 2020 SUSE LLC
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


Name:           urlscan
Version:        0.9.5
Release:        0
Summary:        An other URL extractor/viewer
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            https://github.com/firecat53/urlscan
Source0:        https://github.com/firecat53/urlscan/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        muttrc
Requires:       python3
Requires:       python3-base
Requires:       python3-urwid
BuildRequires:  python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%define python_flavor python3

%description
The urlscan utility displays URLs found in an email message with
the respective context. Selecting an URL uses the Python webbrowser
module to determine which browser to open. It also supports
quoted-printable and base64 encoding.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
rm -rf %{buildroot}/usr/share/doc/%{name}*
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
install -m 0644 %{S:1} %{buildroot}%{_defaultdocdir}/%{name}
rm -rvf %{buildroot}%{python_sitelib}/%{name}-%{version}-*-info

%files
%defattr(-,root,root)
%license COPYING
%doc README.rst
%{_bindir}/%{name}
%{python_sitelib}/%{name}
%{_mandir}/man1/%{name}.1.gz
%doc %{_defaultdocdir}/%{name}/muttrc

%changelog
