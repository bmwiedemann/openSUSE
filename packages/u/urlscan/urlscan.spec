#
# spec file for package urlscan
#
# Copyright (c) 2024 SUSE LLC
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


%define pythons python3
Name:           urlscan
Version:        1.0.6
Release:        0
Summary:        An other URL extractor/viewer
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            https://github.com/firecat53/urlscan
Source0:        https://github.com/firecat53/urlscan/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        muttrc
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-hatch_vcs
BuildRequires:  python3-hatchling
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  sed
Requires:       python3-base
Requires:       python3-urwid >= 1.2.1
BuildArch:      noarch
%global myname  %name

%description
The urlscan utility displays URLs found in an email message with
the respective context. Selecting an URL uses the Python webbrowser
module to determine which browser to open. It also supports
quoted-printable and base64 encoding.

%prep
%setup -q
install -m 0644 %{SOURCE1} muttrc

%build
SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
export SETUPTOOLS_SCM_PRETEND_VERSION
%pyproject_wheel

%install
%pyproject_install
%{python_expand mkdir -p %{buildroot}%{_defaultdocdir}/%{$python_prefix}-%{myname}
 chmod 755 %{buildroot}%{$python_sitelib}/%{name}/__main__*
 sed -ri '1 { s@(/usr/bin/)env +@\1@ }' %{buildroot}%{$python_sitelib}/%{name}/__main__*
 %fdupes %{buildroot}%{$python_sitelib}
}
sed -ri '1 { s@(/usr/bin/)env +@\1@;s@(/python3)\.[[:digit:]]+@\1@ }' %{buildroot}%{_bindir}/%{name}
if test -e %{buildroot}%{_datadir}/doc/%{myname}*
then
    rm -f %{buildroot}%{_datadir}/doc/%{myname}*/LICENSE
fi
rm -rf %{buildroot}%{_datadir}/doc/%{name}*

%files
%{_bindir}/%{myname}
%{_mandir}/man1/%{myname}.1%{?ext_man}
%{python_sitelib}/%{myname}
%{python_sitelib}/%{myname}-%{version}*-info
%license LICENSE
%doc README.md muttrc

%changelog
