#
# spec file for package urlscan
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           urlscan
Version:        0.9.2
Release:        0
Summary:        An other URL extractor/viewer
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Browsers
Url:            https://github.com/firecat53/urlscan
Source0:        https://github.com/firecat53/urlscan/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        muttrc
Requires:       python3-urwid
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

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

%files
%defattr(-,root,root)
%license COPYING
%doc README.rst
%{_bindir}/%{name}
%{python_sitelib}/*
%{_mandir}/man1/%{name}.1.gz
%doc %{_defaultdocdir}/%{name}/muttrc

%changelog
