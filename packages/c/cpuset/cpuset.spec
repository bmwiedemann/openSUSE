#
# spec file for package cpuset
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2008-2011 Novell, Inc. Waltham, MA, USA
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


%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif
Name:           cpuset
Version:        1.6.2
Release:        0
Summary:        Cpuset manipulation tool
License:        GPL-2.0-only
Group:          System/Management
URL:            https://github.com/SUSE/cpuset
Source:         https://github.com/SUSE/cpuset/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  python3-setuptools

%description
Cpuset is a Python application for using the cpuset facilities in
the Linux kernel. The actual included command is called cset
and allows manipulation of cpusets on the system, and provides higher
level functions such as implementation and control of a basic CPU
shielding setup.

%prep
%setup -q
%autopatch -p1

%build
python3 setup.py build
#make doc  ->not yet, asciidoc is missing...

%install
# Install binaries, but do not install docs via setup.py
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix} --install-data=/eraseme
rm -rf %{buildroot}/eraseme

# Install documentation
mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}/html

install -m 0444 doc/*.1 %{buildroot}/%{_mandir}/man1

install -m 0444 NEWS README AUTHORS cset.init.d doc/*.txt %{buildroot}/%{_defaultdocdir}/%{name}
install -m 0444 doc/*.html %{buildroot}/%{_defaultdocdir}/%{name}/html/

%files
%license COPYING
%doc %{_docdir}/%{name}
%{_bindir}/cset
%{python3_sitelib}/*
%{_mandir}/man1/*

%changelog
